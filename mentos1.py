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
        MainWindow.resize(800, 639)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/shrey/Downloads/mentoslogo.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(180, 20, 451, 321))
        self.plainTextEdit.setAcceptDrops(False)
        self.plainTextEdit.setReadOnly(False)
        self.plainTextEdit.setPlainText("")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(280, 370, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.Clear = QtWidgets.QPushButton(self.centralwidget)
        self.Clear.setGeometry(QtCore.QRect(440, 370, 81, 41))
        self.Clear.setObjectName("Clear")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(290, 410, 91, 31))
        self.label.setStyleSheet("color: rgb(0, 170, 0);")
        self.label.setObjectName("label")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(230, 470, 371, 81))
        self.textBrowser_2.setMouseTracking(False)
        self.textBrowser_2.setAcceptDrops(False)
        self.textBrowser_2.setAutoFillBackground(False)
        self.textBrowser_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_2.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.textBrowser_2.setOpenExternalLinks(True)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(530, 480, 31, 31))
        self.label_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("C:/Users/shrey/Downloads/instagram.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setOpenExternalLinks(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(530, 520, 31, 31))
        self.label_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("C:/Users/shrey/Downloads/instagram.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setOpenExternalLinks(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 570, 771, 31))
        self.label_4.setScaledContents(True)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(440, 490, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setItalic(True)
        self.label_5.setFont(font)
        self.label_5.setScaledContents(True)
        self.label_5.setOpenExternalLinks(True)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(450, 530, 71, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setItalic(True)
        self.label_6.setFont(font)
        self.label_6.setTextFormat(QtCore.Qt.AutoText)
        self.label_6.setScaledContents(True)
        self.label_6.setOpenExternalLinks(True)
        self.label_6.setObjectName("label_6")
        self.plainTextEdit.raise_()
        self.pushButton.raise_()
        self.Clear.raise_()
        self.label.raise_()
        self.textBrowser_2.raise_()
        self.label_3.raise_()
        self.label_2.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Mentos"))
        self.plainTextEdit.setPlaceholderText(_translate("MainWindow", "Paste the code here..."))
        self.plainTextEdit.clear()
        self.pushButton.setText(_translate("MainWindow", "Mentos!"))
        self.pushButton.setShortcut(_translate("MainWindow", "Ctrl+M"))
        self.Clear.setText(_translate("MainWindow", "Clear text"))
        self.Clear.setShortcut(_translate("MainWindow", "Shift+Esc"))
        self.label.setText(_translate("MainWindow", "Running..."))
        self.label.hide()
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'cursive\'; font-size:9pt; font-weight:600; font-style:italic; color:#1e549f;\">Created by-:</span><span style=\" font-size:8pt;\"><br />         </span><span style=\" font-family:\'sans-serif\'; font-size:8pt; font-weight:600; color:#2e79ba;\">Shreyans Singh </span><span style=\" font-size:8pt;\"><br /><br />         </span><span style=\" font-family:\'sans-serif\'; font-size:8pt; font-weight:600; color:#2e79ba;\">Himanshu Sharma</span><span style=\" font-size:8pt;\"><br /></span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "Paste the code in the above box, click on Mentos!, place the cursor where you want the to autotype the code then press  escape key. enjoy.  "))
        self.label_5.setText(_translate("MainWindow", "thesilentarrow"))
        self.label_6.setText(_translate("MainWindow", "himmu1144"))

#autotyper code
class Main(QMainWindow, Ui_MainWindow):
    
    def __init__(self, parent=None):
        
        super().__init__(parent)
        
        self.setupUi(self)
        self.x=0
        self.hot=0
        
        
        # Connect the clicked signal of the push button to a new method
        self.Clear.clicked.connect(self.clear_text)
        self.pushButton.clicked.connect(self.start_autotyping)
        self.label_2.mousePressEvent = self.open_insta1
        self.label_3.mousePressEvent = self.open_insta2
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
        self.label.hide()
        # Update the text of the label to reflect the change
        self.plainTextEdit.clear()
        if self.hot==1:
            keyboard.remove_hotkey('escape')
            self.hot=0  
    def start_autotyping(self):   
        self.label.show()  
        print("lol")
        # Get the text from the plain text edit
        #self.pushButton.setStyleSheet("background-color: red")
        self.text = self.plainTextEdit.toPlainText()
        
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

        
        
            

        def start_autotyper():
            self.hot=1
            
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
                                        # return the part of the line before the comment symbol
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
                        pyautogui.typewrite(type_me, delay_speed)
                        if self.drop==1:
                            pyautogui.press('enter')
                        
                        lines1=lines.rstrip()+'\n'
                        
                        if 'break\n' in lines1 or 'return\n' in lines1 or 'pass\n' in lines1:
                            self.x=1
                        else:
                            self.x=0
            self.label.hide()
        if self.hot==0:
            keyboard.add_hotkey('escape', start_autotyper)
            self.hot=1
        
        
        # Keep the script running
        #keyboard.wait()

 
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    m = Main()
    m.show()
    sys.exit(app.exec_())
 