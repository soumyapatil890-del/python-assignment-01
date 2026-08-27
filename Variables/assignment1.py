# Problem Name: Student ID Card Generator
#
# Statement:
# Create variables to store:
# Student Name
# Roll Number
# Branch
# Semester
# College Name
#
# Print the details in a neatly formatted ID card.
#
# Bonus:
# Create a variable called email_id using the student's name and roll number.


# Solution

student_name = "Soumya Patil"
roll_number = "63"
branch = "Computer Science"
semester = "8th"
college_name = "KLE Technological University"

# Bonus
email_id = student_name.lower().replace(" ", ".") + roll_number + "@example.com"


print("=" * 40)
print("           STUDENT ID CARD")
print("=" * 40)
print(f"Student Name : {student_name}")
print(f"Roll Number  : {roll_number}")
print(f"Branch       : {branch}")
print(f"Semester     : {semester}")
print(f"College Name : {college_name}")
print(f"Email ID     : {email_id}")
print("=" * 40)


# answer:
# The required student details are stored in separate variables.
# The details are displayed using formatted strings to create
# a neatly formatted student ID card.
# For the bonus, email_id is created using the student's name
# and roll number.