

import tkinter as tk
from tkinter import messagebox

class ContactManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Management System")
        
        # Create the data store (you can use a database in a real application)
        self.contacts = []

        # Create GUI elements
        self.label_name = tk.Label(root, text="Name:")
        self.entry_name = tk.Entry(root)
        self.label_phone = tk.Label(root, text="Phone:")
        self.entry_phone = tk.Entry(root)
        self.button_add = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.button_display = tk.Button(root, text="Display Contacts", command=self.display_contacts)

        # Layout
        self.label_name.grid(row=0, column=0)
        self.entry_name.grid(row=0, column=1)
        self.label_phone.grid(row=1, column=0)
        self.entry_phone.grid(row=1, column=1)
        self.button_add.grid(row=2, column=0, columnspan=2, pady=10)
        self.button_display.grid(row=3, column=0, columnspan=2, pady=10)

    def add_contact(self):
        name = self.entry_name.get()
        phone = self.entry_phone.get()

        if name and phone:
            self.contacts.append({"name": name, "phone": phone})
            messagebox.showinfo("Success", "Contact added successfully!")
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Please enter name and phone number.")

    def display_contacts(self):
        if not self.contacts:
            messagebox.showinfo("Contacts", "No contacts found.")
        else:
            contacts_list = "\n".join(f"{contact['name']}: {contact['phone']}" for contact in self.contacts)
            messagebox.showinfo("Contacts", contacts_list)

    def clear_entries(self):
        self.entry_name.delete(0, tk.END)
        self.entry_phone.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = ContactManagementApp(root)
    root.mainloop()
