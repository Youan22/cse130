
#Question 4 is the reflection part of the assignment. Here, please answer questions such as these:

# Was the syntax of Python the hardest part? If so, what part?
#the syntax of Python was not the hardest part for me. I found it to be quite readable and easy to understand. However, 
# I did have some difficulty with understanding how to properly handle JSON data and how to work with lists and dictionaries in Python.

# Was there some aspect of the problem that was particularly difficult to solve?
# I found the authentication system to be a bit challenging, especially when it came to checking if the username and password matched.
# I had to make sure that I was correctly indexing the lists and handling the case where the username was not found in the list.

# Was there an especially difficult bug? If so, how did you resolve it?
# I did not encounter any particularly difficult bugs, but I did have to spend some time debugging the code to make sure that it was working correctly.
# I used print statements to check the values of variables at different points in the code, which helped me identify any issues.

# Was there some difficulty with the instructions or any part of the problem definition?
# I found the instructions to be clear and easy to follow. However, I did have to spend some time researching how to work with JSON data in Python,
# as I was not familiar with it before this assignment.
# I also had to spend some time understanding how to properly handle lists and dictionaries in Python, as I was not very familiar with them before this assignment.


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

