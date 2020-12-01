from src import DownloaderFactory, ParserFactory, ForwarderFactory

#URL = 'https://g1.globo.com'
URL = 'https://www.uol.com.br'

OUTPUT = 'stdout'
#OUTPUT = 'csv'

if __name__ == '__main__':
    
    fac = DownloaderFactory()
    downloader = fac.create_downloader('urllib', URL)

    html = downloader.download()
    
    fac = ParserFactory()
    parser = fac.create_parser(URL, html = html)
    #res = [['titulo1'], ['titulo2'], ['titulo3']]
    res = parser.get_news()

    fac = ForwarderFactory()

    if OUTPUT == 'csv':
        forwarder = fac.create_forwarder(OUTPUT, results=res, fl=open('file.csv', 'w'))
    else:
        forwarder = fac.create_forwarder(OUTPUT, results=res)

    forwarder.forward()

'''
Iago Elias
Martim Lima
'''