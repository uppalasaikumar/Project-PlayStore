s = open("./output/s.txt", "r")   
r = open("./output/r.txt", "w")   

thisKey = ""
thisValue = 0.0
thisApp = ""
for line in s:
  data = line.strip().split('\t')
  Category, App, Reviews  = data
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
r.write(thisKey + '\t' + str(thisValue)+'\n')
s.close()
r.close()

   

