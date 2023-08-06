import fitz

def pdf_to_string(filename: str) -> str:

    raw_text: str = ""

    with fitz.open(filename) as file:
        for page in file:
            raw_text = raw_text + page.get_text()

    return raw_text

def text_to_string(filename: str) -> str:

    raw_text: str = ""

    with open(filename, 'r') as file:
        for line in file.readlines():
            raw_text = raw_text + line

    return raw_text