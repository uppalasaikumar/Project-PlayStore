f = open("../Data/googleplaystore.csv","r",encoding="utf8")  # open file, read-only
o = open("./output/o.txt", "w",encoding="utf8") # open file, write
# count = 0
for line in f:
    # count = count + 1
    data = line.strip().split(",") 
    # print(data)
    # if count > 2:
    #     break
    if len(data) == 15:
        App,Category,Rating,Reviews,Size,Installs,Install_tail,Type,Price,Content_Rating,Genres,Last_Updated,Last_Updated_tail,Current_Ver,Android_Ver = data
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