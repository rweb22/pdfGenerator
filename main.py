# main.py

import os
from templates import ah1, ah2

TEMPLATES = {
    "ah1": ah1.generate_pdf,
    "ah2": ah2.generate_pdf,
}

def ensure_output_dir():
    if not os.path.exists("output"):
        os.makedirs("output")

def main():
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

if __name__ == "__main__":
    main()

