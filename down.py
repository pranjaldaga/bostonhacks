import argparse

print("\n\n\n\n\n\DOWN.PY\n\n\n\n")

parser = argparse.ArgumentParser()
parser.add_argument('recid', help='pass the twilio id of the recording')
args = parser.parse_args()

import requests
r = requests.get(args.recid)
file = open( "rails-app/public/responses/" + args.recid.split('/')[-1] + '.mp3', 'w')
file.write(r.content)
file.close()

print("\n\n\n\n\n\n//PYTHON//\n\n\n\n")

'''

# Download the Python helper library from twilio.com/docs/python/install
from twilio.rest import TwilioRestClient

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC291f75aa75b1c8c1bedc1653e5654b6d"
auth_token  = "25c4d5dbc8f0f8a6cb37c39156ce97cf"
client = TwilioRestClient(account_sid, auth_token)

client.transcriptions.get("RE557ce644e5ab84fa21cc21112e22c485")


'''
'''
# Download the Python helper library from twilio.com/docs/python/install
from twilio.rest import TwilioRestClient
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('recid', help='pass the twilio id of the recording')
args = parser.parse_args()
print (args.recid)

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC291f75aa75b1c8c1bedc1653e5654b6d"
auth_token  = "25c4d5dbc8f0f8a6cb37c39156ce97cf"
client = TwilioRestClient(account_sid, auth_token)

file = open('success.mp3', 'w')
file.write(client.recordings.get(args.recid).uri + ".mp3")
file.close()
'''
