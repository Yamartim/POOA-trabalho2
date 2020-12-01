#script para propositos de teste

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
#html = urlopen('https://g1.globo.com/', context=ctx).read() #G1
html = urlopen('https://www.uol.com.br/', context=ctx).read() #UOL

soup = BeautifulSoup(html, 'html.parser')

#result = soup.findAll( 'a', {'class': "feed-post-link gui-color-primary gui-color-hover"}) #G1
result = soup.findAll( 'h2', {'class': "titulo color2"}) #UOL

lst = list()
for titulo in result:
    lst.append(titulo.find(text = True))

print(lst)




#print(type(soup.find(id='bstn-launcher')))