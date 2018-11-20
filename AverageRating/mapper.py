f = open("../Data/googleplaystore.csv","r")  # open file, read-only
o = open("./out.txt", "w") # open file, write
# count = 0
for line in f:

    data = line.strip().split(",") #remove the extra sapces
    if len(data) == 15:
        App,Category,Rating,Reviews,Size,Installs,Install_tail,Type,Price,Content_Rating,Genres,Last_Updated,Last_Updated_tail,Current_Ver,Android_Ver = data
        # print(int(Price) == 0)
        if Price == '0':            #comparing the prices wether 0 or not        
            if '"' in Category:      
                continue
        
            o.write("{0}\t{1}\n".format(Category, Rating)) #formating the output 
f.close()
o.close()