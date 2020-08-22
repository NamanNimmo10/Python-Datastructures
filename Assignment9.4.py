name = input("Enter file:")
handle = open(name)

counts = dict()
for name in handle:
    name = name.rstrip()
    if not name.startswith('From '):
        continue
    splitIt = name.split()
    counts[splitIt[1]] = counts.get(splitIt[1], 0) + 1
    
        
bigcount, bigword = None, None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword, bigcount = word, count

print(bigword, bigcount)
