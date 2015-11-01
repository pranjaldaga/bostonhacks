# coding=utf-8
#__author__ = 'Shrey'

import sys
import re
import operator
import timeit
import urllib2

start = timeit.default_timer()

address = sys.argv[-1]

website = urllib2.urlopen(address)
website_html = website.read()
try:
    website = urllib2.urlopen(address)
except urllib2.HTTPError, e:
    print "Cannot retrieve URL: HTTP Error Code", e.code
except urllib2.URLError, e:
    print "Cannot retrieve URL: " + e.reason[1]

#THE ARTICLE GIVEN ....................................................................................................

#p = """The committee to plan this years Junior/Senior Prom has decided on the theme for this years event. This is a topic that sparked much debate amongst committee members, several of which are rumored to have not spoken to one another since the final decision was made. After ruling out ideas such as a casino theme or a night in Paris, the theme for Prom 2013 will be "Above the Clouds". This ethereal setting will feature both day and night sky displays. A blue backdrop and fluffy white clouds will greet guests as they arrive at the venue, which has yet to be announced. A painted sunset mural, to be created by the advanced art class, will anchor the food tables. The dance floor area will be kept dark and will be illuminated with a suspended moon and over a thousand twinkling lights to represent the stars. Similar to the dance floor atmosphere, the photo area will also feature a dark background lit with stars. A professional photographer will be on hand to photograph couples or individuals. Digital images will be available for immediate viewing. Photo packages must be selected on the night of the event. Half of the packages purchase price will be due upon order. A jazz quartet will entertain the couples while the food is served and pictures are taken. They will also accompany the presentation of the Prom King and Queen. Following the formal portion of the evenings events, the band will be replaced by a DJ who will play more current hits.
#"""
#......................................................................................................................#
#THIS BLOCK SPLITS THE ARTICLE INTO ITS CONSTITUENT SENTENCES..........................................................#
sentenceEnders = re.compile('.*?[\?|\.|\!]')
result = sentenceEnders.findall(website_html)

#print result print "\nThe number of sentences in the article are:", len(result)
#......................................................................................................................#
#THIS BLOCK CREATES THE TEXTRANK 2D ARRAY FOR THE SENTENCES............................................................#

n = len(result)
Matrix = [[0 for x in range(n)] for x in range(n)]
Sum = [0 for x in range(n)]

for i in range(0, n):
	for j in range(0, n):
		if i != j:
			s1 = set(result[i].split(" "))
			s2 = set(result[j].split(" "))
			Matrix[i][j] = len(s1.intersection(s2))
		Sum[i] = Sum[i] + Matrix[i][j]
TempSum = Sum

#......................................................................................................................#
#THIS BLOCK PRINTS THE SUMMARY.........................................................................................#

#print("The summary is :")
#print(result[0])
#print(result[1])

count = 0
for y in range(0, 9):
	max_index, max_value = max(enumerate(Sum), key=operator.itemgetter(1))
	#print(result[max_index])
	n = len(result[max_index].split(" "))
	#print(n)
	count = count + n
	if count < 150:
		f = open('summaryResults.txt','wb')
		f.write(result[max_index])
		f.close()
	else:
		break
	#print(count)
	Sum[max_index] = 0

stop = timeit.default_timer()

#print "The Runtime of the program is:", stop - start ,"seconds"
#......................................................................................................................#
website.close()
