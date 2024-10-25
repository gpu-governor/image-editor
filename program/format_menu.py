from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter.font import Font, families
from tkinter.scrolledtext import *

import time
import sys


class Format():

    def __init__(self, text):
        self.text = text

    def changeBg(self):
        (triple, hexstr) = askcolor()
        if hexstr:
            self.text.config(bg=hexstr)

    def changeFg(self):
        (triple, hexstr) = askcolor()
        if hexstr:
            self.text.config(fg=hexstr)

    def bold(self, *args):  # Works only if text is selected
        try:
            current_tags = self.text.tag_names("sel.first")
            if "bold" in current_tags:
                self.text.tag_remove("bold", "sel.first", "sel.last")
            else:
                self.text.tag_add("bold", "sel.first", "sel.last")
                bold_font = Font(self.text, self.text.cget("font"))
                bold_font.configure(weight="bold")
                self.text.tag_configure("bold", font=bold_font)
        except:
            pass

    def italic(self, *args):  # Works only if text is selected
        try:
            current_tags = self.text.tag_names("sel.first")
            if "italic" in current_tags:
                self.text.tag_remove("italic", "sel.first", "sel.last")
            else:
                self.text.tag_add("italic", "sel.first", "sel.last")
                italic_font = Font(self.text, self.text.cget("font"))
                italic_font.configure(slant="italic")
                self.text.tag_configure("italic", font=italic_font)
        except:
            pass

    def underline(self, *args):  # Works only if text is selected
        try:
            current_tags = self.text.tag_names("sel.first")
            if "underline" in current_tags:
                self.text.tag_remove("underline", "sel.first", "sel.last")
            else:
                self.text.tag_add("underline", "sel.first", "sel.last")
                underline_font = Font(self.text, self.text.cget("font"))
                underline_font.configure(underline=1)
                self.text.tag_configure("underline", font=underline_font)
        except:
            pass

    def overstrike(self, *args):  # Works only if text is selected
        try:
            current_tags = self.text.tag_names("sel.first")
            if "overstrike" in current_tags:
                self.text.tag_remove("overstrike", "sel.first", "sel.last")
            else:
                self.text.tag_add("overstrike", "sel.first", "sel.last")
                overstrike_font = Font(self.text, self.text.cget("font"))
                overstrike_font.configure(overstrike=1)
                self.text.tag_configure("overstrike", font=overstrike_font)
        except:
            pass

    def addDate(self):
        full_date = time.localtime()
        day = str(full_date.tm_mday)
        month = str(full_date.tm_mon)
        year = str(full_date.tm_year)
        date = day + '/' + month + '/' + year
        self.text.insert(INSERT, date, "a")


def main(root, text, menubar):
    objFormat = Format(text)

    fontoptions = families(root)
    font = Font(family="Arial", size=10)
    # text.configure(font=font)

    formatMenu = Menu(menubar)

    fsubmenu = Menu(formatMenu, tearoff=0)
    ssubmenu = Menu(formatMenu, tearoff=0)

    for option in fontoptions:
        fsubmenu.add_command(label=option, command=lambda option=option: font.configure(family=option))
    for value in range(1, 31):
        ssubmenu.add_command(label=str(value), command=lambda value=value: font.configure(size=value))

    formatMenu.add_command(label="Change Background", command=objFormat.changeBg)
    formatMenu.add_cascade(label="Font", underline=0, menu=fsubmenu)
    formatMenu.add_cascade(label="Size", underline=0, menu=ssubmenu)
    menubar.add_cascade(label="Format", menu=formatMenu)

    root.bind_all("<Control-b>", objFormat.bold)
    root.bind_all("<Control-i>", objFormat.italic)
    root.bind_all("<Control-u>", objFormat.underline)
    root.bind_all("<Control-T>", objFormat.overstrike)

    root.grid_columnconfigure(0, weight=1)
    root.resizable(True, True)

    root.config(menu=menubar)


if __name__ == "__main":
    print("Please run 'main.py'")
