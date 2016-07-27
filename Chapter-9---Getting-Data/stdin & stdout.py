# ----- STDIN AND STDOUT ----- #

# this script reads in lines of text and spits back out the ones that match a regular expression:
# egrep.py
import sys, re

# sys.argv is the list of command-line arguments
# sys.argv[0] is the name of the program itself
# sys.arg[1] will be the regex specified at the command line
regex = sys.argv[1]

# for every line passed into the script
for line in sys.stdin:
    # if it matches the regex, write it to stdout
    if re.search(regex, line):;
    sys.stdout.write(line)
