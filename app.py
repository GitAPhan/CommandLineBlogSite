import dbi as d

# Exception to catch if username exceeds 100char
class UsernameTooLong(Exception):
    pass

# welcome message
print('---Welcome to CLB!---')
print('---------------------')
print("")

while True:
    try:
        # username prompt
        username = input('Enter your username: ')
        if len(username) > 100:
            raise UsernameTooLong
        else:
            break
    except UsernameTooLong:
        print('The username you have entered is too long!')
        print('---------------------')
        print("")

print('Hello,', username)
print("")
print('---------------------')

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

    try:    
        if selection is '1':
            options[selection](username)
        else:
            options[selection]()
    except KeyError:
        print('please enter valid selection')
    print("")
    print('---------------------')