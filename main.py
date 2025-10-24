from tkinter import Tk, Frame, Button
from bloques import createBlocks, Play

window = Tk()
window.geometry("800x500")
window.title("BlockX")

paleta = Frame(window, bg="grey", width=200)
paleta.place(x=0, y=0, relheight=1.0)
paleta.config(borderwidth=10, relief="raised")
paleta.grid_propagate(False)
workspace = Frame(window, bg="white")
workspace.place(x=200, y=0, relwidth=1.0, relheight=1.0, anchor="nw")

block_counter = {"i": 0}
createBlocks(paleta, workspace, block_counter)

play = Button(window, text="▶️", command=Play, bg="grey")
play.place(relx=1.0, anchor="ne")

window.mainloop()