import sys
import copy
import os
from PyPDF2 import PdfWriter, PdfReader
from PyQt6.QtWidgets import QApplication, QWidget

def crop_and_duplicate(input_path, output_path):
	with open(input_path, "rb") as pdf1:
		pdf = PdfReader(pdf1)
		output = PdfWriter()
		numpages = len(pdf.pages)
		
		for i in range(numpages):
			page = pdf.pages[i]
			page_copy = copy.copy(page)
			page_copy.mediabox.upper_right = (page_copy.mediabox.right / 2, page_copy.mediabox.top,)
			output.add_page(page_copy)
			page.mediabox.upper_left = (page.mediabox.right / 2, page.mediabox.top,)
			output.add_page(page)
	
	with open(output_path, "wb") as newpdf:
		output.write(newpdf)

def command_line_call(): 
	while True:
		input_pdf = input("Enter pdf location:\n")
		if os.path.isfile(input_pdf):
			break
		print("File does not exist, try again", file=sys.stderr)
		
	output_pdf = input_pdf[:-4] + "_splitted.pdf"
	crop_and_duplicate(input_pdf, output_pdf)

if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = QWidget()
	window.show()
	sys.exit(app.exec())
	
