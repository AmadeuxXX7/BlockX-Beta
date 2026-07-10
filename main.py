from tkinter import Tk, Frame, Button
import tkinter as tk
from bloques import createBlocks, code
from codes import Play

window = Tk()
window.title("BlockX Beta")
window.geometry("800x500")
icon = tk.PhotoImage(file="imgs/logo2.png")
window.iconphoto(True, icon)

paleta = Frame(window, bg="grey", width=200)
paleta.place(x=0, y=0, relheight=1.0)
paleta.config(borderwidth=10, relief="raised")
paleta.grid_propagate(False)
consolaDeBloques = Frame(window, bg="white")
consolaDeBloques.place(x=200, y=0, relwidth=1.0, relheight=1.0, anchor="nw")

block_counter = {"i": 0}
createBlocks(paleta, consolaDeBloques, block_counter)

play = Button(window, text="▶️", command=lambda:Play(code), bg="grey")
play.pack(anchor="ne")

"""def seeCode(): print(code)
seecode = Button(window, text="📜", command=seeCode, bg="grey")
seecode.pack(pady=5, anchor="ne")"""


window.mainloop()
