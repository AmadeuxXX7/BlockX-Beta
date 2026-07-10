from tkinter import Frame, Label, Entry, Menu

def setEntry(event):
    entry = event.widget
    new_width = max(3, len(entry.get()))
    entry.config(width=new_width)

def entrynum(texto):
    if texto in ("", "."):
        return True
    try:
        numero = float(texto)
        return numero >= 0
    except ValueError:
        return False

code = []


def clone_block(consolaDeBloques, counter, block_type, value=""):
    counter["i"] += 1
    i = counter["i"]

    block = Frame(consolaDeBloques, bg="green")
    block.grid(row=i, column=0, padx=5, sticky="w")

    text = Label(block, text=str(block_type), bg="green")
    text.grid(row=0, column=0, pady=5, padx=5)
    if block_type == "wait":
        validacion = block.register(entrynum)
        entry = Entry(block, width=3, validate="key", validatecommand=(validacion, "%P"))
    else:
        entry = Entry(block, width=3)
    entry.insert(0, value)
    entry.grid(row=0, column=1, padx=5)
    entry.bind("<KeyRelease>", setEntry)
    block_data = (block_type, entry)
    code.append(block_data)

    # Click derecho
    menu = Menu(block, tearoff=0)

    def delete_block():
        if block_data in code:
            code.remove(block_data)
        block.destroy()

    menu.add_command(label="Eliminar", command=delete_block)
    def show_menu(event):
        menu.tk_popup(event.x_root, event.y_root)
    text.bind("<Button-3>", show_menu)
    block.bind("<Button-3>", show_menu)  


def createBlocks(paleta, consolaDeBloques, i):

    #print()
    block1 = Frame(paleta, bg="green")
    block1.place(x=20, y=20)
    text1 = Label(block1, text="print", bg="green")
    text1.grid(row=0, column=1, pady=5)
    entry1 = Entry(block1, width=3)
    entry1.grid(row=0, column=2, padx=5)
    text1.bind("<Button-1>", lambda e: clone_block(consolaDeBloques, i, "print", entry1.get()))

    #wait()
    block2 = Frame(paleta, bg="green")
    block2.place(x=20, y=80)
    text2 = Label(block2, text="wait", bg="green")
    text2.grid(row=0, column=1, pady=5)
    entry2 = Entry(block2, width=3)
    entry2.grid(row=0, column=2, padx=5)
    text2.bind("<Button-1>", lambda e: clone_block(consolaDeBloques, i, "wait", entry2.get()))
