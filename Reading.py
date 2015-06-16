import csv
import collections

#def graffiti (self): # reading graffiti date and community area

graffiti_csv = open('Graffiti_Removal.csv',"rU")
graffiti_reader = csv.reader(graffiti_csv)

		
graffitiCommunityArea=[]


for row in graffiti_reader:
	graffitiCommunityArea.append(row[6])
	
counter1=collections.Counter(graffitiCommunityArea)
#print(counter.keys())
#print "counter of Graffiti"
#print(counter1.most_common(77))



crimes_csv = open('Crimes.csv',"rU")
crimes_reader = csv.reader(crimes_csv)

		
crimeCommunityArea=[]


for row in crimes_reader:
	crimeCommunityArea.append(row[4])

counter2=collections.Counter(crimeCommunityArea)
#counter2.most_common(5)
#print(counter.keys())

def sortByKey():
	sortByKeyDict = sorted(counter2.items(), key= lambda t: t[0])
	print sortByKeyDict

sortByKey()
#print "counter of Crimes" 
#for key,value in counter2.items():
	#print ("{value}".format(value=key))





