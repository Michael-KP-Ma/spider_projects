import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import XiamaiItem
from selenium import webdriver
import json
import re



class XiamaiSpiderSpider(CrawlSpider):
    name = 'xiamai_spider'
    allowed_domains = ['xiamai.net']
    start_urls = ['https://xiamai.net/index.php?r=nine&n_id=2&nine_tab=1&page=1']

    browser = webdriver.Chrome()

    rules = (
        Rule(LinkExtractor(allow=r'.*?index\.php\?r=nine&n_id=2&nine_tab=1&page=\d+'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        data_str = re.findall(r'lsitData=(\[{.*?}\]);', response.text)[0]
        datas = json.loads(data_str)

        for data in datas:
            item = XiamaiItem()
            item['id'] = data['id']
            product_url = f'https://xiamai.net/index.php?r=l/d&u=1635713&id={item["id"]}&from=undefined'
            print('product_url: ', product_url)
            yield scrapy.Request(product_url, callback=self.parse_detail, meta={'item': item})


    def parse_detail(self, response):
        item = response.meta['item']
        print('item: ', item)

        item['title'] = response.xpath('//span[@class="title"]/text()').extract_first()
        price = response.xpath('//div[@class="price"]/text()|//div[@class="price"]/i/text()').extract()
        item['price'] = ''.join(price).strip()
        item['pub_time'] = response.xpath('//span[@class="time"]/text()').extract_first()
        item['discount'] = response.xpath('//span[@class="quan"]/text()').extract_first()
        desc = response.xpath('//div[@class="rec-text"]//text()').extract()
        item['description'] = ''.join(desc).strip()
        item['item_url'] = response.url

        yield item

    def closed(self, spider):
        self.browser.quit()
