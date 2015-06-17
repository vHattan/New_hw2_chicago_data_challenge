import csv
import collections

# read graffiti date and community area

id_CommunityArea=(range(1,78))


def graffitiCommunityArea(): 

	graffiti_csv = open('Graffiti_Removal.csv',"rU")
	graffiti_reader = csv.reader(graffiti_csv)
		
	gCommunityArea=[]
	for row in graffiti_reader:
		gCommunityArea.append(row[6])

	return  gCommunityArea

	
gCounter=collections.Counter(graffitiCommunityArea())
#print gCounter
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
	return sortByKeyDict



#x=sortByKey(cCounter)
#y=sortByKey(gCounter)


#for n in  range(1,78):
 #  list.append(gCounter[n], cCounter[n])

#for top in x: 
	#print(top) 
#	for inner in top: 
#		print(inner) 
#y=[z for z in x]

#print "counter of Crimes" 
#for key,value in cCounter.items():
	#print ("{value}".format(value=key))

crimeAreaList= cCounter.values()
graffitiAreaList= gCounter.values()

print len(graffitiAreaList), len(crimeAreaList)

#for n in  range(1,78):
 #   list.append(cCounter[n], gCounter[n])


