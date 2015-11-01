import string
import urllib2
import json
import unirest
import sys

url = sys.argv[-1]

page =urllib2.urlopen(url)
data=page.read()

mainContentIndex=  data.find("main-content")
startWords=data[mainContentIndex:].find("\n<p>")+mainContentIndex

endWords=data[startWords:].find("<div")+startWords

url="http://api.idolondemand.com/1/api/sync/{}/v1"
apikey="17ed017e-bea0-4c2c-b144-da7b5c232589"
def postunirest(function,data={}):
               data['apikey']=apikey
               callurl=url.format(function)
               return unirest.post(callurl, params=data).body



output="mayoArticle.html"

with open("rails-app/public/"+output, "w") as outfile:
	outfile.write("<html>")
	outfile.write(data[startWords:endWords])
	outfile.write("</html>")

strippedDoc=postunirest("extracttext", {"url": "http://cf3de14e.ngrok.io/"+output})

#test2=postunirest("recognizespeech", {"url" : "http://cf3de14e.ngrok.io/voice.mp3" })
#print json.dumps(test2)
strippingNew= str(json.dumps(strippedDoc))
wordList=strippingNew.split()
for each in wordList:
	if "\\u" in each:
		wordList.remove(each)
strippingNew=" ".join(wordList)
print strippingNew
