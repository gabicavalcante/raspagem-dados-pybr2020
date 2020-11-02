from requests_html import HTMLSession
session = HTMLSession()

parameters = {'ano_id': '8', 'mes_id': "04"}
url = "https://www.cmnat.rn.gov.br/ordens/send"

r = session.post(url, data=parameters)
content = r.html.find('.listagem-noticias li p a')

links = [(c.text, c.attrs["href"]) for c in content]

def clean_url(url):
  return doc.lstrip().lower().replace(' ', '_').replace('/', '_').replace('-', '_')

for doc, url in links:
  pdf = session.get(url)
  file_name = f'{clean_url(url)}'
  open(f'{file_name}.pdf', 'wb').write(pdf.content)