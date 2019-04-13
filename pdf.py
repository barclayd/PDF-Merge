import PyPDF2

# open pdf files
file_one = open('./pdfs/two-pages.pdf', 'rb')
file_two = open('./pdfs/three-pages.pdf', 'rb')
# read pdf files
pdf_reader_one = PyPDF2.PdfFileReader(file_one)
pdf_reader_two = PyPDF2.PdfFileReader(file_two)
# get number of pages for each pdf
file_one_pages = pdf_reader_one.getNumPages()
file_two_pages = pdf_reader_two.getNumPages()

output_file = open('merged_doc.pdf', 'wb')
pdf_writer = PyPDF2.PdfFileWriter()

# for every page, add a new file to output file
for page in range(file_one_pages):
    pdf_writer.addPage(pdf_reader_one.getPage(page))

for page in range(file_two_pages):
    pdf_writer.addPage(pdf_reader_two.getPage(page))

pdf_writer.write(output_file)
# close opened files and output file
file_one.close()
file_two.close()
output_file.close()
