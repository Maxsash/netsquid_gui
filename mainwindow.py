from createNet import newNetwork
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

from netsquid.nodes import Network
from netsquid.components import QuantumProcessor, QuantumChannel, Channel

import logging
logging.basicConfig(level=logging.DEBUG)

class TextEdit(QWidget):
        def __init__(self,parent=None):
                super().__init__(parent)

                #self.setWindowTitle("QTextEdit")
                #self.resize(300,270)

                self.textEdit = QTextEdit()
                self.btnPress1 = QPushButton("Button 1")
                self.btnPress2 = QPushButton("Button 2")

                #layout = QVBoxLayout()
                #layout.addWidget(self.textEdit)
                #layout.addWidget(self.btnPress1)
                #layout.addWidget(self.btnPress2)
                #self.setLayout(layout)

                self.btnPress1.clicked.connect(self.btnPress1_Clicked)
                self.btnPress2.clicked.connect(self.btnPress2_Clicked)

        def btnPress1_Clicked(self):
                self.textEdit.setPlainText("Hello PyQt5!\nfrom pythonpyqt.com")

        def btnPress2_Clicked(self):
                self.textEdit.setHtml("<font color='red' size='6'><red>Hello PyQt5!\nHello</font>")

# Subclass QMainWindow to customise your application's main window
class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("My Awesome App")

        self.window = QWidget()
        self.setCentralWidget(self.window)

        self.layout = QVBoxLayout()
        self.window.setLayout(self.layout)

        label = QLabel("This is a PyQt5 window!")

        #self.layout.addWidget(label)

        # The `Qt` namespace has a lot of attributes to customise
        # widgets. See: http://doc.qt.io/qt-5/qt.html
        label.setAlignment(Qt.AlignCenter)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.

        #Add a toolbar 
        toolbar = QToolBar("My main toolbar")
        self.addToolBar(toolbar)

        #Add a button in the toolbar
        button_action = QAction("Create a new Network", self)
        button_action.setStatusTip("This is your button")
        button_action.triggered.connect(self.createNetwork)
        toolbar.addAction(button_action)

        #self.QtWidgets.addWidget(TextEdit.textEdit)

    def createNetwork(self):
        text, okPressed = QInputDialog.getText(self, "Create new Network","Network name:", QLineEdit.Normal, "")
        if okPressed and text != '':
            newNetwork(text)
            print(text + ": Network created succesfully")

            #display the network in the GUI
            self.newLayoutEntry(text)


    def newLayoutEntry(self, name):
        #Create another widget to contain network information
        newWidget = QWidget()
        self.layout.addWidget(newWidget)
        logging.debug('newWidget created and added to the layout of main window')

        #Create another layout to assign to the widget
        newLayout = QHBoxLayout()
        newWidget.setLayout(newLayout)
        logging.debug('newLayout created and set for newWidget')

        #Create another sub-widget for network name and button to create new nodes
        #subWidgetPrimary = QWidget()
        #logging.debug('subWidgetPrimary created')

        #Create layout for the sub-widget
        #subLayoutPrimary = QVBoxLayout()
        #subWidgetPrimary.setLayout(subLayoutPrimary)
        #logging.debug('subLayoutPrimary created and set for subWidgetPrimary')

        #Create final things that will be added to the name and button sub-layout
        newEntryLabel = QLabel(name)
        newLayout.addWidget(newEntryLabel)
        logging.debug('newEntryLabel created and added to subLayoutPrimary')

        add_nodes_button = QPushButton("Add node", self)
        logging.debug('create new QPushButton widget')
        add_nodes_button.setText("This is your button")
        logging.debug('set text for new button')
        #add_nodes_button.triggered.connect(self.createNetwork)
        newLayout.addWidget(add_nodes_button)
        logging.debug('add_nodes_button is added to the subLayoutPrimary')



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
