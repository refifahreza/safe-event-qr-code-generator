import tkinter as tk
from tkinter import *
from tkinter import messagebox
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from RSA import *
#membuat GUI dari frame, label, dan tombol
class GUIKeyGenerator(tk.Tk):
    def __init__(roo):
        super().__init__()     
        def GUIgetkeypair():
            # Setup window
            roo.geometry("800x600")
            roo.title("RSA Key Generator")
            roo.resizable(0, 0)
            roo.configure(bg = "#2C3333")  # Dark background
            
            # Style constants
            FONT_HEADER = ("Helvetica", 16, "bold")
            FONT_LABEL = ("Helvetica", 11)
            FONT_BUTTON = ("Helvetica", 10)
            
            # Updated color scheme to bright theme
            BG_COLOR = "#F0F8FF"  # Light blue-white
            FG_COLOR = "#333333"  # Dark gray text
            ENTRY_BG = "#FFFFFF"  # White entry background
            BUTTON_BG = "#4CAF50"  # Fresh green
            BUTTON_FG = "#FFFFFF"  # White text on buttons
            
            # Create main frame
            main_frame = Frame(roo, bg=BG_COLOR, padx=40, pady=30)
            main_frame.pack(expand=True, fill='both')
            
            # Header
            header = Label(
                main_frame, 
                text="RSA Key Generator",
                font=FONT_HEADER,
                bg=BG_COLOR,
                fg=FG_COLOR,
                pady=20
            )
            header.pack()

            # Create input frame
            input_frame = Frame(main_frame, bg=BG_COLOR)
            input_frame.pack(pady=20)

            # Variables
            pub = StringVar()
            pri = StringVar()

            # Input fields styling
            entry_style = {
                'font': FONT_LABEL,
                'bg': ENTRY_BG,
                'fg': FG_COLOR,
                'insertbackground': FG_COLOR,  # Cursor color
                'relief': 'flat',
                'width': 30
            }

            # Button styling
            button_style = {
                'font': FONT_BUTTON,
                'bg': BUTTON_BG,
                'fg': BUTTON_FG,
                'relief': 'flat',
                'cursor': 'hand2',
                'width': 20,
                'pady': 8,
                'borderwidth': 0,
                'highlightthickness': 0
            }

            # P and Q inputs
            Label(input_frame, text="Nilai p:", font=FONT_LABEL, bg=BG_COLOR, fg=FG_COLOR).grid(row=0, column=0, pady=10, sticky='e', padx=10)
            entry_p = Entry(input_frame, **entry_style)
            entry_p.grid(row=0, column=1, pady=10, padx=10)

            Label(input_frame, text="Nilai q:", font=FONT_LABEL, bg=BG_COLOR, fg=FG_COLOR).grid(row=1, column=0, pady=10, sticky='e', padx=10)
            entry_q = Entry(input_frame, **entry_style)
            entry_q.grid(row=1, column=1, pady=10, padx=10)

            # Public and Private key outputs
            Label(input_frame, text="Kunci Publik:", font=FONT_LABEL, bg=BG_COLOR, fg=FG_COLOR).grid(row=2, column=0, pady=10, sticky='e', padx=10)
            entry_pub = Entry(input_frame, textvariable=pub, **entry_style)
            entry_pub.grid(row=2, column=1, pady=10, padx=10)

            Label(input_frame, text="Kunci Privat:", font=FONT_LABEL, bg=BG_COLOR, fg=FG_COLOR).grid(row=3, column=0, pady=10, sticky='e', padx=10)
            entry_pri = Entry(input_frame, textvariable=pri, **entry_style)
            entry_pri.grid(row=3, column=1, pady=10, padx=10)

            # Button frame
            button_frame = Frame(main_frame, bg=BG_COLOR)
            button_frame.pack(pady=20)

            # Create and style each button
            def create_rounded_button(parent, text, command):
                button = Button(parent, text=text, command=command, **button_style)
                button.pack(pady=10)
                # Add rounded corners using custom border radius
                button.bind('<Map>', lambda e: e.widget.configure(relief='flat'))
                return button

            create_rounded_button(button_frame, "Generate Nilai P dan Q", lambda: fillentryp_q())
            create_rounded_button(button_frame, "Generate Key", lambda: getkey())
            create_rounded_button(button_frame, "Simpan Kunci", lambda: write())
            create_rounded_button(button_frame, "Keluar", lambda: roo.destroy())

            #generate kunci publik dan privat        
            def getkey():
                #membuat p dan q
                content_q = entry_q.get()
                content_p = entry_p.get()
                if len(content_q) == 0 or len(content_p) == 0:
                    a = generate_key_pair(generate_prime_number(), generate_prime_number())
                else:
                    a = generate_key_pair(int(content_q), int(content_p))
                    
                entry_pub.delete(0, len(entry_pub.get()))
                entry_pub.insert(0, a[0][0])
                pub.set(a[0])

                entry_pri.delete(0, len(entry_pri.get()))
                entry_pri.insert(0, a[1][0])
                pri.set(a[1])
            
            #save kunci ke file
            def write():
                with open('public_key.pub', 'w') as f:
                    f.write(pub.get())
                with open('private_key.pri', 'w') as f:
                    f.write(pri.get())
                messagebox.showinfo("Success", "Key has been saved!")

            #memastikan p !=q
            def fillentryp_q():
                p = generate_prime_number()
                q = generate_prime_number()
                while q == p:
                    # make sure q != p
                    q = generate_prime_number()

                entry_p.delete(0, len(entry_p.get()))
                entry_p.insert(0, p)
                entry_q.delete(0, len(entry_q.get()))
                entry_q.insert(0, q)  
        
        GUIgetkeypair()