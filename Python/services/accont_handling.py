from services.json_ops import append_to_json, read_from_json
import re

# validation that the email is in the system
def email_exists(email, filename = "data/accounts.json"):
    accounts = read_from_json(filename)

    for account in accounts:
        if account["email"] == email:
            return account
    
    return None

def validate_input(type, input):
    emailValidationRegex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    NameValidationRegex =  r'^[A-Za-z ]+$'

    if type == 'email':        
        if re.match(emailValidationRegex, input):
            return True
    elif type == 'name':
        if re.match(NameValidationRegex, input) and input <= 10:
            return True
    elif type == 'password':
        if len(input) >= 5:
            return True        
    return False

def validate_and_register_user(email, firstName, lastName, password, phone):
    # check if the email is in the correct format
    if not validate_input('email', email):
        flashMessage = "Invalid email format!"
        flashMessageType = "authenticationError"
        return (False, flashMessage, flashMessageType)

    # check if the email already exists
    if email_exists(email) is not None:
        flashMessage = "An account with this email has already been created!"
        flashMessageType = "authenticationError"
        return (True, flashMessage, flashMessageType)

    # validate name format
    if not validate_input('name', firstName) or not validate_input('name', lastName):
        flashMessage = "Invalid name format! At least 10 characters long and letters only!"
        flashMessageType = "authenticationError"
        return (False, flashMessage, flashMessageType)

    # validate password format
    if not validate_input('password', password):
        flashMessage = "Invalid password format! Password should be at least 5 characters long!"
        flashMessageType = "authenticationError"
        return (False, flashMessage, flashMessageType)
    
    # if everything is good, we create a new account and redirect to Login page
    newAccount = {
        "email": email,
        "password": password,
        "name": firstName,
        "lastName": lastName,
        "phone": phone,
        "role": "customer"
    }
    
    append_to_json("Python/data/accounts.json", newAccount)

    return (True, "Log in to verify your account.", "messageToUser")

def validate_and_login_user(email, password):
    account = email_exists(email)
    
    # check if the email is in the correct format
    if not validate_input('email', email):
        flashMessage = "Invalid email format!"
        flashMessageType = "authenticationError"
        redirectURL = "/login"
        return False, flashMessage, flashMessageType, redirectURL, None

    # check if the email exists
    if not account:
        flashMessage = "No account with this email address! You have to create an account first!"
        flashMessageType = "authenticationError"
        redirectURL = "/register"
        return False, flashMessage, flashMessageType, redirectURL, None

    # validate password
    if account["password"] != password:
        flashMessage = "Incorrect password!"
        flashMessageType = "authenticationError"
        redirectURL = "/login"
        return False, flashMessage, flashMessageType, redirectURL, None

    # redirect URL based on the account role
    redirectURL = "/" if account["role"] == "customer" else "owner_page"

    return True, "Login successful.", "messageToUser", redirectURL, account