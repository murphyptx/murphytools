import pdfplumber # the power tool to rip through and analyze the PDFs
import glob # filename pattern matching
import os # for interacting with the file system
import shutil # sile system operations; copying, etc.

pdf_source_path = ""
pdf_no_text_path = ""
pdf_text_path = ""

print('You are about to analyze PDFs for text content, under the following top level path:')
print(pdf_source_path)
print('\n')
print('PDF files containing text will be copied here:')
print(pdf_text_path)
print('\n')
print('PDF files without text will be copied here:')
print(pdf_no_text_path)
print('\n')
print('******* ATTENTION *******')
print('Check the above paths. \n If they are not correct, press '"Q"' \n If they are correct, press '"C"')
input('')


with pdfplumber.open("2021_bills_wrong_insurance.pdf") as pdf:
        page = pdf.pages[0]
        text = page.extract_text()
        print(text)
