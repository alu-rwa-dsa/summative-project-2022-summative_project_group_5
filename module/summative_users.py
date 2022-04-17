import csv
from summative_restaurant import Restaurant
from location import *
import random


class Customers(Restaurant):
    def __init__(self, id='', fname='', lname='', phone_no='', password=''):
        super().__init__(id, fname, lname, phone_no, password)
        self.id = id
        self.fname = fname
        self.lname = lname
        self.password = password
        self.phone_no = phone_no
        self.queue = list()

    def make_order(self):

        while True:
            user_response = input("\nEnter the index of food you want to order: ")
            from csv import DictWriter
            with open("assets/menu.csv", "r") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if row['id'] == user_response:
                        while True:
                            try:
                                quantity = int(input("\nEnter the desired quantity number: "))
                            except ValueError:
                                print("The quantity should be an integer.")
                            else:
                                break
                        location = choose_location()
                        price = int(row['price']) * quantity
                        print(
                            f"\nYour order of {quantity} {row['name']} worth RWF {price} to {location} has been placed. ")
                        order_id = random.randint(100, 1000)
                        customer_order = {'order_id': order_id, 'customer_id': self.id,
                                          'fname': self.fname, 'lname': self.lname, 'location': location,
                                          'food': row['name'], 'quantity': quantity, 'price': price}
                        self.queue.append(customer_order)
                        header = ['order_id', 'customer_id', 'fname', 'lname', 'location', 'food', 'quantity', 'price']
                        with open("assets/orders.csv", "a", newline='') as ordercsv:
                            writer = csv.DictWriter(ordercsv, fieldnames=header)
                            writer = writer.writerow(customer_order)

                        self.another_order()

            print('\nKindly input the right index')
            self.make_order()

    def another_order(self):
        print("\nDo you want to place another order?\nPress:\n1. if yes\n2. Proceed to checkout")
        while True:
            try:
                user_response = int(input("Enter: "))
                if user_response == 1:
                    print("\n*** OUR MENU ***\n")
                    file = open("assets/menu.csv", "r", newline='')
                    reader = csv.DictReader(file)
                    for row in reader:
                        print(f"{(row['id'])}. {row['name']} = RWF {row['price']}")
                    self.make_order()

                elif user_response == 2:
                    self.check_out()
                else:
                    raise ValueError

            except ValueError:
                print("Please select 1 or 2")

            else:
                break

    def check_out(self):

        print(f"\n*** Order confirmed ***\n")
        amountToPay = 0
        for order in self.queue:
            amountToPay += int(order['price'])
            print("Order id: ", order['order_id'])
            print("Item: ", order['food'])
            print("Quantity: ", order['quantity'])
            print("Price: ", order['price'])
            print("Location: ", order['location'])
            print("\n")

        print(f"You will be required to PAY a total amount of {amountToPay} ON DELIVERY")
        print('\nThank you for choosing us!')
        exit()


class Admin(Restaurant):
    def __init__(self, id='', fname='', lname='', phone_no='', password=''):
        super().__init__(id, fname, lname, phone_no, password)
        self.order_list = None
        self.id = id
        self.fname = fname
        self.lname = lname
        self.password = password
        self.phone_no = phone_no

    def update_menu(self):
        while True:
            try:
                input_id = int(input("\nEnter food ID: "))
                if input_id == '':
                    raise ValueError
            except ValueError:
                print("Food id should be a number")
            else:
                break
        while True:
            try:
                input_name = input("Enter name of food: ")
                if input_name == '':
                    raise ValueError
            except ValueError:
                print("Food name can not be  empty")
            else:
                break
        while True:
            try:
                input_price = int(input("Enter price of the food: "))
                if input_price == '':
                    raise ValueError
            except ValueError:
                print("Food price should be a number")
            else:
                break

        self.foods = {"id": str(input_id), "name": input_name, "price": str(input_price)}
        header = ['id', 'name', 'price']

        with open("assets/menu.csv", "a", newline="") as menucsv:
            writer = csv.DictWriter(menucsv, fieldnames=header)
            writer.writerow(self.foods)

    def view_orders(self):
        self.order_list = []

        with open("assets/orders.csv", "r", newline='') as ordercsv:
            reader = csv.DictReader(ordercsv)
            for row in reader:
                one_food = {"order_id": row["order_id"], "customer_id": row['customer_id'], "location": row["location"],
                            "food": row["food"], "quantity": row["quantity"], "price": row["price"]}
                self.order_list.append(one_food)

            if len(self.order_list) >= 1:
                print('\n*** First Order on queue***\n')
            else:
                print('There are no orders.')
            for record in self.order_list:
                print('order_id: ', record['order_id'])
                print('customer_id: ', record['customer_id'])
                print('Location: ', record['location'])
                print('Food Item: ', record['food'])
                print('Quantity: ', record['quantity'])
                print('Price: ', record['price'])
                self.take_next_order()

    def take_next_order(self):
        file = open('assets/orders.csv', 'r')
        reader = csv.reader(file)
        # we create an empty list that will hold the orders temporarily
        list1 = []
        # we take the user input of the next order which the user wants to remove, this will be used in comparing
        # if they correspond, it will be removed
        # this if found variable is used to indicate if the data is in the csv file or not
        while True:
            order_id = input('\n Please enter order id to take this order: ')
            for i in range(len(self.order_list)):
                if self.order_list[i]['order_id'] == order_id:
                    next_order = self.order_list[i]
                    del self.order_list[i]
                    print(f"You have taken order:\n{next_order}")
                    break
            IfFound = False
            for row in reader:
                if row[0] == str(order_id):
                    IfFound = True

                else:
                    list1.append(row)
            file.close()

            # IfFound remains false that means that the information was not found and the print statement below is
            # printed
            if not IfFound:
                print('Invalid id')
                self.take_next_order()

            else:  # if it is found the file is opened again and written with the information that remained in
                # the list
                # after the order has been removed
                file = open('assets/orders.csv', 'w+', newline='')
                writer = csv.writer(file)
                writer.writerows(list1)
            file.close()
            user_input = input('When done press number 1: ')
            while True:
                if user_input == '1':
                    self.view_orders()
                else:
                    print('kindly press number 1')
                return IfFound
