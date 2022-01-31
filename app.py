import dbi as d
from getpass import getpass

# Exception: username exceeds 100char
class UsernameTooLong(Exception):
    pass

# Exception: username is not in database
class NonExistentUsername(Exception):
    pass

# Exception: incorrect password
class IncorrectPassword(Exception):
    pass

# welcome message
print('---Welcome to CLB!---')
print('---------------------')
print("")

while True:
    try:
        # username 
        username = [] # this will clear the variable after loop
        username = input('Enter your username: ')

        # grabbing key to compare to user input, username check is also triggered here
        validate_key = d.BlogActions.login(username)[0][0] #IndexError means username not existent

        # password prompt
        password = getpass()
        
        # password check
        if validate_key != password:
            raise IncorrectPassword

        # conditional to determine if username entered is too long
        if len(username) > 100:
            raise UsernameTooLong
        else:
            break
    except UsernameTooLong:
        print('The username you have entered is too long!')
        print('---------------------')
        print("")
    except IndexError:
        print("It looks like you aren't in the system...")
        print("please try again")
        print('---------------------')
        print("")
    except IncorrectPassword:
        print("You have entered an incorrect password!")
        print("please try again")
        print('---------------------')
        print("")


print('Hello,', username)
print("")
print('---------------------')

# loop
while True:
    # options prompt
    print('You have 3 options')
    print('Press 1: Write a blog post')
    print('press 2: See all blog posts')
    print('press 3: Leave CLB')
    selection = input('make your selection now: ')

    # dictionary containing possible actions
    options = {
        '1': d.BlogActions.submit_blog,
        '2': d.BlogActions.view_blog,
        '3': exit
    }

    print('---------------------')
    print("")

    # conditional to determine if function requires argument of username
    try:    
        if selection == '1':
            options[selection](username)
        else:
            options[selection]()
    # this will catch any errors if the user enters anything other than the available inputs
    except KeyError:
        print('please enter valid selection')
    print("")
    print('---------------------')