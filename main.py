
import sys
from typing import get_args

from PyQt5.QtWebEngineWidgets import QWebEnginePage, QWebEngineView
from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtGui import QPixmap, QImage
import requests
from requests.api import get
from testv1 import Ui_Test1 
from myparser import Parser1
import re



class testApp(QtWidgets.QWidget, Ui_Test1):
    def __init__(self):
        super(testApp, self).__init__()
        self.setupUi(self)
        parse = Parser1("https://math-ege.sdamgia.ru/test?id=41961331&nt=True&pub=False")        
        parse = parse.text_with_html        
        parse = str(parse)
        self.replace("html.html", "htmltmp.html", "htmlcode", parse)       
        self.loadPage()
        self.anslist = []
        self._checker = checker(data_source=self)
        self.next_qst_btn.clicked.connect(self.get_answer)
        self.next_qst_btn.clicked.connect(self._checker.check)
    
    def replace(self, filein, fileout, pattern, subst):
        # Read contents from file as a single string
        file_handle = open(filein, 'r', encoding="utf-8")
        file_string = file_handle.read()
        file_handle.close()

        # Use RE package to allow for replacement (also allowing for (multiline) REGEX)
        file_string = (re.sub(pattern, subst, file_string))

        # Write contents to file.
        # Using mode 'w' truncates the file.
        file_handle = open(fileout, 'w', encoding="utf-8")
        file_handle.write(file_string)
        file_handle.close()

    def loadPage(self):
       
        with open('htmltmp.html', 'r', encoding="utf-8") as f:
            html = f.read()
            self.webEngineView.setHtml(html)   
    
    def get_answer(self):        
        got_answ = self.answeredit.text()     
        self.anslist.append(got_answ)
        #print(self.anslist)
        return self.anslist


class checker():
    #def __init__(self):
        #super(checker, self).__init__()
        #self.vern_answer = 3
        #self.got_answ = self.anslist[-1]
    def __init__(self, data_source = None):
        self._data_source = data_source  
        self.got_answlist = self._data_source.anslist        
        self.vern_answer = "3"
        
    def check(self):
        self.got_answ = self.got_answlist[-1]
        
        if self.got_answ == []:
            pass        
        
        if self.got_answ == self.vern_answer:
            print("ok")
        else:
            print("no")
        #print(self.got_answ)
        #print(self.got_answlist)


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    Test1 = testApp()
    Test1.show()
    sys.exit(app.exec_())