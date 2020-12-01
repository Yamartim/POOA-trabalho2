from bs4 import BeautifulSoup
from abc import abstractmethod

class Parser():
    def __init__(self, html):
        self._html = html
        self._soup = BeautifulSoup(self._html, 'html.parser')
    
    def Get_News(self):
        "method to be overloaded"
        pass

class ParserG1(Parser):
    def __init__(self, html):
        '''
        @param: results the list of results
        '''
        super().__init__(html)
        self._result = self._soup.findAll( 'a', {'class': "feed-post-link gui-color-primary gui-color-hover"})
    
    def Get_News(self):
        lst = list()
        for title in self._result:
            lst.append(title.find(text = True))
        return lst



class ParserUOL(Parser):
    def __init__(self, html):
        '''
        @param: results the list of results
        '''
        super().__init__(html)

class ParserFactory:
    def create_parser(self, name, html):
        if name == 'G1':
            return ParserG1(html)
        elif name == 'UOL':
            return ParserUOL(html)