contact = {}

def contactHash(key :str, num):
    contact[key] = num
    return contact

while True:
    print("1. Add contact")
    print("2. Delete contact")
    print("3. Search contact")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        key = input("Enter contact name: ")
        num = input("Enter contact number: ")
        contactHash(key, num)
    elif choice == "2":
        key = input("Enter contact name: ")
        if key in contact:
            del contact[key]
            print("Contact Deleted")
        else:
            print("Name isnt in contact")
    elif choice == "3":
        key = input("Enter contact name: ")
        if key in contact:
            print(contact[key])
        else:
            print("Name isnt in contact")
    elif 
for i, item in contact.items():
    print(f"{i} : {item}")