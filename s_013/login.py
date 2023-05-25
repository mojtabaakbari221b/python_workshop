class PasswordError(Exception):
    pass


def password_validator(password):
    if len(password) >= 8 :
        return password
    else :
        raise PasswordError("your password less than 8 char.")

def username_validator(username):
    if len(username) >= 5 :
        return username
    else :
        raise Exception("your username not valid.")

print(password_validator("1234567"))
# print(username_validator("amin"))