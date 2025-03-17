import requests
import smtplib
url="http://demo3367251.mockable.io/demodata"
response=requests.get(url)
print(response)

get_data= response.json()
print(get_data)

price=int(get_data.get("price"))
quantity=5
gst_rate= 5/100

total=price*quantity
gst_amount= total *gst_rate
final_price=total+gst_amount


bill_text= f"""
Supermarket Bill Receipt
total: {total}
GST (5%): {gst_amount}
final amount:{final_price}

Thank you for Shopping with us!!!
"""

choice=input("enter 1 to print the bill or 2 to receive it via email: ")

if choice==1:
    print("\n", bill_text)

elif choice==2:
    user_email=input("enter your email: ")
    sender_email="madhumathijawahar2112@gmail.com"
    send_password="your_password"

    try:
        s=smtplib.SMTP("smtp.gmail.com, 587")
        s.starttls()
        s.login(sender_email, send_password)
        s.sendmail(sender_email, user_email, f"Subject: Supermarket Bill\nn{bill_text}")
        s.quit()
        print("Bill sent successfully to ", user_email)
    except Exception as e:
        print("Error sending email:", e)
else:
    print("Invalid choice. Please enter 1 or 2.")