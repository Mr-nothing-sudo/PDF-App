def pdf_to_json(pdf_path):
    import PyPDF2
    import json

    pdf_data = {}
    
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        pdf_data['num_pages'] = len(reader.pages)
        pdf_data['content'] = []

        for page in reader.pages:
            pdf_data['content'].append(page.extract_text())

    return json.dumps(pdf_data)