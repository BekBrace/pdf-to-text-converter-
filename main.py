'How to extract a text from a PDF file.'
import PyPDF2
# Create a PDF File Object
pdfFileObject = open('law_of_success.pdf', 'rb')
# Create a PDF reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObject)
# Print the number of pages
print('The number of pages in this book is:', pdfReader.numPages, 'pages.')

# Create a page object
pageObject = pdfReader.getPage(123)
# Extract the page
print(pageObject.extractText())
# Close the PDF file object
pdfFileObject.close()
