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
defaultOutPath = "errors.txt"
keyword = ""
about = "Usage: ELF [-o <path>] [-s <path>] [-k <keyword>] \n-o: specifies the output path \n-s: specifies the path of the source log\n-k: specifies a keyword to search for, case-sensitive. Can be used to filter for only ERRORS by using -k ERR (WARNING: beta-feature))"

logPath = defaultLogPath
outPath = defaultOutPath

#evaluate arguments, if none keep defaults

if(argv[1] == "--help"):
    print(about)
    exit()
for i in range(1, len(argv)):   #argv[0] just returns the name of the script
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

