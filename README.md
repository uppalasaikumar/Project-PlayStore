# Project-PlayStore

**Team name** - Thunder buddies  

# MR project Group 2

- Saikumar Uppala   
- phanivardhan Gurram    
- vipul chandoor  
- Anik paul gomes  

# project pair 

Saikumar Uppala, Phanivardhan Gurram

# project pair  

vipul chandoor,Anik paul gomes

# Dataset link

https://www.kaggle.com/lava18/google-play-store-apps#googleplaystore.csv

# Introduction

Our project uses google playstore apps dataset for mapreduce.This project mainly focus
on which category of playstore apps are mostly used by analyzing the data set,

# Dataset:  

- **Google playstore apps records** : 10842  
- **Dataset size**                  : 2MB  
- **File type**                     : Microsoft-excel  
- **Format**                        : structured  

# BigData Qualifications:

- **VOLUME**   : The dataset is of size 2MB  
- **VARIETY**  : The dataset that we are using is a structured  
- **VELOCITY** : The data is recently updated 2 months ago  
- **VERACITY** : The data is taken from a reliable source so the dataset is trustworthy  
- **VALUE**    : we can extract a numeric value output from the dataset  

# setup instructions:
- we are doing the project using python,so we need to install recent version of python  
- Clone the repository and add an ndividual folders.  

# Big data Questions:
- For each Category what is maximum number of installs and minimum numer of installs - Sai Kumar Uppala
- For each category what is the average rating for all applications and highest rated application - Phani Vardhan Gurram
- For each category which application has highest number of reviews which has free downloads - Vipul Chandoor

# Big Data Solutions:

Sai Kumar - Maximum and Minimum number of installations.
- Mapper Input : Photo Editor & Candy Camera & Grid & ScrapBook	ART_AND_DESIGN	4.1	159	19M	10,000+	Free	0	Everyone	Art & Design	7-Jan-18	1.0.0	4.0.3 and up
- Mapper Output/Reducer Input : ART_AND_DESIGN - 500,000+ 
- Reducer Output: ART_AND_DESIGN - 500,000+ - 50,000+ 
- Language: Python
- Bar Chart

**Vipul Chandoor - Highest Number of review for free download.**
- Mapper Input: Kids Paint Free - Drawing Fun	ART_AND_DESIGN	4.7	121	3.1M	10,000+	Free	0	Everyone	Art & Design;Creativity	3-Jul-18	2.8	4.0.3 and up  
- Mapper Output/ Reducer Input: BOOKS_AND_REFERENCE, Skin Care and Natural Beauty, 91615  
- Reducer Output: BOOKS_AND_REFERENCE, Discover Color, 2341  
- Language: Ptyhon  
- 2D bar chart  








