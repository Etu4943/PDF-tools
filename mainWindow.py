from PyQt6.QtWidgets import QFileDialog
from PyQt6.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget, QFileDialog

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("PDF Tools")
        layout = QVBoxLayout()
        button = QPushButton("Press Me!")
        file = QFileDialog(self)
        layout.addWidget(button)
        layout.addWidget(file)
        
        widget = QWidget()
        widget.setLayout(layout)
        
        self.setCentralWidget(widget)