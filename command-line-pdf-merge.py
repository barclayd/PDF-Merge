import PyPDF2
from pdf_merger import pdf_writer
# welcome message
print("Welcome to PDF Merge, a handy python script to help you merge PDFs for free")
while True:
    try:
        document_count = int(input("How many PDF documents would you like to merge? (1-1000+) "))
    except ValueError:
        print("Sorry, I don't understand that number...")
        continue
    break


class PDF:
    def __init__(self):
        self.path = None
        self.pages = None
        self.pdf_reader = None
        self.page_range = None
        self.filename = None

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
        first_page = int(input("Number of first page of PDF to be merged from {}: ".format(self.filename)))
        last_page = int(input("Number of last page of PDF to be merged from {}: ".format(self.filename)))
        self.page_range = (first_page, last_page)

    def get_file_name(self):
        self.path = input('Please enter the name of the PDF file you wish to merge: ')
        self.filename = self.path.split('/')[-1]


# PDF list
for i in range(document_count):
    new_document = PDF()
    new_document.merge()

# set output file settings
extensionsToCheck = '.pdf'
while True:
    try:
        output_file_name = input('Save new file as : ')
        if not output_file_name.endswith(extensionsToCheck):
            raise ValueError()
    except ValueError as error:
        print("File must end with .pdf")
        continue
    break


output_file = open(output_file_name, 'wb')

# write merged pdf file
pdf_writer.write(output_file)
