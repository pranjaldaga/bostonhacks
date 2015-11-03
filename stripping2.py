import string
import urllib2
import urllib
import json
import unirest
import httpclient
import sys


url = sys.argv[-1]

#url="http://www.mayoclinic.org/diseases-conditions/premature-ventricular-contractions/basics/treatment/con-20030205"
page =urllib2.urlopen(url)
data=page.read()
microsoftAPIKey= "9695e6647db243b5ab9b2fec87f7355a"
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

with open("mayoArticle.txt", "w") as outfile:
	outfile.write(" "+json.dumps(strippedDoc)+" ")

#test2=postunirest("recognizespeech", {"url" : "http://cf3de14e.ngrok.io/voice.mp3" })
#print json.dumps(test2)

#conn = http.client.HTTPSConnection("speech.platform.bing.com")
#conn.request("POST","grant_type=client_credentials&client_id={}&client_secret={9695e6647db243b5ab9b2fec87f7355a}&scope={http://cf3de14e.ngrok.io/voice.mp3}")
