'''
ex16 Study Drills 2: 
Wirte a similar to the last exercise that uses read and argv to read the file you just created.
'''

from sys import argv

script, filename = argv

txt = open(filename)

print(txt.read())

# ➜  ex11-20 git:(master) ✗ python3 ex16_drills2.py ex16_test.txt 
# Jay
# loves
# Lily



