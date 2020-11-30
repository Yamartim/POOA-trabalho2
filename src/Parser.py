from bs4 import BeautifulSoup

class Parser(html):
    def __init__(self, html):
        self._html = html
        _soup = BeautifulSoup(_html, 'html.parser')

class ParserG1(Parser):
    pass

class ParserUOL(Parser):
    pass

class ParserFactory:
    def create_downloader(self, name, html):
        if name == 'G1':
            return ParserG1(html)
        elif name == 'G1':
            return ParserUOL(html)