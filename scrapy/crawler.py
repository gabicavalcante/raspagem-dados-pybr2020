import scrapy
import requests

from urllib.parse import urlencode
from scrapy.http import FormRequest

params = {"ano_id": "8", "mes_id": "04"}

def clean(name):
  return name.lstrip().lower().replace(' ', '_').replace('/', '_').replace('-', '_')

class DocSpider(scrapy.Spider):
    name = "doc_spider"
    start_url = "https://www.cmnat.rn.gov.br/ordens/send"

    def start_requests(self):
        yield FormRequest(self.start_url, callback=self.parser, formdata=params)

    def parser(self, response):
        for link in response.css(".listagem-noticias li p"):
            label = link.xpath("a/text()").extract_first()
            url = link.xpath("a/@href").extract_first()
            yield self.get_pdf(label, url)

    def get_pdf(self, label, url):
        pdf = requests.get(url)
        file_name = f'{clean(label)}'
        open(f'{file_name}.pdf', 'wb').write(pdf.content)

