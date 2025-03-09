import smtplib
import random
def read_student_mail():
    try:
        f=open("student_mails.txt", "r")
        student_mails=f.read()

        student_mails=student_mails.split(",")
        print(student_mails)
    except:
        print("file not available")

    sender_email= "madhumathijawahar2112@gmail.com"
    for i in student_mails:
        otp_number= random.randint(1000,9999)
        print(otp_number)
        s=smtplib.SMTP("smtp.gmail.com", 587)
        s.starttls()
        s.login(sender_email, "etww kudg nmnf tuli")
        message=f"Hi your OTP number is {otp_number}"
    try:
        s.sendmail(sender_email, i, message)
        print("Mail sent successfully")
        s.quit()
    except:
        print("Mail not sent")
read_student_mail()