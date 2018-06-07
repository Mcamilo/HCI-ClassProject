import eliza
import time
from webwhatsapi import WhatsAPIDriver
from webwhatsapi.objects.message import Message

therapist = eliza.eliza()
driver = WhatsAPIDriver(loadstyles=True)
print("Waiting for Login")
driver.wait_for_login()
print("ELIZA started")
paciente = 0
while True:
	time.sleep(3)
	print('Checking for Pacients')
	for contact in driver.get_unread():
		for message in contact.messages:
			if isinstance(message, Message):
				if message.content == "/eliza":
					paciente = contact.chat
					contact.chat.send_message("What is on your mind?")
					print("Paciente")
					print(paciente)
				elif paciente == contact.chat:
					print("Reply:")
					reply = therapist.respond(message.content)
					print(reply)
					contact.chat.send_message(reply)