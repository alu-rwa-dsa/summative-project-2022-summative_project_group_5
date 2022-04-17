from summative_users import Customers
from summative_users import Admin
import csv

# we created some dummy users just to ensure that our csv works well in the storage of data
mike = Customers('10', 'Mike', 'Kip', '1000', '100000')
Patch = Customers('20', 'Patch', 'Pati', '2000', '200000')

customer_details = [[10, 'Mike', 'Kip', 1000, 100000], [20, 'Patch', 'Pati', 2000, 200000]]
# appending the agent object to the empty list above, the list will be used when storing the data into a csv file

# ---> wrote the data into a csv file
# ---> commented out so that whn the programme id run again it cannot be written all over
# header = ["id", "fname", "lname", "password", "phone_no"]
# with open("admin_details.csv", "w+", newline="") as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(header)
#     writer.writerows(customer_details)


# this method is for displaying the menu of the restaurant
def main():
    print("\nWelcome to KFC HOME DELIVERY \n")
    print("*** OUR MENU ***\n")
    # the files from the csv is opened in read mode so that it could be displayed for the customers
    file = open("assets/menu.csv", "r", newline='')
    reader = csv.DictReader(file)
    for row in reader:
        print(f"{(row['id'])}. {row['name']} = RWF {row['price']}")
    print("\nWould you like to place an order? \n")
    print("Kindly, login or register\n\n1. Login\n2. Register\n\n3. ADMIN LOGIN")
    # the while loop ensures that the user the correct input to the system
    while True:
        try:
            user_response = int(input("\nenter: "))
            if user_response == 1:
                login()
            elif user_response == 2:
                register()
            elif user_response == 3:
                admin_login()
            else:
                raise ValueError

        except ValueError:
            print("\nWrong input, try again!")
        else:
            break

# this function is for the user to log into the system
# the user is asked his/her id and the password
def login():
    while True:
        user_id = input("\nInput your user ID: ")
        password = input("Input your password: ")
        if len(user_id) == 0 or len(password) == 0:
            print("user_id or password can not be empty")
            login()

        count = 0
        # the information that the user inputs is crosschecked with what is there in the system
        # if the information is available the user is allowed to log in but if it is not available the user
        # cannot log in, instead they are taken to another function that asks them to register into the system
        with open("assets/customer_details.csv", "r") as acsvfile:
            reader = csv.DictReader(acsvfile)
            for row in reader:
                if row['id'] == user_id and row['password'] == password:
                    print(f"\nHello {row['fname']}, welcome back")
                    count += 1
                    customer = Customers(row['id'], row['fname'], row['lname'], row['password'], row['phone_no'])
                    # after a customer has logged in they can see the menu again so that they can make their choice
                    customer.view_menuu()
                    # after seeing the menu the can make their order of what they would like to have
                    customer.make_order()
                    break

            # if we check in the csv and notice that the info is not there we prompt the
            # user to create an account with us
            if count == 0:
                print("\nYou do not have an account\nWould you want to register?")
                user_response = int(input("\n1. Yes\n2. No\nEnter: "))
                while True:
                    if user_response == 1:
                        register()
                    elif user_response == 2:
                        main()
                    else:
                        print("\nWrong input, try again.")

# this is particularly for the restaurant part
# they only have a login since there are only a few particular admins in the system
def admin_login():
    while True:
        user_id = input("Input your user ID: ")
        password = input("Input your password: ")
        if len(user_id) == 0 or len(password) == 0:
            print("user_id or password can not be empty")
            admin_login()
        count = 0
        # the data is fetched from the csv and confirmed if the details are true
        # then the admin will be able to log into the system
        with open("assets/admin_details.csv", "r") as acsvfile:
            reader = csv.DictReader(acsvfile)
            for row in reader:
                if row['id'] == user_id and row['password'] == password:
                    print(f"Hello {row['fname']}, welcome back")
                    count += 1
                    admin = Admin(row['id'], row['fname'], row['lname'], row['password'], row['phone_no'])
                    action(admin)
                    # admin.take_next_order()
                    break
            if count == 0:
                print("wrong input, try again.")

# after the admin has logged in a number of actions that they want to perform is asked to them
# they choose whatever they want to do at that particular time
def action(admin):
    print('\nWhat would you like to do?\npress\n1. to check orders\n2. to update menu\n3. to view menu\n4. to exit')
    user_response = input('Enter: ')
    if user_response == '1':
        Admin.view_orders(admin)
    elif user_response == '2':
        Admin.update_menu(admin)
    elif user_response == '3':
        Admin.view_menuu(admin)
    elif user_response == '4':
        print("Goodbye, Have a great day!")
        exit()
    else:
        print("Kindly input one of the choices given above")
    action(admin)


# if the user does not have an account this function is called to allow them to create an account
def register():
    print("\nWelcome to registration\nPlease input your details below\n")
    # the while loops ensures that the details are put and that they are correct details
    while True:
        try:
            while True:
                try:
                    user_id = input("National ID: ")
                    if user_id == '':
                        raise ValueError
                except ValueError:
                    print("National ID cannot be empty")
                else:
                    break
            while True:
                try:
                    user_fname = str(input("First Name: "))
                    if user_fname == '':
                        raise ValueError
                except ValueError:
                    print("First name cannot be empty")
                else:
                    break
            while True:
                try:
                    user_lname = str(input("Last Name: "))
                    if user_lname == '':
                        raise ValueError
                except ValueError:
                    print("Last name cannot be empty")
                else:
                    break
            while True:
                try:
                    user_phone_no = int(input("Phone Number: "))
                except ValueError:
                    print("Phone number should be numerical")
                else:
                    break
            while True:
                try:
                    user_password = input("Password: ")
                    if user_password == '':
                        raise ValueError
                except ValueError:
                    print("Password cannot be empty")
                else:
                    break
            while True:
                user_confirm_password = input("Confirm Password: ")
                if user_password == user_confirm_password:
                    break
                else:
                    print("password does not match")
            # an object is created the moment that the user finishes to input their data
            new_customer = Customers(user_id, user_fname, user_lname, user_phone_no, user_password)
            # the information about the user is stored in a persistent storage so that next time they would
            # be able to log into the system using the data that is already there in the system
            new_customer_dict = {"id": user_id, "fname": user_fname, "lname": user_lname, "password": user_password,
                                 "phone_no": user_phone_no}
            header = ['id', 'fname', 'lname', 'password', 'phone_no']
            from csv import DictWriter
            # we open the CSV file in append mode
            # Then, for the CSV file, create a file object
            with open('assets/customer_details.csv', 'a', newline='') as csvfile:
                # we passed the CSV  file object to the Dictwriter() function
                dictwriter_object = DictWriter(csvfile, fieldnames=header)
                # then pass the data in the dictionary as an argument into the writerow() function
                dictwriter_object.writerow(new_customer_dict)
                csvfile.close()
            new_customer.view_menuu()
            new_customer.make_order()
        except ValueError:
            print("please input integers")

        else:
            break


main()
