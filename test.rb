require 'rubygems'
require 'sinatra'
require 'twilio-ruby'
require 'net/http'

get '/hello-monkey' do
  Twilio::TwiML::Response.new do |r|
    r.Say "Hello."
	#r.Say 'State where you are calling from at the tone, and press 1 when you are done: '
	#r.Record :maxLength => '30', :action => '/hello-monkey/handle-record', :method => 'get'
	r.Say 'State your symptoms at the tone, and press 1 when you are done: '
	r.Record :maxLength => '30', :action => '/hello-monkey/handle-record', :method => 'get'


    #r.Gather :numDigits => '1', :action => '/hello-monkey/handle-gather', :method => 'get' do |g|
    #  g.Say 'To speak to a real monkey, press 1.'
    #  g.Say 'Press 2 to record your own monkey howl.'
    #  g.Say 'Press any other key to start over.'
    #end
  end.text
end

diagnosis = []


get '/hello-monkey/handle-gather' do
  redirect '/hello-monkey' unless ['1', '2', '3', '4', '5'].include?(params['Digits'])
  print "handler"
  print(diagnosis[params['Digits']]) ##CHANGE
  response.text

  str = 'python bingGRAG.py "' + diagnosis[params['Digits']] + ' site:mayoclinic.com"'
  `#{str}`

end



get '/hello-monkey/handle-record' do
  Twilio::TwiML::Response.new do |r|
    r.Say 'Your responses have been recorded. Please hold while we process your symptoms.'
	#r.Play "http://cf3de14e.ngrok.io/music.mp3"
    #r.Play params['RecordingUrl']

	str = "python down.py " + params['RecordingUrl']
	`#{str}` ##DOWNLOAD AUDIO FILE

	str = "python speechToText.py " + params['RecordingUrl']
	`#{str}` ##CONVERT AUDIO SEARCH TO TEXT

	file = File.read(params['RecordingUrl'].split('/')[-1] + '-search-text.txt')
	hash = JSON.parse(file)
	symptoms = hash["header"]["name"]
	print "\n\nSymptoms are " + symptoms
	r.Say 'Symptoms fetched.'

	print("Calling bing\n\n");
	str = 'python bingGRAG.py \"' + symptoms + ' site:symptomchecker.webmd.com\"'###SEARCH_FOR_WEBMD_DIAGNOSES
	`#{str}` ##SEARCH FOR DIAGNOSIS
	print("Bing Called\n\n")

	file = File.read('bingResults.txt')
	print "\n\nDiagnoses are " + file
	r.Say 'Diagnoses fetched.'



	diagnoses = file.split(" ")
	diagnoses[0] = diagnoses[0].tr("|", "^");
	print("\n\n\n\n"+diagnoses[0]+"\n\n\n\n\n")
	str = 'python webMDParser.py ' + diagnoses[0] + ' webmd.txt'
	`#{str}`
	print "\n\nWebMDParser called " + str
	r.Say 'Web MD Parser called.'

	file = File.read('webmd.txt')
	#conditions = JSON.parse(file)


#		print "i:" + j.to_s
#		Twilio::TwiML::Response.new do |r|
#			r.Gather :numDigits => '1', :action => '/hello-monkey/handle-gather', :method => 'get' do |g|
#				g.Say "Press " + j.to_s + " if you are experiencing " + conditions[1]
#			end
#		end.text
#	end


	str = 'python bingGRAG.py "' + file.readlines.split('"')[1] + ' site:mayoclinic.com"'
	print str 
    `#{str}`

	file = File.read('bingResults.txt')
	print file

	str = 'python Summarizer.py ' + file.readlines()
	print str
	`#{str}`

	results = File.read('summaryResults.txt')

	r.Say results

    r.Say 'Goodbye.'
	end
end
