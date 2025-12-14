import smtplib
from email.mime.text import MIMEText

# Sender email credentials
sender_email = "naseerrafi.pk@gmail.com"
sender_password = "uxkarbxdostrwqkn"

# Predefined list of receiver emails (example: 20+)
receiver_emails = [
    "naseer4uddin4@gmail.com",
     "rahatrafi8@gmail.com",
     "naseer6uddin6@gmail.com",
   
]

# Email content
subject = "Important Announcement"
message_body = """
Hello,

This is a test email sent using an Email Automation System.
The same message is sent to multiple recipients at the same time.

Regards,
Naseer Ud Din
"""

# Setup server
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(sender_email, sender_password)

# Send email to each recipient
for email in receiver_emails:
    msg = MIMEText(message_body)
    msg["From"] = sender_email
    msg["To"] = email
    msg["Subject"] = subject

    server.sendmail(sender_email, email, msg.as_string())
    print(f"Email sent to {email}")

server.quit()
print("✅ All emails sent successfully!")
