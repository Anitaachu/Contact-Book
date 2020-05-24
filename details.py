import os
import json

option = input(
    "1. Create new contact\n2. Edit Contact\n3. Delete contact\n4. Exit program\nChoose action:  "
).lower()
if option == "create new contact":

    def contact_info(
        contact_name, contact_phone_number, contact_email, contact_dic=dict()
    ):
        contact_dic[contact_name] = [contact_phone_number, contact_email]
        return contact_dic

    # contact = open('contact.txt', 'r+')
    # contact.write("Name: %s \n" % name1)
    # contact.write("Phone Number: %s \n" % phone_number1)
    #
    # contact.write("Email Address: %s \n" % email1)

    while True:
        s = input(
            "Enter 'new' if you want to add a new contact,enter 'q 'if you want to finish: "
        )
        if s == "new":
            name = input("contact name: ")
            phone_number = int(input("Contact Phone NUmber: "))
            email = input("Contact Email Address: ")
            print(contact_info(name, phone_number, email))
            with open("contact.txt", "a") as file:
                file.write("Name: %s \n" % name)
                file.write("Phone Number: %s \n" % phone_number)
                file.write("Email Address: %s \n" % email)

        else:
            exit()
