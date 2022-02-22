price = 1000000
has_good_credit = True

if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"Down Payment: ${down_payment}")


""" logical operators in python """
# if applications has high income AND good credit eligible for loan

has_high_income = True
if has_high_income and has_good_credit:
    print("<<<<<<<Eligible for loan")
# if applicant has high income or good credit eligible for loan
if has_high_income or has_good_credit:
    print(">>>>Eligible for loan")
# if applicant has good credit and doesnot have criminal record then they are eligible for loan
has_criminal_record = False
if has_good_credit and not has_criminal_record:
    print("Eligible for loan___________")

# comparison operators (boolean expression)
temperature = 35
if(temperature>30):
    print("It's a hot day")
elif temperature==30:
    print("It's a lovely day")
else:
    print("It's not a hot day")
"""if name is less than 3 characters long name be at least 3 characters 
otherwise if it's more than 50 characters long name can be a maximum of 50 characters
otherwise name looks good
"""
name = input("Please insert your name: ")
if len(name) < 3:
    print("name must be at least 3 characters")
elif len(name)>50:
    print("name can be a maximum of 50 characters")
else:
    print("Name looks good")