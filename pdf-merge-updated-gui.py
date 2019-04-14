import PyPDF2
from tkinter.filedialog import *
root = Tk()
root.title('PDF Merge')

# PDFs
documents = []
documents_length = IntVar()
test = None
display = None


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
        self.set_page_range()
        self.add_pages(self.page_range)
        self.close()

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


def add_new_pdf():
    documents.append(PDF())
    documents_length.set(len(documents))


# GUI
Label(root, text='Combine and Merge PDFs').grid(row=0, column=0, columnspan=4)
Button(root, text='Add PDF', command=add_new_pdf).grid(row=2, column=0)
Button(root, text='Remove PDF', command=add_new_pdf).grid(row=3, column=0)

listbox = Listbox(root)
listbox.bind('<<ListboxSelect>>', display)
listbox.grid(row=1, rowspan=4, column=1)

Label(root, text='File: ').grid(row=1, column=2)
Label(root, textvariable=test, width=20).grid(row=1, column=3, sticky=(N, S, E, W))
Label(root, text='Pages: ').grid(row=2, column=2)
Label(root, textvariable=test, width=20).grid(row=2, column=3, sticky=(N, S, E, W))
Label(root, text='Start: ').grid(row=3, column=2)
entry_1 = Entry(root, textvariable=test, width=3)
entry_1.grid(row=3, column=3)
Label(root, text='End: ').grid(row=4, column=2)
entry_2 = Entry(root, textvariable=test, width=3)
entry_2.grid(row=4, column=3)

Button(root, text='Save and Merge PDF', command=merge_documents, width=10).grid(row=5, column=0, columnspan=4)

# style GUI
for child in root.winfo_children():
    child.grid_configure(padx=10, pady=10)

root.mainloop()
