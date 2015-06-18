import csv
import collections
import numpy



def graffitiCommunityArea(): # Read graffiti.csv and return a list of the community area for all removal requests in the file 

	graffiti_csv = open('Graffiti_Removal.csv',"rU")
	graffiti_reader = csv.reader(graffiti_csv)
		
	gCommunityArea=[]
	for row in graffiti_reader:
		gCommunityArea.append(row[6])# store community area numbers for all removal requests in in gCommunityArea list

	return  gCommunityArea


def crimeCommunityArea():# Read crime.csv and return a list of the community area for all crime records in the file 
		
	crimes_csv = open('Crimes.csv',"rU")
	crimes_reader = csv.reader(crimes_csv)

	cCommunityArea=[]

	for row in crimes_reader:
		cCommunityArea.append(row[4])# store community area numbers for all crime records in cCommunityArea list

	return 	cCommunityArea

 	
def main(): # main method to run the code
		
	#id_CommunityArea=(range(1,78))

	
	gCounter=collections.Counter(graffitiCommunityArea())# call graffitiCommunityArea() and take returned list
															#nd store it in dictionary where area code as keys and repition no. of it as value

	cCounter=collections.Counter(crimeCommunityArea())# call crimeCommunityArea() and take returned list
															#and store it in dictionary where area code as keys and repetion no. of it as value													 
	
	print " The top 5 community areas have the highest no. of removal requests are ", (gCounter.most_common(5))
	print " The top 5 community areas have the highest no. of crimes are ", (cCounter.most_common(5))

	crimeAreaList= cCounter.values() # store values of Crimes repetion no. of each area in a list to use it in correlation function
	graffitiAreaList= gCounter.values() # store values of graffiti repetion no. of each area in a list to use it in correlation function

	print len(graffitiAreaList), len(crimeAreaList)," for testing both lists are eaqual for correlation calculation /"

	result = {}# dic to store area no. and list of no. crimes and no. graffiti
	for key in (cCounter.viewkeys() | gCounter.keys()): # function to combain crime and graffiti no. assighned to the comm. area as key
	    if key in cCounter: result.setdefault(key, []).append(cCounter[key])
	    if key in gCounter: result.setdefault(key, []).append(gCounter[key])
	
	print "{:<8} {:<15} {:<10}".format('CommunAreaNo','CrimeNo','GraffitiRemoval requests')# print last function
	for k, v in result.iteritems():
	    label, num = v
	    print "{:<8} {:<15} {:<10}".format(k, label, num)

	p=numpy.corrcoef(crimeAreaList, graffitiAreaList)[0, 1]# numpy bulit in python function to calculate correlation
	print "correlation =", p # print final result

main() # call main method to run the

