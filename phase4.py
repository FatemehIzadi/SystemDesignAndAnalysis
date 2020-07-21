class reciept:
    def __init__(self, f_p, s):
        self.final_price = f_p
        self.status = s


class payment_ctrl:
    def request_for_payment(self, my_test_request1):
        return my_test_request1.get_total_price()

    def make_reciept(self, price):
        self.my_reciept = reciept(price, "unpaid")
        return self.my_reciept


class time_slot:
    def __init__(self, d, t, n):
        self.my_date = d
        self.my_time = t
        self.my_number = n


class daily_catalog:
    def __init__(self, t1, t2, t3, t4, t5):
        self.time_slot1 = t1
        self.time_slot2 = t2
        self.time_slot3 = t3
        self.time_slot4 = t4
        self.time_slot5 = t5

    def show_list_of_time(self):
        print(self.time_slot1.my_date)
        print(self.time_slot1.my_time)
        print(self.time_slot1.my_number)
        print("\n")
        print(self.time_slot2.my_date)
        print(self.time_slot2.my_time)
        print(self.time_slot2.my_number)
        print("\n")
        print(self.time_slot3.my_date)
        print(self.time_slot3.my_time)
        print(self.time_slot3.my_number)
        print("\n")
        print(self.time_slot4.my_date)
        print(self.time_slot4.my_time)
        print(self.time_slot4.my_number)
        print("\n")
        print(self.time_slot5.my_date)
        print(self.time_slot5.my_time)
        print(self.time_slot5.my_number)
        print("\n")

    def get_time(self, time_number):
        if (self.time_slot1.my_number == time_number):
            return self.time_slot1
        if (self.time_slot2.my_number == time_number):
            return self.time_slot2
        if (self.time_slot3.my_number == time_number):
            return self.time_slot3
        if (self.time_slot4.my_number == time_number):
            return self.time_slot4
        if (self.time_slot5.my_number == time_number):
            return self.time_slot5


class choosing_time_ctrl:
    def show_time_item(self, daily_catalog1):
        daily_catalog1.show_list_of_time()

    def choose_time(self, my_time1, daily_catalog1):
        return daily_catalog1.get_time(my_time1)


class lab:
    def __init__(self, n, a, b_p, c, c_i):
        self.lab_name = n
        self.address = a
        self.base_price = b_p
        self.lab_code = c
        self.covering_insurance = c_i


class lab_catalog:
    def __init__(self, l1, l2, l3, l4, l5):
        self.lab1 = l1
        self.lab2 = l2
        self.lab3 = l3
        self.lab4 = l4
        self.lab5 = l5

    def match_insurance(self, i_name):
        for i in range(0, len(self.lab1.covering_insurance)):
            if self.lab1.covering_insurance[i] == i_name:
                print(self.lab1.lab_name)
                print(self.lab1.address)
                print(self.lab1.base_price)
                print(self.lab1.lab_code)
                print("\n")
        for i in range(0, len(self.lab2.covering_insurance)):
            if self.lab2.covering_insurance[i] == i_name:
                print(self.lab2.lab_name)
                print(self.lab2.address)
                print(self.lab2.base_price)
                print(self.lab2.lab_code)
                print("\n")
        for i in range(0, len(self.lab3.covering_insurance)):
            if self.lab3.covering_insurance[i] == i_name:
                print(self.lab3.lab_name)
                print(self.lab3.address)
                print(self.lab3.base_price)
                print(self.lab3.lab_code)
                print("\n")
        for i in range(0, len(self.lab4.covering_insurance)):
            if self.lab4.covering_insurance[i] == i_name:
                print(self.lab4.lab_name)
                print(self.lab4.address)
                print(self.lab4.base_price)
                print(self.lab4.lab_code)
                print("\n")
        for i in range(0, len(self.lab5.covering_insurance)):
            if self.lab5.covering_insurance[i] == i_name:
                print(self.lab5.lab_name)
                print(self.lab5.address)
                print(self.lab5.base_price)
                print(self.lab5.lab_code)
                print("\n")

    def get_lab(self, my_lab_name):
        if self.lab1.lab_name == my_lab_name:
            return self.lab1
        if self.lab2.lab_name == my_lab_name:
            return self.lab2
        if self.lab3.lab_name == my_lab_name:
            return self.lab3
        if self.lab4.lab_name == my_lab_name:
            return self.lab4
        if self.lab5.lab_name == my_lab_name:
            return self.lab5


