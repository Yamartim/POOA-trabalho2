from bs4 import BeautifulSoup
from abc import abstractmethod

class Parser():
    def __init__(self, html):
        self._html = html
        self._soup = BeautifulSoup(self._html, 'html.parser')
    
    def Get_News(self):
        lst = list()
        for title in self._result:
            lst.append(title.find(text = True))
        return self._result



class ParserG1(Parser):
    def __init__(self, html):
        super().__init__(html)
        self._result = self._soup.findAll( 'a', {'class': "feed-post-link gui-color-primary gui-color-hover"})


class ParserUOL(Parser):
    def __init__(self, html):
        super().__init__(html)
        self._result = self._soup.findAll( 'h2', {'class': "titulo color2"})

class ParserFactory:
    def create_parser(self, name, html):
        if name == 'https://g1.globo.com':
            return ParserG1(html)
        elif name == 'https://www.uol.com.br':
            return ParserUOL(html)