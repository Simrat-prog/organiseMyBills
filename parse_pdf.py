import pdfplumber

def extract_text(pdf_path):
    try:
        with pdfplumber.open(pdf_path) as pdf:
            text = "\n".join(page.extract_text() or "" for page in pdf.pages)
        return text
    except Exception as e:
        print(f"[!] Failed to parse {pdf_path}: {e}")
        return ""
