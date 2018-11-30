f = open("../Data/googleplaystore.csv","r")  # open file, read-only
o = open("./out.txt", "w") # open file, write
# count = 0
for line in f:

    data = line.strip().split(",") #remove the extra sapces
    if len(data) == 13:
        app, Category, Rating, reviews, size, installs, type, Price, contentRating, genres, lastUpdated, currentVer, AndroidVer = data
        # print(int(Price) == 0)
        if Price == '0':            #comparing the prices wether 0 or not        
            if '"' in Category:      
                continue
            o.write("{0}\t{1}\n".format(Category, Rating)) #formating the output 
f.close()
o.close()