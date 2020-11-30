from src import DownloaderFactory, ForwarderFactory

if __name__ == '__main__':
    
    fac = DownloaderFactory()
    downloader = fac.create_downloader('urllib', 'https://g1.globo.com')

    html = downloader.download()
    
    res = [['titulo1'], ['titulo2'], ['titulo3']]
    fac = ForwarderFactory()
    forwarder = fac.create_forwarder('csv', results=res, fl=open('file.csv', 'w'))

    forwarder.forward()