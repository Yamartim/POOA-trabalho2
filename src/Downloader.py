from urllib.request import urlopen
import ssl
from abc import abstractmethod

class Downloader():
    '''
    Class to download a html file 
    child must define the download implementation
    '''
    def __init__(self, url: str):
        '''
        @param: url to be downloaded as html
        '''
        self._url = url
    def download (self):
        "to be overloaded"
        pass

class DownloaderUrlLib(Downloader):
    '''
    Class to download a html file using urllib
    '''
    def __init__(self, url: str):
        super().__init__(url)
    def download (self):
        "Download body of url as html"
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        return urlopen(self._url, context=ctx).read()

'''
A new downloader - inheriting class can be written for cases in which
the UrlLib class does not suffice
'''

'''
Returns the correct downloader class depending on the name param
'''
class DownloaderFactory:
    def create_downloader(self, name, url):
        if name == 'urllib':
            return DownloaderUrlLib(url)
        """ 
        to return a new class simply add another elif statement and compare the 
        name parameter to the new DOWNLOAD constant set in main.py
        """