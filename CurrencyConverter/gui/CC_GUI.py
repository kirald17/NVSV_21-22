# Python Framework
from tkinter import *

# Funktionen bei user eingabe
def convertValue():
    print("Hehehe")

# Ein Fenster erstellen
window = Tk()
# Window widh und height
window.geometry("400x300")
# Einen Fenstertitel hinzufügen
window.title("Currency Converter by Alex")

# Variables Euro
euro_label = Label(window, text="Euro")
euro_label.grid(row=0, column=0)
amount_euro = StringVar()
euro_entry = Entry(window, textvariable=amount_euro)
euro_entry.grid(row=0, column=1)

# Variable Dollar
dollar_label = Label(window, text="Dollar")
dollar_label.grid(row=0, column=3)
amout_dollar = StringVar()
dollar_entry = Entry(window, textvariable=amout_dollar)
dollar_entry.grid(row=0, column=4)

# Convert Button
convertBtn = Button(window, text="Convert", command=convertValue)
convertBtn.grid(row=1, column=2, columnspan=2)



# Components den Window hinzufügen
# convertBtn.pack()
# Never combine .grid() with pack()



# Loop um auf eine Usereingabe zu warten; Hier läuft mein Progamm dann wirklich
window.mainloop()



