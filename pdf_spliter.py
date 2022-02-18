from PyPDF2 import PdfFileWriter, PdfFileReader
from tqdm import tqdm


def split_pdf(input_pdf, output_folder):
    inputpdf = PdfFileReader(open(input_pdf, "rb"))
    for i in tqdm(range(inputpdf.numPages)):
        output = PdfFileWriter()
        output.addPage(inputpdf.getPage(i))
        with open("./.tmp/document-page%s.pdf" % i, "wb") as outputStream:
            output.write(outputStream)
