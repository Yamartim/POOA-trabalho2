from src import DownloaderFactory, ParserFactory, ForwarderFactory

if __name__ == '__main__':
    
    fac = DownloaderFactory()
    downloader = fac.create_downloader('urllib', 'https://g1.globo.com')

    html = downloader.download()
    
    fac = ParserFactory()
    parser = fac.create_parser('G1', html = html)
    #res = [['titulo1'], ['titulo2'], ['titulo3']]
    res = parser.Get_News()

    fac = ForwarderFactory()
    forwarder = fac.create_forwarder('csv', results=res, fl=open('file.csv', 'w'))

    forwarder.forward()