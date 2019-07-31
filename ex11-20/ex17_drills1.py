'''
simplify the ex17 script 
'''
from sys import argv
from os.path import exists

script, from_file, to_file = argv
# automatically closed the file object by Python once that one line runs.
open(to_file, 'w').write(open(from_file).read())
