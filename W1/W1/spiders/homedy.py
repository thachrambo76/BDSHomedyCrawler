import scrapy
from W1.items import W1Item

class HomedySpider(scrapy.Spider):
    name = "homedy"
    allowed_domains = ["homedy.com"]
    start_urls = ["http://homedy.com/"]

    def parse(self, response):
        titles = response.xpath('//div[contains(@class, "p-item border-radius-5px color-blue")]')
        # if not matches:
        #     matches = response.xpath('//div[@class="f-row matchdetail"]')
        for title in titles:
            item = W1Item()
            item["title"] = response.xpath('//span[contains(@class, "hoz-box-title p-info-title")]/text()').get()
            item["fee"] = response.xpath('//span[contains(@class, "info-price")]/text()').get()
            item["location"] = response.xpath('//span[contains(@class, "hoz-box-address p-info-address")]/text()').get()
            item["author"] = response.xpath('//span[contains(@class, "fullname")]/text()').get()

        yield item


