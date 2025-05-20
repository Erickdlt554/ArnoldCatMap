import os
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def arnold_cat_map(image, iterations):
    """ARNOLD CAT MAP CANT DE VECES"""
    width, height = image.size
    img = image.copy()
    
    for _ in range(iterations):
        new_img = Image.new(img.mode, (width, height))
        for x in range(width):
            for y in range(height):
                nx = (2 * x + y) % width
                ny = (x + y) % height
                new_img.putpixel((nx, ny), img.getpixel((x, y)))
        img = new_img

    return img

def precalculate_iterations(image, total_iterations):
    """CALCULO"""
    images = [image]
    for i in range(1, total_iterations + 1):
        transformed = arnold_cat_map(images[-1], 1)
        images.append(transformed)
    return images

def update_image(index):

    img = ImageTk.PhotoImage(images[index])
    label.config(image=img)
    label.image = img
    slider_label.config(text=f"Iteración: {index}")

def load_image():
   
    filepath = filedialog.askopenfilename(filetypes=[("PNG Images", "*.png"), ("JPEG Images", "*.jpg *.jpeg")])
    if not filepath:
        return

    img = Image.open(filepath)
    if img.size[0] != img.size[1]:
        tk.messagebox.showerror("Error", "La imagen debe ser En formato cuadrado.")
        return

    global images
    images = precalculate_iterations(img, 30)


    update_image(0)


    slider.config(state="normal", to=len(images) - 1)


root = tk.Tk()
root.title("Arnold Cat Map Modo Visual")


btn = tk.Button(root, text="Cargar imagen", command=load_image)
btn.pack(pady=10)


slider_label = tk.Label(root, text="Iteración: 0")
slider_label.pack()


slider = tk.Scale(root, from_=0, to=0, orient="horizontal", command=lambda val: update_image(int(val)), state="disabled", length=400)
slider.pack()


label = tk.Label(root)
label.pack(pady=10)

root.mainloop()
