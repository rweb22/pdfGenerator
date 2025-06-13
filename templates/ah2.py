# templates/ah1.py

from fpdf import FPDF
import os
import re

INDIGO = (75, 0, 130)
BRIGHT_RED = (255, 69, 58)

def sanitize_filename(title: str) -> str:
    # Remove invalid characters from title to form a valid filename
    safe_title = re.sub(r'[^\w\s-]', '', title).strip().lower()
    safe_title = re.sub(r'[\s]+', '_', safe_title)
    return safe_title or "document"

class AH1PDF(FPDF):
    def __init__(self):
        super().__init__()
        self.add_page()
        self.set_auto_page_break(auto=True, margin=15)
        self.set_margins(20, 20, 20)
        self.set_font("Courier", size=12)

    def add_heading(self, text, url=None):
        self.set_text_color(*INDIGO)
        self.set_font("Courier", style="B", size=14)
        if url:
            self.write(10, text, link=url)
        else:
            self.cell(0, 10, text, ln=1)
        self.ln(5)

    def add_body_text(self, text):
        self.set_text_color(*BRIGHT_RED)
        self.set_font("Courier", size=12)
        self.multi_cell(0, 10, text)
        self.ln(5)

def generate_pdf():
    pdf = AH1PDF()

    # --- Step 1: Title & Link ---
    title = input("Enter the title: ").strip()
    title_link = input("Enter the title's hyperlink (or leave blank): ").strip() or None
    pdf.add_heading(title, url=title_link)

    # --- Step 2: Author & Link ---
    author = input("Enter the author name: ").strip()
    author_link = input("Enter the author's hyperlink (or leave blank): ").strip() or None
    pdf.add_heading(f"By: {author}", url=author_link)

    # --- Step 3: Chapters ---
    while True:
        add_chapter = input("\nAdd a chapter? (y/n): ").strip().lower()
        if add_chapter != 'y':
            break

        chapter_title = input("  Chapter title: ").strip()
        chapter_link = input("  Chapter hyperlink (or leave blank): ").strip() or None
        body_text = input("  Chapter body text (type or paste):\n")

        pdf.add_heading(chapter_title, url=chapter_link)
        pdf.add_body_text(body_text)

    # --- Output PDF ---
    safe_filename = sanitize_filename(title) + ".pdf"
    output_path = os.path.join("output", safe_filename)
    os.makedirs("output", exist_ok=True)
    pdf.output(output_path)
    print(f"\n✅ PDF generated successfully: {output_path}")

