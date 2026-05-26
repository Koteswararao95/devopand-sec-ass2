import PyPDF2

pdf_path = r'd:\devop1\ass2\Assignment-SecAndDevOpsAI-2026-DevOps.pdf'
pdf = PyPDF2.PdfReader(pdf_path)

print(f"Total pages: {len(pdf.pages)}\n")

for page_num in range(len(pdf.pages)):
    page = pdf.pages[page_num]
    text = page.extract_text()
    print(f"\n{'='*80}")
    print(f"PAGE {page_num + 1}")
    print(f"{'='*80}\n")
    print(text)
