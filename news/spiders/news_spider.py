# -*- coding: utf-8 -*-
import scrapy
from urllib import parse

class NewsSpiderSpider(scrapy.Spider):
    name = 'news_spider'
    allowed_domains = ['www.daum.net']

    def start_requests(self):
        start_urls = [
            'https://search.daum.net/search?w=news'
            #'https://search.daum.net/search?nil_suggest=btn&w=news&DA=STC&cluster=y&q=%ED%95%98%EC%9D%B4%EB%8B%89%EC%8A%A4&period=d&sd=20191218234913&ed=20191219234913'
            ]
        for url in start_urls:
            #maxpage = input("최대 출력할 페이지수 입력하시오: ")
            #query = input("검색어 입력: ")
            #s_date = input("시작날짜 입력(20190101):")  # 2019.01.01
            #e_date = input("끝날짜 입력(20190428):")  # 2019.04.28
            query = "삼성전자"
            s_date = '20190101'
            e_date = '20191231'
            url += "&q=" + parse.quote(query) + "&sd=" + s_date + "000000" + "&ed=" + e_date + "235959"
            yield scrapy.Request(url=url, callback=self.parse_link)

    def parse_link(self, response):
        for link in response.xpath('//*[@id="clusterResultUL"]/li/div[2]/div/span[1]/a/@href').extract():
            print(link)
            yield scrapy.Request(url=link, callback=self.parse_news)

    def parse_news(self, response):
        print('*' * 100)
        #제목 //*[@id="cSub"]/div/h3
        print(response.xpath('//*[@id="cSub"]/div/h3').extract())
        #내용 //*[@id="harmonyContainer"]
        print(response.xpath('//*[@id="harmonyContainer"]').extract())


#//*[@id="clusterResultUL"]/li[1]/div[2]/div/div[2]/dl/dd[1]/span[2]/a
#//*[@id="clusterResultUL"]/li[2]/div[2]/div/span[1]/a
#//*[@id="clusterResultUL"]/li[1]/div[2]/div/span[1]/a

#//*[@id="clusterResultUL"]/li[1]/div[2]/div/span[1]/a
#//*[@id="clusterResultUL"]/li[4]/div[2]/div/span[1]/a
#//*[@id="clusterResultUL"]/li[1]/div[2]/div/span[1]/a
#//*[@id="clusterResultUL"]/li[5]/div[2]/div/span[1]/a