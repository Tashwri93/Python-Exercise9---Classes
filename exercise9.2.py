class Restaurant():

    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("\nThis restaurant is called " + self.restaurant_name.title())
        print("This type of cuisine is " + self.cuisine_type.title())

    def open_restaurant(self):
        print(self.restaurant_name.title() + " is open.")


restaurant_a = Restaurant('nandos', 'portugese')
restaurant_b = Restaurant('wasabi', 'japanese')
restaurant_c = Restaurant('costa', 'italian')

restaurant_a.describe_restaurant()
restaurant_b.describe_restaurant()
restaurant_c.describe_restaurant()

