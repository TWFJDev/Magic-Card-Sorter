from tkinter import *
from tkinter import ttk

# Function to help with clearing entry boxes
def clearEntryBoxes():
    itemNumberEntry.delete(0, END)
    cardNameEntry.delete(0, END)
    typeEntry.delete(0, END)
    subTypeEntry.delete(0, END)
    manaType1Entry.delete(0, END)
    manaCost1Entry.delete(0, END)
    manaType2Entry.delete(0, END)
    manaCost2Entry.delete(0, END)
    powerToughnessEntry.delete(0, END)
    cardNumberEntry.delete(0, END)
    type3Entry.delete(0, END)
    type4Entry.delete(0, END)
    type5Entry.delete(0, END)
    type6Entry.delete(0, END)
    type7Entry.delete(0, END)

#def addACard():

# Selecting a card
def selectACard(e):
    clearEntryBoxes()

    selected = treeTable.focus()

    values = treeTable.item(selected, 'values')

    itemNumberEntry.insert(0, values[0])
    cardNameEntry.insert(0, values[1])
    typeEntry.insert(0, values[2])
    subTypeEntry.insert(0, values[3])
    manaType1Entry.insert(0, values[9])
    manaCost1Entry.insert(0, values[10])
    manaType2Entry.insert(0, values[11])
    manaCost2Entry.insert(0, values[12])
    powerToughnessEntry.insert(0, values[13])
    cardNumberEntry.insert(0, values[14])
    type3Entry.insert(0, values[4])
    type4Entry.insert(0, values[5])
    type5Entry.insert(0, values[6])
    type6Entry.insert(0, values[7])
    type7Entry.insert(0, values[8])

# Updating card info
def updateACard():
    selected = treeTable.focus()
    treeTable.item(selected, text = "", values = (
        itemNumberEntry.get(), 
        cardNameEntry.get(), 
        typeEntry.get(), 
        subTypeEntry.get(),
        type3Entry.get(),
        type4Entry.get(),
        type5Entry.get(),
        type6Entry.get(),
        type7Entry.get(), 
        manaType1Entry.get(), 
        manaCost1Entry.get(),
        manaType2Entry.get(), 
        manaCost2Entry.get(), 
        powerToughnessEntry.get(), 
        cardNumberEntry.get()
        ))

    clearEntryBoxes()

# Removing a card
def removeACard():
    x = treeTable.selection()[0]
    treeTable.delete(x)

# Removing many cards
def removeMultipleCards():
    x = treeTable.selection()

    for card in x:
        treeTable.delete(card)

# Removing everything
def removeCards():
    for card in treeTable.get_children():
        treeTable.delete(card)

magicSorter = Tk()
magicSorter.title('Card Sorter!')

# Styling
style = ttk.Style()

# Theme
style.theme_use('alt')

# Config Colors
style.configure("Treeview",
    background = "grey",
    foreground = "black",
    fieldbackground = "silver",
    rowheight = 25)

# Change selected color
style.map('Treeview',
    background = [('selected', '#A4A8A4')])

# Create Treeview frame
treeFrame = Frame(magicSorter)
treeFrame.pack(padx = 10, pady = 10)

# Scrollbar
treeScroll = Scrollbar(treeFrame)
treeScroll.pack(side = RIGHT, fill = Y)

# Create Treeview
treeTable = ttk.Treeview(treeFrame, yscrollcommand = treeScroll.set, selectmode = "extended")
treeTable.pack()

# Scrollbar config
treeScroll.config(command = treeTable.yview)

# Define columns
treeTable['columns'] = ("Item #", "Card Name", "Type 1", "Type 2", "Type 3", "Type 4", "Type 5", "Type 6", "Type 7", "Mana Type 1", "Mana Cost 1", "Mana Type 2", "Mana Cost 2", "Power/Toughness", "Card Number")

# Format Columns
treeTable.column("#0", width = 0, stretch = NO)
treeTable.column("Item #", anchor = CENTER, width = 70, minwidth = 55)
treeTable.column("Card Name", anchor = CENTER, width = 150)
treeTable.column("Type 1", anchor = CENTER, width = 100)
treeTable.column("Type 2", anchor = CENTER, width = 100)
treeTable.column("Type 3", anchor = CENTER, width = 100)
treeTable.column("Type 4", anchor = CENTER, width = 100)
treeTable.column("Type 5", anchor = CENTER, width = 100)
treeTable.column("Type 6", anchor = CENTER, width = 100)
treeTable.column("Type 7", anchor = CENTER, width = 100)
treeTable.column("Mana Type 1", anchor = CENTER, width = 100)
treeTable.column("Mana Cost 1", anchor = CENTER, width = 100)
treeTable.column("Mana Type 2", anchor = CENTER, width = 100)
treeTable.column("Mana Cost 2", anchor = CENTER, width = 100)
treeTable.column("Power/Toughness", anchor = CENTER, width = 150)
treeTable.column("Card Number", anchor = CENTER, width = 150)

