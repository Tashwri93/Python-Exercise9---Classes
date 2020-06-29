class User():

    def __init__(self, first_name, last_name , age, location, username, email ):

        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.username = username
        self.email = email
        self.login_attempts = 0


    def describe_user(self):
        print("\nFirst name: " + self.first_name.title()
        +"\nLast name: " + self.last_name.title()
        +"\nAge: " + str(self.age)
        +"\nLocation: " + self.location.title()
              +"\nUsername: " + self.username.title()
              +"\nEmail: " + self.email)
        

    def greet_user(self):
        print("Hello " + self.first_name.title() + " " +self.last_name.title())

    def increment_login_attempts(self):
        self.login_attempts += 1
        
    def reset_login_attempts(self):
        self.login_attempts = 0

user_a = User('tashan','wright-mckenzie',26,'london','tashwri93', 'tash93@gmail.com')

print("User details:")
user_a.describe_user()

print("\nAttempted Logins:")
user_a.increment_login_attempts()
user_a.increment_login_attempts()
user_a.increment_login_attempts()
print("Attempted logins: " + str(user_a.login_attempts))

print("\nResetting Logins...")

user_a.reset_login_attempts()
print("Attempted logins: " + str(user_a.login_attempts))
