s = open("./output/s.txt", "r") # open the file in read mode
r = open("./output/r.txt", "w") # open the file in write mode

thisKey = ""
thisValue = 0.0
thisApp = ""
for line in s: # start iterating through rows in input file
  data = line.strip().split('\t') # strip file to remove trailing and leading white spaces
  Category, App, Reviews  = data # loading the fields into a tuple
  if Category != thisKey: 
    if thisKey:
      # output the last key value pair result
      r.write(thisKey + '\t' + str(thisValue)+ '\t' + str(thisApp) + '\n')
   # start over when changing keys
    thisKey = Category
    thisValue = 0.0
    thisApp = ""
  # apply the aggregation function
  if thisValue < float(Reviews):
    thisValue = float(Reviews) 
    thisApp = App
r.write(thisKey + '\t' + str(thisValue)+'\n') # write the last line to file
s.close() # close the sorter output file
r.close() # close the reducer output file

   

