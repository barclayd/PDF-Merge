import PyPDF2
from tkinter.filedialog import *
root = Tk()
root.title('PDF Merge')

# PDFs
documents = []
documents_length = IntVar()
filename = StringVar()
page_count = StringVar()
page_start = StringVar()
page_end = StringVar()


class PDF:
    def __init__(self, file):
        self.file = file
        self.filename = file.split('/')[-1]
        self.pages = self.set_pages()
        self.pdf_reader = None
        self.start = 1
        self.end = self.pages

    def open(self):
        return open(self.file, 'rb')

    def read(self):
        self.pdf_reader = PyPDF2.PdfFileReader(self.open())
        self.close()

    def set_pages(self):
        self.read()
        return self.pdf_reader.getNumPages()

    def add_pages(self, page_range):
        for page in range((int(page_range[0].get())-1), int(page_range[1].get())):
            pdf_writer.addPage(self.pdf_reader.getPage(page))

    def close(self):
        self.open().close()

    def merge(self):
        self.get_file_name()
        self.open()
        self.read()
        self.add_pages([self.start, self.end])
        self.close()

    def get_file_name(self):
        self.file = input('Please enter the name of the PDF file you wish to merge: ')

    def load_file(self):
        self.file = askopenfilename(filetypes=(("PDF File", "*.pdf"), ('All Files', '*.*')))
        self.filename.set(self.file.split('/')[-1])
        self.read()

    def add_to_merged_pdf(self):
        self.add_pages([self.start, self.end])
        self.close()


# instantiated classes
pdf_writer = PyPDF2.PdfFileWriter()


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
    file = askopenfilename(filetypes=(("PDF File", "*.pdf"), ('All Files', '*.*')))
    new_pdf = PDF(file)
    new_pdf.read()
    documents.append(new_pdf)
    # update listbox
    listbox.insert(END, new_pdf.filename)


def remove_pdf():
    documents.pop(get_selected_pdf())
    listbox.delete(ANCHOR)
    clear_display()


def display_pdf(*args):
    index = int(listbox.curselection()[0])
    value = listbox.get(index)
    print(value)
    filename.set(documents[index].filename)
    page_count.set(documents[index].pages)
    page_start.set(documents[index].start)
    page_end.set(documents[index].end)


def clear_display():
    global filename, page_count, page_start, page_end
    filename = StringVar()
    page_count = StringVar()
    page_start = StringVar()
    page_end = StringVar()


def get_selected_pdf():
    return int(listbox.curselection()[0])


def set_page_start(*args):
    index = int(listbox.curselection()[0])
    documents[index].start = int(page_start.get())


def set_page_end(*args):
    index = int(listbox.curselection()[0])
    documents[index].end = int(page_end.get())


# GUI
Label(root, text='Combine and Merge PDFs').grid(row=0, column=0, columnspan=4)
Button(root, text='Add PDF', command=add_new_pdf).grid(row=2, column=0)
Button(root, text='Remove PDF', command=remove_pdf).grid(row=3, column=0)

listbox = Listbox(root)
listbox.bind('<<ListboxSelect>>', display_pdf)
listbox.grid(row=1, rowspan=4, column=1)

Label(root, text='File: ').grid(row=1, column=2)
Label(root, textvariable=filename, width=20).grid(row=1, column=3, sticky=(N, S, E, W))
Label(root, text='Pages: ').grid(row=2, column=2)
Label(root, textvariable=page_count, width=20).grid(row=2, column=3, sticky=(N, S, E, W))
Label(root, text='Start: ').grid(row=3, column=2)
entry_1 = Entry(root, textvariable=page_start, width=3)
entry_1.grid(row=3, column=3)
Label(root, text='End: ').grid(row=4, column=2)
entry_2 = Entry(root, textvariable=page_end, width=3)
entry_2.grid(row=4, column=3)

Button(root, text='Save and Merge PDF', command=merge_documents, width=10).grid(row=5, column=0, columnspan=4)

# style GUI
for child in root.winfo_children():
    child.grid_configure(padx=10, pady=10)

# trace variable changes
page_start.trace('w', set_page_start)
page_end.trace('w', set_page_end)

root.mainloop()
