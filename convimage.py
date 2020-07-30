# -*- coding: utf-8 -*-
#Coded By Ashkan Rafiee https://github.com/AshkanRafiee/ConvImage/
from tkinter import *
from tkinter.ttk import *
from PIL import Image  # Python Image Library - Image Processing
import os
from tkinter import messagebox
import webbrowser
from tkinter.filedialog import askopenfilenames
from tkinter.filedialog import askdirectory


files_list = []


def convert():
    if not listbox.get(0):
        messagebox.showinfo('Error - Images not selected!', 'You have to choose your images first!')
    else:
        cformat = combo.get()
        userpath = askdirectory(title='Select Folder to Save Converted Images')
        for file in files_list:
            im = Image.open(file).convert('RGB')
            working_name = str(os.path.basename(file))
            file_extension = str(os.path.splitext(working_name)[1])
            file_extension = file_extension.replace(".", "")
            userpath = userpath + "\\"
            saving_path = userpath + "Converted_" + working_name
            saving_path = saving_path.replace(file_extension, cformat)

            if not os.path.exists(saving_path):
                im.save(saving_path, quality=95)
            else:
                MsgBox = messagebox.askquestion('Some Files are already exists!',
                                                'Do you want to overwrite ' + working_name + ' ?', icon='warning')
                if MsgBox == 'yes':
                    im.save(saving_path, quality=95)

        messagebox.showinfo('Successful!', 'Images Successfully Converted!')


def browse():
    filez = askopenfilenames(parent=window, title='Choose your images',
                             filetypes=[("image files", ('.png', '.jpg', '.jpeg', '.gif', '.tif', '.webp'))])
    listbox.delete(0, END)
    global files_list
    files_list = list(filez)
    for item in files_list:
        item_name = os.path.basename(item)
        listbox.insert(END, item_name)
    if listbox.get(0):
        lbl1.config(text="Ready to convert!")
    else:
        lbl1.config(text="Files not selected yet!")


def callback(url):
    webbrowser.open_new(url)


window = Tk()
window.title("ConvImage")
window.geometry('550x100')
window.resizable(False, False)


listbox = Listbox(window, width=30, height=2, borderwidth=0)
listbox.grid(column=1, row=0)

lbl0 = Label(window, text="Bulk convert your images")
lbl0.grid(column=0, row=0)

lbl1 = Label(window, text="Files not selected yet!", width=20)
lbl1.grid(column=2, row=0)

lbl2 = Label(window, text="Convert images to")
lbl2.grid(column=0, row=1)

lbl3 = Label(window, text="Select your images")
lbl3.grid(column=1, row=1)

lbl4 = Label(window, text="Click to convert")
lbl4.grid(column=2, row=1)

combo = Combobox(window, state="readonly")
combo['values'] = ("webp", "jpg", "jpeg", "gif", "tif", "png")
combo.current(0)  # set the selected item
combo.grid(column=0, row=2, padx=(40))

btn1 = Button(window, text="Browse", command=browse)
btn1.grid(column=1, row=2)

btn2 = Button(window, text="Convert", command=convert)
btn2.grid(column=2, row=2)

link1 = Label(window, text="Made By AshkanRafiee", cursor="hand2")
link1.bind("<Button-1>", lambda e: callback("https://Ashkanrafiee.ir/"))
link1.grid(column=1, row=3)

window.mainloop()
