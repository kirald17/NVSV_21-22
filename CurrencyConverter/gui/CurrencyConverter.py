# Python Framework
from tkinter import *

# Funktionen bei user eingabe
def convertValue():
    try:
        global amount_euro, amount_dollar
        euros = amount_euro.get()
        dollars = str(float(euros.replace(",", ".")) * 1.17)
        amount_dollar.set(dollars)
    except ValueError:
        print("Please enter a valid number!")
    except:
        print("Something unexpected happened")


# Ein Fenster erstellen
window = Tk()
# Window widh und height
window.geometry("400x100")
# Einen Fenstertitel hinzufügen
window.title("Currency Converter by Alex")

# Variables Euro
euro_label = Label(window, text="Euro")
euro_label.grid(row=0, column=0, columnspan=1, pady=10, padx=15)
amount_euro = StringVar()
euro_entry = Entry(window, textvariable=amount_euro)
euro_entry.grid(row=0, column=1, pady=10, columnspan=1)

# Variable Dollar
dollar_label = Label(window, text="Dollar")
dollar_label.grid(row=0, column=3, pady=10, columnspan=1)
amount_dollar = StringVar()
dollar_entry = Entry(window, textvariable=amount_dollar)
dollar_entry.grid(row=0, column=4, pady=10, columnspan=1)
dollar_entry.config(state=DISABLED)

# Convert Button
convertBtn = Button(window, text="Convert", command=convertValue)
convertBtn.grid(row=2, column=3, pady=20, columnspan=1)

# Components den Window hinzufügen
# convertBtn.pack()
# Never combine .grid() with pack()

# Loop um auf eine Usereingabe zu warten; Hier läuft mein Progamm dann wirklich
window.mainloop()



