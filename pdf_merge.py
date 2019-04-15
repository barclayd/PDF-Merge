import PyPDF2
from tkinter.filedialog import *
root = Tk()

# instantiated classes
pdf_writer = PyPDF2.PdfFileWriter()

# PDFs
documents = []


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
        for page in range((int(page_range[0])-1), int(page_range[1])):
            pdf_writer.addPage(self.pdf_reader.getPage(page))

    def close(self):
        self.open().close()

    def get_file_name(self):
        self.file = input('Please enter the name of the PDF file you wish to merge: ')

    def load_file(self):
        self.file = askopenfilename(filetypes=(("PDF File", "*.pdf"), ('All Files', '*.*')))
        self.filename.set(self.file.split('/')[-1])
        self.read()

    def add_to_merged_pdf(self):
        self.add_pages([self.start, self.end])
        self.close()


# tkinter dynamic variables
filename = StringVar()
page_count = StringVar()
page_start = StringVar()
page_end = StringVar()
