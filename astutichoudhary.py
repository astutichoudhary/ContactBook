import json
import os
import re

# A json file to store contacts.
CONTACTS_FILE = 'contacts.json'

def load_contacts():
    # Loads contacts from the json file.
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE,'r') as file:
            return json.load(file) #json.load will parse the json file into a python object.
    return {}

def save_contacts(contacts):
    # saves contacts to the json file(whatever has been already taken as input)
    with open(CONTACTS_FILE,'w') as file:
        json.dump(contacts,file,indent=4)

def add_contact(contacts):
    # adds a new phone number with phone number validation and email as detail.
    name = input("Enter contact name: ").strip()
    phone = input("Enter phone number: ").strip()

    # validating the phone number length(max 10 digits)
    if len(phone)>10:
        print("Phone number should exceed 10 digits.")
        return
    
    # if type(phone) != int:
    #     print("Phone number should contain digits only from 0-9.")
    #     return
    #code part didnt work. commented out for now
    
    email = input("Enter contact email: ").strip()
    contacts[name] = {'phone':phone, 'email': email}
    print(f"Contact {name} has been added.")

def view_contacts(contacts):
    # to view all contacts
    if not contacts:
        print("No contacts found.")
        return
    for name,info in contacts.items():
        print(f"Name: {name}")
        print(f"Phone: {info['phone']}")
        print(f"Email: {info['email']}\n")
    
def delete_contact(contacts):
    # to delete any specified contact
    name = input("Enter the contact name you would like to delete: ").strip()

    if name in contacts:
        del contacts[name]
        print(f"Contact {name} has been deleted.")
    else:
        print("Contact not found.")


def search_contact(contacts):
    # to search for the details of any contact in the file.
    name = input("Enter the contact which you want to search: ").strip()
    if name in contacts:
        info = contacts[name]
        print(f"Name: {name}")
        print(f"Phone: {info['phone']}")
        print(f"Email: {info['email']}\n")
    else:
        print("Contact not found.")


def main():
    contacts = load_contacts()
    
    while True:
        print("\nContact Book.")
        print("1.Add contact.\n2.View contacts.\n3.Delete contacts.\n4.Search contacts.\n5.Save and Exit.\n")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_contact(contacts)
        elif choice == 2:
            view_contacts(contacts)
        elif choice == 3:
            delete_contact(contacts)
        elif choice == 4:
            search_contact(contacts)
        elif choice == 5:
            save_contacts(contacts)
            print("Contacts saved. Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
   main()