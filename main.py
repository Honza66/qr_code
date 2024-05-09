import pyqrcode
from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title('Generátor QR kodu')
root.geometry('300x300')

global_photo_image = None

def generate_qr():
    global global_photo_image
    qr = pyqrcode.create(url_entry.get())
    qr.png('qr_code.png', scale=5)
    image = Image.open('qr_code.png')
    global_photo_image = ImageTk.PhotoImage(image)
    label = Label(root, image=global_photo_image)
    label.pack()


url_label = Label(root, text='Zdejte URL adresu')
url_label.pack(pady=(10,5))
url_entry = Entry(root, width=40)
url_entry.pack(pady=(0,20))
button = Button(root, text='Vygeneruj QR kod', command=generate_qr)
button.pack()

root.mainloop()