import sys #import sys
import simpleeval #replace python eval function with external library
#import required modules from pyqt6
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

#app UI and functionality class
class MainWindow(QWidget):
    #startup function
    def __init__(self):
        super().__init__()#super init func
        self.setWindowTitle("PySimpleCalculator")#set title
        self.setLayout(QVBoxLayout())#set default layout
        
        self.SetupVars() #setup variables in another function
        self.SetupUI() #setup UI in another function
        self.SetupStyle() #setup styling in another function
        self.SetupFunc() #setup functionality in another function
        
        self.show()#show the program
        
    #setup UI from top to bottom container
    def SetupUI(self):
        
        #results of calculations go here
        self.result_text = QLineEdit()
        
        #add empty widget with a grid layout for everything else to go into
        self.container = QWidget()
        self.container.setLayout(QGridLayout())      
        
        #Create other buttons
        self.btn_0 = QPushButton("0")
        self.btn_1 = QPushButton("1")
        self.btn_2 = QPushButton("2")
        self.btn_3 = QPushButton("3")
        self.btn_4 = QPushButton("4")
        self.btn_5 = QPushButton("5")
        self.btn_6 = QPushButton("6")
        self.btn_7 = QPushButton("7")
        self.btn_8 = QPushButton("8")
        self.btn_9 = QPushButton("9")
        self.btn_clear = QPushButton("Clear")
        self.btn_equals = QPushButton("=")
        self.btn_plus = QPushButton("+")
        self.btn_minus = QPushButton("-")
        self.btn_divide = QPushButton("÷")
        self.btn_multiply = QPushButton("x")
        self.btn_dot = QPushButton(".")
        self.btn_pi = QPushButton("x²")
        self.btn_ans = QPushButton("Ans")
        
        #add buttons to container in order-ish
        self.container.layout().addWidget(self.btn_1,1,0)
        self.container.layout().addWidget(self.btn_2,1,1)
        self.container.layout().addWidget(self.btn_3,1,2)
        self.container.layout().addWidget(self.btn_4,2,0)
        self.container.layout().addWidget(self.btn_5,2,1)
        self.container.layout().addWidget(self.btn_6,2,2)
        self.container.layout().addWidget(self.btn_7,3,0)
        self.container.layout().addWidget(self.btn_8,3,1)
        self.container.layout().addWidget(self.btn_9,3,2)
        self.container.layout().addWidget(self.btn_0,4,0)
        self.container.layout().addWidget(self.btn_multiply,4,3)
        self.container.layout().addWidget(self.btn_divide,3,3)
        self.container.layout().addWidget(self.btn_minus,2,3)
        self.container.layout().addWidget(self.btn_plus,1,3)
        self.container.layout().addWidget(self.btn_equals,0,3)
        self.container.layout().addWidget(self.btn_clear,0,0)
        self.container.layout().addWidget(self.btn_dot,4,1)
        self.container.layout().addWidget(self.btn_pi,4,2)
        self.container.layout().addWidget(self.btn_ans,0,1,1,2)
        #add whole containers and boxes
        self.layout().addWidget(self.result_text)
        self.layout().addWidget(self.container)
    
    #setup custom styling
    def SetupStyle(self):
        self.setStyle(QStyleFactory.create("Fusion"))#set style of whole app
        
        self.container.setStyleSheet("""padding-bottom:14px;padding-top:14px;padding-left:20px;padding-right:20px""") #set bottom grid container style
        
        #add styling to the top text box
        self.result_text.setStyleSheet("""padding-left:0px;padding-right:0px""") 
        self.result_text.setFont(QFont("RaleWay",16,80))

    def SetupVars(self):
        self.list_all = [] #list of all things in program
        self.full_string = "" #full list compact string
        self.answer = None #answer/result of last calculation

    def SetupFunc(self):
        #basic number buttons
        self.btn_0.clicked.connect(lambda:self.add_str("0"))
        self.btn_1.clicked.connect(lambda:self.add_str("1"))
        self.btn_2.clicked.connect(lambda:self.add_str("2"))
        self.btn_3.clicked.connect(lambda:self.add_str("3"))
        self.btn_4.clicked.connect(lambda:self.add_str("4"))
        self.btn_5.clicked.connect(lambda:self.add_str("5"))
        self.btn_6.clicked.connect(lambda:self.add_str("6"))
        self.btn_7.clicked.connect(lambda:self.add_str("7"))
        self.btn_8.clicked.connect(lambda:self.add_str("8"))
        self.btn_9.clicked.connect(lambda:self.add_str("9"))
        self.btn_dot.clicked.connect(lambda:self.add_str("."))
        self.btn_pi.clicked.connect(lambda:self.add_str("**"))
        #operators
        self.btn_equals.clicked.connect(lambda:self.FindAnswer())
        self.btn_plus.clicked.connect(lambda:self.add_str("+"))
        self.btn_minus.clicked.connect(lambda:self.add_str("-"))
        self.btn_divide.clicked.connect(lambda:self.add_str("/"))
        self.btn_multiply.clicked.connect(lambda:self.add_str("*"))
        #other buttons
        self.btn_ans.clicked.connect(lambda:self.add_str(self.answer))
        self.btn_clear.clicked.connect(lambda:self.Clear())

    #update the text in the top box
    def UpdateBox(self):
        self.Make_String()
        self.result_text.setText(self.full_string)

    #make a string out of the list
    def Make_String(self):
        self.full_string = "".join(self.list_all)

    #find the answer of the expression
    def FindAnswer(self):
        self.UpdateBox()
        answer = simpleeval.simple_eval(self.full_string) #use external libary eval
        self.answer = str(answer)
        
        self.list_all.clear()
        self.UpdateBox()
        self.result_text.setText(self.answer) #set the text as the answer

    #clear all data/variables from the app
    def Clear(self):
        self.UpdateBox() 
        self.answer = None #set answer to none
        self.list_all.clear() #clear list
        self.UpdateBox()

    #add a letter as string to the list
    def add_str(self,string:str):
        self.UpdateBox()
        self.list_all.append(str(string)) #append a string to the list
        self.UpdateBox()
    
        
#execute the application    
app = QApplication(sys.argv)#make app class with arguements
Window = MainWindow()#instantiate window class
app.exec()#execute app with UI window class inside of it
