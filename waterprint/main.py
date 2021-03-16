from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title("appfromape 浮水印")
root.geometry('530x570')
root.resizable(width=True, height=True)

def openfn():
    filename = filedialog.askopenfilename(title='open')
    return filename

def open_img():
    global x
    x = openfn()
    img = Image.open(x)
    img = img.resize((500, 500), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = Label(root, image=img)
    panel.image = img
    panel.grid(row=0, column=0, columnspan = 2, padx = 10, pady = 10)


def add_wp():
    global x
    image = Image.open(x)
    logo = Image.open('waterprint/appfromape.jpg')
    image_copy = image.copy()
    position = ((image_copy.width - logo.width), (image_copy.height - logo.height))
    image_copy.paste(logo, position)
    image_copy.save('waterprint/watermark.jpg')
    image_copy.show()

canv = Canvas(root, width=500, height=500, bg='white')
canv.grid(row=0, column=0, columnspan = 2, padx = 10, pady = 10)
img = ImageTk.PhotoImage(Image.open("waterprint/bg.jpg"))
canv.create_image(32, 32, anchor=NW, image=img)

btn_1 = Button(root, text='選擇照片', command=open_img).grid(row=1, column=0)
btn_2 = Button(root, text='加水印', command=add_wp).grid(row=1, column=1)

root.mainloop()

