class Restaurant():

    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
      long_name =  "This restaurant is called " + self.restaurant_name + " This type of cuisine is " + self.cuisine_type
      return long_name.title()
    
    def open_restaurant(self):
        print(self.restaurant_name.title() + " is open.")

    def set_number_served(self, served):
        self.number_served = served

    def increment_number_served(self, addon):
        self.number_served += addon
        


restaurant = Restaurant('nandos', 'portugese')


print(restaurant.describe_restaurant())
restaurant.open_restaurant()


print("\nNumber served: " + str(restaurant.number_served))
restaurant.number_served = 430

print("\nNumber served: " + str(restaurant.number_served))

restaurant.set_number_served(500)
print("\nNumber served: " + str(restaurant.number_served))

restaurant.increment_number_served(100)
print("\nNumber served: " + str(restaurant.number_served))
