import csv
import collections

#def graffiti (self): # reading graffiti date and community area

def graffitiCommunityArea(): 

	graffiti_csv = open('Graffiti_Removal.csv',"rU")
	graffiti_reader = csv.reader(graffiti_csv)
		
	gCommunityArea=[]

	for row in graffiti_reader:
		gCommunityArea.append(row[6])

	return  gCommunityArea


	
gCounter=collections.Counter(graffitiCommunityArea())
#print(gCounter.keys())
#print "counter of Graffiti"
#print(gCounter.most_common(77))

def crimeCommunityArea():
		
	crimes_csv = open('Crimes.csv',"rU")
	crimes_reader = csv.reader(crimes_csv)

	cCommunityArea=[]

	for row in crimes_reader:
		cCommunityArea.append(row[4])

	return 	cCommunityArea


cCounter=collections.Counter(crimeCommunityArea())
	#cCounter.most_common(5)
	#print(counter.keys())




def sortByKey(self):
	sortByKeyDict = sorted(self.items(), key= lambda t: t[0])
	print sortByKeyDict

sortByKey(cCounter)


#print "counter of Crimes" 
#for key,value in cCounter.items():
	#print ("{value}".format(value=key))





