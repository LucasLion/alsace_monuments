import scrapy


class SpiderSpider(scrapy.Spider):
    name = 'spider'
    allowed_domains = ['monumentum.fr']
    start_urls = ['http://monumentum.fr/']

    def parse(self, response):
        pass
