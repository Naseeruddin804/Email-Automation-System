# =================================================================================
# =========================EMAIL AUTOMATION SYSTEM ================================
# =================================================================================
import smtplib
from email.mime.text import MIMEText

sender_email = "nasee8785@gmail.com"
sender_password = "uxostrddkhsn"

# Predefined list of receiver emails (example: 20+)
receiver_emails = [
    "user1@gmail.com",
     "user2@gmail.com",
     "user3@gmail.com",
     "user4@gmail.com",
     "user5@gmail.com",
     "user6@gmail.com",
     "user7@gmail.com",
     "user8@gmail.com",
     "user9@gmail.com",
     "user10@gmail.com",
     "user11@gmail.com",
     "user12@gmail.com",
     "user13@gmail.com",
     "user14@gmail.com",
     "user15@gmail.com",
     "user16@gmail.com",
     "user17@gmail.com",
     "user18@gmail.com",
     "user19@gmail.com",
     "user20@gmail.com",
     "user21@gmail.com",
]


subject = "Important Announcement"
message_body = """
Hello,

This is a test email sent using an Email Automation System.
The same message is sent to multiple recipients at the same time.
In compliance with data privacy and ethical coding practices,
no real user email addresses have been included directly in the codebase.
During testing, the application was verified using the my own email account.
This approach ensures that the system functionality is demonstrated without ,
exposing sensitive personal data or risking unintended email distribution.

Regards,
Naseer Ud Din
"""


server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(sender_email, sender_password)

for email in receiver_emails:
    msg = MIMEText(message_body)
    msg["From"] = sender_email
    msg["To"] = email
    msg["Subject"] = subject

    server.sendmail(sender_email, email, msg.as_string())
    print(f"Email sent to {email}")

server.quit()
print("✅ All emails sent successfully!")
