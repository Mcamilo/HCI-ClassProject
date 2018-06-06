import time
from webwhatsapi import WhatsAPIDriver
from webwhatsapi.objects.message import Message

driver = WhatsAPIDriver(loadstyles=True)
print("Waiting for QR")
driver.wait_for_login()

print("Bot started")

while True:
    time.sleep(3)
    print('Checking for more messages')
    for contact in driver.get_unread():
    	for message in contact.messages:
            	if isinstance(message, Message):  # Currently works for text messages only.
            		if message.content == "/oi":
            			contact.chat.send_message("HelloWorld")	
