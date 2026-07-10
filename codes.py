import time, os

def Play(code):
    print("Play")
    for block_type, entry in code:
        if block_type == "print":
            print(entry.get())
        elif block_type == "wait":
            time.sleep(float(entry.get()))