fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line = line.rstrip()
    splitIt = line.split()
    for i in splitIt:
        if i not in lst:
            lst.append(i)
lst.sort()
print(lst)
