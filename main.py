import tkinter as tk
from gui import WebScraperApp

def main():
    """
    Main function to initialize and run the tkinter application.
    """
    root = tk.Tk()
    app = WebScraperApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
