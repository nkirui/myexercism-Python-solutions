myname = "Edgar Allan Poe"
namelist = myname.split('\n')
print(namelist)
init = ""
for aname in namelist:
    init += aname[1]
print(init)