contact = {}

def contactHash(key :str, num):
    contact[key] = num
    return contact

while True:
    print("-"*50)
    print("{:<20}{:<20}".format("Nama", "No. Telepon"))
    print("-"*50)
    if not contact:
        print("{:<20}{:<20}".format("None", "None"))
    else:
        for name, number in contact.items():
            if number == "":
                print("{:<20}{:<20}".format(name, "None"))
            else:
                print("{:<20}{:<20}".format(name, number))
    print("\n")    
    print("-"*50)
    print("1. Add contact")
    print("2. Delete contact")
    print("3. Search contact")
    print("4. Exit")
    print("-" * 50)
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
            print("The call number is ",contact[key])
        else:
            print("Name isnt in contact")
    elif choice == "4":
        break
    else:
        print("Pilihan tidak ada")