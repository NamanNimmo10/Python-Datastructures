# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
count = 0
total = 0
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    else:
        count = count + 1
        a = line.find('0')
        n = float(line[a:])
        total = total  + n
print("Average spam confidence:",float(total/count))
