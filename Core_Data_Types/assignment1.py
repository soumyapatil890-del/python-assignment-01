# Problem Name: Hospital Patient Record

# Statement:
# Store:
# Patient Name
# Age
# Weight
# Is Insured
#
# Print each value with its datatype.
# Then explain why each datatype is appropriate.


# Solution:

patient_name = "Rahul"
age = 30
weight = 68.5
is_insured = True


print("Patient Name :", patient_name)
print("Datatype     :", type(patient_name))

print("Age          :", age)
print("Datatype     :", type(age))

print("Weight       :", weight)
print("Datatype     :", type(weight))

print("Is Insured   :", is_insured)
print("Datatype     :", type(is_insured))


# answer:
#
# patient_name is a str because the patient's name is text.
#
# age is an int because age is represented as a whole number.
#
# weight is a float because a patient's weight can contain
# decimal values.
#
# is_insured is a bool because insurance status has two
# logical states: True or False.