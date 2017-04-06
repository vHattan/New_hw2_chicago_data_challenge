# chicago_data_challenge
A repository for h.w2

This is Project is made for COMP412-Open Source Computing for summer 2015 class.
Done by Hattan Baraqan

#Abstract:

The purpose of the project is to work with the open government data and find an interesting correlation between different data sources/services.

#Problem:
This project is intended to find whether there is a correlation between Graffiti and Crimes in the a neighborhood.In other word, we intend to find if graffiti, in general or relatively, linked to more crimes (The neighborhood is dangerous).

#Data Sets Involved:
For this project I used two data sets from Chicago Data Portal at https://data.cityofchicago.org/.

1- Crimes_-_2001_to_present.csv 
https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-present/ijzp-q8t2
 
2- Graffiti_Removal_requests.csv
https://data.cityofchicago.org/Service-Requests/311-Service-Requests-Graffiti-Removal/hec5-y4x5


#Details :
Both data sets were cleaned and used for the time between 2010-2015 only.
From those sets I used the community area number to find how many crimes occurred in each community area individually that I found by finding the repetition number of the Area_code in each data set.

The code is written in Python. 
I used collections.Counter() to find the repetition number of each community area in each of the data sets.In order to use it to find correlation.

Correlation basically is a single number that describes the degree of relationship between two variables.The output number calculated by the code is between -1.0 and +1.0. if the correlation is negative, we have a negative relationship; if it's positive, the relationship is positive. 
more information can be found in the link
http://www.socialresearchmethods.net/kb/statcorr.php

To find the correlation I used NumPy function.

#Result
correlation = -0.00918950267846 since the output is negative, that means there is no correlation in the city of Chicago. If a neighborhood has graffiti that doesn’t necessary mean it is dangerous. 

 
