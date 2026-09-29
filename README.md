# Word Counter

Count the words in your own paragraphs and in a PDF, and get one combined total.

**Live demo:** https://word-counter-web-chi.vercel.app

## Features
- Enter multiple paragraphs of text and count their words
- Optionally add a PDF file; its text is extracted page by page and counted
- Shows words from text, words from the PDF, and the total word count
- Handles unreadable PDFs with an error message instead of crashing
- Words are counted by splitting on whitespace (Python `str.split()`)

## Tech stack
- **Python CLI:** Python 3, PyPDF2 (`word_counter.py`)
- **Web version:** HTML, CSS and JavaScript, pdf.js for PDF text extraction (`web/`). Everything runs in the browser and files are never uploaded.

## Run locally
```bash
pip install PyPDF2
python word_counter.py
```
Type your paragraphs, then `STOP` on its own line, then a PDF path (or press Enter to skip).

Example:
```
Enter multiple paragraphs (type 'STOP' on a new line to finish):
Python is widely used in AI and web development.
It is known for its simplicity and efficiency.
STOP
Enter the path of a PDF file to count words (or press Enter to skip): sample.pdf
Words counted from PDF: 1250
Total Word Count: 1274
```

Web version: open `web/index.html`, or serve the folder with any static server (`npx serve web`).

---

Portfolio: [khuwaish-portfolio.vercel.app](https://khuwaish-portfolio.vercel.app) · Built by **Khuwaish Goyal**
