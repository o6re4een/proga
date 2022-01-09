import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


class link_taker():
    def __init__(self, url):
        self._url = url 
        self.driver = webdriver.Chrome()
        self.pause = 0
        self.driver.get(self._url)
        
        self.scrol()
        #self.driver.execute_script("document.getElementById('prob_maindiv').scrollIntoView();")
        #if self.end ==1:
        self.page = self.driver.page_source
        
        self.soup = BeautifulSoup(self.page, "html.parser")
        self.problem_body = self.soup.find("div", class_="pbody")
        self.driver.close() 
    

    def scrol(self):    
        self.lastHeight = self.driver.execute_script("return document.body.scrollHeight")
        while True:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            self.newHeight = self.driver.execute_script("return document.body.scrollHeight")
            if self.newHeight == self.lastHeight:
                break
            self.lastHeight = self.newHeight


    
    def _parse_problem_nums(self):
        ref = "https://math-ege.sdamgia.ru"
        spans = self.soup.findAll("span", class_= "prob_nums")
        hrefs = []
        hrefs_ful = []
        for tag in spans:
            a_s = tag.findAll("a")
            for a in a_s:
                hrefs.append(a.get("href"))
        for el in hrefs:
            clear = ref + el
            hrefs_ful.append(clear)



        return hrefs_ful


    @property
    def hrefs(self):
        return self._parse_problem_nums()       
class Parser1():
    def __init__(self, url):
        self.url = url     
        self.page1 = requests.get(self.url)
        self.soup = BeautifulSoup(self.page1.text, "html.parser")
        self.problem_body = self.soup.find("div", class_="pbody")

    def _get_imglist(self):          
        images = []
        for img in self.problem_body.findAll('img'):
            images.append(img.get('src'))
        return images      
            
    def _parse_clear_text(self):
        filtered_body = []
        for data in self.problem_body:
            filtered_body.append(data.text)
        return filtered_body
        
    def _parse_html(self):
        body = []
        for data1 in self.problem_body:
            body = data1
        return body
    def _parse_problem_num(self):
        problem_num = []
        self.problem_num = self.soup.find("span", class_= "prob_nums") 
        self.problem_num = self.problem_num.find("a")
        self.problem_num = self.problem_num.text
        return self.problem_num
    
    
        
    def _parse_answer(self):
        answer = []
        self.answerr = self.soup.find("div", class_= "answer")
        self.answerr = self.answerr.text
        return self.answerr
    
    @property
    def images(self):
        return self._get_imglist()
    
    @property
    def clear_text(self):
        return self._parse_clear_text()

    @property
    def text_with_html(self):
        return self._parse_html()

    @property
    def problem_id(self):
        return self._parse_problem_num()

    @property
    def answer(self):
        return self._parse_answer()
  
#