import http.client, urllib.parse, json

#Note: Sign up at http://www.projectoxford.ai to get a subscription key.  
#Search for Speech APIs from Azure Marketplace.
#Use the subscription key as Client secret below.
clientId = "b3649707-29a1-4bde-abac-8d5e1d6d2ea5"
clientSecret = "9695e6647db243b5ab9b2fec87f7355a"
ttsHost = "https://speech.platform.bing.com"

params = urllib.parse.urlencode({'grant_type': 'client_credentials', 'client_id': clientId, 'client_secret': clientSecret, 'scope': ttsHost})



headers = {"Content-type": "application/x-www-form-urlencoded"}
			
AccessTokenHost = "oxford-speech.cloudapp.net"
path = "/token/issueToken"

# Connect to server to get the Oxford Access Token
conn = http.client.HTTPSConnection(AccessTokenHost)
conn.request("POST", path, params, headers)
response = conn.getresponse()


data = response.read()

conn.close()
accesstoken = data.decode("UTF-8")

#decode the object from json
ddata=json.loads(accesstoken)
access_token = ddata['access_token']

body = "<speak version='1.0' xml:lang='en-us'><voice xml:lang='en-us' xml:gender='Female' name='Microsoft Server Speech Text to Speech Voice (en-US, ZiraRUS)'>This is me being awesome. All we have to do is link this code together and we're great!</voice></speak>"

headers = {"Content-type": "application/ssml+xml", 
			"X-Microsoft-OutputFormat": "riff-16khz-16bit-mono-pcm", 
			"Authorization": "Bearer " + access_token, 
			"X-Search-AppId": "07D3234E49CE426DAA29772419F436CA", 
			"X-Search-ClientID": "1ECFAE91408841A480F00935DC390960", 
			"User-Agent": "TTSForPython"}
			
#Connect to server to synthesize the wave
conn = http.client.HTTPSConnection("speech.platform.bing.com:443")
conn.request("POST", "/synthesize", body, headers)
response = conn.getresponse()
print(response.status, response.reason)
data = response.read()
f = open('test.wav','wb')
f.write(data)
f.close()
conn.close()
print("The synthesized wave length: %d" %(len(data)))
