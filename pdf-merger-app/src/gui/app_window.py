from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QMessageBox
from pdf_utils.merge_pdfs import merge_pdfs
from pdf_utils.pdf_to_json import pdf_to_json

class AppWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PDF Merger App")
        self.setGeometry(100, 100, 600, 400)

        self.merge_button = QPushButton("Merge PDFs", self)
        self.merge_button.setGeometry(50, 50, 200, 50)
        self.merge_button.clicked.connect(self.merge_pdfs)

        self.convert_button = QPushButton("Convert Merged PDF to JSON", self)
        self.convert_button.setGeometry(50, 150, 300, 50)
        self.convert_button.clicked.connect(self.convert_to_json)

    def merge_pdfs(self):
        file_paths, _ = QFileDialog.getOpenFileNames(self, "Select PDF files", "", "PDF Files (*.pdf)")
        if file_paths:
            output_path, _ = QFileDialog.getSaveFileName(self, "Save Merged PDF", "", "PDF Files (*.pdf)")
            if output_path:
                try:
                    merge_pdfs(file_paths, output_path)
                    QMessageBox.information(self, "Success", "PDFs merged successfully!")
                except Exception as e:
                    QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")

    def convert_to_json(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Merged PDF", "", "PDF Files (*.pdf)")
        if file_path:
            try:
                json_data = pdf_to_json(file_path)
                json_file_path, _ = QFileDialog.getSaveFileName(self, "Save JSON File", "", "JSON Files (*.json)")
                if json_file_path:
                    with open(json_file_path, 'w') as json_file:
                        json_file.write(json_data)
                    QMessageBox.information(self, "Success", "PDF converted to JSON successfully!")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")