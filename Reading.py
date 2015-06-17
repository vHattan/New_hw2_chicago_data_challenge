import csv
import collections
import numpy

# read graffiti date and community area

def graffitiCommunityArea(): 

	graffiti_csv = open('Graffiti_Removal.csv',"rU")
	graffiti_reader = csv.reader(graffiti_csv)
		
	gCommunityArea=[]
	for row in graffiti_reader:
		gCommunityArea.append(row[6])

	return  gCommunityArea


def crimeCommunityArea():
		
	crimes_csv = open('Crimes.csv',"rU")
	crimes_reader = csv.reader(crimes_csv)

	cCommunityArea=[]

	for row in crimes_reader:
		cCommunityArea.append(row[4])

	return 	cCommunityArea

 	
def main():
		
	#id_CommunityArea=(range(1,78))

	gCounter=collections.Counter(graffitiCommunityArea())	
	print " The top 5 community areas have the highest no. of removal requests are ", (gCounter.most_common(5))

	cCounter=collections.Counter(crimeCommunityArea())
	print " The top 5 community areas have the highest no. of crimes are ", (cCounter.most_common(5))


	#print "counter of Crimes" 
	#for key,value in cCounter.items():
		#print("{value}".format(value=key))


	crimeAreaList= cCounter.values()
	graffitiAreaList= gCounter.values()

	#print len(graffitiAreaList), len(crimeAreaList)

	result = {}

	for key in (cCounter.viewkeys() | gCounter.keys()):
	    if key in cCounter: result.setdefault(key, []).append(cCounter[key])
	    if key in gCounter: result.setdefault(key, []).append(gCounter[key])
	#print result


	p=numpy.corrcoef(crimeAreaList, graffitiAreaList)[0, 1]
	print "correlation =", p

main()

