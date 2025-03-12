def welcome_message():
  print("Welcome to Book My Show!")
welcome_message()
def user_login():
  name=input("Enter your name: ")
  contact=input("Enter your contact number: ")
user_login()
def select_theatre():
  print("Select Theater: ")
  print("1. PVR")
  print("2. INOX")
  print("3. Satyam")
  choose_num=int(input("Enter your choice: "))
  if choose_num==1:
    return "PVR"
  elif choose_num==2:
    return "INOX"
  elif choose_num==3:
    return "Satyam"
  else:
    print("Invalid choice, please try again.")
    return select_theatre()
choice=select_theatre()
print(f"You selected: {choice}")
def movie():
  print("\nAvailable movies: \n1. Dragon\n2. Avatar\n3. Titanic")
  movie_choice=input("Enter your choice (1-3): ")
  movies={"1":"Dragon","2":"Avatar","3":"Titanic"}
  if movie_choice in movies:
    print(f"You selected: {movies[movie_choice]}")
  else:
    print("Invalid option, Please check")
  return movies.get(movie_choice, "Unknown")
movie_choice=movie()
def timing():
  print("\nAvailable Timings:\n1. 11AM\n2. 2PM\n3. 6PM")
  select_time=input("Select your time (1-3): ")
  timings={"1":"11AM","2":"2PM","3":"6PM"}
  if select_time in timings:
    print(f"Your selected time is: {timings[select_time]}")
  else:
    print("Your choice is wrong!")
  return timings.get(select_time, "Unknown")
select_time=timing()
def seat():
  available_seat=["AA1","AA2","AA3","AA4","AA5","AA6","AA7"]
  tickets=int(input("Enter the number of tickets: "))
  if tickets<=len(available_seat):
    booked_seats=available_seat[:tickets]
    available_seat=available_seat[tickets:]
    print(f"Your booked seats: {booked_seats}")
    print(f"Remaining available seats: {available_seat}")
  else:
    print("Not enough seats available!!")
  per_ticket=[150,200,250]
  print(f"Ticket price ranges are {per_ticket}")
  while True:
    price_choice=int(input("Enter a price range: "))
    if price_choice in per_ticket:
      break
    else:
      print("Invalid choice! Please select a valid price from the given options.")
  total=tickets*price_choice
  gst_rate=10
  gst_amount=(total*gst_rate)/100
  final_price=total+gst_amount
  print(f"Your total booking price before GST: {total}")
  print(f"GST ({gst_rate}%): {gst_amount}")
  print(f"Final price after GST: {final_price}")
  return final_price,total,booked_seats
total_price,total,booked_seats=seat()
def booking_confirmation():
  confirm=input("Confirm your booking? (yes/no): ").lower()
  if confirm=="yes":
    print("\nBooking confirmed!")
  else:
    print("\nBooking Cancelled!")
booking_confirmation()
def cancel_booking(total_price):
  cancel=input("Do you want to cancel your booking? (yes/no): ").lower()
  if cancel=="yes":
    refund_amount=total_price*0.8
    print("\nBooking cancelled successfully.")
    print(f"\nRefund processed! Amount refunded: {refund_amount}")
    return refund_amount
  else:
    print("\nYour booking remains confirmed!")
    return 0
refund_amount=cancel_booking(total_price)
def show_ticket():
  print("\n--------- YOUR TICKET ---------")
  print(f"Theatre: {choice}")
  print(f"Movie: {movie_choice}")
  print(f"Time: {select_time}")
  print(f"Seats: {booked_seats}")
  print(f"Total Price Paid: {total_price}")
  print("------------------------------")
show_ticket()
def refund():
  if refund_amount > 0:
    print(f"Refund of {refund_amount} has been processed successfully.")
  print("\nThank you for using Book My Show! Enjoy your movie!")
  print("Visit us again for more entertainment!")
refund()
