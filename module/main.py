from summative_users import Customers
from summative_users import Admin
import csv

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
    file = open("assets/menu.csv", "r", newline='')
    reader = csv.DictReader(file)
    for row in reader:
        print(f"{(row['id'])}. {row['name']} = RWF {row['price']}")
    print("\nWould you like to place an order? \n")
    print("Kindly, login or register\n\n1. Login\n2. Register\n\n3. ADMIN LOGIN")

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


def login():
    while True:
        user_id = input("\nInput your user ID: ")
        password = input("Input your password: ")
        if len(user_id) == 0 or len(password) == 0:
            print("user_id or password can not be empty")
            login()

        count = 0
        with open("assets/customer_details.csv", "r") as acsvfile:
            reader = csv.DictReader(acsvfile)
            for row in reader:
                if row['id'] == user_id and row['password'] == password:
                    print(f"\nHello {row['fname']}, welcome back")
                    count += 1
                    customer = Customers(row['id'], row['fname'], row['lname'], row['password'], row['phone_no'])
                    customer.view_menuu()
                    customer.make_order()
                    break

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


def admin_login():
    while True:
        user_id = input("Input your user ID: ")
        password = input("Input your password: ")
        if len(user_id) == 0 or len(password) == 0:
            print("user_id or password can not be empty")
            admin_login()
        count = 0
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


def register():
    print("\nWelcome to registration\nPlease input your details below\n")

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

            new_customer = Customers(user_id, user_fname, user_lname, user_phone_no, user_password)

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
