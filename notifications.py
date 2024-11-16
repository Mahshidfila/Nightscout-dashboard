import smtplib
from email.mime.text import MIMEText

def send_email_alert(subject, body, to_email):
    from_email = "your_email@example.com"
    password = "your_password"
    
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = from_email
    msg["To"] = to_email
    
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(from_email, password)
        server.sendmail(from_email, to_email, msg.as_string())

def check_glucose_level(glucose_level):
    if glucose_level > 180:  
        send_email_alert(
            "هشدار قند خون بالا!",
            f"سطح قند خون شما {glucose_level} mg/dL است که از حد مجاز بالاتر است.",
            "user_email@example.com"
        )