class choosing_lab_ctrl:
    def show_insurance_match_labs(self, lab_catalog1, name):
        lab_catalog1.match_insurance(name)

    def choose_lab(self, lab_name1, lab_catalog1):
        return lab_catalog1.get_lab(lab_name1)


class description:
    def __init__(self, n, p):
        self.test_name = n
        self.test_price = p

    def get_price(self):
        return self.test_price


class description_catalog:
    def __init__(self, d1, d2, d3, d4, d5):
        self.description1 = d1
        self.description2 = d2
        self.description3 = d3
        self.description4 = d4
        self.description5 = d5

    def get_description(self, name):
        if (self.description1.test_name == name):
            return self.description1
        if (self.description2.test_name == name):
            return self.description2
        if (self.description3.test_name == name):
            return self.description3
        if (self.description4.test_name == name):
            return self.description4
        if (self.description5.test_name == name):
            return self.description5


class test_item:
    def __init__(self, n):
        self.item_name = n

    def map_test_item_description(self, name_of_item, description_catalog1):
        self.my_description = description_catalog1.get_description(name_of_item)

    def get_price_item(self):
        return self.my_description.get_price()


class system_test_items:
    def __init__(self, a, b, c, d, e):
        self.item1_name = a
        self.item2_name = b
        self.item3_name = c
        self.item4_name = d
        self.item5_name = e

    def show_list(self):
        print(self.item1_name.item_name)
        print(self.item2_name.item_name)
        print(self.item3_name.item_name)
        print(self.item4_name.item_name)
        print(self.item5_name.item_name)
        print("\n")


class test_item_ctrl:
    def show_system_items(self, system_test_items1):
        system_test_items1.show_list()

    def choose_test_item(self, test_request1, item):
        return test_request1.enter_test_item_by_name(item)


class test_request:
    def __init__(self, d, t, c):
        self.date = d
        self.time = t
        self.code = c

    def enter_test_item_by_name(self, name_of_item):
        self.my_test_item = test_item(name_of_item)
        return self.my_test_item

    def map_test_request_lab(self, my_lab1):
        self.lab_info = my_lab1

    def map_test_request_timeslot(self, my_time1):
        self.timeslot = my_time1

    def get_total_price(self):
        return self.my_test_item.get_price_item()

    def map_test_request_reciept(self, reciept1):
        self.my_reciept1 = reciept1


class patient:
    def __init__(self, n, a, u, p, e, nunber, address, i):
        self.patient_name = n
        self.age = a
        self.username = u
        self.password = p
        self.email_address = e
        self.mobile_number = nunber
        self.address = address
        self.insurance = i

    def make_new_test_request(self):
        self.test = test_request("1399/04/27", "13:00", 5667)
        return self.test


class test_request_ctrl():

    def request_for_test(self, patient1):
        return patient1.make_new_test_request()


Patients = [
    patient("gholi gholian", "60", "GH_GH", "1234", "gholi@gmail.com", "09127108331", "Tehran-Amirabad",
            "tamin_egtemaie"),
    patient("maryam maryami", "21", "M_M", "1234", "maryam@gmail.com", "09357108331", "Tehran-Vanak", "kosar"),
    patient("fatemeh ebrahimi", "35", "F_E", "1234", "fatemeh@gmail.com", "09128645351", "Tehran-Resalat",
            "tamin_egtemaie"),
    patient("hassan kachal", "90", "H_C", "1234", "hassan@gmail.com", "09163412331", "Tehran-Piroozi", "moalem")]

loginInfo = []
for P in Patients:
    loginInfo.append((P.username, P.password))


