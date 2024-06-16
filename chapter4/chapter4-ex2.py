# this program is asking the user to prompt their company name, hours and rates. At the end, it prints out the company name, hours, rates and the random document number and gross pay.

from random import randint

documentNumber = randint(1000, 2000)
standardHours = 40
pay = 0
extraHours = 0

while(True):
    company = input("Enter your company name: ").strip()
    
    hours = input("Enter Hours: ").strip()
    if not (hours.isdigit()):
        print("Please enter numeric input")
        continue
    rates = input("Enter Rates ($ per hour): ").strip()
    if not (rates.isdigit()):
        print("Please enter numeric input")
        continue
    else:
        hours = float(hours)
        rates = float(rates)
        if hours > 40:
            extraHours = hours - standardHours
            pay = standardHours * rates + extraHours * 15
            break
        else:
            pay = hours * rates
            break

hours = round(hours, 2)
rates = round(rates, 2)
pay = round(pay, 2)
print("Company: " + company)
print("hours: " + str(hours))
print("rates: " + str(rates))

print("*" * 46)
print("Your document number is: " + str(documentNumber))
print("Your " + company + " gross pay is " + str(pay) + " dollars.")

# Output: 
# Enter your company name: Google
# Enter Hours: 45
# Enter Rates ($ per hour): 10 
# Company: Google
# hours: 45.0
# rates: 10.0
# **********************************************
# Your document number is: 1147
# Your Google gross pay is 475.0 dollars.

# Enter your company name: Google
# Enter Hours: -1 
# Please enter numeric input
# Enter your company name: Google
# Enter Hours: 56 
# Enter Rates ($ per hour): -10
# Please enter numeric input
# Enter your company name: Facebook
# Enter Hours: 45
# Enter Rates ($ per hour): 20
# Company: Facebook
# hours: 45.0
# rates: 20.0
# **********************************************
# Your document number is: 1725
# Your Facebook gross pay is 875.0 dollars.

# Enter your company name: Netflix
# Enter Hours: 15.5
# Please enter numeric input
# Enter your company name: Netflix
# Enter Hours: 35
# Enter Rates ($ per hour): 10
# Company: Netflix
# hours: 35.0
# rates: 10.0
# **********************************************
# Your document number is: 1799
# Your Netflix gross pay is 350.0 dollars.