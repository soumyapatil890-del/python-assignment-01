# Problem Name: Company Email Generator

# Statement:
# Store:
# First Name
# Last Name
# Company Name
#
# Create an email like:
# john.doe@abccompany.com
#
# Print:
# Original name
# Uppercase email
# Length of email


# Solution:

first_name = "John"
last_name = "Doe"
company_name = "ABCCompany"

email = first_name.lower() + "." + last_name.lower() + "@" + company_name.lower() + ".com"

original_name = first_name + " " + last_name
uppercase_email = email.upper()
email_length = len(email)


print("=" * 40)
print("       COMPANY EMAIL GENERATOR")
print("=" * 40)
print(f"Original Name : {original_name}")
print(f"Email         : {email}")
print(f"Uppercase     : {uppercase_email}")
print(f"Email Length  : {email_length}")
print("=" * 40)


# answer:
# The first name, last name, and company name are stored in variables.
# The email is created by converting the names to lowercase and
# combining them in the required email format.
# upper() converts the email to uppercase.
# len() calculates the number of characters in the email.