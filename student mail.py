import smtplib
import random
def read_student_mail():
    try:
        with open("student_mails.txt", "r") as f:
            student_mails = f.read().strip().split(",")  # Read and split emails

        print("Student Emails:", student_mails)
    except FileNotFoundError:
        print("File not available")
        return

    sender_email = "your_email"
    sender_password = "your_password"  

    try:
        s = smtplib.SMTP("smtp.gmail.com", 587) 
        s.starttls()
        s.login(sender_email, sender_password)

        for email in student_mails:
            otp_number = random.randint(1000, 9999)
            print(f"Sending OTP {otp_number} to {email}")

            message = f"Subject: OTP Verification\n\nHi, your OTP number is {otp_number}"

            try:
                s.sendmail(sender_email, email.strip(), message)
                print(f"Mail sent successfully to {email}")
            except Exception as e:
                print(f"Failed to send email to {email}: {e}")

        s.quit() 

    except Exception as e:
        print("SMTP connection error:", e)

read_student_mail()
