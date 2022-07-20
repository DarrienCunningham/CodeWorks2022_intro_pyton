def send(email):
    emails.append(email)
    print("email sent")
    return emails

def printEmails():
    print("---New Email---")
    print("From: "+email['sender'])
    print("To: "+email[reciver'])
    print("Subject: "+email['subject'])
    print(email['message'])
    print("---/n/n/n/n/n")
                       
                       
sender = "me"
reciever = "you"
subject = "Congradulations Your Code is Working!/n/n"
message = "Hello user,/n Congradulations your code seems to be working perfectly./n Just be sure to run it again
                       
print(str(type(send({'sender':semder, 'reciver':reciver, 'subject':subject, 'message':message,})))+"/n/n/n")
                       
sender = "me again"
reciver = "you"
