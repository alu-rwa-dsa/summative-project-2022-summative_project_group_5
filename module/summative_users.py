import csv
from summative_restaurant import Restaurant
from location import *
import random


class Customers(Restaurant):
    # initialised the attributes that will be required when creating an object
    def __init__(self, id='', fname='', lname='', phone_no='', password=''):
        super().__init__(id, fname, lname, phone_no, password)
        self.id = id
        self.fname = fname
        self.lname = lname
        self.password = password
        self.phone_no = phone_no
        self.queue = list()

    # this mwthod allows the customer to make an order
    def make_order(self):
        while True:
            user_response = input("\nEnter the index of food you want to order: ")
            from csv import DictWriter
            # the menu is opened for the customer to have a look at it
            with open("assets/menu.csv", "r") as csvfile:
                reader = csv.DictReader(csvfile)
                # when the customer enters the index of a certain food
                # it is confirmed if the food is actually in the menu
                # if it is there the customer proceeds with the order placement
                for row in reader:
                    if row['id'] == user_response:
                        while True:
                            try:
                                quantity = int(input("\nEnter the desired quantity number: "))
                            except ValueError:
                                print("The quantity should be an integer.")
                            else:
                                break
                        # the customer is asked about the location that they are in
                        # this is to allow the system to calculate the distance and time taken for the delivery
                        location = choose_location()
                        price = int(row['price']) * quantity
                        print(
                            f"\nYour order of {quantity} {row['name']} worth RWF {price} to {location} has been placed. ")
                        # we generate a random order id that will identify the orders differently
                        # these order ids will enable the restaurant to take them from the queue systematically
                        order_id = random.randint(100, 1000)
                        customer_order = {'order_id': order_id, 'customer_id': self.id,
                                          'fname': self.fname, 'lname': self.lname, 'location': location,
                                          'food': row['name'], 'quantity': quantity, 'price': price}
                        self.queue.append(customer_order)
                        header = ['order_id', 'customer_id', 'fname', 'lname', 'location', 'food', 'quantity', 'price']
                        # the order is then placed to the csv file of the orders
                        with open("assets/orders.csv", "a", newline='') as ordercsv:
                            writer = csv.DictWriter(ordercsv, fieldnames=header)
                            writer = writer.writerow(customer_order)

                        self.another_order()

            print('\nKindly input the right index')
            self.make_order()

    # this method asks the user if they want to place another order
    # then the same process of placing an order is repeated all over again
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

    # after the customer has placed an order and is satisfied, this method is called
    # the customer is able to log out of the system
    def check_out(self):
        print(f"\n*** Order confirmed ***\n")
        amountToPay = 0
        # everything that hte customer orders is printed out for them
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

# this class is for the admin of the restaurant
class Admin(Restaurant):
    def __init__(self, id='', fname='', lname='', phone_no='', password=''):
        super().__init__(id, fname, lname, phone_no, password)
        self.order_list = None
        self.id = id
        self.fname = fname
        self.lname = lname
        self.password = password
        self.phone_no = phone_no

    # the admin is able to update the menu
    def update_menu(self):
        # the admin enters the different details that needs to be added to the menu
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
        # the menu csv is fetched so that it could be updated
        self.foods = {"id": str(input_id), "name": input_name, "price": str(input_price)}
        header = ['id', 'name', 'price']
        # all the details are appended to the menu csv
        with open("assets/menu.csv", "a", newline="") as menucsv:
            writer = csv.DictWriter(menucsv, fieldnames=header)
            writer.writerow(self.foods)

    # the admin is able to view the orders using this method
    def view_orders(self):
        # this list will be holding the orders that have been retrieved from the csv file
        self.order_list = []

        with open("assets/orders.csv", "r", newline='') as ordercsv:
            reader = csv.DictReader(ordercsv)
            for row in reader:
                one_food = {"order_id": row["order_id"], "customer_id": row['customer_id'], "location": row["location"],
                            "food": row["food"], "quantity": row["quantity"], "price": row["price"]}
                # we loop through the orders in the csv
                # then it gets appended to the list as a dictionary
                self.order_list.append(one_food)
            # this if statement checks if there are still orders in the list
            # if the orders are not there it informs the admin that the orders are over
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

    # when an admin has finished taking an order they should be able to take the next order
    # then the order that has been taken should be removed from the list and the csv
    def take_next_order(self):
        file = open('assets/orders.csv', 'r')
        reader = csv.reader(file)
        # we create an empty list that will hold the orders temporarily
        list1 = []
        # we take the user input of the next order which the user wants to remove, this will be used in comparing
        # if they correspond, it will be removed
        # this if found variable is used to indicate if the data is in the csv file or not
        while True:
            # the user inputs the order id
            # the order id is checked if it is in the queue then it is deleted
            order_id = input('\n Please enter order id to take this order: ')
            for i in range(len(self.order_list)):
                if self.order_list[i]['order_id'] == order_id:
                    next_order = self.order_list[i]
                    del self.order_list[i]
                    print(f"You have taken order:\n{next_order}")
                    break
            IfFound = False
            # if the id that  the admin has put is in the list it means it is in the csv as well
            # we use this for loop to check if the data is in the csv
            for row in reader:
                if row[0] == str(order_id):
                    # the variable is changed to true if the data is there in the csv
                    IfFound = True

                else:
                    # the rest of the ids that are not in the csv are  appended to the empty list that we created

                    list1.append(row)
            file.close()

            # IfFound remains false that means that the information was not found and the print statement below is
            if not IfFound:
                print('Invalid id')
                self.take_next_order()

            else:  # if it is found the file is opened again and written with the information that
                # was appended to the empty list above
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
#             the process keeps on repeating until all the orders are done
