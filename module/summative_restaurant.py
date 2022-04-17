import csv


class Restaurant:
    def __init__(self, id='', fname='', lname='', phone_no='', password=''):
        self.id = id
        self.fname = fname
        self.lname = lname
        self.password = password
        self.phone_no = phone_no
        self.foods = {}

    def view_menuu(self):
        print("\nWelcome to KFC HOME DELIVERY \n")
        print("*** OUR MENU ***\n")
        file = open("assets/menu.csv", "r", newline='')
        reader = csv.DictReader(file)
        for row in reader:
            print(f"{(row['id'])}. {row['name']} = RWF {row['price']}")
