print("Welcome to the Contact Book!")

name1 = input("\nEnter first contact name: ")
phone1 = input(f"Enter phone number for {name1}: ")

name2 = input("\nEnter second contact name: ")
phone2 = input(f"Enter phone number for {name2}: ")

name3 = input("\nEnter third contact name: ")
phone3 = input(f"Enter phone number for {name3}: ")
contacts = {
    name1: phone1,
    name2: phone2,
    name3: phone3
}

print("\nContacts saved successfully!")

print("\nCurrent Contact List:")
print(f"{name1}: {contacts[name1]}")
print(f"{name2}: {contacts[name2]}")
print(f"{name3}: {contacts[name3]}")

search = input("\nDo you want to search for a contact? (yes/no): ")
if search.lower() == "yes":
    search_name = input("Enter contact name to search: ")

    if search_name in contacts:
        print(f"Phone number of {search_name}: {contacts[search_name]}")
    else:
        print(f"{search_name} is not found in contacts.")

update = input("\nDo you want to update a contact's phone number? (yes/no): ")
if update.lower() == "yes":
    update_name = input("Enter contact name to update: ")

    if update_name in contacts:
        new_phone = input(f"Enter new phone number for {update_name}: ")
        contacts[update_name] = new_phone
        print(f"Phone number for {update_name} updated successfully.")
    else:
        print(f"{update_name} is not found in contacts.")

delete = input("\nDo you want to delete a contact? (yes/no): ")
if delete.lower() == "yes":
    delete_name = input("Enter contact name to delete: ")

    if delete_name in contacts:
        del contacts[delete_name]
        print(f"{delete_name} has been removed from contacts.")
    else:
        print(f"{delete_name} is not found in contacts.")

print("\nFinal Contact List:")
if name1 in contacts:
    print(f"{name1}: {contacts[name1]}")
if name2 in contacts:
    print(f"{name2}: {contacts[name2]}")
if name3 in contacts:
    print(f"{name3}: {contacts[name3]}")
print("\nThank you for using the Contact Book!")

