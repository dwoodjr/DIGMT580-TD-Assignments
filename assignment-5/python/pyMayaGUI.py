'''
This script creates a  PyQt GUI in Maya to create cubes. 
'''

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from shiboken2 import wrapInstance

from maya import OpenMayaUI as omui
import maya.cmds as cmds


# Get a reference to the main Maya application window
def maya_main_window():
    mayaMainWindowPtr = omui.MQtUtil.mainWindow()
    return wrapInstance(int(mayaMainWindowPtr), QWidget)


class MyCubeMakerWidget(QWidget):
    
    # Main function
    def __init__(self, parent=maya_main_window()):
        super(MyCubeMakerWidget, self).__init__(parent)            
        
        # Set the UI display title and size    
        self.setWindowTitle('Make-a-Cubes')
        self.setObjectName('Make Cubes')
        self.setWindowFlags(Qt.Tool)
        self.setAttribute(Qt.WA_DeleteOnClose)        
        
        self.create_layout()
        self.create_connections()
        
    
         
    # Layout function
    def create_layout(self):
        global cubeHeightField
        
        self.dim_label = QLabel(self)
        self.dim_label.setText('Cube Dimensions')
        
        #number of cubes
        self.num_of_cubes = QLabel(self)
        self.num_of_cubes.setText('Number of Cubes:')
        self.numCubes = QSpinBox(self)
        self.numCubes.valueChanged.connect(self.show_values)
        
        #cube heigh
        self.dim_label_h = QLabel(self)
        self.dim_label_h.setText('Height:')
        self.heightInput = QDoubleSpinBox(self)
        self.heightInput.valueChanged.connect(self.show_values)
        #cube width
        self.dim_label_w = QLabel(self)
        self.dim_label_w.setText('Width:')
        self.widthInput = QDoubleSpinBox(self)
        self.widthInput.valueChanged.connect(self.show_values)
        #cube depth
        self.dim_label_d = QLabel(self)
        self.dim_label_d.setText('Depth:')
        self.depthInput = QDoubleSpinBox(self)
        self.depthInput.valueChanged.connect(self.show_values)
        
        self.cube_make_btn = QPushButton('Make Cube(s)')
        
        # Layout the Widget UI
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(5,5,5,5)
        main_layout.setSpacing(5)
        main_layout.addWidget(self.num_of_cubes)
        main_layout.addWidget(self.numCubes)
        main_layout.addWidget(self.dim_label)
        main_layout.addWidget(self.dim_label_h)
        main_layout.addWidget(self.heightInput)
        main_layout.addWidget(self.dim_label_w)
        main_layout.addWidget(self.widthInput)
        main_layout.addWidget(self.dim_label_d)
        main_layout.addWidget(self.depthInput)
        main_layout.addWidget(self.cube_make_btn)
        main_layout.addStretch()
        
        self.setLayout(main_layout)
            
    #connections function
    def create_connections(self):
        self.cube_make_btn.clicked.connect(MyCubeMakerWidget.make_cubes)
    
    def show_values(self):
        global height
        global width
        global depth
        global cubeNum
        
        height = self.heightInput.value()
        width = self.widthInput.value()
        depth = self.depthInput.value()
        cubeNum = self.numCubes.value()
    
    # Function to create cube
    @classmethod
    def make_cubes(cls):
        for i in range(cubeNum):
            cmds.polyCube(h = height, w = width, d = depth)
            cmds.move(((i * depth) * 2), 0, 0)

# Display the Widget        
if __name__ == '__main__':
    try:
        ui.close()
    except:
        pass
    
    ui = MyCubeMakerWidget()
    ui.show()
    
