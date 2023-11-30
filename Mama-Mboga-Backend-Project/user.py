class User:
    def __init__(self, username, email, password, firstName, lastName,confirm_password, phoneNumber):
        self.username = username
        self.email = email
        self.password = password
        self.confirm_password=confirm_password
        self.firstName = firstName
        self.lastName = lastName
        self.phoneNumber = phoneNumber