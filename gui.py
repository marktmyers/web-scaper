import tkinter as tk
from tkinter import messagebox, filedialog

from scraper import scrape
from storage import save_to_json

class WebScraperApp:
    def __init__(self, root):
        self.root = root
        root.title("Web Scraper")

        # URL Input
        self.url_label = tk.Label(root, text="Enter URL:")
        self.url_label.pack()
        self.url_entry = tk.Entry(root, width=50)
        self.url_entry.pack()

        # Data Type Selection
        self.data_types_label = tk.Label(root, text="Select Data Types to Scrape:")
        self.data_types_label.pack()
        self.headings_var = tk.BooleanVar()
        self.links_var = tk.BooleanVar()
        self.images_var = tk.BooleanVar()
        self.text_var = tk.BooleanVar()

        self.headings_check = tk.Checkbutton(root, text="Headings", variable=self.headings_var)
        self.links_check = tk.Checkbutton(root, text="Links", variable=self.links_var)
        self.images_check = tk.Checkbutton(root, text="Images", variable=self.images_var)
        self.text_check = tk.Checkbutton(root, text="Text", variable=self.text_var)
        self.headings_check.pack()
        self.links_check.pack()
        self.images_check.pack()
        self.text_check.pack()

        # Scrape Button
        self.scrape_button = tk.Button(root, text="Scrape", command=self.scrape)
        self.scrape_button.pack()

    def scrape(self):
        url = self.url_entry.get()
        if not url:
            messagebox.showerror("Error", "URL is required")
            return

        data_types = []
        if self.headings_var.get():
            data_types.append('headings')
        if self.links_var.get():
            data_types.append('links')
        if self.images_var.get():
            data_types.append('images')
        if self.text_var.get():
            data_types.append('text')

        scraped_data = scrape(url, data_types)

        # Save File Dialog
        if messagebox.askyesno("Save", "Would you like to save the results?"):
            filename = filedialog.asksaveasfilename(
                defaultextension=".json",
                filetypes=[("JSON files", "*.json")]
            )
            if filename:
                save_to_json(scraped_data, filename)
            else:
                messagebox.showinfo("Cancelled", "Save operation cancelled.")
