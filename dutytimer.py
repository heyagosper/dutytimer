#!/usr/bin/env python

from Tkinter import *

#TODO find out about playing sounds
#import mp3play

def messageWindow() :
    win = Toplevel()

    b = Button(win, text='Good work, Princess',
               bg="blue", fg="yellow",
               activebackground="red", activeforeground="white",
               padx=root.winfo_screenwidth()/2,
               pady=root.winfo_screenheight()/2,
               command=quit)
    b.pack()

    #root.mainloop()

def show_alert() :
    root.bell()
    finished.set(1)
    messageWindow()

    #quit()

def phase_change() :
    root.bell()
    if finished.get() == 0:
        root.after(phaseScale.get() * 1000, phase_change)

def start_timer() :
    root.after(phaseScale.get() * 1000, phase_change)
    root.after(mainScale.get() * 5000, show_alert)

root = Tk()

finished = IntVar()
finished.set(0)

minutes = Label(root, text="Minutes of quality time:")
minutes.grid(row=0, column=0)

mainScale = Scale(root, from_=1, to=45, orient=HORIZONTAL, length=300)
mainScale.grid(row=0, column=1)

phaseScale = Label(root, text="Seconds in phase:")
phaseScale.grid(row=1, column=0)

phaseScale = Scale(root, from_=1, to=45, orient=HORIZONTAL, length=300)
phaseScale.grid(row=1, column=1)

button = Button(root, text="Start quality time", command=start_timer)
button.grid(row=2, column=1, pady=5, sticky=E)

#TODO sounds
#pushPhaseSound = mp3play.load('push.mp3'); playPushSound = lambda: pushPhaseSound.play()
#stirPhaseSound = mp3play.load('siir.mp3'); playStirSound = lambda: stirPhaseSound.play()

root.mainloop()
