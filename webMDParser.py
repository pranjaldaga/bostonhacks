import string
import urllib2
import json
import cookielib
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('url', help='url of webmd')
parser.add_argument('fileout', help='file to output')
args = parser.parse_args()

def find2ndIndex(someString, subString):
    first=someString.find(subString)

    return first+ someString[first+1:].find(subString)
def parse(url, fileout):
    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
           'Accept-Encoding': 'none',
           'Accept-Language': 'en-US,en;q=0.8',
           'Connection': 'keep-alive'}

    req = urllib2.Request(url, headers=hdr)
    page =urllib2.urlopen(req)
    print "DATA FUCKING IS!!!"
    data=page.readline()
    with open("FUKC.txt") as outfile:
		outfile.write(str(repr(data)))
    returning=[]
    currentLine=0
    while "results_list" not in data[currentLine]:
	    currentLine+=1
    while "<li" in data[currentLine] or "</li" in data[currentLine]:
		if "</li" in data[currentLine]:
			currentLine+=1
		else:
			nameIndexStart=find2ndIndex(data[currentLine], ">")+2
			nameIndexEnd=data[currentLine][nameIndexStart:].find("<")+nameIndexStart
			name=data[currentLine][nameIndexStart:nameIndexEnd]

			descriptionIndexStart=nameIndexEnd+find2ndIndex(data[currentLine][nameIndexEnd:],">")+2
			descriptionIndexEnd=descriptionIndexStart+data[currentLine][descriptionIndexStart:].find("</p")
			description=data[currentLine][descriptionIndexStart:descriptionIndexEnd]
			returning.append(name)
			returning.append(description)
			currentLine+=1
    json.dumps(returning)


    with open(fileout, "w") as outfile:
		outfile.write(json.dumps(returning))


#test2=postunirest("recognizespeech", {"url" : "http://cf3de14e.ngrok.io/voice.mp3" })
#print json.dumps(test2)

args.url = args.url.replace("^", "|");
parse(args.url, args.fileout)
