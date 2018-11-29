s = open("./sor.txt", "r")   
r = open("./redc.txt", "w")   

thisKey = ""
thisValue = 0.0
highest_Rating = 0
sum = 0
count = 0

# 
for line in s:
    data = line.strip().split('\t')    #removing the spaces
    Category, rating = data
    if rating != "NaN":      
        if Category != thisKey: # for 
            
            if thisKey and thisKey!="": 
                r.write(thisKey + '\t' + str(highest_Rating) +'\t'+ str(round(sum/count,2))+ '\n')
                # print Category+'\t'+'Maximum: '+str(highest_Rating)+'\t'+'Minumum: ' +str(minValue)
            thisKey = Category # initializing values to default again
            thisValue = 0.0 
            highest_Rating=float(thisValue) #intializing the highest_Rating with thisValue as default value as to find out the maximum residue count
            sum=float(rating) #intializing the minValue with rating as default value as to find out the minimum residue count
            count = 1
        if (float(rating)>highest_Rating): #comparing each value of rating and if it is greater than the present value assign it to highest_Rating
            highest_Rating=float(rating)
        sum += float(rating)
        count += 1

print '\n'
r.write(thisKey + '\t' + str(highest_Rating)+ '\t' + str(sum/count) +'\n') 
# print Category+'\t'+'Maximum: '+str(highest_Rating)+'\t'+'Minumum: ' + str(sum/count))

s.close()
r.close()