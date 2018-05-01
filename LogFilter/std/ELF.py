"""
Created on 14.10.2017

@author: benef

A Script to filter out all entries in the logfile containing the selected keywords

"""
import argparse
from functools import reduce
import re


# define utility functions
# returns True, if log-entry x contains one of the keywords searched for
def is_searched_for(entry, keyword_list, warnings, errors, logs, only_all):
    base = (warnings and "[WRN" in entry) or (errors and "[ERR" in entry) or (logs and "[LOG" in entry) or ("[EXC" in entry)
    if not keyword_list:
        return base
    else:
        if only_all:
            return base and reduce(lambda a, b: a if b in entry else False, keyword_list, True)
        return base and reduce(lambda a, b: True if b in entry else a, keyword_list, False)


# parses command-line arguments and returns a object containing all user input
def parse_arguments():
    # evaluate arguments with ArgumentParser
    argsparser = argparse.ArgumentParser(description=docstring)
    argsparser.add_argument(["-o", "--output"], default=defaultOutPath, help="specifies the output path")
    argsparser.add_argument(["-i", "--input"], default=defaultLogPath, help="specifies the input path")
    argsparser.add_argument("-logs", action="store_true", default=False, help="include log entries")
    argsparser.add_argument("-noWrn", action="store_false", default=True, help="exclude warnings", dest="warnings")
    argsparser.add_argument("-noErr", action="store_false", default=True, help="exclude errors", dest="errors")
    argsparser.add_argument(["-a", "--and"], action="store_true", default=False, help="only show entries with all "
                                                                                      "keywords in them")
    argsparser.add_argument(["-k", "--keywords"], nargs=argparse.REMAINDER,
                            help="all args after this are interpreted as keywords to search for", dest="keywords")
    return argsparser.parse_args()


# returns a list of (string) log-entries read from the specified file. Entries may span multiple lines
def read_file(log_path):
    with open(log_path, "r") as inp:
        p = re.compile("(^\[((.)*\n*(?!^\[))*$)", re.MULTILINE)
        return re.split(p, inp.read())


# filters the entries accoding to the user-input
def filter_entries(keywords, warnings, errors, logs, entries, only_all):
    return list(filter(lambda x: is_searched_for(x, keywords, warnings, errors, logs, only_all), entries))


# writes the output to file
def write_out(entries):
    out = "\n".join(entries).replace("\n\n", "\n")
    with open(choices.outPath, "w") as file:
        file.write(out)
        print("successful: ", len(result), "entries in filtered log")


# default variables
defaultLogPath = "KSP.log"
defaultOutPath = "errors.txt"
docstring = "A Script to filter out all entries in the logfile containing the selected keywords"

# do the work
choices = parse_arguments()
entries = read_file(choices.logPath)
result = filter_entries(choices.keywords, choices.warnings, choices.errors, choices.logs, entries, choices.only_all)
write_out(result)


