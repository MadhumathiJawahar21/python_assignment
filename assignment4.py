print("Welcome to the Student Grading System\n")

name = input("Enter your name: ")
subject = input("Enter subject name: ")
marks = float(input(f"Enter marks obtained in {subject}: "))


if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 50:
    grade = "D"
else:
    grade = "F"

print("\nStudent Report")
print(f"Name: {name}")
print(f"Subject: {subject}")
print(f"Marks: {marks}")
print(f"Grade: {grade}")

if grade == "A+" or grade == "A":
    print("Excellent work! Keep it up.")
elif grade == "B":
    print("Good job! You can improve further.")
elif grade == "C" or grade == "D":
    print("You passed, but try to work harder.")
else:
    print("Unfortunately, you failed. Study harder next time!")

if grade != "F":
    print("Congratulations! You have passed.")
else:
    print("Don't give up! Try again next time.")
    
