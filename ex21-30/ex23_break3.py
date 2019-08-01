'''
    reversing the ex23.py script to b'' bytes.
'''


def reverse_to_bbytes(input_file):
    line = input_file.readline()
    if line:
        line = line.strip()
        raw_bytes = line.encode('utf-8', errors='strict')
        print(raw_bytes)
        return reverse_to_bbytes(input_file)
        

input_file = open('ex23.py')
reverse_to_bbytes(input_file)

