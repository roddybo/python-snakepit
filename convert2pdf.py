import os
from docx import Document
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def convert_docx_to_pdf(input_path, output_path):
    try:
        doc = Document(input_path)
        pdf_path = os.path.splitext(output_path)[0] + ".pdf"

        # Create a PDF file
        pdf_canvas = canvas.Canvas(pdf_path, pagesize=letter)
        pdf_canvas.setFont("Helvetica", 12)

        # Iterate through paragraphs in the docx file and write to the PDF
        for paragraph in doc.paragraphs:
            pdf_canvas.drawString(100, 800, paragraph.text)
            pdf_canvas.showPage()

        pdf_canvas.save()
        print(f"Conversion from {input_path} to {pdf_path} successful.")
    except Exception as e:
        print(f"Error converting {input_path} to {output_path}: {e}")

def convert_txt_to_pdf(input_path, output_path):
    try:
        with open(input_path, 'r', encoding='utf-8') as txt_file:
            txt_content = txt_file.read()

        pdf_path = os.path.splitext(output_path)[0] + ".pdf"

        # Create a PDF file
        pdf_canvas = canvas.Canvas(pdf_path, pagesize=letter)
        pdf_canvas.setFont("Helvetica", 12)

        # Write the text content to the PDF
        pdf_canvas.drawString(100, 800, txt_content)

        pdf_canvas.save()
        print(f"Conversion from {input_path} to {pdf_path} successful.")
    except Exception as e:
        print(f"Error converting {input_path} to {output_path}: {e}")

if __name__ == "__main__":
    # Example usage
    docx_input_path = "example.docx"
    docx_output_path = "example.pdf"

    txt_input_path = "example.txt"
    txt_output_path = "example.pdf"

    # Convert .docx to PDF
    convert_docx_to_pdf(docx_input_path, docx_output_path)

    # Convert .txt to PDF
    convert_txt_to_pdf(txt_input_path, txt_output_path)

