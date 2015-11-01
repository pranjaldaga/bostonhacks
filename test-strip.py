import unirest
url="http://api.idolondemand.com/1/api/sync/{}/v1"
apikey="17ed017e-bea0-4c2c-b144-da7b5c232589"
def postunirest(function,data={}):
               data['apikey']=apikey
               callurl=url.format(function)
               return unirest.post(callurl, params=data).body
results=postunirest('querytextindex',{'text':'great'})
for document in results["documents"]:
   print document["title"]
