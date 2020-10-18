import requests
from bs4 import BeautifulSoup

parameters = {'ano_id': '8', 'mes_id': "04"}
url = "https://www.cmnat.rn.gov.br/ordens/send"

# request to find the documents
response = requests.post(url, data=parameters)
doc = BeautifulSoup(response.text, 'html.parser')

# find tag a <inside> tag p <inside> tag li
content = doc.select(".listagem-noticias li p a")
links = [(c.get_text(), c['href']) for c in content]

def clean_url(url):
  return doc.lstrip().lower().replace(' ', '_').replace('/', '_').replace('-', '_')

for doc, url in links:
  pdf = requests.get(url)
  file_name = f'{clean_url(url)}'
  open(f'{file_name}.pdf', 'wb').write(pdf.content)