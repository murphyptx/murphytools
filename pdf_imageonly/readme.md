Overview

Goal: identify image-only PDFs

See: https://stackoverflow.com/questions/55704218/how-to-check-if-pdf-is-scanned-image-or-contains-text

See also (for PDFMiner tool):
https://stackoverflow.com/questions/55704218/how-to-check-if-pdf-is-scanned-image-or-contains-text 


Install Python 3 and PIP

Python 3

Mac

Windows

Linux

Install PIP
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py

Add /Users/pamurphy/Library/Python/3.8/bin to the path

sudo vi / etc/paths

edit file

:wq

Install Packages

Install PDFPlumber

https://github.com/jsvine/pdfplumber 

pip3 install pdfplumber

https://stackoverflow.com/questions/55939921/use-pdfplumber-to-find-text-in-pdf-return-page-number-then-return-table 

Hacky sample code:
import pdfplumber
with pdfplumber.open("2021_bills_wrong_insurance.pdf") as pdf:
        page = pdf.pages[0]
        text = page.extract_text()
        print(text)

Install Keyboard
https://pypi.org/project/keyboard/

pip3 install keyboard







