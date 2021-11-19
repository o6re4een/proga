import requests
from bs4 import BeautifulSoup

class Parser1():
    def __init__(self, url):
        self.page = requests.get(url)
        self.soup = BeautifulSoup(self.page.text, "html.parser")
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
    @property
    def hrefs(self):
        return self._parse_problem_nums()       

