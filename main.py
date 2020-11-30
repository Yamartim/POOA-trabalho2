from src import DownloaderFactory

if __name__ == '__main__':
    
    fac = DownloaderFactory()
    downloader = fac.create_downloader('urllib', 'https://g1.globo.com')

    print (downloader.download())