import sys
from tkinter import *
# Title, Description, Setup
mGui = Tk()

endinput = StringVar()
vitinput = StringVar()
carinput = StringVar()
atninput = StringVar()

mGui.geometry("300x900")
mGui.title("Dark Souls 2 Stats")

mlabel = Label(mGui, text = "\nA Simple Dark Souls 2 Calculator\nCopyright (C) Benjamin Massey 2014\n").pack()

#Endurance

def mend():
    mendtext = endinput.get()
    endurance = int(mendtext)
    if endurance < 21:
        stamina = 80 + (2 * endurance)

    if endurance > 20:
        stamina = 80 + 40 + (endurance - 20)
        
    endans = "You have " , str(stamina), " total stamina."
    mlabel2 = Label(mGui, text = endans).pack()
    return


endlabel = Label(mGui, text = "Enter your endurance:").pack()

endinputry = Entry(mGui, textvariable = endinput).pack()

mbutton = Button(mGui, text = "Confirm", command = mend).pack()

#Vitality

def mvit():
    mvittext = vitinput.get()
    vitality = int(mvittext)
    CarryWeight = (1.5 * vitality) + 38.5

    if vitality > 29:
        mlabel3 = Label(mGui, text = "Your vitality is too high to\nperfectly calculate, but it should be\naround " + str(CarryWeight) + " pounds.").pack()

    if vitality <= 29:
        mlabel3 = Label(mGui, text = "You can hold: " + str(CarryWeight) + " pounds.").pack()
    return

vitlabel = Label(mGui, text = "Enter your vitality:").pack()

vitinputry = Entry(mGui, textvariable = vitinput).pack()

mbutton2 = Button(mGui, text = "Confirm", command = mvit).pack()

#Carrrying (Uses Vitality)

def mcar():
    mcartext = carinput.get()
    carrying = int(mcartext)
    mvittext = vitinput.get()
    vitality = int(mvittext)
    CarryWeight = (1.5 * vitality) + 38.5
    CarryPercent = round((100 * carrying / CarryWeight), 1)
    mlabel4 = Label(mGui, text = "You should have around " + str(CarryPercent) + "% carry capacity.").pack()
    return
    
carlabel = Label(mGui, text = "How much are you carrying?:").pack()

carinputry = Entry(mGui, textvariable = carinput).pack()

mbutton3 = Button(mGui, text = "Confirm", command = mcar).pack()

#Attunement

def matn():
    matntext = atninput.get()
    attunement = int(matntext)
    if attunement < 10:
        mlabel45 = Label(mGui, text = "You have no attunement slots.").pack()

    elif attunement < 14:
        mlabel45 = Label(mGui, text = "You have one attunement slot.").pack()

    elif attunement < 16:
        mlabel45 = Label(mGui, text = "You have two attunement slots.").pack()

    elif attunement < 20:
        mlabel45 = Label(mGui, text = "You have three attunemnet slots.").pack()

    elif attunement < 25:
        mlabel45 = Label(mGui, text = "You have four attunement slots.").pack()

    elif attunement < 30:
        mlabel45 = Label(mGui, text = "You have five attunemnet slots.").pack()
    
    elif attunement < 40:
        mlabel45 = Label(mGui, text = "You have six attunement slots.").pack()

    elif attunement < 50:
        mlabel45 = Label(mGui, text = "You have seven attunemnet slots.").pack()

    elif attunement < 60:
        mlabel45 = Label(mGui, text = "You have eight attunement slots.").pack()
    
    elif attunement < 75:
        mlabel45 = Label(mGui, text = "You have nine attunement slots.").pack()

    else:
        mlabel45 = Label(mGui, text = "You have the maximum attunement slots, 10.").pack()
    return

atnlabel = Label(mGui, text = "Enter your attunement:").pack()

atninputry = Entry(mGui, textvariable = atninput).pack()

mbutton3 = Button(mGui, text = "Confirm", command = matn).pack()

outlabel = Label(mGui, text = "\n\nCHARACTER INFORMATION:\n").pack()
