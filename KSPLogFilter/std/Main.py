'''
Created on 14.10.2017

@author: benef
'''
from sys import argv

def nichtFiltern(x, keyword):
    warning = (x != "" and ("[ERR" in x or "[WRN" in x or x[0] == " "))
    if(keyword == ""):
        return warning
    else:
        return warning and keyword in x

defaultLogPath = "C:/Steam/steamapps/common/Kerbal Space Program/KSP.log"
defaultOutPath = "C:/ELF/errors.txt"
keyword = ""

logPath = defaultLogPath
outPath = defaultOutPath

#evaluate arguments, if none keep defaults
for i in range(len(argv)-1):
    if(argv[i] == "-o"):
        outPath = argv[i+1]
    elif(argv[i] == "-s"):
        logPath = argv[i+1]
    elif(argv[i] == "-k"):
        keyword = argv[i+1]

#filter the input
log = "\n".join(list(filter(lambda x: nichtFiltern(x, keyword), open(logPath, "r").read().split("\n"))))

#write the output
file = open(outPath, "w")
file.write(log)
file.close()

