def contact_info(contact_name,contact_phone_number,contact_email,contact_dic ):
    contact_dic[contact_name] = [contact_phone_number,contact_email]
    return contact_dic
cd = dict()

name1 = input("Contact Name: ")
phone_number1  = int(input("Contact Phone NUmber: "))
email1 = input("Contact Email Address: ")
print(contact_info(name1,phone_number1,email1,cd))

while True:
    s = input("Enter 'new' if you want to add a new student,enter 'q 'if you want to finish: ")
    if s == 'new':
        name = input("Contact name: ")
        phone_number = int(input("Contact Phone NUmber: "))
        email = input("Contact Email Address: ")
        print(contact_info(name,phone_number,email,cd))

    else:
        break
