import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Initialize Firebase credentials and Firestore client
cred = credentials.Certificate("C:/Users/shara/OneDrive/Desktop/contact-management-syste-dadc0-firebase-adminsdk-xbazp-c563713be7.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# Collection name for contacts
CONTACTS_COLLECTION = "contacts"

# Function to load contacts from Firebase
def load_contacts():
    contacts = []
    docs = db.collection(CONTACTS_COLLECTION).get()
    for doc in docs:
        contacts.append(doc.to_dict())
    return contacts

# Function to save contacts to Firebase
def save_contacts(contacts):
    db.collection(CONTACTS_COLLECTION).document("contacts").set({"contacts": contacts})

# Function to add a new contact
def add_contact(contacts):
    name = input("Enter the name: ")
    phone = input("Enter the phone number: ")
    email = input("Enter the email address: ")
    contact = {"name": name, "phone": phone, "email": email}
    contacts.append(contact)
    save_contacts(contacts)
    print("Contact added successfully!")

# Function to search for a contact by name
def search_contact(contacts):
    name = input("Enter the name to search: ")
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            print("Contact found:")
            print("Name:", contact["name"])
            print("Phone:", contact["phone"])
            print("Email:", contact["email"])
            return
    print("Contact not found!")

# Function to update contact information
def update_contact(contacts):
    name = input("Enter the name of the contact to update: ")
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            print("Contact found. Enter new information:")
            contact["name"] = input("Enter the new name: ")
            contact["phone"] = input("Enter the new phone number: ")
            contact["email"] = input("Enter the new email address: ")
            save_contacts(contacts)
            print("Contact updated successfully!")
            return
    print("Contact not found!")

# Main function
def main():
    contacts = load_contacts()

    while True:
        print("\n*** Contact Management System ***")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            search_contact(contacts)
        elif choice == "3":
            update_contact(contacts)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
