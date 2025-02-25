import PyPDF2

def count_words(text):
    """Counts the number of words in a given text."""
    words = text.split()  # Splitting text into words based on spaces
    return len(words)

def read_pdf(file_path):
    """Reads text from a PDF file and returns the extracted content."""
    try:
        with open(file_path, "rb") as file:
            pdf_reader = PyPDF2.PdfReader(file)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text() + " "  # Extracting text from each page
            return text.strip()
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return ""

def main():
    """Main function to process user input and optional PDF file."""
    total_word_count = 0
    
    # User Input for Paragraphs
    print("Enter multiple paragraphs (type 'STOP' on a new line to finish):")
    user_input = []
    while True:
        line = input().strip()
        if line.upper() == "STOP":  # Stop reading input when user types STOP
            break
        user_input.append(line)
    
    full_text = " ".join(user_input)
    total_word_count += count_words(full_text)

    # PDF Word Count (Optional)
    pdf_path = input("Enter the path of a PDF file to count words (or press Enter to skip): ").strip()
    if pdf_path:
        pdf_text = read_pdf(pdf_path)
        pdf_word_count = count_words(pdf_text)
        total_word_count += pdf_word_count
        print(f"Words counted from PDF: {pdf_word_count}")
    
    # Displaying Results
    print(f"Total Word Count: {total_word_count}")

if __name__ == "__main__":
    main()
