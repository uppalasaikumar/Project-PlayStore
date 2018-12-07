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
- we are doing the project using python,so install the recent version of python  
- Clone the repository.
- We worked on 4 Big data problems each have seperate folder which includes mapper.py, reducer.py and sorter.py
- First run mapper then sorter and reducer
- Command to run Mapper: python mapper.py
- output of the mapper.py will be saved to output folder.
- Command to run Sorter: python sorter.py
- output of the sorter.py will be saved to output folder.
- Command to run Reducer: python reducer.py
- output of the mappe.pyr will be saved to output folder.


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

**Bar Chart Screenshot**    
![min_maxbarchart](https://user-images.githubusercontent.com/31738776/49472591-705c6c00-f7d5-11e8-8c2d-77dc6e5cd954.PNG)

**Mapper.py Output Screenshot**
![minmax_sorteroutput](https://user-images.githubusercontent.com/31738776/49255318-4e3ba600-f3f1-11e8-9cbf-806ddb254d47.PNG)

**Reducer.py Output Screenshot**
![minmax_reduceroutput](https://user-images.githubusercontent.com/31738776/49255317-4da30f80-f3f1-11e8-808e-f38abedaa788.PNG)

**Phanivardhan Gurram - average rating for all applications and highest rated application.**
- Mapper Input :Smoke Effect Photo Maker - Smoke Editor	ART_AND_DESIGN	3.8	178	19M	50,000+	Free	0	Everyone	Art & Design	26-Apr-18	1.1	4.0.3 and up

- Mapper Output/Reducer Input : AUTO_AND_VEHICLES - AutoScout24 - 4.5
- Reducer Output:  AUTO_AND_VEHICLES - SKencar - 4.9  
- Language: Python
- Bar Chart

**Bar Chart Screenshot**

This is the output Bar graph for the map reduce problem.

![phanioutputgraph](https://user-images.githubusercontent.com/31742627/49255233-0452c000-f3f1-11e8-8503-02fb763e9bab.PNG)

**Mapper.py Output Screenshot**

This the mapper output for the map reduce problem
![phanimapper](https://user-images.githubusercontent.com/31742627/49254740-ab365c80-f3ef-11e8-8efc-3ed6f0d566c8.PNG)

**Reducer.py Output Screenshot**

This is the reducer output for the map reduce problem.
![phanireducer](https://user-images.githubusercontent.com/31742627/49255115-a45c1980-f3f0-11e8-9e0c-f8be3ac1f05c.PNG)

**Vipul Chandoor - Highest Number of review for free download.**  
- Mapper Input: Kids Paint Free - Drawing Fun	ART_AND_DESIGN	4.7	121	3.1M	10,000+	Free	0	Everyone	Art & Design;Creativity	3-Jul-18	2.8	4.0.3 and up  
- Mapper Output/ Reducer Input: BOOKS_AND_REFERENCE, Skin Care and Natural Beauty, 91615  
- Reducer Output: BOOKS_AND_REFERENCE, Discover Color, 2341  
- Language: Ptyhon  
- 2D bar chart  

**Bar Chart Screenshot**  

![graph](https://user-images.githubusercontent.com/36544701/49472787-f24c9500-f7d5-11e8-9928-bb27ae352b04.PNG)

**Mapper.py Output Screenshot**  

![2](https://user-images.githubusercontent.com/36544701/49255871-df5f4c80-f3f2-11e8-98f5-b3b15838b855.PNG)


**Reducer.py Output Screenshot**  

![3](https://user-images.githubusercontent.com/36544701/49255896-ed14d200-f3f2-11e8-9fa1-e68a62fa7e34.PNG)


## Anik Paul Gomes 
- Question: For each price, number of installs.
- Language: Python

#### Mapper

- **Mapper Input:**  

| App | Category | Rating | Reviews | Size | Installs | Type | Price | Content Rating | Genres | Last Updated | Current Ver | Android Ver |
|--------------------------------------------------|----------------|--------|---------|------|----------|------|-------|----------------|--------------|--------------|-------------|--------------|
| Photo Editor & Candy Camera &   Grid & ScrapBook | ART_AND_DESIGN | 4.1 | 159 | 19M | 10000 | Free | 0 | Everyone | Art & Design | 7-Jan-18 | 1.0.0 | 4.0.3 and up |

- **Mapper output/Reducer Input -** Key: Price, Value: Number of installs (For example: $3.99, 10,000)
- **Mapper Code**
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
- **Screenshot of MapperOutput**
![Mapper Output Screenshot](https://github.com/S530489/Project-PlayStore/blob/master/priceVsInstalls/output/image/mapperOutputScreenshot.PNG "Mapper output screenshot")

#### Sort

- To sort the mapper output, use command ***python sorter.py***.
- It will produce a sorted file named readyForReducer.txt in the output folder.

#### Reducer 
- **Reducer output -** Key: Price, Value: Sum of all installs of that corresponding price (For example: $3.99, 2239251)
- **Reducer code:**
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
- Run the reducer with ***python reducer.py*** command.
- It will produce a text file named results.txt in the output folder.
- **Screenshot of reducer output**
![Reducer Output Screenshot](https://github.com/S530489/Project-PlayStore/blob/master/priceVsInstalls/output/image/reducerOutputScreenshot.PNG "Reducer output screenshot")

#### MapReduce result in a Historgram chart  
![PriceVsInstallHistogram](https://github.com/S530489/Project-PlayStore/blob/master/priceVsInstalls/output/image/priceVsInstalls.PNG "Histogram chart of number of installs in a price range")

The visual representation of the map-reduce output indicates that the applications with lower price have more frequent installs. Applications with mid-range price have a very lower number of installs. However, The higher price range ($390.01 - $420.00) have a slightly more number of installs then mid-range price applications. This may be because of the quality of the applications. 





