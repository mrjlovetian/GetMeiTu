# -*- coding: utf-8 -*-
import scrapy
from GetMeiTu.items  import GetmeituItem

#//div[@class="bg1 border post"]//img/@src

class MeituSpider(scrapy.Spider):
    name = 'meitu'
    # allowed_domains = ['http://www.btbtt.net/']
    offset = 1
    meitu_domin = "http://www.btbtt.net/"
    start_url = meitu_domin + "forum-index-fid-957-page-" + str(offset) + ".htm"
    start_urls = [start_url]

# //a[@class="subject_link thread-old" or @class="subject_link thread-new"]/@href

    def parse(self, response):


        results = response.xpath('//a[@class="subject_link thread-old" or @class="subject_link thread-new"]/@href').extract()
        image_results = response.xpath('//div[@class="bg1 border post"]//img/@src').extract()
        if len(results) > 0:
            for xm in results:
                image_url = self.meitu_domin + xm
                print("-=-=-=-=-=-=-", image_url)
                yield scrapy.Request(image_url, callback=self.parse)

            self.offset += 1
            next_url = self.meitu_domin + "forum-index-fid-957-page-" + str(self.offset) + ".htm"
            yield scrapy.Request(next_url, callback=self.parse)


        if len(image_results) > 0:
            for image_url in image_results:
                print('********************', image_url)
                item = GetmeituItem()
                item['image_url'] = image_url
                yield item
