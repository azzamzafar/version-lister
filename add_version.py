import os,re
import sys

def requirementsfile():
    """
    check if requirements.txt is present
    """
    for file in os.listdir('./'):
        if file=='requirements.txt':
            return True

def parse_extras(parts):
    """ parse package extras present inside
        square brackets.
    """
    for part in parts:
        if ']' in part:
            extras = part.split(']')[0]
            extra_list = extras.split(',')
            for val in extra_list:
                if val!='':
                    return re.split('==|>=|>|<=|<',val)[0]

def lock_dependencies():
    """
    lock dependencies
    """          
    listings=[]
    with open('./requirements.txt','r') as requirements:
        for line in requirements.readlines():
            parts = line.split('[')
            if len(parts)==1:
                listing = re.split(r'\n|==|<=|<|>=|>',line)[0]
                listings.append(listing)
            else:
                # print(parts[0])
                listings.append(parts[0])
                package=parse_extras(parts)
                listings.append(package)
    return listings


def main():
    """
    driver function
    """
    # check if venv is active
    
    # if not os.system('env | grep ^"VIRTUAL_ENV=" | wc -l'):
    if sys.prefix==sys.base_prefix:
        print("Aborted\nNo virtual environments active!!!",file=sys.stderr)
    
    # Create a dicionary of installed packages and their versions 
    os.system('pip freeze >> temp')
    packages={}
    with open('./temp','r') as versionfile:
        for line in versionfile.readlines():
            ...
            content = line.split('\n')[0]
            package,version = content.split('==')
            packages[package]=version
    
    # check if requirements file is present 
    if requirementsfile():
        # generate list of dependencies present in requirementsfile
        dependency_list = lock_dependencies()
        #remove undirect dependencies from dict not present in req.file 
        for package in packages.keys():
            if package not in dependency_list:
                packages[package]=None
        os.system('touch newreq')
        with open('./newreq','a+') as newreq:
            for key,val in packages.items():
                if val!=None:
                    newreq.write(f'{key}=={val}\n')
        os.system('rm temp && mv ./newreq ./requirements.txt --force')

    else:
        """
        if requirements file is not created
        yet then write all the listings in 
        `pip freeze`, it may be noisy as it
        is going to include packages present
        in envir. not strictly required(formatters
        etc.) or related to project.
        """
        with open('./requirements.txt','a+') as req_file:
            for key,val in packages.items():
                req_file.write(f'{key}=={val}\n')
        

  

if __name__=="__main__":
    
    main()