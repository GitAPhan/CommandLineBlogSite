import dbi as d
from getpass import getpass
from mariadb import IntegrityError

# Exception: username exceeds 100char


class UsernameTooLong(Exception):
    pass

# Exception: username is not in database


class NonExistentUsername(Exception):
    pass

# Exception: incorrect password


class IncorrectPassword(Exception):
    pass

# Exception: incorrect password


class PasswordTooLong(Exception):
    pass


# welcome message
print('---Welcome to CLB!---')
print('---------------------')
print("")


while True:
    try:
        # login or signup prompt
        print('Login or signup?')
        print('press 1: login')
        print('press 2: signup')
        choice = input('make your selection now: ')
        print('')
        print('---------------------')

        # empty choice
        choices = {
            '1': 1,
            '2': 2
        }
        # check to see if the user make a correct choice
        choice = choices[choice]
        break
    except KeyError:
        print("That is not a valid option")
        print("please try again")

# conditional to run this loop if user chooses option 2
if choice == 2:
    while True:
        try:
            # prompt user for signup info
            username = input('Enter desired username: ')
            password = input('Enter your password: ')
            # validating user input
            if len(username) > 100:
                raise UsernameTooLong
            elif len(password) > 100:
                raise PasswordTooLong

            d.BlogActions.create_user(username, password)
            break
        except IntegrityError:
            print('Oops! Looks like someone already has taken this username')
            print('Please choose a different username')
            print('---------------------')
            print("")
        except UsernameTooLong:
            print('The username you have entered is too long!')
            print('Please choose a shorter username')
            print('---------------------')
            print("")
        except PasswordTooLong:
            print('The password you have entered is too long!')
            print('Please choose a shorter password')
            print('---------------------')
            print("")

# user login loop
else:
    while True:
        try:
            # username
            username = []  # this will clear the variable after loop
            username = input('Enter your username: ')

            # grabbing key to compare to user input, username check is also triggered here
            # IndexError means username not existent
            validate_key = d.BlogActions.login(username)[0][0]

            # password prompt
            password = getpass()

            # password check
            if validate_key != password:
                raise IncorrectPassword
            break
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
