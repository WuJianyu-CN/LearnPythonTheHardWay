'''
    Strings, Bytes, and Character Encodings
    download a prepare file "wget https://learnpythonthehardway.org/python3/languages.txt"
    DBES, which stands for Decode Bytes, Encode Strings, "deebess"
    when you have bytes and need a string, decode bytes
    when you have a string and need bytes, encode strings.
    你好 to test the ex23_break3.py rewrite this script to b'' instead of UTF-8 strings
'''
# receive argvs from terminal
import sys
script, input_encoding, error = sys.argv

# define the main function and will be called in the end of this file
def main(language_file, encoding, errors):
    line = language_file.readline()
    if line:
        print_line(line, encoding, errors)
        # There is a loop by calling main() until the "line" is False.
        return main(language_file, encoding, errors)


def print_line(line, encoding, errors):
    # a stripping of the trailing \n one the line string
    next_lang = line.strip()
    # DBES
    # next_lang is a string so I encode it and get bytes assigned to raw_bytes
    raw_bytes = next_lang.encode(encoding, errors=errors)
    # raw_bytes are bytes so I decode them and get a string assigned to cooked_string
    cooked_string = raw_bytes.decode(encoding, errors=errors)
    
    print(raw_bytes, "<===>", cooked_string)
    

languages = open("languages.txt", encoding="utf-8")


main(languages, input_encoding, error)
