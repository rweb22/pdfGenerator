# templates/ah1.py

import pyperclip
import re

# === Helpers ===
def sanitize_filename(title: str) -> str:
    safe_title = re.sub(r'[^\w\s-]', '', title).strip().lower()
    return re.sub(r'[\s]+', '_', safe_title) or "document"

def init():
    lang = "english"
    # Title and Author
    title = input("Enter the title: ").strip()
    title_link = input("Enter the title's hyperlink (or leave blank): ").strip() or None

    author = input("Enter the author name: ").strip()
    author_link = input("Enter the author's hyperlink (or leave blank): ").strip() or None

    code = fr"""\lang      {{{lang}}}
\title     {{\href{{{title_link}}}{{{title}}}}}
\authors   {{\href{{{author_link}}}{{{author}}}}}

    """

    return code

def is_valid_url(url):
    # Simple regex-based check for a valid URL
    url_pattern = re.compile(
        r'^(https?|ftp)://'                      # http:// or https:// or ftp://
        r'(([A-Za-z0-9-]+\.)+[A-Za-z]{2,6})'     # domain...
        r'(:\d+)?'                               # optional port
        r'(/.*)?$'                               # optional path
    )
    return bool(url_pattern.match(url))

def chapter(title, link, body):
    if is_valid_url(link):
        header = fr"\hy{{{title}}}{{{link}}}"
    else:
        header = fr"\hx{{{title}}}"
    
    return header + "\n" + body + "\n"

def get_multiline_input(prompt="Enter text (end with a single line 'END'):\n") -> str:
    print(prompt)
    lines = []
    while True:
        line = input("> ")
        if line.strip().upper() == "END":
            break
        lines.append(line)
    return "\n".join(lines)

# === Entry Point ===
def generate_pdf():

    base = r"""\documentclass{novella}

\renewcommand{\familydefault}{\ttdefault}
\usepackage[T1]{fontenc}
\usepackage{courier}

\usepackage{xcolor}
\usepackage{hyperref}

\definecolor{indigo}{RGB}{75,0,130}

\newcommand{\hx}[1]{\chapter{\textcolor{indigo}{#1}}}

\newcommand{\hy}[2]{%
  \chapter{\href{#2}{\textcolor{indigo}{#1}}}%
}

    """

    then = init()

    body = r"""\begin{document}
\color{red}

"""

    last = r"""\end{document}
    """

    # Chapters
    while True:
        add_chapter = input("\nAdd a chapter? (y/n): ").strip().lower()
        if add_chapter != 'y':
            break

        chapter_title = input("  Chapter title: ").strip()
        chapter_link = input("  Chapter hyperlink (or leave blank): ").strip() or None
        body_text = get_multiline_input("  Chapter body text (end input with 'END'):")

        body = body + chapter(chapter_title, chapter_link, body_text)


    complete = base + then + body + last
    pyperclip.copy(complete)
