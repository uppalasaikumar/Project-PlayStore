

o = open("readyForReducer.txt", "r")
s = open("result.txt", "w")

totalInstalls = 0
oldKey = None


for line in o:
    data_mapped = line.strip().split(",")
    if len(data_mapped) != 2:
        continue
    thisKey, thisInstall = data_mapped

    if oldKey and oldKey != thisKey:
        s.write(oldKey + "\t" + str(totalInstalls) + "\n")
        oldKey = thisKey
        totalInstalls = 0

    oldKey = thisKey
    totalInstalls += long(thisInstall)

if oldKey != None:
    s.write(oldKey + "\t" + str(totalInstalls) + "\n")

