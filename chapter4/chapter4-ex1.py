# This program will ask the user to prompt the valid email address with '@' and '.' and find the domain of the email address 
# and print it out 
# while loop to keep looping if the user prompt an invalid email address

while(True):
    emailAddress = input("Please enter your email address: ")
    if '@' and '.' in emailAddress:
        # split the @ to get the list after @    
        domain = emailAddress.split('@')       
        # Access to the location that contains domain.com
        domain = domain[1]
        # split the . the get the list of domain_name and com
        domain_name = domain.split('.')
        # Access the location of the domain_name
        domain_name = domain_name[0]
        
        print("Domain: " + domain_name + "\n")
        break
    else:
        print("\nYou enter an invalid email, please do it again")
        
# Output:
# Please enter your email address: dohoangkhoi341@gmail.com
# Domain: gmail

# Please enter your email address: dohoangkhoi341
# You enter an invalid email, please do it again
# Please enter your email address: dohoangkhoi341@yahoo.com
# # Domain: yahoo

