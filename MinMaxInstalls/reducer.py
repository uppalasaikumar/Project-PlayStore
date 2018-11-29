s = open("./output/s.txt", "r")    # open file, read-only
r = open("./output/r.txt", "w")   # open file, write

thisKey = ""
thisValue = 0.0
minValue = 0
maxValue = 0

# for loop is used to iterate the lines in the file and store it into two variables named Category and Installs
for line in s:
    data = line.strip().split('\t')
    Category, Installs = data
    
    if Category != thisKey: # for each key value we calculate the minimum and maximum values 
        if thisKey and thisKey!="": 
             r.write(thisKey + '\t' + str(maxValue) +'\t'+ str(minValue)+ '\n')
            # print Category+'\t'+'Maximum: '+str(maxValue)+'\t'+'Minumum: ' +str(minValue)
        thisKey = Category # initializing values to default again
        thisValue = 0.0 
        maxValue=thisValue #intializing the maxValue with thisValue as default value as to find out the maximum residue count
        minValue=Installs #intializing the minValue with Installs as default value as to find out the minimum residue count
    if (Installs>maxValue): #comparing each value of Installs and if it is greater than the present value assign it to maxValue
        maxValue=Installs
    if (Installs<minValue): #comparing each value of Installs and if it is less than the present value assign it to minValue
        minValue=Installs

print '\n'
r.write(thisKey + '\t' + str(maxValue)+ '\t' + str(minValue) +'\n') 
print Category+'\t'+'Maximum: '+str(maxValue)+'\t'+'Minumum: ' +str(minValue)

s.close()
r.close()

