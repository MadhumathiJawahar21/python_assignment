original_price = float(input("Enter the original price: "))
gst_rate = float(input("Enter the GST rate (%): "))

gst_amount = (original_price * gst_rate) / 100

final_price = original_price + gst_amount

print("GST Amount:", gst_amount)
print("Final Price (Including GST):", final_price)