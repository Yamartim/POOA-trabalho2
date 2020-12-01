from src import DownloaderFactory, ParserFactory, ForwarderFactory

#URL = 'https://g1.globo.com'
URL = 'https://www.uol.com.br'

if __name__ == '__main__':
    
    fac = DownloaderFactory()
    downloader = fac.create_downloader('urllib', URL)

    html = downloader.download()
    
    fac = ParserFactory()
    parser = fac.create_parser(URL, html = html)
    #res = [['titulo1'], ['titulo2'], ['titulo3']]
    res = parser.Get_News()

    fac = ForwarderFactory()
    forwarder = fac.create_forwarder('csv', results=res, fl=open('file.csv', 'w'))

    forwarder.forward()

'''
Iago Elias
Martim Lima
'''