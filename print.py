import keyboard
import sys
import win32print
from pathlib import Path

if keyboard.is_pressed('q'): 
    printers = win32print.EnumPrinters(4)
    printercount = 0
    for x in printers:
        print(printercount, "-", x[2])
        printercount += 1

    chosenprinter = int(input("Printer number? "))

    chosenfile = Path()
    while not chosenfile.is_file():
        file_name = r"directory of the chats file"
        chosenfile = Path(file_name)

    myprinter = win32print.OpenPrinter(printers[chosenprinter][2])

    printjob = win32print.StartDocPrinter(
        myprinter, 1, ("Python test RAW print", None, "raw"))

    with open(chosenfile, mode='rb') as file:
        buf = file.read()

    bytesprinted = win32print.WritePrinter(myprinter, buf)

    win32print.EndDocPrinter(myprinter)
    win32print.ClosePrinter(myprinter)
    sys.exit()