# Problem Name: Variable Naming Inspector

# Statement:
# You receive these variable names:
#
# EmployeeName
# employee_name
# employee-name
# employeeName
# Employee_Name
# employee1
# 1employee
#
# Tasks:
# 1. Identify valid names.
# 2. Rewrite invalid ones.
# 3. Mention which names follow Python best practices.


# Solution:

# answer:
#
# EmployeeName
# Valid variable name.
# It does not follow the recommended snake_case style.
#
# employee_name
# Valid variable name.
# Follows the recommended snake_case style.
#
# employee-name
# Invalid variable name because '-' is treated as the subtraction
# operator.
# Recommended rewrite: employee_name
#
# employeeName
# Valid variable name.
# It uses camelCase, but snake_case is preferred in Python.
# Recommended rewrite: employee_name
#
# Employee_Name
# Valid variable name.
# However, uppercase letters are generally avoided for ordinary
# variable names.
# Recommended style: employee_name
#
# employee1
# Valid variable name.
#
# 1employee
# Invalid variable name because a variable name cannot start with
# a number.
# Recommended rewrite: employee1
#
# Final Answer:
#
# Valid:
# EmployeeName
# employee_name
# employeeName
# Employee_Name
# employee1
#
# Invalid:
# employee-name
# 1employee
#
# Best practice:
# employee_name