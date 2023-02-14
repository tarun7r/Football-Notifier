<h2>Football-Notifier</h2>
Football-Notifier is a Python application that sends you WhatsApp messages with updates on the events of your favourite football team.
<h2>Setup Details</h2>
<ol>
	<li>Clone the repository.</li>
	<li>Open the terminal, navigate to the folder where your clone of this repository is located, and type: <br><code>pip install -r requirements.txt</code></li>
	<li>Open the config.py file and update the Twilio account info from the Twilio console.</li>
	<img src="Football Notifier/twilio_console.png" width="400" height="200">
	<li>Update your WhatsApp number in the client message data to which you want to receive notifications.</li>
	<li>Update the support_team with the team you wish to follow from the event_scraper.py file.</li>
	<li>Type <code>python Notifier.py</code> in the terminal, and the script will run for as long as you let it run.</li>
	<li>You can run the script on some cloud service providers and receive notifications without interruptions.</li>
</ol>
