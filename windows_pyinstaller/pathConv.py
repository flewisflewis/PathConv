# pathConv
# Python 3 for PyInstaller on Win
# Operates on the clipboard
# Converts Windows Path to Unix
# Converts Unix Path to Windows

import tkinter as tk
from tkinter import messagebox as msg

import pyperclip


def notValidMsg():
    msg.showinfo("Info", "Not a valid source path.")


def main():

    root = tk.Tk()  # Needed to avoid having a window pop up
    root.withdraw()  # Needed to avoid having a window pop up
    path = pyperclip.paste().replace('"', "")

    if path:
        # The first item in reps will always be used when converting to Unix
        reps = ["/Volumes/Shogun", "Shogun"]
        if "/" in path:
            if not "\\" in path:
                for rep in reps:
                    if path.startswith(rep):
                        path = path.replace(rep, "X:", 1)
                        break
                path = path.replace("/", "\\")
                pyperclip.copy(path)
                msg.showinfo("Info", "Converted Unix Path to Windows.")
            else:
                notValidMsg()
        else:
            if "\\" in path:
                path = path.replace("\\", "/")
                if path.startswith("X:"):
                    path = path.replace("X:", reps[0], 1)
                pyperclip.copy(path)
                msg.showinfo("Info", "Converted Windows Path to Unix.")
            else:
                notValidMsg()
    else:
        notValidMsg()


if __name__ == "__main__":
    main()
