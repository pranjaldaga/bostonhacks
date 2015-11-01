import string
import urllib2
import sys

url = sys.argv[-1]

import requests

havenTextRequest="https://api.havenondemand.com/1/api/sync/{}/v1"

apikey="17ed017e-bea0-4c2c-b144-da7b5c232589"

#url="http://www.mayoclinic.org/diseases-conditions/premature-ventricular-contractions/basics/treatment/con-20030205"
page =urllib2.urlopen(url)
data=page.read()

mainContentIndex=  data.find("main-content")
startWords=data[mainContentIndex:].find("<p>")+mainContentIndex

endWords=data[startWords:].find("<div")+startWords


def postrequests(function,data={},files={}):
	data["apikey"]=apikey
	callurl=url.format(function)
	r=requests.post(callurl,data=data,files=files)
	print(type(r))
	return r.json()


strippedDoc=postrequests("extracttext", {"reference": str(data[startWords:endWords])})
