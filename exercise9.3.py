class User():

    def __init__(self, first_name, last_name , age, location ):

        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location


    def describe_user(self):
        print("\nFirst name: " + self.first_name.title()
        +"\nLast name: " + self.last_name.title()
        +"\nAge: " + str(self.age)
        +"\nLocation: " + self.location.title())

    def greet_user(self):
        print("Hello " + self.first_name.title() + " " +self.last_name.title())


user_a = User('tashan','wright-mckenzie',26,'london')
user_a.describe_user()
user_a.greet_user()

user_b = User('dylan','kawende',23,'london')
user_b.describe_user()
user_b.greet_user()        
