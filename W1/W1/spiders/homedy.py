import scrapy
from W1.items import W1Item

class HomedySpider(scrapy.Spider):
    name = "homedy"
    allowed_domains = ["homedy.com"]
    start_urls = ["https://homedy.com/"]

    def parse(self, response):
        tables = response.xpath('//div[contains(@class, "p-item border-radius-5px color-blue")]')

        for table in tables:
            item = W1Item()
            item["title"] = table.xpath('.//span[contains(@class, "hoz-box-title p-info-title")]/text()').get()
            item["fee"] = table.xpath('.//span[contains(@class, "info-price")]/text()').get()
            item["location"] = table.xpath('.//span[contains(@class, "hoz-box-address p-info-address")]/text()').get()
            item["author"] = table.xpath('.//span[contains(@class, "fullname")]/text()').get()
            
            detail_url = table.xpath('.//a[contains(@class, "hoz-box-title")]/@href').get()
            
            if detail_url:
                yield response.follow(detail_url, self.parse_detail, meta={'item': item})
            else:
                yield item

    def parse_detail(self, response):
        """Hàm này xử lý trang chi tiết từng bài viết"""
        item = response.meta['item']
        item["description"] = response.xpath('//div[contains(@class, "property-description")]/p/text()').getall()
        item["area"] = response.xpath('//span[contains(@class, "property-area")]/text()').get()
        item["bedrooms"] = response.xpath('//span[contains(@class, "property-bedrooms")]/text()').get()
        item["bathrooms"] = response.xpath('//span[contains(@class, "property-bathrooms")]/text()').get()
        
        yield item
