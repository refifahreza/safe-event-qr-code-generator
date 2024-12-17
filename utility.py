from tkinter.filedialog import askopenfile, asksaveasfile, askopenfilename
from tkinter import messagebox
import binascii

def openPublicKeyFile():
    '''
    Meminta user membuka file Public Key
    '''
    f = askopenfile(mode='r', title="Open Public Key File", filetypes=[('Public Key File (*.pub)', '.pub')])
    if(f != ''):
        content = f.read()
        f.close()
        return content
    else:
        messagebox.showerror('No File Chosen', 'Tidak ada file yang dipilih, nyaa~')

def openPrivateKeyFile():
    '''
    Meminta user membuka file Private Key
    '''
    f = askopenfile(mode='r', title="Open Private Key File", filetypes=[('Private Key File (*.pri)', '.pri')])
    if(f != ''):
        content = f.read()
        f.close()
        return content
    else:
        messagebox.showerror('No File Chosen', 'Tidak ada file yang dipilih, nyaa~')

def stringtokey(stringkey:str):
    '''
    Mengembalikan nilai key dari key yg dalam bentuk string
    '''
    key_temp = (stringkey.replace(')', '')).split('(')[1]
    k = key_temp.split(', ')[0]
    n = key_temp.split(', ')[1].replace("'", '')
    key = int(k), int(n)
    return key

def str2num(string):
    '''
    Mengubah nilai string plaintext ke integer agar bisa dienkripsi rsa
    '''
    return int(binascii.hexlify(string.encode("utf-8")), 16)


def num2str(number):
    '''
    Mengubah nilai int hasil dekripsi ciphertext rsa ke string agar kembali ke plaintext awal
    '''
    return binascii.unhexlify(format(number, "x").encode("utf-8")).decode("utf-8")
    