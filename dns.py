
import sys
import subprocess

domain = input("enter domain name: ")
output = subprocess.check_output(["nslookup", domain], universal_newlines=True)

# print(output)

count = 0
pos = 0

var = output.count("Name")
# print(var)

while count < var:
    name_startpos = output.find("Name", pos, len(output)) + 5
    #print("name_startpos is:",name_startpos)
    name_endpos = name_startpos + len(domain)+1
    #print("name_endpos is:",name_endpos)
    pos = name_endpos
    #print("new pos is",pos)

    add_startpos = name_endpos+9
    add_endpos = add_startpos+14
    name = output[name_startpos:name_endpos]
    # print(name)
    address = output[add_startpos:add_endpos]
    # print(address)

    resol = name + ':' + address
    print(resol)
    count += 1