# Create Headings
treeTable.heading("#0", text = "", anchor = CENTER)
treeTable.heading("Item #", text = "Item #", anchor = CENTER)
treeTable.heading("Card Name", text = "Card Name", anchor = CENTER)
treeTable.heading("Type 1", text = "Type 1", anchor = CENTER)
treeTable.heading("Type 2", text = "Type 2", anchor = CENTER)
treeTable.heading("Type 3", text = "Type 3", anchor = CENTER)
treeTable.heading("Type 4", text = "Type 4", anchor = CENTER)
treeTable.heading("Type 5", text = "Type 5", anchor = CENTER)
treeTable.heading("Type 6", text = "Type 6", anchor = CENTER)
treeTable.heading("Type 7", text = "Type 7", anchor = CENTER)
treeTable.heading("Mana Type 1", text = "Mana Type 1", anchor = CENTER)
treeTable.heading("Mana Cost 1", text = "Mana Cost", anchor = CENTER)
treeTable.heading("Mana Type 2", text = "Mana Type 2", anchor = CENTER)
treeTable.heading("Mana Cost 2", text = "Mana Cost", anchor = CENTER)
treeTable.heading("Power/Toughness", text = "Power/Toughness", anchor = CENTER)
treeTable.heading("Card Number", text = "Card Number", anchor = CENTER)

# Add fake data
data = [
    ["1", "Card Name 1", "Type 1", "Type 2", "Type 3", "Type 4", "Type 5", "Type 6", "Type 7", "Mana Type 1", "Mana Cost 1", "Mana Type 2", "Mana Cost 1", "Power/Toughness 1", "Card Number 1"],
    ["2", "Card Name 2", "Type 1", "Type 2", "Type 3", "Type 4", "Type 5", "Type 6", "Type 7", "Mana Type 2", "Mana Cost 2", "Mana Type 2", "Mana Cost 1", "Power/Toughness 2", "Card Number 2"],
    ["3", "Card Name 3", "Type 1", "Type 2", "Type 3", "Type 4", "Type 5", "Type 6", "Type 7", "Mana Type 3", "Mana Cost 3", "Mana Type 2", "Mana Cost 1", "Power/Toughness 3", "Card Number 3"],
    ["4", "Card Name 4", "Type 1", "Type 2", "Type 3", "Type 4", "Type 5", "Type 6", "Type 7", "Mana Type 4", "Mana Cost 4", "Mana Type 2", "Mana Cost 1", "Power/Toughness 4", "Card Number 4"],
    ["5", "Card Name 5", "Type 1", "Type 2", "Type 3", "Type 4", "Type 5", "Type 6", "Type 7", "Mana Type 5", "Mana Cost 5", "Mana Type 2", "Mana Cost 1", "Power/Toughness 5", "Card Number 5"],
    ["6", "Card Name 6", "Type 1", "Type 2", "Type 3", "Type 4", "Type 5", "Type 6", "Type 7", "Mana Type 6", "Mana Cost 6", "Mana Type 2", "Mana Cost 1", "Power/Toughness 6", "Card Number 6"],
    ["7", "Card Name 7", "Type 1", "Type 2", "Type 3", "Type 4", "Type 5", "Type 6", "Type 7", "Mana Type 7", "Mana Cost 7", "Mana Type 2", "Mana Cost 1", "Power/Toughness 7", "Card Number 7"],
    ["8", "Card Name 8", "Type 1", "Type 2", "Type 3", "Type 4", "Type 5", "Type 6", "Type 7", "Mana Type 8", "Mana Cost 8", "Mana Type 2", "Mana Cost 1", "Power/Toughness 8", "Card Number 8"],
    ["9", "Card Name 9", "Type 1", "Type 2", "Type 3", "Type 4", "Type 5", "Type 6", "Type 7", "Mana Type 9", "Mana Cost 9", "Mana Type 2", "Mana Cost 1", "Power/Toughness 9", "Card Number 9"],
    ["10", "Card Name 10", "Type 1", "Type 2", "Type 3", "Type 4", "Type 5", "Type 6", "Type 7", "Mana Type 10", "Mana Cost 10", "Mana Type 2", "Mana Cost 1", "Power/Toughness 10", "Card Number 10"],
    ["11", "Card Name 11", "Type 1", "Type 2", "Type 3", "Type 4", "Type 5", "Type 6", "Type 7", "Mana Type 11", "Mana Cost 11", "Mana Type 2", "Mana Cost 1", "Power/Toughness 11", "Card Number 11"],
    ["12", "Card Name 12", "Type 1", "Type 2", "Type 3", "Type 4", "Type 5", "Type 6", "Type 7", "Mana Type 12", "Mana Cost 12", "Mana Type 2", "Mana Cost 1", "Power/Toughness 12", "Card Number 12"],
    ["13", "Card Name 13", "Type 1", "Type 2", "Type 3", "Type 4", "Type 5", "Type 6", "Type 7", "Mana Type 13", "Mana Cost 13", "Mana Type 2", "Mana Cost 1", "Power/Toughness 13", "Card Number 13"],
    ["14", "Card Name 14", "Type 1", "Type 2", "Type 3", "Type 4", "Type 5", "Type 6", "Type 7", "Mana Type 14", "Mana Cost 14", "Mana Type 2", "Mana Cost 1", "Power/Toughness 14", "Card Number 14"],
    ["15", "Card Name 15", "Type 1", "Type 2", "Type 3", "Type 4", "Type 5", "Type 6", "Type 7", "Mana Type 15", "Mana Cost 15", "Mana Type 2", "Mana Cost 1", "Power/Toughness 15", "Card Number 15"],
    ["16", "Card Name 16", "Type 1", "Type 2", "Type 3", "Type 4", "Type 5", "Type 6", "Type 7", "Mana Type 16", "Mana Cost 16", "Mana Type 2", "Mana Cost 1", "Power/Toughness 16", "Card Number 16"],
    ["17", "Card Name 17", "Type 1", "Type 2", "Type 3", "Type 4", "Type 5", "Type 6", "Type 7", "Mana Type 17", "Mana Cost 17", "Mana Type 2", "Mana Cost 1", "Power/Toughness 17", "Card Number 17"],
    ["18", "Card Name 18", "Type 1", "Type 2", "Type 3", "Type 4", "Type 5", "Type 6", "Type 7", "Mana Type 18", "Mana Cost 18", "Mana Type 2", "Mana Cost 1", "Power/Toughness 18", "Card Number 18"],
]

