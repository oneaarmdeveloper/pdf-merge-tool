from pypdf import PdfReader, PdfWriter
import sys

def merge_pdfs(front_pdf, existing_pdf, output_pdf):
    writer = PdfWriter()

    ##Adding front page
    reader_front = PdfReader(front_pdf)
    for page in reader_front.pages:
        writer.add_page(page)

    #Append existing document
    reader_existing = PdfReader(existing_pdf)
    for page in reader_existing.pages:
        writer.add_page(page)

    #Save merged
    with open(output_pdf, "wb") as f_out:
        writer.write(f_out)
    print(f"Merged saved to : {output_pdf}")

if __name__=="__main__":
    # Usage: python merge_pdf.py front.pdf existing.pdf merged.pdf

    if len(sys.argv) != 4:
        print("Usage: python merge_pdf.py front.pdf existing.pdf output.pdf")
    else:
        merge_pdfs(sys.argv[1], sys.argv[2], sys.argv[3])
