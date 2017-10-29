#from win32com.client import DispatchEx
from openpyxl import *
from tkinter import *
from tkinter.filedialog import askopenfilename, askdirectory

def RemoveItem():
    inFiles.remove(inList.get(inList.curselection()))
    inList.delete(inList.curselection())

def AddItem():
    fname = askopenfilename(filetypes=(
        ("MS Excel Files", "*.xlsx"),
        ("All files", "*.*") ))
    inFiles.append(fname)
    inList.insert(END, fname)

def ChangeOutput():
    OutDir = askdirectory()
    OutFile = OutDir + "/Output.xlsx"
    outList.delete(END, 0)
    outList.insert(END, OutFile)
    pass

def mergeSheets():
    outXLS = Workbook()
    for inFile in inFiles:
        inXLS = load_workbook(inFile)
        inXLS.close()

mGui=Tk()
ment=StringVar()

mGui.geometry("800x600")
mGui.title("First Instance")

inFiles=[]

OutFile=""

InputLabel=Label(mGui, text="Input File(s)").grid(column=0, row=0, columnspan=2)
OutputLabel=Label(mGui, text="Output File(s)").grid(column=2, row=0, columnspan=2)

inList = Listbox(mGui, width=50, height=30)
inList.grid(column=0, row=1, columnspan=2)

outList = Listbox(mGui, width=50, height=30)
outList.grid(column=2, row=1, columnspan=2)

AddButton=Button(mGui, text="Add Input File...", command=AddItem).grid(column=0, row=2)
RemoveButton=Button(mGui, text="Remove Input File", command=RemoveItem).grid(column=1, row=2)

ChangeButton=Button(mGui, text="Change Output Directory...", command=ChangeOutput).grid(column=2, row=2, columnspan=2)

















































