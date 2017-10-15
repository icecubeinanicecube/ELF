'''
Created on 14.10.2017

@author: benef

git is shit
'''
from sys import argv
from functools import reduce
import re


def nichtFiltern(x, keywords, wrn, err, log):
    base = (wrn and "[WRN" in x) or (err and "[ERR" in x) or (log and "[LOG" in x) or ("[EXC" in x)
    if keywords == []:
        return base
    else:
        return base and reduce(lambda a, b: (True or a) if b in x else a, keywords, False)
        
    

defaultLogPath = "KSP.log"
defaultOutPath = "errors.txt"
keywords = []
about = "Usage: ELF [-o <path>] [-s <path>] [-k <keyword>] [-log] [-noWrn] [-noErr]\n-o: specifies the output path \n-s: specifies the path of the source log\n-k: specifies a keyword to search for, case-sensitive (WARNING: beta-feature))\n-log: include log-entries\n-noWrn: exclude Warnings\n-noErr: exclude Errors"

logPath = defaultLogPath
outPath = defaultOutPath
wrn = True
err = True
log = False

#evaluate arguments, if none keep defaults

if(len(argv) > 1 and argv[1] == "--help"):
    print(about)
    exit()
for i in range(1, len(argv)):   #argv[0] just returns the name of the script
    if(argv[i] == "-o"):
        outPath = argv[i+1]
    elif(argv[i] == "-s"):
        logPath = argv[i+1]
    elif(argv[i] == "-k"):
        keywords.append(argv[i+1])
    elif(argv[i] == "-log"):
        log = True
    elif(argv[i] == "-noWrn"):
        wrn = False
    elif(argv[i] == "-noErr"):
        err = False
    

#filter the input
inp = open(logPath, "r")
p = re.compile("(^\[((.)*\n*(?!^\[))*$)", re.MULTILINE)
entries = re.split(p, inp.read())
inp.close()

result = list(filter(lambda x: nichtFiltern(x, keywords, wrn, err, log), entries))

out = "\n".join(result).replace("\n\n", "\n")

#write the output
file = open(outPath, "w")
file.write(out)
print("successful: ", len(result),"entries in filtered log")
file.close()

"""
#only for debug
debug = open("debug.txt", "w")
debug.write("".join(entries))
debug.close()
print(len(entries))
"""
