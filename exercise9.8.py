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


        

class Admin(User):

    def __init__(self, first_name, last_name , age, location, username, email):
        super().__init__(first_name, last_name, age, location, username, email)
        self.privileges = Privileges()

class Privileges():

    def __init__(self):
        self.privileges = []
    
    def show_privileges(self):
        print("Admin's set of privileges: ")
        if self.privileges:
            for privileges in self.privileges:
                print(" - " + privileges)
        else:
            print(" - This user does not have privileges.")




admin = Admin('sam','smith',34,'liverpool','sam_smith33','sam_smith@gmail.com')
admin.describe_user()

print("\n")

admin.privileges.show_privileges()

admin_privileges= ['can reset password', 'can delete account', 'can add users']
admin.privileges.privileges = admin_privileges

print("\n")
admin.privileges.show_privileges()




