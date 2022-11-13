import scrapy


class PrecisionsSpider(scrapy.Spider):
    name = 'precisions'
    allowed_domains = ['monumentum.fr']
    start_urls = ['http://monumentum.fr/']

    def parse(self, response):
        pass
