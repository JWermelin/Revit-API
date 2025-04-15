fh = open('mbox-short.txt')

for lx in fh:
    ly = lx.rstrip()
    print(ly.upper())
# ly.upper is a string method that returns an 
# uppercase version of all the strings in the file