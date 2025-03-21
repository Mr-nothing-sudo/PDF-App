def merge_pdfs(pdf_list, output_path):
    from PyPDF2 import PdfMerger

    merger = PdfMerger()

    for pdf in pdf_list:
        merger.append(pdf)

    merger.write(output_path)
    merger.close()