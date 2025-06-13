# templates/__init__.py

from .ah1 import generate_pdf as generate_ah1
from .ah2 import generate_pdf as generate_ah2

# Central imports used in main.py
generate_invoice = generate_ah1
generate_report = generate_ah2
generate_certificate = lambda: print("🔧 Certificate template not implemented.")

# Optional: expose directly for dictionary mapping in main.py
from . import ah1, ah2

