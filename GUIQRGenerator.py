import tkinter as tk
from tkinter import *
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter import filedialog
from tkinter import messagebox
from RSA import *
from utility import *
import qrcode
from datetime import datetime

#membuat GUI dari frame, label, dan tombol
class GUIQRGenerator(tk.Tk):
    def __init__(roo):
        super().__init__()
        def GUIQRGen():
                       
            def selecttextfile():
                filename = filedialog.askopenfile(mode='r', filetypes=[('Text files', 'txt')])
                if filename is not None:
                    content = filename.read()
                    entry_plain.delete(0, len(entry_plain.get()))
                    entry_plain.insert(0, content)
                    plain.set(content)
                                    
            def selectprivkey():
                content = openPrivateKeyFile()
                if content is not None:
                    entry_privkey.delete(0, len(entry_privkey.get()))
                    entry_privkey.insert(0, content)
                    privkey.set(content)

            def enkripsi():
                if len(privkey.get()) == 0:
                    messagebox.showerror("Error", "Private Key is empty")
                elif len(plain.get()) == 0:
                    messagebox.showerror("Error", "Plain text is empty")
                else:
                    print("plain: ",plain.get())
 
                    print("privkey: ",privkey.get())

                    
                    stringkey = str(privkey.get())
                    real_key = stringtokey(stringkey)
                    
                    chi = encrypt(real_key, str2num(plain.get()))
                    entry_cipher.delete(0, len(entry_cipher.get()))
                    entry_cipher.insert(0, chi)
                    cipher.set(chi)
                    
                    print("cipher: ",cipher.get())
                    print("cipher type: ", type(cipher.get()))
                    print("chi type: ", type(chi))
            
            def makeqr():
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                qr_filename = f"QR_code_{timestamp}.png"
                cipher_filename = f"cipher_{timestamp}.txt"
                
                # Save QR code
                myQR = qrcode.make(cipher.get())
                myQR.save(qr_filename)
                
                # Save cipher to text file
                with open(cipher_filename, 'w') as f:
                    f.write(str(cipher.get()))
                
                messagebox.showinfo("Success", f"QR Code saved as {qr_filename}\nCipher saved as {cipher_filename}")
            
            def reset_fields():
                entry_plain.delete(0, tk.END)
                entry_privkey.delete(0, tk.END)
                entry_cipher.delete(0, tk.END)
                plain.set("")
                privkey.set("")
                cipher.set("")

            # Setup window
            roo.geometry("800x600")
            roo.title("QR Code Generator")
            roo.resizable(0, 0)
            roo.configure(bg="#2C3333")  # Dark background

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
                text="QR Code Generator",
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
            privkey = StringVar()
            plain = StringVar()
            cipher = StringVar()

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

            # Identitas input
            Label(input_frame, text="Pilih User:", font=FONT_LABEL, bg=BG_COLOR, fg=FG_COLOR).grid(row=0, column=0, pady=10, sticky='e', padx=10)
            entry_plain = Entry(input_frame, textvariable=plain, **entry_style)
            entry_plain.grid(row=0, column=1, pady=10, padx=10)
            Button(input_frame, text="Pilih User", command=selecttextfile, **button_style).grid(row=0, column=2, pady=10, padx=10)

            # Private Key input
            Label(input_frame, text="Private Key:", font=FONT_LABEL, bg=BG_COLOR, fg=FG_COLOR).grid(row=1, column=0, pady=10, sticky='e', padx=10)
            entry_privkey = Entry(input_frame, textvariable=privkey, **entry_style)
            entry_privkey.grid(row=1, column=1, pady=10, padx=10)
            Button(input_frame, text="Browse Private Key", command=selectprivkey, **button_style).grid(row=1, column=2, pady=10, padx=10)

            # Ciphertext output
            Label(input_frame, text="Ciphertext:", font=FONT_LABEL, bg=BG_COLOR, fg=FG_COLOR).grid(row=2, column=0, pady=10, sticky='e', padx=10)
            entry_cipher = Entry(input_frame, textvariable=cipher, **entry_style)
            entry_cipher.grid(row=2, column=1, pady=10, padx=10)
            Button(input_frame, text="Enkripsi", command=enkripsi, **button_style).grid(row=2, column=2, pady=10, padx=10)

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

            create_rounded_button(button_frame, "Buat QR Code", makeqr)
            create_rounded_button(button_frame, "Reset Input", reset_fields)
            create_rounded_button(button_frame, "Keluar", lambda: roo.destroy())
        GUIQRGen()
        
