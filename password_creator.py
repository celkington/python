#This is a function that prompts the user to create a password. The password must consist of at least 8 characters, contain
#at least one lowercase letter contain at least one uppercase letter contain at least one number contain at least one special character.

#The user will then be prompted to re-enter their selected password to verify that the password was typed in correctly.

#This function will need to be edited later on to include an upper length limit to the password as well as well as ensuring 
#that the password is stored into a relational database upon successful password verification.

def validate():
    import re
    while True:
        password_creation = input(str("Enter a password: "))
        if len(password_creation) < 8:
            print("Make sure your password is at lest 8 characters. ")
        elif re.search('\d', password_creation) is None:
            print("Make sure your password contains a number. ")
        elif re.search('[A-Z]', password_creation) is None:
            print("Make sure your password contains an upper case letter. ")
        elif re.search('[a-z]', password_creation) is None:
            print("Make sure your password contains a lower case letter. ")
        elif re.search('[!£$_=+\'?><,.{}\[\]%|`¬^&*@~#\"]', password_creation) is None:
            print("Make sure your password contains a special character. ")
        else:
            print("Password valid. ")
            break
    password_confirmation = input(str("Confirm your password by re-entering it. "))
    if password_confirmation == password_creation:
        print("Password confirmation completed. "
              "We have successfully created an account."
              "You must now log in to access your account. ")
    else:
        password_confirmation = False
        print("Error. Your password doesn't match the password you entered above.")
        return


validate()
