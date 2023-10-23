# Type student name
print("Start!")
print("******************")
name_of_student = input("Student Name:")
print("******************")

# Type of student
print("What type of student are you?")
print("Working", "Studying", "With Children")
student_type = input("Student Type:")
print("******************")

# Passive income or no?
answer_a = int(input("Do you want passive income? 1 for yes, 0 for no:"))
if answer_a == 1:
    response = "Start your passive income journey today!"
else:
    if answer_a == 0:
        response = "Work smart, not just hard! Proceed to end and answer this next time."
print(response)
print("******************")

# Type of passive income
print("For 1, what do you think is the most lucrative?")
print("Drop shopping", "Print-on-Demand", "Cryptocurrency", "Stocks/Forex", "Real Estate/Property",
      "Investing/Dealership", "Online Selling and Servicing", "App Creation", "Blogging", "Business Affiliation",
      "YouTube Content", "Lending", "N/A")
passive_income_choice = input("My Passive Income Choice:")
print("******************")

# Finishing selection
answer_b = int(input("Done picking? Reply by typing 2 or 3 for yes and no, respectively.:"))
if answer_b == 2:
    response = "Yay! Congrats (SKIP BY PRESSING 2 IF YOU CHOSE N/A IN MY PASSIVE INCOME CHOICE). :)"
else:
    if answer_b == 3:
        response = "Go back and review your choice (RUN THE WHOLE PROGRAM IF YOU DID NOT CHOOSE ANY PASSIVE INCOME)."
print(response)
print("******************")
print("End!")