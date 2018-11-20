
import csv

c = open("./output/mapperOutput.txt", "w")                                       # opening the file to write

with open("../Data/googleplaystore.csv", "rb") as csvFile:                       #Reading CSV file from the specific loaction
    reader = csv.reader(csvFile, delimiter=',')                                  #Reader reads the whole file
    line_count = 0;                                                              #Keeping track of line count to skip the first line
    for row in reader:                                                           #Goes through each row in reader
        if (line_count != 0):                                                    #Skips the first line
            if (len(row) == 13):                                                 #Only proceeds if the specific row has 13 columns
                price = row[7].replace("$", "")                                  #Gets rid of $ sign from the price
                installs = row[5].replace("+", "").replace(",", "")              #Gets rid of + and , symbol from the installs
                c.write(price + "\t" + installs + "\n")                          #writes the price and installs as a tab separated values
        line_count += 1

c.close()
#
