class Restaurant():

    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("This restaurant is called " + self.restaurant_name.title())
        print("This type of cuisine is " + self.cuisine_type.title())

    def open_restaurant(self):
        print(self.restaurant_name.title() + " is open.")


restaurant_a = Restaurant('nandos', 'portugese')

print(restaurant_a.restaurant_name.title())
print(restaurant_a.cuisine_type.title())

restaurant_a.describe_restaurant()
restaurant_a.open_restaurant()
