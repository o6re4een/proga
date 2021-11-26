
import sys
import sqlite3 
import re
#
from PyQt5.QtWebEngineWidgets import QWebEnginePage, QWebEngineView
from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtGui import QBrush, QColor
from PyQt5.sip import enableautoconversion
#
from testv1 import Ui_Test1 
from finish_screen import Ui_finish_screen
#
class testApp(QtWidgets.QWidget, Ui_Test1):
    def __init__(self):
        super(testApp, self).__init__()   
        self.setupUi(self)
        self._counter = 0
        self.nodetaker()
        self.webEngineView.setHtml(self.nodemassive[self._counter].get_text)
        self.anslist = []
        self.clear_list()
        self.get_keylist()

        print(self.keylist)
        #self.next_qst_btn.clicked.connect(self.get_answer)
        #self.next_qst_btn.clicked.connect(self._checker.check)
        self.next_qst_btn.clicked.connect(self.page_swith_forward)
        self.prev_qst_btn.clicked.connect(self.page_swith_backward)
        self.answeredit.editingFinished.connect(self.saver)
        
        
        
        
        #
        self._checker = checker(self.anslist, self.keylist)
        
        self.finish_btn.clicked.connect(self._checker.check)
        
        self.finish_btn.clicked.connect(self.open_finish)
        
    

    
    def open_finish(self):
        self.dialog = finish_app(self.anslist, self.keylist, self._checker._score)
        self.dialog.show()
        
   
    def close_win(self):
        self.close()
        

    def get_keylist(self):
        self.keylist= []
        for k in range(len(self.nodemassive)):
            self.keylist.append(self.nodemassive[k].get_asnwer)
        return self.keylist
    
    def saver(self):
        self._gotten_answ = self.answeredit.text()
        self.anslist[self._counter] = self._gotten_answ
        return self.anslist



    def clear_list(self):
         for i in range(0, 91):
             self.anslist.append("")
         return self.anslist
        
    def nodetaker(self): 
        self.nodemassive = []
        for node in db_con("pars.db", "quest").select(92):
            self.nodemassive.append(node)
        return self.nodemassive



    
    def fill_str(self):
        self.answeredit.clear()
        self.answeredit.setText(self.anslist[self._counter])
        
    def page_swith_forward(self): 
        
        if self._counter <90:
            self._counter = self._counter + 1
        
        self.fill_str()
         
        self._text = self.nodemassive[self._counter].get_text   
        self.replace("html.html", "htmltmp.html", "htmlcode", self._text)
        #self.answeredit.clear()
        self.loadPage()   
          
        print(self._counter)
        print(self.anslist)
        
        return self._counter
        
    def page_swith_backward(self):  
        if self._counter > 0:
            self._counter = self._counter - 1
        
        self.fill_str()
        
        self._text = self.nodemassive[self._counter].get_text    
        self.replace("html.html", "htmltmp.html", "htmlcode", self._text)
        
        self.loadPage()
 
        print(self._counter)
        print(self.anslist)

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
    
    




class finish_app(QtWidgets.QWidget, Ui_finish_screen):
    def __init__(self, anlist, keys_list, score):
        super(finish_app, self).__init__()
        self.setupUi(self)
        self._score = score
        self._score = str(self._score)
        self._answlist = anlist
        self._keys = keys_list  
        self.tableWidget.setColumnCount(len(self._keys))
        self.label.setText("Всего правильных ответов:" + self._score)
        self.build_table()
    
    def build_table(self):
        
        
        for _x in range(0, len(self._keys)-1): 
            self.tableWidget.setItem(0, _x , QtWidgets.QTableWidgetItem(self._answlist[_x]))
            # if self._answlist[_x] == self._keys[_x]:
            #     item = self.tableWidget.QTableWidgetItem()
            #     self.tableWidget.QTableWidgetItem.setForeground(QBrush(QColor(0, 255, 0)))
            # else:
            #    self.tableWidget.QTableWidgetItem.setForeground(QBrush(QColor(0, 255, 0)))
            self.tableWidget.setItem(1, _x , QtWidgets.QTableWidgetItem(self._keys[_x]))




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
    def __init__(self,anslist, keylist): 
        self._answlist = anslist       
        self._keylist = keylist
        self._score = 0
        
    def check(self):
        for _i in range(len(self._answlist)):
            if self._answlist[_i] == self._keylist[_i]:
                self._score +=1
            else:
                self._score += 0
        print(self._score)
        return self._score

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    Test1 = testApp()
    Test1.show()
    sys.exit(app.exec_())