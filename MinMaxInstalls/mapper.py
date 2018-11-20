f = open("../Data/googleplaystore.csv","r")  # open file, read-only
o = open("./output/o.txt", "w") # open file, write

# This for lopp to fetch line by line of data 
for line in f:
    # stripping and splitting line by ","
    data = line.strip().split(",") 
    # checking if each line has length of 15
    if len(data) == 15:
        # Assiging values to all these variables
        App,Category,Rating,Reviews,Size,Installs,Install_tail,Type,Price,Content_Rating,Genres,Last_Updated,Last_Updated_tail,Current_Ver,Android_Ver = data
        #slicing the strings
        Total_Installs = Installs[1:] + ""+ Install_tail[:len(Install_tail)-2]
        #writing the data to o.txt file and formatting mapperoutput
        o.write("{0}\t{1}\n".format(Category, Total_Installs)) 
f.close()
o.close()           
#close the file after writing