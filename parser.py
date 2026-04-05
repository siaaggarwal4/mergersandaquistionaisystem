import pytesseract
import pymupdf as pdflib
from PIL import Image
import re

def get_text(pdf):
    doc = pdflib.open(pdf)
    text = ""
    for pagen, page in enumerate(doc, start=0):
        textl = doc[pagen].get_text("text").strip()
        if textl and len(textl) > 2:
            text += textl + "\n"
            # return get_text_t(doc) # text doc
        else:
            zoom=2
            matriz = pdflib.Matrix(zoom, zoom)
            pix = page.get_pixmap(matrix=matriz)
            img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
            text += pytesseract.image_to_string(img).strip() + "\n"
    

            # return get_text_s(doc) # scan doc
    return text

def clean_text(text):
    text = text.replace("\r", "\n")
    text = re.sub(r'\[\s*Remainder of page inentionally left blank\.\s*\]', text, flags=re.I)
    text = re.sub(r'\b\d+\s+of\s+\d+\b', ' ', text,flags=re.I)
    text = re.sub(r'_{2,}', ' ', text)

    # text = re.sub(r'\n', ' ', text)
    # text = re.sub()

    return text.lower()