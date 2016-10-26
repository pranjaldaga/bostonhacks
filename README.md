Boston Hacks
============
### **Authors:** John Ward, Pranjal Daga, Suyash Gupta, Evan DeSantola
 * **The Idea:** 60% of the world doesn't have Internet, but 80% do have phones. Take advantage of existing resources to transmit critical information.
 * **Goal:** To provide medical advice without Internet.
 * **How it works:** Call our system with any phone, speak your symptoms, and the system will determine your diagnosis and suggest treatment.

### Quickstart Guide:
1. Set up a phone number on Twilio.com to use with the application
2. Download What's Up Doc
3. Install dependencies
4. Start ngrok server one: ./ngrok http 3000
5. Start ngrok server two: ./ngrok http 4567
6. Navigate to rails-app folder and run: rails server
7. Navigate back up to parent directory and start ruby application: ruby test.rb
8. Navigate to the phone number you set up on Twilio at: https://www.twilio.com/user/account/phone-numbers/
9. Under the Voice category, enter the ngrok server two URL into Request URL and change HTTP POST to HTTP GET

### Dependencies:
 * Ruby
 * Rails
 * Sinatra
 * [Twilio-ruby helper library](https://github.com/twilio/twilio-ruby)
 * Python
 * Pip
 * Ngrok
