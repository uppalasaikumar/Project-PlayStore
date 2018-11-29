f = open("../Data/googleplaystore.csv","r")  # open file, read-only
o = open("./output/o.txt", "w") # open file, write
linecount = 1
# This for lopp to fetch line by line of data 
for line in f:
    # stripping and splitting line by ","
    data = line.strip().split(",") 
    # checking if each line has length of 13
    if len(data) == 13 and linecount != 1:
        # Assiging values to all these variables
        app, Category, rating, reviews, size, installs, Type, price, contentRating, genres, lastUpdated, currentVer, AndroidVer = data
        #writing the data to o.txt file and formatting mapperoutput
        o.write("{0}\t{1}\n".format(Category, installs)) 
    linecount = linecount+1
f.close()
o.close()           
#close the file after writing