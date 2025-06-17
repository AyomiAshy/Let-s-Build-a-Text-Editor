from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
# Setup the  main window
root = Tk()
root.title("Text Editor")
root.geometry("600x500")
root.rowconfigure(0, minsize = 800, weight = 1)
root.columnconfigure(1, minsize = 800, weight = 1)
# Function to open a file
def open_file():
    filepath = askopenfilename(
        filetypes = [
            ("Text files", "*.txt"),
            ("Python files", "*py"),
            ("All files", ".")
        ]
    )
    if not filepath:
        return
    txt_edit.delete(1.0, END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(END, text)
    root.title(f"Ibrahim's Text Editor - {filepath}")
# Function to save a file
def save_file():
    filepath = asksaveasfilename(
        defaultextension = ".txt",
        filetypes = [
            ("Text Files", "*.txt"),
            ("Python Files", "*.py"),
            ("All files", "*.*")
        ]
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_edit.get(1.0, END)
        output_file.write(text)
    root.title(f"Ibrahim's Text Editor  - {filepath}")
# Add widgets in the application 
txt_edit = Text(root)
fr_buttons = Frame(root, relief = RAISED,  bd = 2)
btn_open = Frame(fr_buttons, text = "Open", command = open_file)
btn_save = Frame(fr_buttons, text ="Save As...", command = save_file)
btn_open.grid(row = 0, column = 0, sticky = "ew", padx = 5, pady = 5)
btn_save.grid(row = 0, column = 0, sticky = "ew", padx = 5)
fr_buttons.grid(row = 0, column = 0 , sticky = "ns")
txt_edit.grid(row = 0, column = 1, sticky = "nsew")
# Run the applictaion
root.mainloop()
