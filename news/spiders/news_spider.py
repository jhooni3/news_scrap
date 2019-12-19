# -*- coding: utf-8 -*-
import scrapy


class NewsSpiderSpider(scrapy.Spider):
    name = 'news_spider'
    allowed_domains = ['www.daum.net']

    def start_requests(self):
        start_urls = [
            'https://search.daum.net/search?w=news&q=%ED%95%98%EC%9D%B4%EB%8B%89%EC%8A%A4&sd=20191201000000&ed=20191219235959'
            #'https://search.daum.net/search?nil_suggest=btn&w=news&DA=STC&cluster=y&q=%ED%95%98%EC%9D%B4%EB%8B%89%EC%8A%A4&period=d&sd=20191218234913&ed=20191219234913'
            ]
        for url in start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for link in response.xpath('//*[@id="clusterResultUL"]/li/div[2]/div/span[1]/a/@href').extract():
            print(link)
#//*[@id="clusterResultUL"]/li[1]/div[2]/div/div[2]/dl/dd[1]/span[2]/a
#//*[@id="clusterResultUL"]/li[2]/div[2]/div/span[1]/a
#//*[@id="clusterResultUL"]/li[1]/div[2]/div/span[1]/a

#//*[@id="clusterResultUL"]/li[1]/div[2]/div/span[1]/a
#//*[@id="clusterResultUL"]/li[4]/div[2]/div/span[1]/a
#//*[@id="clusterResultUL"]/li[1]/div[2]/div/span[1]/a
#//*[@id="clusterResultUL"]/li[5]/div[2]/div/span[1]/a