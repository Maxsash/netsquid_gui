from createNet import newNetwork
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

from netsquid.nodes import Network
from netsquid.components import QuantumProcessor, QuantumChannel, Channel

import logging
logging.basicConfig(level=logging.DEBUG)

class NetworkInfo(QWidget):
        def __init__(self,parent=None):
                super().__init__(parent)
                self.number_of_nodes = 0

                #self.setWindowTitle("QTextEdit")
                #self.resize(300,270)

                self.addNode = QPushButton("Add node")
                self.genNet = QPushButton("Generate network file")

                layout = QVBoxLayout()
                layout.addWidget(self.addNode)
                layout.addWidget(self.genNet)
                self.setLayout(layout)

                self.addNode.clicked.connect(self.addNode_clicked)
                self.genNet.clicked.connect(self.genNet_clicked)

                label = QLabel("No nodes have been added to this network" + str(self.number_of_nodes))
                layout.addWidget(label)


        def addNode_clicked(self):
            self.number_of_nodes += 1

        def genNet_clicked(self):
            pass

# Subclass QMainWindow to customise your application's main window
class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("Quantum Network Generator")

        self.window = QWidget()
        self.setCentralWidget(self.window)

        self.layout = QVBoxLayout()
        self.window.setLayout(self.layout)

        # The `Qt` namespace has a lot of attributes to customise
        # widgets. See: http://doc.qt.io/qt-5/qt.html

        #Add a toolbar 
        toolbar = QToolBar("My main toolbar")
        self.addToolBar(toolbar)

        #Add a button in the toolbar
        button_action = QAction("Create a new Network", self)
        button_action.setStatusTip("This is your button")
        button_action.triggered.connect(self.newNetworkEntry)
        toolbar.addAction(button_action)

    def createNetwork(self, name, nodes):
            newNetwork(name)
            print(name + ": Network created succesfully")

    def newNetworkEntry(self):
        name, okPressed = QInputDialog.getText(self, "Create new Network","Network name:", QLineEdit.Normal, "")
        if okPressed and name != '':
            print(name + ": Network Entry created succesfully")

        #Create another widget to contain network information
        newWidget = QWidget()
        self.layout.addWidget(newWidget)
        logging.debug('newWidget created and added to the layout of main window')

        #Create another layout to assign to the widget
        newLayout = QHBoxLayout()
        newWidget.setLayout(newLayout)
        logging.debug('newLayout created and set for newWidget')

        #Create final things that will be added to the name and button sub-layout
        newEntryLabel = QLabel(name)
        newLayout.addWidget(newEntryLabel)
        logging.debug('newEntryLabel created and added to subLayoutPrimary')

        add_nodes_button = NetworkInfo()
        logging.debug('create new QPushButton widget')
        #add_nodes_button.setText("This is your button")
        logging.debug('set text for new button')
        #add_nodes_button.clicked.connect(self.createNetwork)
        newLayout.addWidget(add_nodes_button)
        logging.debug('add_nodes_button is added to the subLayoutSecondary')



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