# Create Striped Rows
treeTable.tag_configure('oddrow', background = "lightpink")
treeTable.tag_configure('evenrow', background = "white")

# Add data to screen
count = 0

for card in data:
    if count % 2 == 0:
        treeTable.insert(parent = '', index = 'end', iid = count, text = '', values = (card[0], card[1], card[2], card[3], card[4], card[5], card[6], card[7], card[8], card[9], card[10], card[11], card[12], card[13], card[14]), tags = ('evenrow',))
    else:
        treeTable.insert(parent = '', index = 'end', iid = count, text = '', values = (card[0], card[1], card[2], card[3], card[4], card[5], card[6], card[7], card[8], card[9], card[10], card[11], card[12], card[13], card[14]), tags = ('oddrow',))
    
    # Increment counter
    count += 1

# Add card data frame
cardDataFrame = LabelFrame(magicSorter, text = "Card Data:")
cardDataFrame.pack(fill = 'x', expand = 'yes', padx = 10, pady = 10)

# Add card data label / entry boxes
itemNumberLabel = Label(cardDataFrame, text = "Item #:")
itemNumberLabel.grid(row = 0, column = 0, padx = 10, pady = 10)

itemNumberEntry = Entry(cardDataFrame, border = 2)
itemNumberEntry.grid(row = 0, column = 1, padx = 10, pady = 10)

cardNameLabel = Label(cardDataFrame, text = "Card Name:")
cardNameLabel.grid(row = 0, column = 2, padx = 10, pady = 10)

cardNameEntry = Entry(cardDataFrame, border = 2)
cardNameEntry.grid(row = 0, column = 3, padx = 10, pady = 10)

typeLabel = Label(cardDataFrame, text = "Type 1:")
typeLabel.grid(row = 0, column = 4, padx = 10, pady = 10)

typeEntry = Entry(cardDataFrame, border = 2)
typeEntry.grid(row = 0, column = 5, padx = 10, pady = 10)

subTypeLabel = Label(cardDataFrame, text = "Type 2:")
subTypeLabel.grid(row = 0, column = 6, padx = 10, pady = 10)

subTypeEntry = Entry(cardDataFrame, border = 2)
subTypeEntry.grid(row = 0, column = 7, padx = 10, pady = 10)

powerToughnessLabel = Label(cardDataFrame, text = "Power/Toughness:")
powerToughnessLabel.grid(row = 1, column = 0, padx = 10, pady = 10)

powerToughnessEntry = Entry(cardDataFrame, border = 2)
powerToughnessEntry.grid(row = 1, column = 1, padx = 10, pady = 10)

cardNumberLabel = Label(cardDataFrame, text = "Card Number:")
cardNumberLabel.grid(row = 1, column = 2, padx = 10, pady = 10)

