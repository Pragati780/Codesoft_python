class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email, address):
        contact = Contact(name, phone, email, address)
        self.contacts.append(contact)
        print("Contact added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
            return
        for idx, contact in enumerate(self.contacts):
            print(idx + 1," Name: ",contact.name," Phone: ",contact.phone)

    def search_contact(self, keyword):
        found_contacts = [contact for contact in self.contacts if keyword.lower() in contact.name.lower() or keyword in contact.phone]
        if not found_contacts:
            print("No contacts found.")
            return
        for contact in found_contacts:
            print("Name:", {contact.name}, "Phone:", {contact.phone}, "Email:", {contact.email}, "Address:", {contact.address})

    def update_contact(self, name, new_phone=None, new_email=None, new_address=None):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                if new_phone:
                    contact.phone = new_phone
                if new_email:
                    contact.email = new_email
                if new_address:
                    contact.address = new_address
                print("Contact updated successfully.")
                return
        print("Contact not found.")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                print("Contact deleted successfully.")
                return
        print("Contact not found.")

def display_menu():
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

def contact():
    manager = ContactManager()

    while True:
        display_menu()
        choice = int(input("Choose an option: "))

        if choice == 1:
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            manager.add_contact(name, phone, email, address)
        elif choice == 2:
            manager.view_contacts()
        elif choice == 3:
            keyword = input("Enter name or phone to search: ")
            manager.search_contact(keyword)
        elif choice == 4:
            name = input("Enter the name of the contact to update: ")
            new_phone = input("Enter new phone (leave blank to skip): ")
            new_email = input("Enter new email (leave blank to skip): ")
            new_address = input("Enter new address (leave blank to skip): ")
            manager.update_contact(name, new_phone or None, new_email or None, new_address or None)
        elif choice == 5:
            name = input("Enter the name of the contact to delete: ")
            manager.delete_contact(name)
        elif choice == 6:
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    contact()
