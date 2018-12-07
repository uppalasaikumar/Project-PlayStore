

o = open("./output/readyForReducer.txt", "r")                             #open file in readonly mode
s = open("./output/result.txt", "w")                                      #opens file in writeonly more

totalInstalls = 0
oldKey = None
startOfBucket = 0


for line in o:                                                           #loops through file and read each lines
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:                                            #if more than one cloumns, skips
        continue
    thisKey, thisInstall = data_mapped
    thisKey = float(thisKey)
    if(oldKey !=None and startOfBucket == 0  and thisKey != 0.0):
        s.write(str(startOfBucket) + "\t" + str(totalInstalls) + "\n")
        startOfBucket = 0.1
        oldKey = thisKey
        totalInstalls = 0

    if (oldKey and thisKey > (startOfBucket + 30)):                                     #only writes the first time and when the key changes
        s.write(str(startOfBucket) +"-"+ str(startOfBucket + 30 - 0.1) + "\t" + str(totalInstalls) + "\n")
        oldKey = thisKey
        totalInstalls = 0
        startOfBucket += 30

    oldKey = thisKey
    totalInstalls += long(thisInstall)

if oldKey != None:                                                      #prints the last time
    s.write(str(startOfBucket) + "-" + str(startOfBucket + 30 - 0.1) + "\t" + str(totalInstalls) + "\n")

