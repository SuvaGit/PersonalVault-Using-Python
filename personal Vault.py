import hashlib

# Define the personal vault as a dictionary
personal_vault = {}

# Define a function to add credentials to the vault
def add_credentials():
    website = input("Enter the website name: ")
    username = input("Enter the username: ")
    password = input("Enter the password: ")

    # Hash the password before storing it in the vault
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    # Add the credentials to the vault
    personal_vault[website] = {'username': username, 'password': hashed_password}

    print("Credentials added successfully.")

# Define a function to retrieve credentials from the vault
def get_credentials():
    website = input("Enter the website name: ")

    # Check if the website is in the vault
    if website in personal_vault:
        # Retrieve the hashed password from the vault
        hashed_password = personal_vault[website]['password']

        # Prompt the user for the password and hash it for comparison
        password = input("Enter the password: ")
        hashed_input_password = hashlib.sha256(password.encode()).hexdigest()

        # Compare the hashed password with the stored hashed password
        if hashed_input_password == hashed_password:
            print("Username:", personal_vault[website]['username'])
            print("Password:", personal_vault[website]['password'])
        else:
            print("Incorrect password.")
    else:
        print("Website not found in personal vault.")

# Main program loop
while True:
    print("1. Add credentials to personal vault")
    print("2. Retrieve credentials from personal vault")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_credentials()
    elif choice == '2':
        get_credentials()
    elif choice == '3':
        break
    else:
        print("Invalid choice. Please try again.")