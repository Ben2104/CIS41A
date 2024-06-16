# Hoang Khoi Do
# This program prompt the user for hours and rate per hour to compute gross pay. Also, your pay computation gives the employee 1.5 times the hourly rate for hours worked above 40 hours. Also it also checks if the user enter non-numeric input.

standardHours = 40
pay = 0
extraHours = 0

hours = input("Enter Hours: ")
if not (hours.isdigit()):
    print("Please enter numeric input")
    exit()
    
rates = input("Enter Rates: ")
if not (rates.isdigit()):
    print("Please enter numeric input")
    exit()
else:
    hours = float(hours)
    rates = float(rates)
    if hours > 40:
        extraHours = hours - standardHours
        pay = standardHours * rates + extraHours * 15
        print(str(pay) + " = " + str(standardHours) + " * " + str(rates) + " + " + str(extraHours) + " * 15")
    else:
        pay = hours * rates

print("Pay: " + str(pay))

# output:
# Enter Hours: 20
# Enter Rates: nine
# Please enter numeric input

# Enter Hours: forty
# Please enter numeric input

# Enter Hours: 45
# Enter Rates: 10 
# 475.0 = 40 * 10.0 + 5.0 * 15
# Pay: 475.0

