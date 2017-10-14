'''
Created on 14.10.2017

@author: benef
'''
def nichtFiltern(x):
    return x != "" and ("[ERR" in x or "[WRN" in x or x[0] == " ")

logPath = "C:\Steam\steamapps\common\Kerbal Space Program\KSP.log"
outPath = "C:/Users/benef/Desktop/errors.txt"

log = "\n".join(list(filter(lambda x: nichtFiltern(x), open(logPath, "r").read().split("\n"))))

file = open(outPath, "w")
file.write(log)
file.close()

