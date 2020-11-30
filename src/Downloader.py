from urllib.request import urlopen
import ssl
from abc import abstractmethod

class Downloader():
    def __init__(self, url: str):
        self._url = url

    def download (self):
        # to overwrite
        pass

class DownloaderUrlLib(Downloader):
    def __init__(self, url: str):
        super(url)
    def download (self):
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        return urlopen(self._url, context=ctx).read()

class DownloaderFactory:
    def create_downloader(self, name, url):
        if name == 'urllib':
            return DownloaderUrlLib(url)