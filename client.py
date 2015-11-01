'''
John Ward
10/17/2015
Computer Networking
Python Programming: SMTP Mail Client
client.py
'''

from socket import *

serverName = "https://speech.platform.bing.com/recognize"
serverPort = 465

# Choose a mail server (e.g. Google mail server) and call it mailserver
# mailserver = ("smtp-relay.google.com", 25)
# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(serverName, serverPort)

recv = clientSocket.recv(1024)
print recv

if recv[:3] != '220':
	print '220 reply not received from server.'

while(1):
	in = raw_input("? ")
	ssl_sock.send(in)
	recv1 = ssl_sock.recv(1024)
	print recv1

'''
# Send HELO command and print server response.
print("HELO")
heloCommand = 'HELO\r\n'
ssl_sock.send(heloCommand)
recv1 = ssl_sock.recv(1024)
print recv1
if recv1[:3] != '250':
	print '250 reply not received from server.'

authCommand = "AUTH LOGIN\r\n"
print("AUTH LOGIN")
ssl_sock.send(authCommand)
recv1 = ssl_sock.recv(1024)
print recv1
if recv1[:3] != '334':
	print 'Username not asked for'
username = raw_input("USERNAME: ")
ssl_sock.send(base64.b64encode(username) + "\r\n")
recv1 = ssl_sock.recv(1024)
print recv1
if recv1[:3] != '334':
	print 'Password not asked for'
password = raw_input("PASSWORD: ")
ssl_sock.send(base64.b64encode(password) + "\r\n")
recv1 = ssl_sock.recv(1024)
print recv1
if recv1[:3] != '235':
	print 'Not logged in'
else:
	print "AUTHENTICATION SUCCESSFUL"

# Send HELO command and print server response.
print("HELO")
heloCommand = 'HELO\r\n'
ssl_sock.send(heloCommand)
recv1 = ssl_sock.recv(1024)
print recv1
if recv1[:3] != '250':
	print '250 reply not received from server.'

# Send MAIL FROM command and print server response.
print("MAIL FROM:<" + username + ">")
mailFromCommand = "MAIL FROM:<" + username + ">\r\n"
ssl_sock.send(mailFromCommand)
recv1 = ssl_sock.recv(1024)
print recv1
if recv1[:3] != '250':
	print '250 reply not received from server.'

# Send RCPT TO command and print server response.
to_in = raw_input("TO: ")
recptCommand = "RCPT TO:<" + to_in + ">\r\n"
print("RCPT TO:<" + to_in + ">")
ssl_sock.send(recptCommand)
recv1 = ssl_sock.recv(1024)
print recv1
if recv1[:3] != '250':
	print '250 reply not received from server.'
	exit(1)

# Send DATA command and print server response.
print("DATA")
dataCommand = 'DATA\r\n'
ssl_sock.send(dataCommand)

# Send message data.
dataCommand = raw_input("MESSAGE: ")
ssl_sock.send(dataCommand + '\r\n')
recv1 = ssl_sock.recv(1024)
print recv1

# Message ends with a single period.
print(".")
dataCommand = '\r\n.\r\n'
ssl_sock.send(dataCommand)
recv1 = ssl_sock.recv(1024)
print recv1
if recv1[:3] != '250':
	print '250 reply not received from server.'

# Send QUIT command and get server response.
print("QUIT")
quitCommand = 'QUIT\r\n'
ssl_sock.send(quitCommand)
recv1 = ssl_sock.recv(1024)
print recv1
if recv1[:3] != '221':
	print '221 reply not received from server.'

'''
