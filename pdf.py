import PyPDF2

output_file = open('merged.pdf', 'wb')
pdf_writer = PyPDF2.PdfFileWriter()


class PDF:
    def __init__(self, name):
        self.name = name
        self.path = './pdfs/' + name
        self.pages = 0
        self.pdf_reader = None

    def open(self):
        return open(self.path, 'rb')

    def read(self):
        self.pdf_reader = PyPDF2.PdfFileReader(self.open())

    def add_pages(self):
        self.pages = self.pdf_reader.getNumPages()

        for page in range(self.pages):
            pdf_writer.addPage(self.pdf_reader.getPage(page))

    def close(self):
        self.open().close()

    def merge(self):
        self.open()
        self.read()
        self.add_pages()
        self.close()


# instantiated classes
pdf_two = PDF('three-pages.pdf')
pdf_two.merge()

pdf_one = PDF('two-pages.pdf')
pdf_one.merge()

pdf_writer.write(output_file)
