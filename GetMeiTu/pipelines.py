# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
from scrapy.pipelines.images import ImagesPipeline

class GetmeituPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        return scrapy.Request(item['image_url'])




#KKAPIResponseHandler successHandler: