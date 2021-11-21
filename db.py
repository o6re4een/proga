import sqlite3
from main import TestNode
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

        for _ in range(count):
            _el = _all[_]
            yield TestNode(_el[0],_el[1], _el[2])



        
        # for i in range(len(self.db)):
        #     self.quest_dict[self.db[i][0]] = [self.db[i][1], self.db[i][2]]
        # print(self.quest_dict)
    
    
    
    
    # for i in range(len(db)):
    #     quest_dict[db[i][0]] = [db[i][1], db[i][2]]
    # print(quest_dict)



[print(node) for node in db_con("pars.db", "quest").select(3)]