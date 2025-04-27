import json
def load_data(filename):
    try:
        with open   (filename, 'r') as file:
            data = json.load(file)
            return data['username'], data['password']
    except FileNotFoundError:
        print("Unable to open file Lab02.json")
        return None, None
    except json.JSONDecodeError:
        print("Invalid JSON format in Lab02.json")
        return None, None
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None, None
    

def autthencation(username, password, usernames, passwords):
    try:
        if username in usernames and password == passwords[usernames.index(username)]:
            return True
        else:
            return False
    except Exception as e:  
        print(f"An error occurred during authentication: {str(e)}")
        return False
def main():
    # Load data from the JSON file
    usernames, passwords = load_data('Lab02.json')
    if usernames is None or passwords is None:
        return
    
    # Prompt user for username and password
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")

    #check if the username and password are correct
    if autthencation(username, password, usernames, passwords):
        print("You are authenticated successfully!")
    else:
        print("You are not authorized to use the system.")
if __name__ == "__main__":
    main()
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