cardNumberEntry = Entry(cardDataFrame, border = 2)
cardNumberEntry.grid(row = 1, column = 3, padx = 10, pady = 10)

# Add mana frame
manaDataFrame = LabelFrame(magicSorter, text = "Mana Types & Cost:")
manaDataFrame.pack(fill = 'x', expand = 'yes', padx = 10, pady = 10)

# Add mana types & entry
manaType1Label = Label(manaDataFrame, text = "Mana Type 1:")
manaType1Label.grid(row = 0, column = 0, padx = 10, pady = 10)

manaType1Entry = Entry(manaDataFrame, border = 2)
manaType1Entry.grid(row = 0, column = 1, padx = 10, pady = 10)

manaCost1Label = Label(manaDataFrame, text = "Mana Cost:")
manaCost1Label.grid(row = 0, column = 2, padx = 10, pady = 10)

manaCost1Entry = Entry(manaDataFrame, border = 2)
manaCost1Entry.grid(row = 0, column = 3, padx = 10, pady = 10)

manaType2Label = Label(manaDataFrame, text = "Mana Type 2:")
manaType2Label.grid(row = 0, column = 4, padx = 10, pady = 10)

manaType2Entry = Entry(manaDataFrame, border = 2)
manaType2Entry.grid(row = 0, column = 5, padx = 10, pady = 10)

manaCost2Label = Label(manaDataFrame, text = "Mana Cost:")
manaCost2Label.grid(row = 0, column = 6, padx = 10, pady = 10)

manaCost2Entry = Entry(manaDataFrame, border = 2)
manaCost2Entry.grid(row = 0, column = 7, padx = 10, pady = 10)

# Add extra type frame
typeDataFrame = LabelFrame(magicSorter, text = "Extra Types:")
typeDataFrame.pack(fill = 'x', expand = 'yes', padx = 10, pady = 10)

# Add extra type label / entry boxes
type3Label = Label(typeDataFrame, text = "Type 3:")
type3Label.grid(row = 0, column = 0, padx = 10, pady = 10)

type3Entry = Entry(typeDataFrame, border = 2)
type3Entry.grid(row = 0, column = 1, padx = 10, pady = 10)

type4Label = Label(typeDataFrame, text = "Type 4:")
type4Label.grid(row = 0, column = 2, padx = 10, pady = 10)

type4Entry = Entry(typeDataFrame, border = 2)
type4Entry.grid(row = 0, column = 3, padx = 10, pady = 10)

type5Label = Label(typeDataFrame, text = "Type 5:")
type5Label.grid(row = 0, column = 4, padx = 10, pady = 10)

type5Entry = Entry(typeDataFrame, border = 2)
type5Entry.grid(row = 0, column = 5, padx = 10, pady = 10)

type6Label = Label(typeDataFrame, text = "Type 6:")
type6Label.grid(row = 0, column = 6, padx = 10, pady = 10)

type6Entry = Entry(typeDataFrame, border = 2)
type6Entry.grid(row = 0, column = 7, padx = 10, pady = 10)

type7Label = Label(typeDataFrame, text = "Type 7:")
type7Label.grid(row = 0, column = 8, padx = 10, pady = 10)

type7Entry = Entry(typeDataFrame, border = 2)
type7Entry.grid(row = 0, column = 9, padx = 10, pady = 10)

# Add button frame
commandDataFrame = LabelFrame(magicSorter, text = "Commands:")
commandDataFrame.pack(fill = 'x', expand = 'yes', padx = 10, pady = 10)

# Add command buttons
addCard = Button(commandDataFrame, text = "Add A Card")
addCard.grid(row = 0, column = 0, padx = 10, pady = 10)

updateCard = Button(commandDataFrame, text = "Update A Card", command = updateACard)
updateCard.grid(row = 0, column = 1, padx = 10, pady = 10)

removeCard = Button(commandDataFrame, text = "Remove A Card", command = removeACard)
removeCard.grid(row = 0, column = 2, padx = 10, pady = 10)

removeManyCards = Button(commandDataFrame, text = "Remove Multiple Cards", command = removeMultipleCards)
removeManyCards.grid(row = 0, column = 3, padx = 10, pady = 10)

removeAllCards = Button(commandDataFrame, text = "Remove All Cards", command = removeCards)
removeAllCards.grid(row = 0, column = 4, padx = 10, pady = 10)

clearEntries = Button(commandDataFrame, text = "Clear Entries", command = clearEntryBoxes)
clearEntries.grid(row = 0, column = 5, padx = 10, pady = 10)

# Key binding
treeTable.bind("<ButtonRelease-1>", selectACard)

# Closing window
magicSorter.mainloop()

# Search bar for each field