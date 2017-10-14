'''
Created on 14.10.2017

@author: benef
'''
def nichtFiltern(x):
    return x != "" and ("[ERR" in x or "[WRN" in x or x[0] == " ")

log = "\n".join(list(filter(lambda x: nichtFiltern(x), open("C:\Steam\steamapps\common\Kerbal Space Program\KSP.log", "r").read().split("\n"))))

file = open("C:/Users/benef/Desktop/errors.txt", "w")
file.write(log)
file.close()

