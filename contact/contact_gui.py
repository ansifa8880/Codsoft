import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactBookApp:
    def __init__(self, master):
        self.master = master
        master.title("Contact Book")

        self.contacts = []

        # Create frames for different sections
        self.contact_frame = tk.Frame(master)
        self.contact_frame.pack(padx=10, pady=10)

        self.contact_list_frame = tk.Frame(master)
        self.contact_list_frame.pack(padx=10, pady=10)

        # Create widgets for the contact frame
        self.name_label = tk.Label(self.contact_frame, text="Name:")
        self.name_label.grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(self.contact_frame, width=30)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        self.phone_label = tk.Label(self.contact_frame, text="Phone:")
        self.phone_label.grid(row=1, column=0, padx=5, pady=5)
        self.phone_entry = tk.Entry(self.contact_frame, width=30)
        self.phone_entry.grid(row=1, column=1, padx=5, pady=5)

        self.email_label = tk.Label(self.contact_frame, text="Email:")
        self.email_label.grid(row=2, column=0, padx=5, pady=5)
        self.email_entry = tk.Entry(self.contact_frame, width=30)
        self.email_entry.grid(row=2, column=1, padx=5, pady=5)

        self.address_label = tk.Label(self.contact_frame, text="Address:")
        self.address_label.grid(row=3, column=0, padx=5, pady=5)
        self.address_entry = tk.Entry(self.contact_frame, width=30)
        self.address_entry.grid(row=3, column=1, padx=5, pady=5)

        # Create buttons for the contact frame
        self.add_button = tk.Button(self.contact_frame, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=4, column=0, columnspan=2, padx=5, pady=10)

        # Create widgets for the contact list frame
        self.contact_list = tk.Listbox(self.contact_list_frame, width=40, height=10)
        self.contact_list.pack(side=tk.LEFT, padx=5, pady=5)

        self.scrollbar = tk.Scrollbar(self.contact_list_frame, orient=tk.VERTICAL, command=self.contact_list.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.contact_list.config(yscrollcommand=self.scrollbar.set)

        # Create buttons for the contact list frame
        self.view_button = tk.Button(self.contact_list_frame, text="View Contact", command=self.view_contact)
        self.view_button.pack(pady=5)

        self.search_button = tk.Button(self.contact_list_frame, text="Search Contact", command=self.search_contact)
        self.search_button.pack(pady=5)

        self.update_button = tk.Button(self.contact_list_frame, text="Update Contact", command=self.update_contact)
        self.update_button.pack(pady=5)

        self.delete_button = tk.Button(self.contact_list_frame, text="Delete Contact", command=self.delete_contact)
        self.delete_button.pack(pady=5)

        self.update_contact_list()

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if not all([name, phone, email, address]):
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        contact = Contact(name, phone, email, address)
        self.contacts.append(contact)

        self.clear_entry_fields()
        self.update_contact_list()

    def clear_entry_fields(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

    def update_contact_list(self):
        self.contact_list.delete(0, tk.END)
        for contact in self.contacts:
            self.contact_list.insert(tk.END, f"{contact.name} - {contact.phone}")

    def view_contact(self):
        selection = self.contact_list.curselection()
        if selection:
            index = selection[0]
            contact = self.contacts[index]
            messagebox.showinfo("Contact Details", f"Name: {contact.name}\nPhone: {contact.phone}\nEmail: {contact.email}\nAddress: {contact.address}")
        else:
            messagebox.showerror("Error", "Please select a contact to view.")

    def search_contact(self):
        search_term = tk.simpledialog.askstring("Search Contact", "Enter name or phone number:")
        if search_term:
            found = False
            for contact in self.contacts:
                if search_term.lower() in contact.name.lower() or search_term in contact.phone:
                    found = True
                    messagebox.showinfo("Search Result", f"Contact found:\nName: {contact.name}\nPhone: {contact.phone}\nEmail: {contact.email}\nAddress: {contact.address}")
                    break
            if not found:
                messagebox.showinfo("Search Result", "No matching contact found.")

    def update_contact(self):
        selection = self.contact_list.curselection()
        if selection:
            index = selection[0]
            contact = self.contacts[index]

            # Create a new window for updating contact details
            update_window = tk.Toplevel(self.master)
            update_window.title("Update Contact")

            # Create widgets for updating contact details
            name_label = tk.Label(update_window, text="Name:")
            name_label.grid(row=0, column=0, padx=5, pady=5)
            name_entry = tk.Entry(update_window, width=30)
            name_entry.grid(row=0, column=1, padx=5, pady=5)
            name_entry.insert(0, contact.name)

            phone_label = tk.Label(update_window, text="Phone:")
            phone_label.grid(row=1, column=0, padx=5, pady=5)
            phone_entry = tk.Entry(update_window, width=30)
            phone_entry.grid(row=1, column=1, padx=5, pady=5)
            phone_entry.insert(0, contact.phone)

            email_label = tk.Label(update_window, text="Email:")
            email_label.grid(row=2, column=0, padx=5, pady=5)
            email_entry = tk.Entry(update_window, width=30)
            email_entry.grid(row=2, column=1, padx=5, pady=5)
            email_entry.insert(0, contact.email)

            address_label = tk.Label(update_window, text="Address:")
            address_label.grid(row=3, column=0, padx=5, pady=5)
            address_entry = tk.Entry(update_window, width=30)
            address_entry.grid(row=3, column=1, padx=5, pady=5)
            address_entry.insert(0, contact.address)

            # Create a button to save updated contact details
            def save_updated_contact():
                updated_name = name_entry.get()
                updated_phone = phone_entry.get()
                updated_email = email_entry.get()
                updated_address = address_entry.get()

                if not all([updated_name, updated_phone, updated_email, updated_address]):
                    messagebox.showerror("Error", "Please fill in all fields.")
                    return

                contact.name = updated_name
                contact.phone = updated_phone
                contact.email = updated_email
                contact.address = updated_address

                update_window.destroy()
                self.update_contact_list()

            save_button = tk.Button(update_window, text="Save", command=save_updated_contact)
            save_button.grid(row=4, column=0, columnspan=2, padx=5, pady=10)

        else:
            messagebox.showerror("Error", "Please select a contact to update.")

    def delete_contact(self):
        selection = self.contact_list.curselection()
        if selection:
            if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this contact?"):
                index = selection[0]
                del self.contacts[index]
                self.update_contact_list()
        else:
            messagebox.showerror("Error", "Please select a contact to delete.")

root = tk.Tk()
app = ContactBookApp(root)
root.mainloop()

