import PyPDF2
from tkinter.filedialog import *
root = Tk()
root.title('PDF Merge')


class PDF:
    def __init__(self):
        self.file = None
        self.filename = StringVar()
        self.pages = IntVar()
        self.pdf_reader = None
        self.page_range = [IntVar(), IntVar()]

    def open(self):
        return open(self.file, 'rb')

    def read(self):
        self.pdf_reader = PyPDF2.PdfFileReader(self.open())
        self.pages.set(self.pdf_reader.getNumPages())
        self.page_range[0].set(1)
        self.page_range[1].set(int(self.pages.get()))

    def add_pages(self, page_range):
        for page in range((int(page_range[0].get())-1), int(page_range[1].get())):
            pdf_writer.addPage(self.pdf_reader.getPage(page))

    def close(self):
        self.open().close()

    def merge(self):
        self.get_file_name()
        self.open()
        self.read()
        self.display_pages()
        self.set_page_range()
        self.add_pages(self.page_range)
        self.close()

    def display_pages(self):
        print("{} has {} pages".format(self.file, self.pages))

    def set_page_range(self):
        first_page = int(input("Number of first page of PDF to be merged: "))
        last_page = int(input("Number of last page of PDF to be merged: "))
        self.page_range = (first_page, last_page)

    def get_file_name(self):
        self.file = input('Please enter the name of the PDF file you wish to merge: ')

    def load_file(self):
        self.file = askopenfilename(filetypes=(("PDF File", "*.pdf"), ('All Files', '*.*')))
        self.filename.set(self.file.split('/')[-1])
        self.read()

    def add_to_merged_pdf(self):
        self.add_pages(self.page_range)
        self.close()


# instantiated classes
pdf_writer = PyPDF2.PdfFileWriter()
pdf_two = PDF()
pdf_one = PDF()

# PDFs
documents = [pdf_one, pdf_two]


# functions
def merge_documents():
    output_filename = asksaveasfilename(filetypes=(('PDF File', '*.pdf'), ('All Files', '*.*')), defaultextension='.pdf')
    output_file = open(output_filename, 'wb')
    for pdf in documents:
        pdf.add_to_merged_pdf()
    # write merged pdf file
    pdf_writer.write(output_file)
    # close and quit
    output_file.close()
    root.quit()


# draw tkinter gui using grid
Label(root, text='Combine and Merge PDFs').grid(row=0, column=2)
# pdf row
Button(root, text='Add PDF', command=documents[0].load_file).grid(row=1, column=0)
Label(root, textvariable=documents[0].filename, width=20).grid(row=1, column=1, sticky=(N, S, E, W))
Label(root, text='Pages').grid(row=1, column=2)
Label(root, textvariable=documents[0].pages, width=3).grid(row=1, column=3, sticky=(N, S, E, W))
Label(root, text='Start: ').grid(row=1, column=4)
entry_1 = Entry(root, textvariable=documents[0].page_range[0], width=3)
entry_1.grid(row=1, column=5)
Label(root, text='End: ').grid(row=1, column=6)
entry_2 = Entry(root, textvariable=documents[0].page_range[1], width=3)
entry_2.grid(row=1, column=7)
# 2nd pdf row
Button(root, text='Add PDF', command=documents[1].load_file).grid(row=2, column=0)
Label(root, textvariable=documents[1].filename, width=20).grid(row=2, column=1, sticky=(N, S, E, W))
Label(root, text='Pages').grid(row=2, column=2)
Label(root, textvariable=documents[1].pages, width=3).grid(row=2, column=3, sticky=(N, S, E, W))
Label(root, text='Start: ').grid(row=2, column=4)
entry_1 = Entry(root, textvariable=documents[1].page_range[0], width=3)
entry_1.grid(row=2, column=5)
Label(root, text='End: ').grid(row=2, column=6)
entry_2 = Entry(root, textvariable=documents[1].page_range[1], width=3)
entry_2.grid(row=2, column=7)


Button(root, text='Save and Merge PDF', command=merge_documents, width=10).grid(row=3, column=2, sticky=E)

# style each element in GUI
for child in root.winfo_children():
    child.grid_configure(padx=10, pady=10)


# set output file settings
# output_file_name = input('Save new file as : ')
# output_file = open(output_file_name, 'wb')

# write merged pdf file
# pdf_writer.write(output_file)

root.mainloop()
