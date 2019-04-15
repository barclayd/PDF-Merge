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
documents = []
documents_length = IntVar()


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
    draw_gui()


def draw_gui():
    for i in range(int(documents_length.get())):
        # pdf row
        Button(root, text='Add PDF', command=documents[i].load_file).grid(row=i + 1, column=0)
        Label(root, textvariable=documents[i].filename, width=20).grid(row=i + 1, column=1, sticky=(N, S, E, W))
        Label(root, text='Pages').grid(row=i + 1, column=2)
        Label(root, textvariable=documents[i].pages, width=3).grid(row=i + 1, column=3, sticky=(N, S, E, W))
        Label(root, text='Start: ').grid(row=i + 1, column=4)
        entry_1 = Entry(root, textvariable=documents[i].page_range[0], width=3)
        entry_1.grid(row=i + 1, column=5)
        Label(root, text='End: ').grid(row=i + 1, column=6)
        entry_2 = Entry(root, textvariable=documents[i].page_range[1], width=3)
        entry_2.grid(row=i + 1, column=7)


def draw_buttons():
    Button(root, text='Add new PDF', command=add_new_pdf, width=10, bg="blue").grid(row=int(documents_length.get()) + 2,
                                                                                    column=8, sticky=E)
    Button(root, text='Save and Merge PDF', command=merge_documents, width=10, bg="blue")\
        .grid(row=int(documents_length.get()) + 3, column=8, sticky=E)


# draw tkinter gui using grid
Label(root, text='Combine and Merge PDFs').grid(row=0, column=2)
draw_buttons()

# style each element in GUI
for child in root.winfo_children():
    child.grid_configure(padx=10, pady=10)


root.mainloop()
