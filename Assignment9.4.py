name = input("Enter file:")
handle = open(name)

counts = dict() #creating a dictionary
for name in handle:
    name = name.rstrip()
    if not name.startswith('From '):
        continue
    splitIt = name.split()
    counts[splitIt[1]] = counts.get(splitIt[1],0) + 1
    
        
bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count>bigcount:
        bigword = word
        bigcount = count
print(bigword, bigcount)
