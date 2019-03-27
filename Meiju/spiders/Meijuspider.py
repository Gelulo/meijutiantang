# -*- coding: utf-8 -*-
import scrapy
from lxml import etree
from Meiju.items import MeijuspiderItme

class MeijuspiderSpider(scrapy.Spider):
    name = 'Meijuspider'
    allowed_domains = ['meijutt.com']
    start_urls = ['https://www.meijutt.com/new100.html']

    def parse(self, response):
        content = etree.HTML(response.body.decode('GBK'))
        movies = content.xpath('//ul[@class="top-list  fn-clear"]/li')
        # print(movies)
        for movie in movies:
            a_list = movie.xpath('./h5/a')
            a = a_list[0].text  #电影名字
            print(a)

            #电影状态
            stats = movie.xpath('.//span[@class="state1 new100state1"]/font')[0].text

            #数据传入item
            item = MeijuspiderItme()
            item['name'] = a
            item['stats'] = stats

            print(item)

            yield item