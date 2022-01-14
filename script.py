from myparser import Parser1, link_taker
import sqlite3
  
url = "https://ege.sdamgia.ru/test?theme=88"

spis = link_taker(url)
#list1 = spis.hrefs

con = sqlite3.connect("pars.db")
cur = con.cursor()
#cur.execute('''CREATE TABLE test_dvig
               #(id, text, answer)''')

quets_dict = {}

theme = "test_procent"

def main():
    for el in spis.hrefs:
        #print(parse.text_with_html)
        parse = Parser1(el)
        #print(parse.text_with_html)
        pars = parse.text_with_html
        
        
        
        text = str(parse.text_with_html)
        text_two = text[23:len(text)-5]
        govno = text_two.find("<")
        s = parse.answer.replace("Ответ: " , "")
        
        
        if govno == -1:
            text_two = text_two.replace("\u202f", ' ')
            #sqlite_update_query = """Update quest where id = ? set theme = ?"""
            #cur.executemany(sqlite_update_query, parse.problem_id, theme)
            update_theme(parse.problem_id)
            #cur.execute("UPDATE quest set ('{}')".format(theme))
            quets_dict[parse.problem_id] = [text_two, s]
        #print(parse.text_with_html,s, ":" , parse.problem_id)


def update_theme(id):
       
    # cur.execute("SELECT rowid FROM quest WHERE id = ?", (id,))
    # data=cur.fetchone()
    # if data is None:
    #     pass
    # else:
    #     cur.execute(
    #         """UPDATE {} SET theme=? WHERE ROWID = ?""".format("quest"),(theme, id))

   
    cur.execute("SELECT count(*) FROM quest WHERE id = ?", (id,))
    data=cur.fetchone()[0]
    if data==0:
       pass
    else:
        sql_update_query = """Update quest set theme = ? where id = ?"""
        data = (theme, id)
        cur.execute(sql_update_query, data)


main()
print(quets_dict)
con.commit()

#for i in range(len(list_text)):
#    text = list_text[i][23:len(list_text[i])-5]
#    text = text.replace("<i>", "")
#    text = text.replace("</i>", "")
    
#print(responce)




