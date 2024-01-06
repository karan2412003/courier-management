import tkinter as tk
from tkinter import messagebox
import random

class CourierManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Courier Management System")

        self.packages = {}

        self.create_widgets()

    def create_widgets(self):
        # Labels and Entry widgets for package information
        tk.Label(self.root, text="Recipient Name:").grid(row=0, column=0, padx=10, pady=5)
        self.entry_recipient_name = tk.Entry(self.root)
        self.entry_recipient_name.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Status:").grid(row=1, column=0, padx=10, pady=5)
        self.entry_status = tk.Entry(self.root)
        self.entry_status.grid(row=1, column=1, padx=10, pady=5)

        # Button to add a new package
        tk.Button(self.root, text="Add Package", command=self.add_package).grid(row=2, column=0, columnspan=2, pady=10)

        # Listbox to display existing packages
        self.listbox = tk.Listbox(self.root, height=10, width=40)
        self.listbox.grid(row=3, column=0, columnspan=2, pady=10)

        # Button to track a selected package
        tk.Button(self.root, text="Track Package", command=self.track_package).grid(row=4, column=0, columnspan=2, pady=10)

        self.update_listbox()

    def add_package(self):
        recipient_name = self.entry_recipient_name.get()
        status = self.entry_status.get()

        if recipient_name and status:
            package_id = self.generate_package_id()
            self.packages[package_id] = {"Recipient Name": recipient_name, "Status": status}
            messagebox.showinfo("Success", f"Package added successfully. Package ID: {package_id}")
            self.update_listbox()
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

    def generate_package_id(self):
        return f"PKG{random.randint(1000, 9999)}"

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for package_id, info in self.packages.items():
            self.listbox.insert(tk.END, f"Package ID: {package_id}, Recipient: {info['Recipient Name']}, Status: {info['Status']}")

    def track_package(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            package_id = self.listbox.get(selected_index).split(",")[0].split(":")[1].strip()
            info = self.packages.get(package_id, {})
            if info:
                messagebox.showinfo("Package Information", f"Recipient Name: {info['Recipient Name']}\nStatus: {info['Status']}")
            else:
                messagebox.showerror("Error", "Package not found.")
        else:
            messagebox.showerror("Error", "Please select a package to track.")

if __name__ == "__main__":
    root = tk.Tk()
    app=CourierManagementSystem(root)
    root.mainloop()
