from tkinter import *
from tkinter.filedialog import *
root = Tk()
root.title('PDF Merge')

file_loader = None
filename1 = StringVar()
total_pages = str(6)
pages_1 = 1
save_pdf = None


def load_file():
    file = askopenfilename(filetypes=(("PDF File", "*.pdf"), ('All Files', '*.*')))
    filename1.set(file.split('/')[-1])


# draw tkinter gui using grid
Label(root, text='PDF Merge').grid(row=0, column=2, sticky=E)
Button(root, text='Add PDF', command=load_file).grid(row=1, column=0)
Label(root, textvariable=filename1, width=20).grid(row=1, column=1, sticky=(N, S, E, W))
Label(root, text='Pages').grid(row=1, column=2)
Label(root, textvariable=total_pages, width=3).grid(row=1, column=3, sticky=(N, S, E, W))
Label(root, text='Start: ').grid(row=1, column=4)
entry_1 = Entry(root, textvariable=pages_1, width=3)
entry_1.grid(row=1, column=5)
Label(root, text='End: ').grid(row=1, column=6)
entry_2 = Entry(root, textvariable=pages_1, width=3)
entry_2.grid(row=1, column=7)

Button(root, text='Save and Merge PDF', command=save_pdf, width=10).grid(row=3, column=2, sticky=E)

# style each element in GUI
for child in root.winfo_children():
    child.grid_configure(padx=10, pady=10)

root.mainloop()
