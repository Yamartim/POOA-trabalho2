from bs4 import BeautifulSoup

class Parser():
    def __init__(self, html):
        self._html = html
        _soup = BeautifulSoup(self._html, 'html.parser')

class ParserG1(Parser):
    pass

class ParserUOL(Parser):
    pass

class ParserFactory:
    def create_parser(self, name, html):
        if name == 'G1':
            return ParserG1(html)
        elif name == 'UOL':
            return ParserUOL(html)