from tkinter import *
import ttkbootstrap as ttk

stop = 0
speed = 150
window = ttk.Window(themename="darkly")
window.title("Speed Reader")
window.geometry(f'{int(window.winfo_screenwidth() / 4)}x{int(window.winfo_screenheight() * 3 / 4)}')

def loop_reader(idx, textCut, reader, word):
    global stop
    global speed
    word.config(text = textCut[idx])
    idx += 1
    if stop == 1:
        stop = 0
        idx = 0
    if idx < len(textCut):
        reader.after(speed, lambda: loop_reader(idx, textCut, reader, word))
    else:
        stop = -1

def restart_reader(textCut, reader, word):
    global stop
    if stop == -1:
        stop = 0
        loop_reader(0, textCut, reader, word)
    else:
        stop = 1

def open_reader(text):
    global speed
    reader = Toplevel(window)
    reader.title("Reader")

    textCut = text.split()
    word = Label(reader, text="", font=("Helvetica", 16))
    word.pack(padx=20, pady=20)
    loop_reader(0, textCut, reader, word)

    double = DoubleVar()
    double.set(speed)
    scale = ttk.Scale(reader, from_=150, to=1000, orient='horizontal', variable=double, length=400 )
    scale.pack(pady = 10, padx = 10)
    def update_speed():
        global speed
        speed = int(double.get())
    scale.config(command=lambda value: update_speed())

    frame = Frame(reader)
    frame.pack(expand=True)
    restartButton = Button(frame, text="Restart", command=lambda:restart_reader(textCut, reader, word), width = 20)
    restartButton.pack(side = LEFT,pady=10, padx = 10)
    closeButton = Button(frame, text="Close", command=reader.destroy, width = 20)
    closeButton.pack(side = LEFT,pady=10, padx = 10)

def mainPage():
    label = Label(window, text="Please enter your texte", font=("Helvetica", 16))
    label.pack(pady=20)

    textBox = Text(window, height=35, width=60)
    textBox.pack()

    frame = Frame(window)
    frame.pack(expand=True)
    closeBouton=ttk.Button(frame, text="Close", command=window.quit, width = 20)
    enterBouton=ttk.Button(frame, text="Enter", command=lambda: open_reader(textBox.get("1.0", END)), width = 20)
    closeBouton.pack(side=LEFT, padx=10)
    enterBouton.pack(side=LEFT, padx=10)

mainPage()
window.mainloop()