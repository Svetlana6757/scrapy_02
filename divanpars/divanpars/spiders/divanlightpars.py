import scrapy
import csv

# Настройки для экспорта в CSV
FEED_FORMAT = "csv"
FEED_URI = "divan_light.csv"

# Настройки для порядка полей в CSV
FEED_EXPORT_FIELDS = ["name", "price", "url"]

class DivanlightparsSpider(scrapy.Spider):
    name = "divanlightpars"
    allowed_domains = ["https://divan.ru"]
    start_urls = ["https://www.divan.ru/category/svet"]

    def parse(self, response):
        lis = response.css('div._Ud0k')
        for li in lis:
            yield {
                'name': li.css('div.lsooF span::text').get(),
                'price': li.css('div.pY3d2 span::text').get(),
                'url': li.css('a').attrib['href']
            }
