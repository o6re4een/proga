from myparser import Parser1
#import requests
#from bs4 import BeautifulSoup as BS
  
url = input()
#url = requests.get(url, timeout=(3.05, 27))
#responce = requests.post(url,data={'ajax':'1','skip':'10'})

spis = Parser1(url)
#list1 = spis.hrefs
print(spis.hrefs)
for el in spis.hrefs:
    
    parse = Parser1(el)
    
    #s = parse.answer.replace("Ответ: " , "")
    #print(parse.text_with_html,s, ":" , parse.problem_id)



#print(responce)


