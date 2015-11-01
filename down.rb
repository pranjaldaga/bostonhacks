# Get twilio-ruby from twilio.com/docs/ruby/install
require 'rubygems'          # This line not needed for ruby > 1.8
require 'twilio-ruby'

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC291f75aa75b1c8c1bedc1653e5654b6d"
auth_token  = "{{ auth_token }}"

@client = Twilio::REST::Client.new account_sid, auth_token
@recording = @client.account.recordings.get("CAf288f165b3b00293e68a3f70cc9a0b79").uri

File.open('success2.wav', 'w') do |f2|
	# use "\n" for two lines of text
	f2.puts @recording.get
end
