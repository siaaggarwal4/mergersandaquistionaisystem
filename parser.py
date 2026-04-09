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


def is_contact_line(line):
    line = line.strip()
    if not line:
        return False

    patterns = [
        r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}',   # email
        r'(?:\+1[-.\s]?)?(?:\(?\d{3}\)?[-.\s]?)\d{3}[-.\s]?\d{4}',  # phone
        r'\+?\d[\d\-\.\s\(\)]{7,}\d',   # broader number/fax
        r'\b\d{1,6}\s+[A-Za-z0-9.\- ]+\b(?:Street|St|Avenue|Ave|Road|Rd|Boulevard|Blvd|Lane|Ln|Drive|Dr|Court|Ct|Way|Suite|Ste)\b',  # address
        r'\b[A-Z][a-zA-Z ]+,\s*[A-Z]{2}\s*\d{5}(?:-\d{4})?\b',  # city state zip
        r'Name: [A-Z][a-z]+(?:\s+[A-Z]\.)?(?:\s+[A-Z][a-z]+){1,2}', 
        r'NAME: [A-Z][a-z]+(?:\s+[A-Z]\.)?(?:\s+[A-Z][a-z]+){1,2}', 
        r'By:\s+',
        r'CONTACT:\s*(.*)'
        r'\b(?:CEO|CFO|COO|CTO|President|Vice President|Director|Chairman|Secretary|Treasurer|Manager|Officer|Counsel)\b',  # title
    ]

    for p in patterns:
        if re.search(p, line, flags=re.I):
            return True

    return False

def clean_text(text):
    text = text.replace("\r", "\n")
    text = re.sub(r'\[\s*Remainder of page inentionally left blank.\s*\]'," ", text, flags=re.I)
    text = re.sub(r'\b\d+\s+of\s+\d+\b', ' ', text,flags=re.I)
    text = re.sub(r'_{2,}', ' ', text)
    text = re.split(r'\bIN WITNESS WHEREOF\b', text, flags= re.I)[0]
    text = re.sub(r' *\n\n *', '\n\n', text)
    text = re.sub('-+', " ", text)
    # emails = re.findall(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}', text)
    # text = re.sub(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}', " ", text)
    # text = re.sub(r'(?:\+1[-.\s]?)?(?:\(?\d{3}\)?[-.\s]?)\d{3}[-.\s]?\d{4}', " ", text)
    # text = re.sub(r'\+?\d[\d\-\.\s\(\)]{7,}\d', " ", text)
    # text = re.sub(r'.*\b\d{1,6}\s+[A-Za-z0-9.\- ]+\b(?:Street|St|Avenue|Ave|Road|Rd|Boulevard|Blvd|Lane|Ln|Drive|Dr|Court|Ct|Way|Suite|Ste)\b.*\n?','',text,flags=re.I)
    # text = re.sub(r'\b[A-Z][a-zA-Z ]+,\s*[A-Z]{2}\s*\d{5}(?:-\d{4})?\b', " ", text)
    texts = text.split("\n")
    keep = []
    for line in texts:
        if not is_contact_line(line):
            keep.append(line.strip())
    
    return "\n".join(keep).strip()
    # text = re.sub(r'\n', ' ', text)
    # text = re.sub()

    return text.strip()