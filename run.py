# run.py

import os
from .templates import ah1

TEMPLATES = {
    "ah1": ah1.generate_pdf,
}

def ensure_output_dir():
    if not os.path.exists("output"):
        os.makedirs("output")

def run():
    print("\nPDF Generator")
    print("-------------")
    print("Available templates:")
    for name in TEMPLATES:
        print(f" - {name}")

    choice = input("\nEnter the template name you want to generate: ").strip().lower()
    if choice in TEMPLATES:
        ensure_output_dir()
        TEMPLATES[choice]()  # Call the selected PDF generator
    else:
        print("❌ Invalid choice. Exiting.")