def register():
    name = input('Name:')
    age = input('Age:')
    username = input('Username:')
    password = input('Password:')
    email = input('Email:')
    mobileNumber = input('Mobile Number:')
    address = input('Address:')
    insurance = input('Insurance:')

    if name == '' or age == '' or username == '' or password == '' or email == '' or mobileNumber == '' or address == '' or insurance == '':
        print('You need to fill every field, press 1 to repeat the menu or 6 to exit')
        choice = int(input())
        if choice == 1:
            register()
        elif choice == 6:
            exit()
        else:
            print('You entered the wrong number, menu will be repeated')
            register()

    elif insurance not in ["tamin_egtemaie", "kosar", "melat", "moalem", "asia", "pasargad"]:
        print('Unfortunately none of our labs cover your insurance, exit by entering 6')
        choice = input()
        if choice == 6:
            exit()
    else:
        p = patient(name, age, username, password, email, mobileNumber, address, insurance)
        Patients.append(p)
        print('Welcome, ', p.patient_name)


patient1 = patient("Jane Doe", "100", "J_D", "1234", "jd@gmail.com", "00000000000", "Neverland", "None")


def login():
    user = input('User:')
    passW = input('Pass:')

    if (user, passW) not in loginInfo:
        print('Username or Password not found, 1 for retry, 2 for register, and 6 for exit')
        choice = int(input())
        if choice == 1:
            login()
        elif choice == 2:
            register()
            print('Now, Login!')
            login()
        elif choice == 6:
            exit()
        else:
            print('You entered the wrong number, menu will be repeated')
            register()
    else:
        for p in Patients:
            if (p.username, p.password) == (user, passW):
                patient1.username = p.username
                patient1.password = p.password
                patient1.patient_name = p.patient_name
                patient1.age = p.age
                patient1.insurance = p.insurance
                patient1.mobile_number = p.mobile_number
                patient1.address = p.address
                patient1.email_address = p.email_address


t_item1 = test_item("blood")
t_item2 = test_item("urine")
t_item3 = test_item("skin")
t_item4 = test_item("thyroid")
t_item5 = test_item("blood_suger")
system_test_item1 = system_test_items(t_item1, t_item2, t_item3, t_item4, t_item5)
d1 = description("blood", 60000)
d2 = description("urine", 40000)
d3 = description("skin", 70000)
d4 = description("thyroid", 70000)
d5 = description("blood_suger", 30000)
description_catalog1 = description_catalog(d1, d2, d3, d4, d5)
ci1 = ["tamin_egtemaie", "kosar", "melat"]
ci2 = ["tamin_egtemaie", "kosar", "moalem"]
ci3 = ["kosar", "moalem", "asia"]
ci4 = ["moalem", "pasargad", "melat"]
ci5 = ["tamin_egtemaie", "melat", "pasargad"]
l1 = lab("rayehe", "Tehran_Vanak", 10000, "123", ci1)
l2 = lab("razi", "Tehran_Amirabad", 12000, "342", ci2)
l3 = lab("saman", "Tehran_Resalat", 15000, "756", ci3)
l4 = lab("sarv", "Tehran_Piroozi", 10000, "908", ci4)
l5 = lab("ashkan", "Tehran_Amirabad", 15000, "387", ci5)
lab_catalog1 = lab_catalog(l1, l2, l3, l4, l5)
t1 = time_slot("1399/05/01", "9:00", "1")
t2 = time_slot("1399/05/01", "13:00", "2")
t3 = time_slot("1399/05/12", "11:30", "3")
t4 = time_slot("1399/06/7", "10:30", "4")
t5 = time_slot("1399/06/8", "10:30", "5")
daily_catalog1 = daily_catalog(t1, t2, t3, t4, t5)


def start():
    choice = int(input('1 for login, 2 for register, 6 for exit'))
    if choice == 1:
        login()
    elif choice == 2:
        register()
    elif choice == 6:
        exit()
    else:
        print('Wrong! Try again')
        start()


