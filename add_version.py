import os,re

os.system('pip freeze >> temp')
packages={}
with open('./temp','r') as versionfile:
    for line in versionfile.readlines():
        ...
        package,version = line.split('==')
        packages[package]=version
listings=[]
with open('./requirements.txt','r') as requirements:
    for line in requirements.readlines():
        listing = re.split(r'\n|==|<=|<|>=|>',line)[0]
        listings.append(listing) 

for package in packages.keys():
    if package not in listings:
        packages[package]=None
os.system('touch newreq')
with open('./newreq','a+') as newreq:
    for key,val in packages.items():
        if val!=None:
            newreq.write(f'{key}=={val}')


