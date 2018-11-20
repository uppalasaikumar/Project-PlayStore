

o = open("./output/readyForReducer.txt", "r")                             #open file in readonly mode
s = open("./output/result.txt", "w")                                      #opens file in writeonly more

totalInstalls = 0
oldKey = None


for line in o:                                                           #loops through file and read each lines
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:                                            #if more than one cloumns, skips
        continue
    thisKey, thisInstall = data_mapped

    if oldKey and oldKey != thisKey:                                     #only writes the first time and when the key changes
        s.write(oldKey + "\t" + str(totalInstalls) + "\n")
        oldKey = thisKey
        totalInstalls = 0

    oldKey = thisKey
    totalInstalls += long(thisInstall)

if oldKey != None:                                                      #prints the last time
    s.write(oldKey + "\t" + str(totalInstalls) + "\n")

