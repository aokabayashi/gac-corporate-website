import sys
try:
    import fitz  # PyMuPDF
except ImportError as e:
    print(f"Error importing fitz: {e}")
    sys.exit(1)

def extract_text(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python extract_pdf.py <pdf_path>")
        sys.exit(1)
        
    pdf_path = sys.argv[1]
    extracted_text = extract_text(pdf_path)
    
    with open("extracted_text.txt", "w", encoding="utf-8") as f:
        f.write(extracted_text)
        
    print(f"Successfully extracted {len(extracted_text)} characters.")
