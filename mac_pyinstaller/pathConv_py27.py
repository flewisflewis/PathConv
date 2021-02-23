# pathConv
# Operates on the clipboard in Windows
# Converts Windows Path to Unix
# Converts Unix Path to Windows

import Tkinter as tk
import tkMessageBox as msg


def notValidMsg():
    msg.showinfo("Info", "Not a valid source path.")


def main():
    root = tk.Tk()
    root.withdraw()

    path = root.clipboard_get()

    if path:
        # The first item in reps will always be used when converting to Unix
        reps = ["/Volumes/Rodan", "Rodan"]
        if "/" in path:
            if not "\\" in path:
                reps = ["/Volumes/Rodan", "Rodan"]
                for rep in reps:
                    if path.startswith(rep):
                        path = path.replace(rep, "X:", 1)
                        break
                path = path.replace("/", "\\")
                root.clipboard_clear()
                root.clipboard_append(path)
                print "Converted Unix Path to Windows."
                msg.showinfo("Info", "Converted Unix Path to Windows.")
            else:
                notValidMsg()
        else:
            if "\\" in path:
                path = path.replace("\\", "/")
                if path.startswith("X:"):
                    path = path.replace("X:", reps[0], 1)
                root.clipboard_clear()
                root.clipboard_append(path)
                msg.showinfo("Info", "Converted Windows Path to Unix.")
            else:
                notValidMsg()
    else:
        notValidMsg()


if __name__ == "__main__":
    main()
