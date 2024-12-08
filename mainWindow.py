from PyQt6.QtWidgets import QFileDialog
from PyQt6.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget, QFileDialog, QLabel, QToolBar
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtCore import Qt

import utils as UTILS


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("PDF Tools")
        toolbar = QToolBar()
        toolbar.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.addToolBar(toolbar)
        
        add_file_button = QAction(QIcon(UTILS.icon_path("notebook--plus")),"Add a file", self)
        add_file_button.setStatusTip("Click to add a pdf file")
        add_file_button.triggered.connect(self.addFileButtonOnClick)
        
        merge_button = QAction(QIcon(UTILS.icon_path("document-pdf")),"Merge", self)
        merge_button.setStatusTip("Merge every files")
        merge_button.triggered.connect(self.mergeButtonOnClick)
        
        toolbar.addAction(add_file_button)
        toolbar.addAction(merge_button)
    
    def addFileButtonOnClick(self, s):
        dialog = QFileDialog.getOpenFileName(self, "Open file", "/")
        print(dialog)
    
    def mergeButtonOnClick(self, s):
        print("Click", s)


        