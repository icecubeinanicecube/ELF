"""
Created on 14.10.2017

@author: benef

A Script to filter out all entries in the logfile containing the selected keywords

"""
import argparse
from functools import reduce
import re


# define utility functions
def is_searched_for(x, keyword_list, warnings, errors, logs, only_all):
    base = (warnings and "[WRN" in x) or (errors and "[ERR" in x) or (logs and "[LOG" in x) or ("[EXC" in x)
    if not keyword_list:
        return base
    else:
        if only_all:
            return base and reduce(lambda a, b: a if b in x else False, keyword_list, True)
        return base and reduce(lambda a, b: True if b in x else a, keyword_list, False)


def parse_arguments():
    # evaluate arguments with ArgumentParser
    argsparser = argparse.ArgumentParser(description=docstring)
    argsparser.add_argument(["-o", "--out"], default=defaultOutPath, help="specifies the output path", dest="output")
    argsparser.add_argument(["-i", "--in"], default=defaultLogPath, help="specifies the input path", dest="input")
    argsparser.add_argument("-log", action="store_true", default=False, help="include log entries", dest="logs")
    argsparser.add_argument("-noWrn", action="store_false", default=True, help="exclude warnings", dest="warnings")
    argsparser.add_argument("-noErr", action="store_false", default=True, help="exclude errors", dest="errors")
    argsparser.add_argument(["-a", "--and"], action="store_true", default=False, help="only show entries with all "
                                                                                      "keywords in them", dest="errors")
    argsparser.add_argument(["-k", "--keywords"], nargs=argparse.REMAINDER,
                            help="all args after this are interpreted as keywords to search for", dest="keywords")
    return argsparser.parse_args()


def read_file(log_path):
    with open(log_path, "r") as inp:
        p = re.compile("(^\[((.)*\n*(?!^\[))*$)", re.MULTILINE)
        return re.split(p, inp.read())


def filter_entries(keywords, warnings, errors, logs, entries):
    return list(filter(lambda x: is_searched_for(x, keywords, warnings, errors, logs), entries))


# default variables
defaultLogPath = "KSP.log"
defaultOutPath = "errors.txt"
docstring = "A Script to filter out all entries in the logfile containing the selected keywords"

# do the work
choices = parse_arguments()
entries = read_file(choices.logPath)
result = filter_entries(choices.keywords, choices.warnings, choices.errors, choices.logs, entries)

# write the output to file
out = "\n".join(result).replace("\n\n", "\n")
with open(choices.outPath, "w") as file:
    file.write(out)
    print("successful: ", len(result), "entries in filtered log")
