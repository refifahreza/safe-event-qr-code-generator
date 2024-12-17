import tkinter as tk
import string
from tkinter import filedialog
from tkinter import messagebox
from tkinter import *
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from RSA import *

import GUIKeyGenerator as GUIKey
import GUIDecriptor as GUIDecript
import GUIQRGenerator as GUIQR

class Main(tk.Tk):
    def __init__(root):
        super().__init__()
        
        # Window setup
        root.geometry("800x500")
        root.title("QR Code Generator - With RSA Encryption")
        root.configure(bg = "#FFFFFF")

        canvas = Canvas(
            root,
            bg = "#FFFFFF",
            height = 600,
            width = 900,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )
        canvas.place(x = 0, y = 0)

        # Modern title styling
        canvas.create_text(
            400,
            50,
            anchor="center",
            text="Safe Event QR Code Generator",
            fill="#333333",
            font=("Helvetica", 36, "bold")
        )

        canvas.create_text(
            400,
            100,
            anchor="center",
            text="with RSA Encryption",
            fill="#666666",
            font=("Helvetica", 16)
        )
        
        # Updated footer text
        canvas.create_text(
            400,
            450,
            anchor="center",
            text="Cryptography Project | Refi Fahreza (2111102441175)",
            fill="#999999",
            font=("Helvetica", 12)
        )
            
        # Modernized button layout
        buttons = [
            ("Key Generator", "img/Key.png", lambda: GUIKey.GUIKeyGenerator()),
            ("QR Generator", "img/QR Generator.png", lambda: GUIQR.GUIQRGenerator()),
            ("Decryptor", "img/Decryptor.png", lambda: GUIDecript.GUIDecriptor()),
            ("Exit", "img/Exit.png", lambda: root.destroy())
        ]

        # Create buttons with vertical spacing
        button_start_y = 150  # Starting Y position
        button_spacing = 70   # Vertical space between buttons
        
        for i, (name, img_path, command) in enumerate(buttons):
            btn_img = PhotoImage(file=img_path)
            btn = Button(
                image=btn_img,
                borderwidth=0,
                highlightthickness=0,
                command=command,
                bg="#FFFFFF",
                relief="flat"
            )
            btn.image = btn_img  # Keep a reference to prevent garbage collection
            btn.place(
                x=337,  # Centered horizontally (800/2 - button_width/2)
                y=button_start_y + (i * button_spacing),
                width=125,
                height=55
            )
        
        root.resizable(False, False)
        root.mainloop()
        
if __name__ == "__main__":
    Main()
    