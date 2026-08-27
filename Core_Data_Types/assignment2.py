# Problem Name: Online Exam Result

# Statement:
# Store:
# Student Name
# Marks Obtained
# Percentage
# Passed (True/False)
#
# Print a result summary.
# When the student is failed, mention how many more marks
# are needed to pass.
# Passing mark = 35.


# Solution:

student_name = "Rahul"
marks_obtained = 28
percentage = marks_obtained
passed = marks_obtained >= 35


print("=" * 40)
print("          ONLINE EXAM RESULT")
print("=" * 40)
print(f"Student Name    : {student_name}")
print(f"Marks Obtained  : {marks_obtained}")
print(f"Percentage      : {percentage}%")
print(f"Passed          : {passed}")

if not passed:
    marks_needed = 35 - marks_obtained
    print(f"More Marks Needed: {marks_needed}")

print("=" * 40)


# answer:
#
# student_name is stored as a string because it contains text.
#
# marks_obtained is stored as an integer because marks are represented
# as a whole number in this example.
#
# percentage is calculated from the marks obtained.
#
# passed is a boolean expression. It becomes True when the marks
# obtained are 35 or more, otherwise it becomes False.
#
# If the student fails, marks_needed calculates the difference
# between the passing mark (35) and the marks obtained.