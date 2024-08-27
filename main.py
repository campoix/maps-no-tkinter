#sudo python3 code/skull/main1.py
import paramiko
from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
from urllib.request import *
import threading
from tkintermapview import TkinterMapView
from scapy.all import ARP, Ether, srp
import socket

root = tk.Tk()
root.title("DEDSEC PROJECT V1.2")
root.geometry("450x800")
root.resizable(False, False)

lbl4 = tk.Label(root, text="exemplo", bg="#f820dd", font="Avenir 20 bold")
lbl4.place(anchor="nw", relx=0, rely=0)

URL1 = "https://github.com/campoix/banco-de-imagens/blob/main/Captura%20de%20Tela%202024-05-25%20a%CC%80s%2017.32.19%20(2).png?raw=true"
load_image1 = urlopen(URL1)
raw_data1 = load_image1.read()
load_image1.close()
image1 = ImageTk.PhotoImage(data=raw_data1)



def clicar1():
    for widgets in root.winfo_children():
        widgets.place_forget()
    map_widget = TkinterMapView(root, width=1000, height=700, corner_radius=0)
    map_widget.pack(fill="both", expand=True)
    map_widget.set_position(-23.6605483, -46.6917224)  # indentificar atual
    map_widget.set_zoom(14)


label_image1 = tk.Button(root, image=image1, command=clicar1)
label_image1.image = image1
label_image1.place(x=28.0, y=340.0)


lbl1 = tk.Label(root, text="Maps", background="purple", font="Arial 20")
lbl1.place(x=33.0, y=400.0)



root.mainloop()
