f = open("../Data/googleplaystore.csv","r")  # open file, read-only
o = open("./output/o.txt", "w") # open file, write
for line in f: # iterate through all rows in a file
    data = line.strip().split(",") # trimming the record to remove whitespaces
    if len(data) == 13: # checking whether the length of the record is 13 or not to avoid bad data
        App, Category, Rating, Reviews, size, installs, Type, Price, contentRating, genres, lastUpdated, currentVer, AndroidVer = data
        if Price == '0': # writing record to file only if price is 0
            if '"' in Category: # Checking that category needs to have '"'
                continue # continue to next iteration
            o.write("{0}\t{1}\t{2}\n".format(Category, App, Reviews)) # writing record to a file
f.close() # closing the input data file
o.close() # closing the output file
