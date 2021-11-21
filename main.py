
import sys

import sqlite3 
from PyQt5.QtWebEngineWidgets import QWebEnginePage, QWebEngineView
from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtGui import QPixmap, QImage
import requests
from testv1 import Ui_Test1 
from myparser import Parser1
import re



class testApp(QtWidgets.QWidget, Ui_Test1):
    def __init__(self):
        super(testApp, self).__init__()   
        self.setupUi(self)
        self._counter = 0
        self.nodetaker()
        self.webEngineView.setHtml(self.nodemassive[self._counter].get_text)
        self.anslist = []
        self._checker = checker(data_source=self)
        self.next_qst_btn.clicked.connect(self.get_answer)
        self.next_qst_btn.clicked.connect(self._checker.check)
        self.next_qst_btn.clicked.connect(self.page_swither_forward)
        self.prev_qst_btn.clicked.connect(self.page_swither_backward)
        

        
        
    def nodetaker(self): 
        self.nodemassive = []
        for node in db_con("pars.db", "quest").select(10):
            self.nodemassive.append(node)
        return self.nodemassive

           
         
       
        
        


    def page_swither_forward(self):  
        self._counter = self._counter + 1 
       
        self._text = self.nodemassive[self._counter].get_text
        
        self.replace("html.html", "htmltmp.html", "htmlcode", self._text)
        self.loadPage()   
        
        print(self._counter)
        return self._counter
        
    def page_swither_backward(self):
        if self._counter > 0:
            self._counter = self._counter - 1
        self._text = self.nodemassive[self._counter].get_text
       
        
        self.replace("html.html", "htmltmp.html", "htmlcode", self._text)
        self.loadPage()
        print(self._counter)
        return self._counter
       
        
        
        
        
        
        

        




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
        print(self.anslist)
        return self.anslist








class db_con():
    def __init__(self, db_name, tname):
        self._db = db_name 
        self._con = sqlite3.connect(self._db)
        self._cur = self._con.cursor()
        self._tname = tname
        
        
    def sel_all(self):
        self._cur.execute(f"SELECT * FROM {self._tname}")    
        self._res = self._cur.fetchall()
        return self._res
    
    def select(self, count):
        _all = self.sel_all()

        for i in range(count):
            _el = _all[i]
            yield TestNode(_el[0],_el[1], _el[2])


class TestNode():
    def __init__(self, id, text, key):
        self._id = id
        self._text = text
        self._key = key
        
    @property
    def get_id(self):
        return self._id

    @property
    def get_text(self):
        return self._text
    
    @property
    def get_asnwer(self):
        return self._key

        

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
   


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    Test1 = testApp()
    Test1.show()
    sys.exit(app.exec_())