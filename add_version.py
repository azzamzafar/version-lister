import os,re

os.system('pip freeze >> temp')
packages={}
with open('./temp','r') as versionfile:
    for line in versionfile.readlines():
        ...
        package,version = line.split('==')
        packages[package]=version

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

for package in packages.keys():
    if package not in listings:
        packages[package]=None
os.system('touch newreq')
with open('./newreq','a+') as newreq:
    for key,val in packages.items():
        if val!=None:
            newreq.write(f'{key}=={val}')
os.system('rm temp && mv ./newreq ./requirements.txt --force')


