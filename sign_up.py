# A simple sign in and sign up

# Sign up:
first_name = input("First name: ")
last_name = input("Last name: ")
username = first_name + " " + last_name
email = input("Email: ")

# Checking for power password:
while True:
    password = input("Password: more than six caracters.")
    if len(password) >= 6:
        break

# Confirmation the password:    
while True:
    confirme = input("Renter password: ")
    if confirme == password:
        break

# Store information of new user in a list:
new_users =[]
new_users.append(first_name.lower())
new_users.append(last_name.lower())
new_users.append(username.lower())
new_users.append(email.lower())
new_users.append(password)

# Greeting and Display user's information:
if new_users:
    print(f"Welcome {username.title()}!")
    print('\nYour profile:')
    print(f"First name: {first_name}")
    print(f"Last name : {last_name}")
    print(f"Email: {email}")  


# Sign in:
users = [email, password]

for user in users:
    if user in new_users:
        print(f"\nHello {username.title()}")
        break
    else:
        print("You need to sign up: ")
    
