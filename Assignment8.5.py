fname = input("Enter file name: ")
count = 0
fh = open(fname)
for line in fh:
    line  = line.rstrip()
    if not line.startswith('From '):
        continue
    splitIt = line.split()
    print(splitIt[1])
    count = count + 1    
print("There were", count, "lines in the file with From as the first word")
