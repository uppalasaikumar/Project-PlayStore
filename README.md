# Project-PlayStore

**Team name** - Thunder buddies  

## MR project Group 2

- Saikumar Uppala   
- phanivardhan Gurram    
- vipul chandoor  
- Anik paul gomes  

## project pair 

Saikumar Uppala, Phanivardhan Gurram

## project pair  

vipul chandoor,Anik paul gomes

## Links
Repository: https://github.com/S530489/Project-PlayStore  
Issue Tracker: https://github.com/S530489/Project-PlayStore/issues  


## Dataset link

https://www.kaggle.com/lava18/google-play-store-apps#googleplaystore.csv

## Introduction

Our project uses google playstore apps dataset for mapreduce.This project mainly focuses
on performing differnt mapreduce jobs to anylayze the dataset to see which app category is popular, how price affect the user interest in installing a particulat application etc. Mapreduces jobs are written in python language. 


## Dataset:  

- **Google playstore apps records** : 10842  
- **Dataset size**                  : 2MB  
- **File type**                     : Microsoft-excel  
- **Format**                        : structured  

## BigData Qualifications:

- **VOLUME**   : The dataset is of size 2MB  
- **VARIETY**  : The dataset that we are using is a structured  
- **VELOCITY** : The data is recently updated 2 months ago  
- **VERACITY** : The data is taken from a reliable source so the dataset is trustworthy  
- **VALUE**    : we can extract a numeric value output from the dataset  

## setup instructions:
- we are doing the project using python,so we need to install recent version of python  
- Clone the repository and add an ndividual folders.  

## Big data Questions:
- For each Category what is maximum number of installs and minimum numer of installs - Sai Kumar Uppala
- For each category what is the average rating for all applications and highest rated application - Phani Vardhan Gurram
- For each category which application has highest number of reviews which has free downloads - Vipul Chandoor
- For each price, the number of installs to see if the price of the application affects the downloads - Anik Paul Gomes

## Big Data Solutions:

Sai Kumar - Maximum and Minimum number of installations.
- Mapper Input : Photo Editor & Candy Camera & Grid & ScrapBook	ART_AND_DESIGN	4.1	159	19M	10,000+	Free	0	Everyone	Art & Design	7-Jan-18	1.0.0	4.0.3 and up
- Mapper Output/Reducer Input : ART_AND_DESIGN - 500,000+ 
- Reducer Output: ART_AND_DESIGN - 500,000+ - 50,000+ 
- Language: Python
- Bar Chart


**Phanivardhan Gurram - average rating for all applications and highest rated application.**
- Mapper Input :Smoke Effect Photo Maker - Smoke Editor	ART_AND_DESIGN	3.8	178	19M	50,000+	Free	0	Everyone	Art & Design	26-Apr-18	1.1	4.0.3 and up

- Mapper Output/Reducer Input : AUTO_AND_VEHICLES - AutoScout24 - 4.5
- Reducer Output:  AUTO_AND_VEHICLES - SKencar - 4.9  
- Language: Python
- Bar Chart


**Vipul Chandoor - Highest Number of review for free download.**  
- Mapper Input: Kids Paint Free - Drawing Fun	ART_AND_DESIGN	4.7	121	3.1M	10,000+	Free	0	Everyone	Art & Design;Creativity	3-Jul-18	2.8	4.0.3 and up  
- Mapper Output/ Reducer Input: BOOKS_AND_REFERENCE, Skin Care and Natural Beauty, 91615  
- Reducer Output: BOOKS_AND_REFERENCE, Discover Color, 2341  
- Language: Ptyhon  
- 2D bar chart  


**Anik Paul Gomes - For each price, number of installs.**
- Language: Python
- Mapper Input:  
| App                                              | Category       | Rating | Reviews | Size | Installs | Type | Price | Content Rating | Genres       | Last Updated | Current Ver | Android Ver  |
|--------------------------------------------------|----------------|--------|---------|------|----------|------|-------|----------------|--------------|--------------|-------------|--------------|
| Photo Editor & Candy Camera &   Grid & ScrapBook | ART_AND_DESIGN | 4.1    | 159     | 19M  | 10000    | Free | 0     | Everyone       | Art & Design | 7-Jan-18     | 1.0.0       | 4.0.3 and up |
- Mapper output/Reducer Input: 
Key: Price, Value: Number of installs
(For example: $3.99, 10,000)
- Mapper Code
```

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
```
- Run the mapper with ***python mapper.py*** command.
- It will produce a text file named mapperOutput.txt in the output folder.
- Screenshot of MapperOutput 
- To sort the mapper output, use command ***python sorter.py***.
- it will produce a sorted file named readyForReducer.txt in the output folder.
- Reducer output: Key: Price, Value: Sum of all installs of that corresponding price (For example: $3.99, 2239251)
- Reducer code:
```o = open("./output/readyForReducer.txt", "r")                             #open file in readonly mode
s = open("./output/result.txt", "w")                                      #opens file in writeonly more

totalInstalls = 0
oldKey = None


for line in o:                                                           #loops through file and read each lines
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:                                            #if more than one cloumns, skips
        continue
    thisKey, thisInstall = data_mapped

    if oldKey and oldKey != thisKey:                                     #only writes the first time and when the key changes
        s.write(oldKey + "\t" + str(totalInstalls) + "\n")
        oldKey = thisKey
        totalInstalls = 0

    oldKey = thisKey
    totalInstalls += long(thisInstall)

if oldKey != None:                                                      #prints the last time
    s.write(oldKey + "\t" + str(totalInstalls) + "\n")

```
- Run the mapper with ***python reducer.py*** command.
- It will produce a text file named results.txt in the output folder.
- Screenshot of reducer output
- Histogram
![PriceVsInstallHistogram](output/images/priceVsInstalls.PNG "Histogram chart of number of installs in a price range")