def run():
    flag = False
    test_request_flag = False
    test_item_flag = False
    choosing_lab_flag = False
    while not flag:
        print("What do you want to do?")
        print("Enter 1 if you want request for test.")
        print("Enter 2 if you want choose your test items.")
        print("Enter 3 if you want choose lab.")
        print("Enter 4 if you want choose time.")
        print("Enter 5 if you want request for payment.")
        print("Enter 6 if you want exit!\n")
        number = int(input("Please choose the number:"))
        if number == 1:
            obj1 = test_request_ctrl()
            test_request1 = obj1.request_for_test(patient1)
            test_request_flag = True
            print("The test request created successfully\n")
        if number == 2:
            if not test_request_flag:
                print("First Please request for test...\n")
                continue
            obj2 = test_item_ctrl()
            print("This is a list of items...Please enter the item that you want!\n")
            obj2.show_system_items(system_test_item1)
            item1 = input("Enter the item name:")
            if (
                    item1 != "blood" and item1 != "urine" and item1 != "skin" and item1 != "thyroid" and item1 != "blood_suger"):
                print("your chois dosen't exsit the item list...please try again")
                print("\n")
                continue
            test_item1 = obj2.choose_test_item(test_request1, item1)
            test_item1.map_test_item_description(item1, description_catalog1)
            test_item_flag = True
            print("The test item was selected successfully\n")
        if number == 3:
            if not test_request_flag:
                print("First Please request for test...\n")
                continue
            obj3 = choosing_lab_ctrl()
            obj3.show_insurance_match_labs(lab_catalog1, patient1.insurance)
            my_lab_choise = input("Enter the lab name:")
            if (
                    my_lab_choise != lab_catalog1.lab1.lab_name and my_lab_choise != lab_catalog1.lab2.lab_name and my_lab_choise != lab_catalog1.lab3.lab_name and my_lab_choise != lab_catalog1.lab4.lab_name and my_lab_choise != lab_catalog1.lab5.lab_name):
                print("your chois dosen't exsit the lab list...please try again")
                print("\n")
                continue
            lab1 = obj3.choose_lab(my_lab_choise, lab_catalog1)
            test_request1.map_test_request_lab(lab1)
            choosing_lab_flag = True
            print("The lab was selected successfully\n")
        if number == 4:
            if not test_request_flag:
                print("First Please request for test...\n")
                continue
            obj4 = choosing_time_ctrl()
            obj4.show_time_item(daily_catalog1)
            my_time_choise = input("Enter the number of the time slot that you want:")
            if (
                    my_time_choise != "1" and my_time_choise != "2" and my_time_choise != "3" and my_time_choise != "4" and my_time_choise != "5"):
                print("your chois dosen't exsit the time list...please try again")
                print("\n")
                continue
            time1 = obj4.choose_time(my_time_choise, daily_catalog1)
            test_request1.map_test_request_timeslot(time1)
            print("The time was selected successfully\n")
        if number == 5:
            if not test_request_flag:
                print("First Please request for test...\n")
                continue
            if not test_item_flag:
                print("First Please choose the test item...\n")
                continue
            if not choosing_lab_flag:
                print("First Please choose the lab...\n")
                continue
            obj5 = payment_ctrl()
            total_p = obj5.request_for_payment(test_request1)
            totalprice = total_p + test_request1.lab_info.base_price
            reciept1 = obj5.make_reciept(totalprice)
            test_request1.map_test_request_reciept(reciept1)
            flag = True
            print("The reciept creat successfully\n")
            return test_request1
        if number == 6:
            exit()


start()
test_request1 = run()

print("*****************************Total information:*********************************\n")
print("*****************************Information about test request:********************\n")
print(test_request1.date, "\n")
print(test_request1.time, "\n")
print(test_request1.code, "\n")
print("*****************************Information about lab:*****************************\n ")
print(test_request1.my_test_item.item_name, "\n")
print(test_request1.lab_info.lab_name, "\n")
print(test_request1.lab_info.address, "\n")
print(test_request1.lab_info.base_price, "\n")
print(test_request1.lab_info.lab_code, "\n")
for i in range(0, len(test_request1.lab_info.covering_insurance)):
    print(test_request1.lab_info.covering_insurance[i], "\n")
print("******************************Information about time slot:*********************\n")
print(test_request1.timeslot.my_date, "\n")
print(test_request1.timeslot.my_time, "\n")
print(test_request1.timeslot.my_number, "\n")
print("******************************Information about reciept:************************\n")
print(test_request1.my_reciept1.final_price, "\n")
print(test_request1.my_reciept1.status, "\n")
