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
        self.privileges = []


    def show_privileges(self):
        print("Admin's set of privileges: ")
        for privileges in self.privileges:
            print(privileges)

admin = Admin('sam','smith',34,'liverpool','sam_smith33','sam_smith@gmail.com')
admin.privileges = ['can add post', 'can delete post', 'can ban user']
admin.show_privileges()
    
