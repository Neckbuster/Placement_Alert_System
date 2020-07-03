
import smtplib 
def sendMail(message):
	# creates SMTP session 
	s = smtplib.SMTP('smtp.gmail.com', 587) 

	# start TLS for security 
	s.starttls() 

	# Authentication 
	s.login("sender_gmail", "sender_pwd") 

	# message to be sent 
	message = "You got a new update on College Placements\n" + message

	# sending the mail 
	s.sendmail("sender_gmail", "reciever_mail", message) 

	# terminating the session 
	s.quit() 
