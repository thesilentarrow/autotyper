from PyQt5 import QtCore, QtGui, QtWidgets
import pyautogui
import re
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QPixmap
import io
import keyboard



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 690)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.central_widget_sub = QtWidgets.QWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(7)
        self.central_widget_sub.setFont(font)
        self.central_widget_sub.setObjectName("central_widget_sub")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.central_widget_sub)
        self.verticalLayout_2.setContentsMargins(0, 2, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget = QtWidgets.QWidget(self.central_widget_sub)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QtCore.QSize(230, 160))
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setContentsMargins(9, 9, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.code_input = QtWidgets.QPlainTextEdit(self.widget)
        self.code_input.setMinimumSize(QtCore.QSize(450, 321))
        self.code_input.setMaximumSize(QtCore.QSize(750, 621))
        font = QtGui.QFont()
        font.setFamily("Doppio One")
        font.setPointSize(7)
        self.code_input.setFont(font)
        self.code_input.setWhatsThis("")
        self.code_input.setObjectName("code_input")
        self.verticalLayout_3.addWidget(self.code_input, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_2.addWidget(self.widget, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.radio = QtWidgets.QWidget(self.central_widget_sub)
        font = QtGui.QFont()
        font.setFamily("Doppio One")
        font.setPointSize(8)
        self.radio.setFont(font)
        self.radio.setObjectName("radio")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.radio)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.python = QtWidgets.QRadioButton(self.radio)
        font = QtGui.QFont()
        font.setFamily("Doppio One")
        font.setPointSize(8)
        self.python.setFont(font)
        self.python.setObjectName("python")
       
        self.horizontalLayout_7.addWidget(self.python)
        self.non_python = QtWidgets.QRadioButton(self.radio)
        font = QtGui.QFont()
        font.setFamily("Doppio One")
        font.setPointSize(8)
        self.non_python.setFont(font)
        self.non_python.setStyleSheet("padding-left:19;\n"
"padding-right:19;")
        self.non_python.setObjectName("non_python")
        self.horizontalLayout_7.addWidget(self.non_python)
        self.normal_text = QtWidgets.QRadioButton(self.radio)
        font = QtGui.QFont()
        font.setFamily("Doppio One")
        font.setPointSize(8)
        self.normal_text.setFont(font)
        self.normal_text.setObjectName("text")
        self.horizontalLayout_7.addWidget(self.normal_text)
        self.verticalLayout_2.addWidget(self.radio, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.widget_2 = QtWidgets.QWidget(self.central_widget_sub)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setMinimumSize(QtCore.QSize(0, 0))
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setContentsMargins(-1, 0, 0, 32)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_3 = QtWidgets.QFrame(self.widget_2)
        font = QtGui.QFont()
        font.setFamily("Forte")
        font.setPointSize(12)
        self.frame_3.setFont(font)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_9.setContentsMargins(0, 0, 14, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.mentos_button = QtWidgets.QPushButton(self.frame_3)
        self.mentos_button.setMinimumSize(QtCore.QSize(60, 10))
        self.mentos_button.setMaximumSize(QtCore.QSize(100, 57))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.mentos_button.setFont(font)
        self.mentos_button.setAutoFillBackground(False)
        self.mentos_button.setStyleSheet("padding: 0 17 0 17;\n"
"margin:0")
        self.mentos_button.setIconSize(QtCore.QSize(24, 24))
        self.mentos_button.setObjectName("mentos_button")
        self.verticalLayout_9.addWidget(self.mentos_button)
        self.running_label = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Doppio One")
        font.setPointSize(8)
        self.running_label.setFont(font)
        self.running_label.setStyleSheet("color:rgb(0, 170, 0)")
        self.running_label.setObjectName("running_label")
        self.verticalLayout_9.addWidget(self.running_label, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout.addWidget(self.frame_3)
        self.frame_2 = QtWidgets.QFrame(self.widget_2)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setContentsMargins(20, 1, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.clear_text_button = QtWidgets.QPushButton(self.frame_2)
        self.clear_text_button.setMinimumSize(QtCore.QSize(62, 22))
        self.clear_text_button.setMaximumSize(QtCore.QSize(92, 52))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(9)
        self.clear_text_button.setFont(font)
        self.clear_text_button.setStyleSheet("padding : 10 4 10 4\n"
"")
        self.clear_text_button.setObjectName("clear_text_button")
        self.horizontalLayout_2.addWidget(self.clear_text_button)
        self.horizontalLayout.addWidget(self.frame_2, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_2.addWidget(self.widget_2, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.widget_4 = QtWidgets.QWidget(self.central_widget_sub)
        self.widget_4.setMinimumSize(QtCore.QSize(400, 87))
        self.widget_4.setMaximumSize(QtCore.QSize(400, 99))
        self.widget_4.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(7)
        self.widget_4.setFont(font)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_4.setContentsMargins(12, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_4 = QtWidgets.QFrame(self.widget_4)
        self.frame_4.setMinimumSize(QtCore.QSize(400, 99))
        self.frame_4.setMaximumSize(QtCore.QSize(600, 299))
        self.frame_4.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.widget_6 = QtWidgets.QWidget(self.frame_4)
        self.widget_6.setObjectName("widget_6")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.widget_6)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.created_by_label = QtWidgets.QLabel(self.widget_6)
        self.created_by_label.setMinimumSize(QtCore.QSize(80, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.created_by_label.setFont(font)
        self.created_by_label.setStyleSheet("color:rgb(0, 85, 127)")
        self.created_by_label.setWordWrap(False)
        self.created_by_label.setObjectName("created_by_label")
        self.verticalLayout_7.addWidget(self.created_by_label)
        self.verticalLayout_5.addWidget(self.widget_6, 0, QtCore.Qt.AlignVCenter)
        self.widget_7 = QtWidgets.QWidget(self.frame_4)
        self.widget_7.setObjectName("widget_7")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.widget_7)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.widget_8 = QtWidgets.QWidget(self.widget_7)
        self.widget_8.setStyleSheet("")
        self.widget_8.setObjectName("widget_8")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_8)
        self.horizontalLayout_5.setContentsMargins(10, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(12)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.name1 = QtWidgets.QLabel(self.widget_8)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.name1.setFont(font)
        self.name1.setStyleSheet("color:rgb(69, 150, 255)")
        self.name1.setObjectName("name1")
        self.horizontalLayout_5.addWidget(self.name1, 0, QtCore.Qt.AlignLeft)
        self.username1 = QtWidgets.QLabel(self.widget_8)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.username1.setFont(font)
        self.username1.setObjectName("username1")
        self.horizontalLayout_5.addWidget(self.username1, 0, QtCore.Qt.AlignRight)
        self.name1_icon = QtWidgets.QLabel(self.widget_8)
        self.name1_icon.setMaximumSize(QtCore.QSize(32, 32))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.name1_icon.setFont(font)
        self.name1_icon.setLineWidth(1)
        self.name1_icon.setMidLineWidth(0)
        self.name1_icon.setText("")
        self.name1_icon.setPixmap(QtGui.QPixmap(".\\../verson2/autotyper/otto/instlogo.jpg"))
        self.name1_icon.setScaledContents(True)
        self.name1_icon.setObjectName("name1_icon")
        self.horizontalLayout_5.addWidget(self.name1_icon, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_8.addWidget(self.widget_8, 0, QtCore.Qt.AlignTop)
        self.widget_9 = QtWidgets.QWidget(self.widget_7)
        self.widget_9.setStyleSheet("")
        self.widget_9.setObjectName("widget_9")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_9)
        self.horizontalLayout_6.setContentsMargins(10, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(12)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.name2 = QtWidgets.QLabel(self.widget_9)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.name2.setFont(font)
        self.name2.setAutoFillBackground(False)
        self.name2.setStyleSheet("color:rgb(69, 150, 255)")
        self.name2.setObjectName("name2")
        self.horizontalLayout_6.addWidget(self.name2, 0, QtCore.Qt.AlignLeft)
        self.username2 = QtWidgets.QLabel(self.widget_9)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(True)
        self.username2.setFont(font)
        self.username2.setObjectName("username2")
        self.horizontalLayout_6.addWidget(self.username2, 0, QtCore.Qt.AlignRight)
        self.name2_icon = QtWidgets.QLabel(self.widget_9)
        self.name2_icon.setMaximumSize(QtCore.QSize(32, 32))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.name2_icon.setFont(font)
        self.name2_icon.setLineWidth(1)
        self.name2_icon.setMidLineWidth(0)
        self.name2_icon.setText("")
        self.name2_icon.setPixmap(QtGui.QPixmap(".\\../verson2/autotyper/otto/instlogo.jpg"))
        self.name2_icon.setScaledContents(True)
        self.name2_icon.setObjectName("name2_icon")
        self.horizontalLayout_6.addWidget(self.name2_icon, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_8.addWidget(self.widget_9, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_5.addWidget(self.widget_7, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.verticalLayout_4.addWidget(self.frame_4)
        self.verticalLayout_2.addWidget(self.widget_4, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.widget_3 = QtWidgets.QWidget(self.central_widget_sub)
        font = QtGui.QFont()
        font.setFamily("Rage Italic")
        font.setPointSize(7)
        self.widget_3.setFont(font)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_5 = QtWidgets.QFrame(self.widget_3)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.note_label = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.note_label.setFont(font)
        self.note_label.setLineWidth(1)
        self.note_label.setScaledContents(False)
        self.note_label.setWordWrap(True)
        self.note_label.setObjectName("note_label")
        self.horizontalLayout_4.addWidget(self.note_label)
        self.verticalLayout_6.addWidget(self.frame_5)
        self.verticalLayout_2.addWidget(self.widget_3)
        self.verticalLayout.addWidget(self.central_widget_sub)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.code_input.setPlaceholderText(_translate("MainWindow", "Paste the Python code here..."))
        self.python.setText(_translate("MainWindow", "python"))
        self.python.setChecked(True)
        self.non_python.setText(_translate("MainWindow", "non-python"))
        self.normal_text.setText(_translate("MainWindow", "normal text"))
        self.mentos_button.setText(_translate("MainWindow", "Mentos!"))
        self.running_label.setText(_translate("MainWindow", "running..."))
        self.clear_text_button.setText(_translate("MainWindow", "Clear Text"))
        self.created_by_label.setText(_translate("MainWindow", "Created by -"))
        self.name1.setText(_translate("MainWindow", "Shreyans Singh"))
        self.username1.setText(_translate("MainWindow", "thesilentarrow"))
        self.name2.setText(_translate("MainWindow", "Himanshu Sharma"))
        self.username2.setText(_translate("MainWindow", "himmu1144"))
        self.note_label.setText(_translate("MainWindow", "Paste the code in the above box, click on Mentos!, place the cursor where you want to autotype the code then press \"escape key\" and enjoy!"))


#autotyper code
class Main(QMainWindow, Ui_MainWindow):
    
    def __init__(self, parent=None):
        
        super().__init__(parent)
        
        self.setupUi(self)
        self.x=0
        self.hot=0
        self.running_label.hide()
        
        # Connect the clicked signal of the push button to a new method
        self.clear_text_button.clicked.connect(self.clear_text)
        
        self.python.toggled.connect(self.clear_text)
        self.non_python.toggled.connect(self.clear_text)
        self.normal_text.toggled.connect(self.clear_text)
        
        self.mentos_button.clicked.connect(self.start_autotyping)
        self.name1_icon.mousePressEvent = self.open_insta1
        self.name2_icon.mousePressEvent = self.open_insta2
        print("connected")
        
    def open_insta1(self,event):
        # Hide the label when it is clicked
        QDesktopServices.openUrl(QUrl('https://www.instagram.com/thesilentarrow/'))    
    def open_insta2(self,event):
        # Hide the label when it is clicked
        QDesktopServices.openUrl(QUrl('https://instagram.com/himmu1144?igshid=ZDdkNTZiNTM='))    
    
    def clear_text(self):
        # Set the value of the text variable to an empty string
        self.text = ''
        self.running_label.hide()
        # Update the text of the label to reflect the change
        self.code_input.clear()
        
        if self.python.isChecked():
                self.code_input.setPlaceholderText("Paste the Python code here...")
        if self.non_python.isChecked():
                self.code_input.setPlaceholderText("Paste the Non-Python code here...")
        if self.normal_text.isChecked():
                self.code_input.setPlaceholderText("Paste Normal Text here...")
        
        if self.hot==1:
            keyboard.remove_hotkey('escape')
            keyboard.remove_hotkey('`')
            self.hot=0  
            
    def start_autotyping(self): 
        
          
        self.running_label.show()  
        print("lol")
        # Get the text from the plain text edit
        #self.pushButton.setStyleSheet("background-color: red")
        self.text = self.code_input.toPlainText()
        
        print(self.text)
        
        self.spaces = 0 
        
        delay_speed = 0

        def tabbing_mech(line):
            
            
            count_space = 0
            
            
            if self.x==1:
                pyautogui.press('tab')
                print("xxxxxxxxxxxxx")
            for char in line:
                if char == " ":
                    count_space += 1
                elif char == "\t":
                    count_space += 4
                else:
                    break
            print(count_space, self.spaces, line)
            print("bug")
            
            if self.spaces > count_space:
                back_tab = (self.spaces - count_space) // 4 
                self.spaces = count_space
                print("tab back")
                for i in range(back_tab):
                    pyautogui.keyDown('shift')
                    pyautogui.press('tab')
                    pyautogui.keyUp('shift')
                return line.lstrip()
            elif count_space == 0:
                return line
            elif self.spaces == count_space:
                return line.lstrip()
            elif self.spaces < count_space:
                print("indenting")
                self.spaces = count_space
                return line.lstrip()

        
        
            

        def start_autotyper_java():
            self.hot=1
            self.running_label.show()  
            self.drop=0
            with io.StringIO(self.text) as f:
                for lines in f:
                    
                    if not lines.strip():
                        print("empty line")
                        continue
                    else:
                        #for finding comments
                        def remove_comments(line):
                            # check if the line contains a comment symbol
                            if "//" in line:
                                # initialize two flag variables to False
                                in_single_quote = False
                                in_double_quote = False
                                # loop through each character in the line
                                for i, char in enumerate(line):
                                # if the character is a single quote and we are not inside a double quote string literal
                                    if char == "'" and not in_double_quote:
                                        # toggle the in_single_quote flag variable
                                        in_single_quote = not in_single_quote
                                    # if the character is a double quote and we are not inside a single quote string literal
                                    if char == '"' and not in_single_quote:
                                        # toggle the in_double_quote flag variable
                                        in_double_quote = not in_double_quote
                                    # if the character is a comment symbol and we are not inside any string literal
                                    if char == "/" and not (in_single_quote or in_double_quote):
                                        print("comment found")
                                        print("i:",i)
                                        print("line[i+1]:",line[i+1])
                                        # return the part of the line before the comment symbol
                                        if line[i+1]=='/' and not (in_single_quote or in_double_quote):
                                            print("comment found//")
                                            self.drop=1
                                        
                                        
                                            return line[:i]
                                        
                                # if we reach the end of the loop without returning, it means the comment symbol was inside a string literal
                                # so we return the line as it is
                                self.drop=0
                                return line
                            else:
                                # return the line as it is
                                self.drop=0
                                return line

                        
                        
                        lines = remove_comments(lines)
                        print("lines:",lines)
                        if not lines.strip():
                            print("empty line")
                            continue 
                        type_me = tabbing_mech(lines) #Used for IDEs
                        if type_me.endswith('{\n'):
                            type_me= type_me[:-1] + ' ' + type_me[-1]
                        pyautogui.typewrite(type_me, delay_speed)
                        if self.drop==1:
                            pyautogui.press('enter')
                        lines1=lines.rstrip()+'\n'
                        
                        if 'break\n' in lines1 or 'return\n' in lines1 or 'pass\n' in lines1 or 'continue\n' in lines1:
                            self.x=1
                        else:
                            self.x=0
            self.running_label.hide()
            
            
        def start_autotyper_python():
            self.hot=1
            self.running_label.show()  
            self.drop=0
            with io.StringIO(self.text) as f:
                for lines in f:
                    
                    if not lines.strip():
                        print("empty line")
                        continue
                    else:
                        #for finding comments
                        def remove_comments(line):
                            # check if the line contains a comment symbol
                            if "#" in line:
                                # initialize two flag variables to False
                                in_single_quote = False
                                in_double_quote = False
                                # loop through each character in the line
                                for i, char in enumerate(line):
                                # if the character is a single quote and we are not inside a double quote string literal
                                    if char == "'" and not in_double_quote:
                                        # toggle the in_single_quote flag variable
                                        in_single_quote = not in_single_quote
                                    # if the character is a double quote and we are not inside a single quote string literal
                                    if char == '"' and not in_single_quote:
                                        # toggle the in_double_quote flag variable
                                        in_double_quote = not in_double_quote
                                    # if the character is a comment symbol and we are not inside any string literal
                                    if char == "#" and not (in_single_quote or in_double_quote):
                                        print("comment found")
                                        self.drop=1                                       
                                        return line[:i]
                                        
                                # if we reach the end of the loop without returning, it means the comment symbol was inside a string literal
                                # so we return the line as it is
                                self.drop=0
                                return line
                            else:
                                # return the line as it is
                                self.drop=0
                                return line

                        
                        
                        lines = remove_comments(lines)
                        print("lines:",lines)
                        if not lines.strip():
                            print("empty line")
                            continue 
                        type_me = tabbing_mech(lines) #Used for IDEs
                        if type_me.endswith('{\n'):
                            type_me= type_me[:-1] + ' ' + type_me[-1]
                        pyautogui.typewrite(type_me, delay_speed)
                        if self.drop==1:
                            pyautogui.press('enter')
                        lines1=lines.rstrip()+'\n'
                        
                        if 'break\n' in lines1 or 'return\n' in lines1 or 'pass\n' in lines1 or 'continue\n' in lines1:
                            self.x=1
                        else:
                            self.x=0
            self.running_label.hide()
            
            
        def start_autotyper_text():
            self.hot=1
            self.running_label.show()  
            self.drop=0
            with io.StringIO(self.text) as f:
                for lines in f:
                    pyautogui.typewrite(lines, delay_speed)
                    
            self.running_label.hide()
            
        if self.hot==0:
            if self.python.isChecked():
                print("for python")
                keyboard.add_hotkey('escape', start_autotyper_python)
                keyboard.add_hotkey('`', start_autotyper_python)
                self.hot=1
            if self.non_python.isChecked():
                print("for python")
                keyboard.add_hotkey('escape', start_autotyper_java)
                keyboard.add_hotkey('`', start_autotyper_java)
                self.hot=1
            if self.normal_text.isChecked():
                print("simple text")
                keyboard.add_hotkey('escape', start_autotyper_text)
                keyboard.add_hotkey('`', start_autotyper_text)
                self.hot=1

    #-----------for java--------------
    #---------------------------------
        
            
        

 
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    m = Main()
    m.show()
    sys.exit(app.exec_())
 
