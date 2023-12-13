#kush patel
#9/27/2023
#main file

from contacts import *

contacts = {"65432345": ["",""], "65456754" : ["",""],"35746464" : ["",""] }



print("*** TUFFY TITAN CONTACT MAIN MENU")

print("1. Add contact")
print("2. Modify contact")
print("3. Delete contact")
print("4. Sort and Print List")
print("5. Find Conact")
print("6. Exit the program")
print()



while True:
    try:
        choice_number = int(input("Enter menu choice: "))

        if choice_number == 1:
            first_name = input("First Name: ")
            last_name = input("Last Name: ")
            val = add_contact(contacts, first_name, last_name)
            if val == "error":
                print(val)
        elif choice_number == 2:
            first_name = input("First Name: ")
            last_name = input("Last Name: ")
            ind = int(input("Enter index: "))
            val = modify_contact(contacts, first_name, last_name,ind)
            if val == "error":
                print(val)
        elif choice_number == 3:
        
            num = int(input("Enter ID: "))
            val = delete_contact(contacts, num)
            if val == "error":
                print(val)
        elif choice_number == 4:
            val = sort_contacts(contacts)
            print(val)
            
        elif choice_number == 5:
            ind = int(input("Enter number: "))
            val = find_contact(contacts,ind)
        elif choice_number == 6:
            break
            



        else:
            print("Invalid choice")
    except Exception:
            print("Invalid choice")





