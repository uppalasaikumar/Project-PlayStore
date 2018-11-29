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
- Command to run Sorter: python reducer.py
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
![min_maxbarchart](https://user-images.githubusercontent.com/31738776/49255319-4e3ba600-f3f1-11e8-8358-5ca00d830799.PNG)

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

![maximumreviewsscreenshot](https://user-images.githubusercontent.com/36544701/49255914-f9009400-f3f2-11e8-91f2-63568a025669.PNG)


**Mapper.py Output Screenshot**  

![2](https://user-images.githubusercontent.com/36544701/49255871-df5f4c80-f3f2-11e8-98f5-b3b15838b855.PNG)


**Reducer.py Output Screenshot**  

![3](https://user-images.githubusercontent.com/36544701/49255896-ed14d200-f3f2-11e8-9fa1-e68a62fa7e34.PNG)


**Anik Paul Gomes - For each price, number of installs.**
- Mapper Input:  477	Moco+ - Chat, Meet People	DATING	4.2	1545	Varies with device	10,000+	Paid	$3.99	Mature 17+	Dating	June 19, 2018	2.6.139	4.1 and up
- Mapper output/Reducer Input: $3.99, 10,000
- Reducer output: $3.99, 10,00000(Made up number - sum of all the 3.99$ installs)
- Language: Python
- Histogram






