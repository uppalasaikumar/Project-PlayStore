f = open("../Data/googleplaystore.csv","r")  # open file, read-only
o = open("./output/o.txt", "w") # open file, write
# count = 0
for line in f:
    # count = count + 1
    data = line.strip().split(",") 
    # print(data)
    # if count > 2:
    #     breakcd
    if len(data) == 13:
        App, Category, Rating, Reviews, size, installs, Type, Price, contentRating, genres, lastUpdated, currentVer, AndroidVer = data
        # print(int(Price) == 0)
        if Price == '0':
            if '"' in Category:
                continue
            # print(Category)
            # print(App)
            # print(Reviews)
            o.write("{0}\t{1}\t{2}\n".format(Category, App, Reviews))
f.close()
o.close()
