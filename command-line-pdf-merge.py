import PyPDF2
# welcome message
print("Welcome to PDF Merge, a handy python script to help you merge PDFs for free")


class PDF:
    def __init__(self):
        self.path = None
        self.pages = None
        self.pdf_reader = None
        self.page_range = None

    def open(self):
        return open(self.path, 'rb')

    def read(self):
        self.pdf_reader = PyPDF2.PdfFileReader(self.open())
        self.pages = self.pdf_reader.getNumPages()

    def add_pages(self, page_range):
        for page in range((page_range[0]-1), page_range[1]):
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
        print("{} has {} pages".format(self.path, self.pages))

    def set_page_range(self):
        first_page = int(input("Number of first page of PDF to be merged: "))
        last_page = int(input("Number of last page of PDF to be merged: "))
        self.page_range = (first_page, last_page)

    def get_file_name(self):
        self.path = input('Please enter the name of the PDF file you wish to merge: ')


# instantiated classes
pdf_writer = PyPDF2.PdfFileWriter()

pdf_two = PDF()
pdf_two.merge()

pdf_one = PDF()
pdf_one.merge()

# set output file settings
output_file_name = input('Save new file as : ')
output_file = open(output_file_name, 'wb')

# write merged pdf file
pdf_writer.write(output_file)
