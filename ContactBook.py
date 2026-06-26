import json
import os

FILE_NAME = "contacts.json"

# Load contacts
if os.path.exists(FILE_NAME):
    with open(FILE_NAME, "r") as file:
        contacts = json.load(file)
else:
    contacts = {}

while True:
    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # Add Contact
    if choice == "1":
        name = input("Enter Name: ").strip()
        phone = input("Enter Phone Number: ").strip()

        contacts[name] = phone
        print("✅ Contact added successfully!")

    # View Contacts
    elif choice == "2":
        if contacts:
            print("\n--- Contact List ---")
            for name, phone in sorted(contacts.items()):
                print(f"{name}: {phone}")
        else:
            print("No contacts found.")

    # Search Contact
    elif choice == "3":
        name = input("Enter Name to Search: ").strip()

        if name in contacts:
            print(f"{name}: {contacts[name]}")
        else:
            print("Contact not found.")

    # Update Contact
    elif choice == "4":
        name = input("Enter Name to Update: ").strip()

        if name in contacts:
            new_phone = input("Enter New Phone Number: ").strip()
            contacts[name] = new_phone
            print("✅ Contact updated successfully!")
        else:
            print("Contact not found.")

    # Delete Contact
    elif choice == "5":
        name = input("Enter Name to Delete: ").strip()

        if name in contacts:
            del contacts[name]
            print("✅ Contact deleted successfully!")
        else:
            print("Contact not found.")

    # Exit
    elif choice == "6":
        with open(FILE_NAME, "w") as file:
            json.dump(contacts, file, indent=4)

        print("Contacts saved successfully.")
        print("Goodbye!")
        break

    else:
        print("❌ Invalid choice. Please try again.")