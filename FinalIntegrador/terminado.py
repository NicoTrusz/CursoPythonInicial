import json

# Function to create a user
def create_user(username, password):
    if username in users:
        print("The username already exists.")
    else:
        users[username] = password
        print("User created successfully!")

# Function to log in
def login():
    for attempts in range(3):
        print("*" * 30)
        print("Option >>> 2")
        username = input("Enter username: ")
        password = input("Enter password: ")
        if username in users and users[username] == password:
            print("Login successful!")
            break
        elif attempts < 2:
            print(f"Try again. Attempts: {attempts + 1}")
        else:
            print(f"Attempts: {attempts + 1}\nUser blocked")

# Function to save users to a file
def save_users_to_file(filename, format):
    with open(filename, 'w') as file:
        if format == 'txt':
            for username, password in users.items():
                file.write(f"{username}: {password}\n")
        elif format == 'json':
            json.dump(users, file, indent=4)

# Variables
users = {}  # Dictionary to store users and passwords

# Menu
while True:
    print("*" * 30)
    option = input("* Menu *\n1_Create User\n2_Login\n3_Save and Exit\nYour option is: ")

    if option == "1":  # Create user
        print("*" * 30)
        print("Option >>> 1")
        new_user = input("Enter username: ")
        new_password = input("Enter password: ")
        create_user(new_user, new_password)

    elif option == "2":  # Login
        login()

    elif option == "3":  # Save and Exit
        save_format = input("Enter the format to save (txt/json): ").lower()
        save_users_to_file('users_data.' + save_format, save_format)
        print("*" * 30)
        print("Option >>> 3")
        print('''Thank you for using our app
        End of program''')
        break

    else:
        print("*" * 30)
        print("The option does not match any.")
        