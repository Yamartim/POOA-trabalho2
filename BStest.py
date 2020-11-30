from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
html = urlopen('https://g1.globo.com/', context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

print(soup.findAll(id='bstn-launcher'))