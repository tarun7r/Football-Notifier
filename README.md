<h2>Football-Notifier</h2>
A Python application that sends you a WhatsApp Messages of the  serie of events of the football team you supports
<h2>Setup Details</h2>
Follow the following instructions to run the application and get the notifications to your WhatsApp DM 
<li>Clone the repository</li>
<li>Open the terminal, navigate to the folder where your clone of this repository is located and type:
  
  `$ pip install -r requirements.txt` </li>
 
<li> Open the conifg.py file and update the twilio account info from the <a href="https://console.twilio.com/?frameUrl=/console">console</a></li>
<br> <img src="Football Notifier/twilio_console.png" width="400" height="200"> <br>
<li> Update your whatsapp number in the client message data to which you want to get notifications </li>  
<li> Update the support_team with the team whom you wish to follow from the event_scraper.py file </li>
<li> Type $ python Notifier.py in the terminal and the script will run for as long as you let it run. </li>
> You can run the script on some cloud service providers and get the notifications without interruptions.


