import tkinter as tk
from tkinter import *
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter import filedialog
from RSA import *
from utility import *
from tkinter import messagebox

class GUIDecriptor(tk.Tk):
    def __init__(roo):
        super().__init__()
        def GUITQRVerif():
            
            def selecttextfile():
                filename = filedialog.askopenfile(mode='r', filetypes=[('Text files', 'txt')])
                if filename is not None:
                    content = filename.read()
                    entry_cipher.delete(0, len(entry_cipher.get()))
                    entry_cipher.insert(0, content)
                    cipher.set(content)

            def selectpubkey():
                content = openPublicKeyFile()
                if content is not None:
                    entry_pubkey.delete(0, len(entry_pubkey.get()))
                    entry_pubkey.insert(0, content)
                    pubkey.set(content) 
                                    
            def dekripsi():
                if len(pubkey.get()) == 0:
                    messagebox.showerror("Error", "Public Key is empty")
                elif len(cipher.get()) == 0:
                    messagebox.showerror("Error", "Cipher text is empty")
                else:
                    try:
                        # Check if the ciphertext is a valid integer
                        cipher_text = cipher.get()
                        if not cipher_text.isdigit():
                            raise ValueError("Ciphertext is not a valid integer.")

                        stringkey = str(pubkey.get())
                        real_key = stringtokey(stringkey)
                        
                        pla = decrypt(real_key, int(cipher_text))
                        
                        try:
                            plaintext = num2str(pla)
                            entry_plain2.delete(0, len(entry_plain2.get()))
                            entry_plain2.insert(0, plaintext)
                            plain2.set(plaintext)
                        except UnicodeDecodeError:
                            hex_text = format(pla, "x")
                            entry_plain2.delete(0, len(entry_plain2.get()))
                            entry_plain2.insert(0, f"(Hex) {hex_text}")
                            plain2.set(f"(Hex) {hex_text}")
                            messagebox.showwarning("Warning", "The decrypted text contains invalid characters.\nDisplaying hexadecimal representation instead.")
                        except Exception as e:
                            messagebox.showerror("Error", f"Decryption error: Kode Cipher Tidak Valid")
                        
                    except ValueError as ve:
                        messagebox.showerror("Error", f"Invalid ciphertext: {str(ve)}")
                    except Exception as e:
                        messagebox.showerror("Error", f"Invalid input data: {str(e)}")
            
            roo.geometry("800x600")
            roo.title("Decrypt QR Code")
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
                text="Decrypt QR Code",
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
            pubkey = StringVar()
            plain2 = StringVar()
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

            # Ciphertext input
            Label(input_frame, text="Ciphertext:", font=FONT_LABEL, bg=BG_COLOR, fg=FG_COLOR).grid(row=0, column=0, pady=10, sticky='e', padx=10)
            entry_cipher = Entry(input_frame, textvariable=cipher, **entry_style)
            entry_cipher.grid(row=0, column=1, pady=10, padx=10)
            Button(input_frame, text="Buka Ciphertext", command=selecttextfile, **button_style).grid(row=0, column=2, pady=10, padx=10)

            # Public Key input
            Label(input_frame, text="Public Key:", font=FONT_LABEL, bg=BG_COLOR, fg=FG_COLOR).grid(row=1, column=0, pady=10, sticky='e', padx=10)
            entry_pubkey = Entry(input_frame, textvariable=pubkey, **entry_style)
            entry_pubkey.grid(row=1, column=1, pady=10, padx=10)
            Button(input_frame, text="Browse", command=selectpubkey, **button_style).grid(row=1, column=2, pady=10, padx=10)

            # Decryption button
            Button(input_frame, text="Dekripsi", command=dekripsi, **button_style).grid(row=2, column=1, pady=10, padx=10)

            # Decrypted text output
            Label(input_frame, text="Hasil Dekripsi:", font=FONT_LABEL, bg=BG_COLOR, fg=FG_COLOR).grid(row=3, column=0, pady=10, sticky='e', padx=10)
            entry_plain2 = Entry(input_frame, textvariable=plain2, **entry_style)
            entry_plain2.grid(row=3, column=1, pady=10, padx=10)

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

            create_rounded_button(button_frame, "Reset Input", lambda: [entry_cipher.delete(0, 'end'), entry_pubkey.delete(0, 'end'), entry_plain2.delete(0, 'end')])
            create_rounded_button(button_frame, "Keluar", lambda: roo.destroy())

        GUITQRVerif()