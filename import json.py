import json

contacts = {}

def menu():
    print("\nContact Management System")
    print("1. Add a new contact")
    print("2. View contact list")
    print("3. Edit contact")
    print("4. Delete contact")
    print("5. Exit")

def add_contact():
    name = input("Enter name: ")
    number = input("Enter contact number: ")
    email = input("Enter email address: ")
    contacts[name] = {"number": number, "email": email}
    print("Contact added successfully!")

def view_contacts():
    if contacts:
        print("\n--- Contacts ---")
for name, contact in contacts.items():
            print(f"Name: {name}, Number: {contact['number']}, Email: {contact['email']}")
else:
     print("No contacts found.")

def edit_contact():
    name = input("Enter the name of the contact you want to edit: ")
    if name in contacts:
        number = input("Enter new contact number: ")
        email = input("Enter new email address: ")
        contacts[name] = {"number": number, "email": email}
        print("Contact updated successfully!")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter the name of the contact you want to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")

def save_contacts_to_file():
    with open("contacts.json", "w") as file:
        json.dump(contacts, file)
    print("Contacts saved to file.")

def load_contacts_from_file():
    global contacts
    try:
        with open("contacts.json", "r") as file:
            contacts = json.load(file)
        print("Contacts loaded from file.")
    except FileNotFoundError:
        print("No saved contacts found.")

def main():
    load_contacts_from_file()

    while True:
        menu()

        choice = input("Enter your choice: ")
        add_contact()
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
           edit_contact()
        elif choice == '4':
           delete_contact()
        elif choice == '5':
            save_contacts_to_file()
        break
    else:
        print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()