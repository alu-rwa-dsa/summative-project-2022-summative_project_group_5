import csv

# this is the parent class of all the classes that we have in this project
class Restaurant:
    # we initialise the attributes that should be passed when creating an object
    def __init__(self, id='', fname='', lname='', phone_no='', password=''):
        self.id = id
        self.fname = fname
        self.lname = lname
        self.password = password
        self.phone_no = phone_no
        self.foods = {}
    # the view menu is in the main class as it allows both the customers and the admin to access
    def view_menuu(self):
        print("\nWelcome to KFC HOME DELIVERY \n")
        print("*** OUR MENU ***\n")
        # the menu is fetched from the csv and displayed to the user or the admin
        file = open("assets/menu.csv", "r", newline='')
        reader = csv.DictReader(file)
        for row in reader:
            print(f"{(row['id'])}. {row['name']} = RWF {row['price']}")
