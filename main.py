'''
Iago Elias
Martim Lima

ENPE 2020 bloco B
POOA - trabalho 2
'''
from src import DownloaderFactory, ParserFactory, ForwarderFactory

#to switch between different settings for download method, news source and output set the values for the DOWNLOAD, URL, OUTPUT and OUTPUT_FILE constants below.
#new values for the constants should be set if you plan to extend the functionality

DOWNLOAD = 'urllib'

URL = 'https://g1.globo.com'
#URL = 'https://www.uol.com.br'

#OUTPUT = 'stdout'
OUTPUT = 'csv'

OUTPUT_FILE = 'file.csv'

if __name__ == '__main__':
    
    #the chosen downloader is instantiated and returns an html file
    fac = DownloaderFactory()
    downloader = fac.create_downloader(DOWNLOAD, URL)

    html = downloader.download()
    
    #the chosen parser is instantiated and parses the obtained html file, obtaining a results list
    fac = ParserFactory()
    parser = fac.create_parser(URL, html = html)
    
    #dummy results list for testing
    #res = [['titulo1'], ['titulo2'], ['titulo3']]
    res = parser.get_news()

    #the chosen forwarder is instantiated and forwards the results list to the desired output
    fac = ForwarderFactory()

    forwarder = fac.create_forwarder(OUTPUT, results=res, fl=open(OUTPUT_FILE, 'w'))
    forwarder.forward()