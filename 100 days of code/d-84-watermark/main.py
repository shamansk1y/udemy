import os
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont

root = Tk()
root.title("Watermark App")

def select_file():
    global img_path
    img_path = filedialog.askopenfilename(title="Select an image", filetypes=(("Image files", "*.jpg;*.png;*.jpeg"), ("All files", "*.*")))
    file_label.config(text="Selected file: " + img_path)

select_button = Button(root, text="Select Image", command=select_file)
select_button.pack()

file_label = Label(root, text="No file selected.")
file_label.pack()


def add_watermark():
    global img_path
    img = Image.open(img_path)
    draw = ImageDraw.Draw(img)
    text = watermark_entry.get()
    font = ImageFont.truetype("arial.ttf", 40)
    textbbox = draw.textbbox((0, 0), text, font=font)
    textwidth = textbbox[2] - textbbox[0]
    textheight = textbbox[3] - textbbox[1]
    width, height = img.size
    x = width - textwidth - 10
    y = height - textheight - 10
    draw.text((x, y), text, font=font, fill=(255, 255, 255, 128))
    filename = "watermarked_" + os.path.basename(img_path)
    img.save(os.path.join(os.path.dirname(img_path), filename))



watermark_label = Label(root, text="Enter watermark text:")
watermark_label.pack()

watermark_entry = Entry(root)
watermark_entry.pack()

add_button = Button(root, text="Add Watermark", command=add_watermark)
add_button.pack()


root.mainloop()
