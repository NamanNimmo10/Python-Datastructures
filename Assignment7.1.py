# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
for name in fh:
    fn = name.rstrip()
    print(fn.upper())
