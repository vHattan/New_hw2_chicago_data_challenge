import csv
import collections

#def graffiti (self): # reading graffiti date and community area

graffiti_csv = open('Graffiti_Removal.csv',"rU")
graffiti_reader = csv.reader(graffiti_csv)

		
g_communityArea=[]


for row in graffiti_reader:
	g_communityArea.append(row[6])
	
counter1=collections.Counter(g_communityArea)
#print(counter.keys())
print "counter of Graffiti"
print(counter1.most_common(77))



crimes_csv = open('Crimes.csv',"rU")
crimes_reader = csv.reader(crimes_csv)

		
c_communityArea=[]


for row in crimes_reader:
	c_communityArea.append(row[4])
counter2=collections.Counter(c_communityArea)

#print(counter.keys())
print "counter of Crimes"
print (counter2.most_common(5))





