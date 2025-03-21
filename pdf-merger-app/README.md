# PDF Merger App

## Overview
PDF Merger App is a simple GUI application that allows users to merge multiple PDF files into a single PDF document. Additionally, it provides functionality to convert the merged PDF into JSON format for easy data extraction and manipulation.

## Features
- Merge multiple PDF files into one.
- Convert the merged PDF into JSON format.
- User-friendly graphical interface.

## Requirements
To run this application, you need to have Python installed along with the following dependencies:

- PyPDF2
- pdf2json

You can install the required packages using pip:

```
pip install -r requirements.txt
```

## Project Structure
```
pdf-merger-app
├── src
│   ├── main.py                # Entry point of the application
│   ├── gui
│   │   ├── __init__.py        # GUI package initializer
│   │   └── app_window.py       # Main application window and functionality
│   ├── pdf_utils
│   │   ├── __init__.py        # PDF utilities package initializer
│   │   ├── merge_pdfs.py      # Function to merge PDF files
│   │   └── pdf_to_json.py     # Function to convert PDF to JSON
│   └── assets
│       └── styles.css         # Styles for the GUI application
├── requirements.txt           # List of dependencies
├── .gitignore                 # Files and directories to ignore
└── README.md                  # Project documentation
```

## Usage
1. Run the application by executing the `main.py` file.
2. Use the GUI to select the PDF files you want to merge.
3. Click the merge button to create a single PDF file.
4. Optionally, convert the merged PDF to JSON format using the provided functionality.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.