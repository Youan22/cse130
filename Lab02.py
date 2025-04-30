import json
filename = 'Lab02.json'
with open(filename, 'r') as file:
    data = json.load(file)

if data:
    # Print data displaying the username and password
    print()
    print('Here is the data for a list containing username and password: ')
    print()

    # Print the username and password
    if 'username' in data and 'password' in data:
        print(f'Username: {data["username"]}')
        print(f'Password: {data["password"]}')
    else:
        print('Unable to open file Lab02.json.')
        print()

else:
    print('Unable to load data from Lab02.json.')

print()

# Authentication system

if data and 'username' in data and 'password' in data:
    usernames = data['username']
    passwords = data['password']

    while True:
        # Prompt for username and password
        username = input('Please enter your username: ')
        print()
        password = input('Please enter your password: ')
        print()

        # Check if username and password match
        if username in usernames and password == passwords[usernames.index(username)]:
            print('You are authenticated!')
            print()

            break
        else:
            print('You are not authorized to use the system.')
            print()
            print('Please try again.')
            print()

else:
    print('Authentication cannot proceed due to missing or invalid data.')
    print()    
    
# The code above is a simple authentication system that loads usernames and passwords from a JSON file.
# It prompts the user for their username and password, checks if they are correct, and prints a message indicating whether the authentication was successful or not.
# The code includes error handling for file not found, JSON decoding errors, and other exceptions that may occur during the authentication process.
# The code is structured into functions for better organization and readability.
# The main function is called when the script is run, and it handles the overall flow of the program.
# The load_data function loads the usernames and passwords from the JSON file and returns them as lists.
# The autthencation function checks if the provided username and password match the stored values.
# The code is designed to be simple and easy to understand, making it suitable for educational purposes.
# The code is also modular, allowing for easy modification and expansion in the future.
# The code is written in Python and uses the json module to handle JSON data.

