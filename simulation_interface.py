from tkinter import *

fenetre = Tk()
fenetre.geometry('325x500')
fenetre.title('Calculatrice')
fenetre['bg']= 'black'
fenetre.resizable(height=False, width=False)

label = Label(fenetre, text="text")
label.pack(side=RIGHT, padx=50)

fenetre.mainloop()
