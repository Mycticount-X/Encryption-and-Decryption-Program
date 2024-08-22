from tkinter import *
from tkinter import messagebox
import base64
import os

"""
Made by Mycticount Xeta Ahlovely (Mycticount-X)
Some of this code belongs to Parvat Computer Technology (YouTube)
"""

# Fungsi Enkripsi
def enkripsi():
    password=code.get()
    """
    [ENG]
    Basically, this section test the correctness of the inputted password
    and then encrypts the inputted text.

    [IND]
    Pada dasarnya, bagian ini menguji kebenaran dari password yang dimasukan
    lalu mengenkripsi teks yang diinput.
    """
    if password == "MXA23":
        screen1 = Toplevel(screen)
        screen1.title("Enkripsi")
        screen1.geometry("400x200")
        screen1.configure(bg="#ed3833")
        
        pesan = teks1.get(1.0, END)
        encode_pesan = pesan.encode("ascii")
        base64_bytes = base64.b64encode(encode_pesan)
        encrypt=base64_bytes.decode("ascii")
        
        Label(screen1, text="Hasil Enkripsi Base64", font= "arial", fg="white", bg="#ed3833").place(x=10, y=8)
        teks2=Text(screen1, font="Roboto 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        teks2.place(x=10, y=40, width = 380, height = 150)
        teks2.insert(END,encrypt)
        
    elif password == "":
        messagebox.showerror("Encryption", "Password Dibutuhkan!")
            
    elif password != "MXA23":
        messagebox.showerror("Encryption", "Password Salah! \n Akses Ditangguhkan")
    

# Fungsi Dekripsi
def dekripsi():
    password=code.get()
    """
    [ENG]
    Similar to enkripsi(), this section test the correctness of the password
    and then decrypts the inputted text.

    [IND]
    Mirip seperti enkripsi(), bagian ini menguji kebenaran dari password yang dimasukan
    lalu mengdekripsi teks yang diinput.
    """
    if password == "MXA23":
        screen2 = Toplevel(screen)
        screen2.title("Dekripsi")
        screen2.geometry("400x200")
        screen2.configure(bg="#00bd56")
        
        pesan = teks1.get(1.0, END)
        decode_pesan = pesan.encode("ascii")
        base64_bytes=base64.b64decode(decode_pesan)
        decrypt=base64_bytes.decode("ascii")
        
        Label(screen2, text="Hasil Dekripsi Base64", font= "arial", fg="white", bg="#00bd56").place(x=10, y=8)
        teks2 = Text(screen2, font="Roboto 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        teks2.place(x=10, y=40, width = 380, height = 150)
        teks2.insert(END,decrypt)
        
    elif password == "":
        messagebox.showerror("Decryption", "Password Dibutuhkan!")
            
    elif password != "MXA23":
        messagebox.showerror("Decryption", "Password Salah! \n Akses Ditangguhkan") 

def hapus():
    code.set("")
    teks1.delete(1.0, END)


# Fungsi Layar Utama
def screen_inti():
    global screen
    global code
    global teks1
    
    """ [ENG]
    This is the Main Screen (screen_inti())
    This is the most crusial part because you must adjust
    the settings of the UI correctly so the app looks good
    This include the screen, button, and input box
    """

    """ [IND]
    Ini adalah Layar Utama (screen_inti())
    Ini adalah bagian yang paling krusial karena kalian harus
    menyesuaikan settingan UI dengan benar supaya applikasinya terlihat bagus
    Ini termasuk layar, tombol, dan kotak input
    """
    
    screen = Tk()
    screen.geometry("375x360")
    screen.title("Enkripsi dan Dekripsi")
    screen.configure(bg="#F5F7F8")
    
    # === logo ===
    # Logo ini adalah orisinil buatan Mycticount Xeta Ahlovely
    image_icon=PhotoImage(file="Logo_Enkripsi_Dekripsi.png")
    screen.iconphoto(False, image_icon)

    # *** Input Teks Utama ***
    Label(text="Masukan Teks", fg="black", font =("calibri", 13)).place(x = 10, y= 15)
    teks1=Text(font="Roboto 20", bg = "white", relief = GROOVE, wrap = WORD, bd=0)
    teks1.place(x=10,y=45, width = 355,height = 100)
    
    Label(text= "Masukan Kata Sandi", fg="black", font =("calibri", 13)).place(x = 10, y= 160)
    code = StringVar()
    Entry(textvariable=code, width = 19, bd=0, font=("arial", 25), show="*").place(x=10,y=190)
    

    # *** Tombol Enkripsi ***
    enkripsi_btn = Button(text="Enkripsi", height=2, width=23, bg="#ed3833", fg="white", bd=0, command=enkripsi)
    enkripsi_btn.place(x=10, y=250)
    
    def on_enter(e):
        e.widget['background'] = '#FF5733'  
    def on_leave(e):
        e.widget['background'] = '#ed3833'  
    
    enkripsi_btn.bind("<Enter>", on_enter)
    enkripsi_btn.bind("<Leave>", on_leave)
    

    # *** Tombol Dekripsi ***
    dekripsi_btn = Button(text="Dekripsi", height=2, width=23, bg="#00bd56", fg="white", bd=0, command=dekripsi)
    dekripsi_btn.place(x=200, y=250)
    
    def on_enter_dekripsi(e):
        e.widget['background'] = '#33FF57'  
    def on_leave_dekripsi(e):
        e.widget['background'] = '#00bd56'  
    
    dekripsi_btn.bind("<Enter>", on_enter_dekripsi)
    dekripsi_btn.bind("<Leave>", on_leave_dekripsi)
    
    
    # *** Tombol Hapus ***
    Button(text="Hapus", height ="2", width=50, bg="#1089ff", fg="white", bd=0, command=hapus).place(x=10,y=300)
    
    
    
    screen.mainloop()
screen_inti()