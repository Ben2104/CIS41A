# a program to prompt the user for hours and rate per hour to compute gross pay. Rewrite the pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.

hours = float(input("Enter Hours: "))
rates = float(input("Enter Rates: "))
standardHours = 40
pay = 0
extraHours = 0
if hours > 40:
    extraHours = hours - standardHours
    pay = standardHours * rates + extraHours * 15
    print(str(pay) + " = " + str(standardHours) + " * " + str(rates) + " + " + str(extraHours) + " * 15")

else:
    pay = hours * rates

print("Pay: " + str(pay))

# Output:

# Enter Hours: 45
# Enter Rates: 15
# 675.0 = 40 * 15.0 + 5.0 * 15
# Pay: 675.0

# Enter Hours: 40
# Enter Rates: 15
# Pay: 600.0


