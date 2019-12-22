# -*- coding: utf-8 -*-
import scrapy
from urllib import parse
from news.items import NewsItem
import time
class NewsSpiderSpider(scrapy.Spider):
    name = 'news_spider'
    #allowed_domains = ['www.daum.net']
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
            maxpage = 10
            for page in range(1, maxpage+1):
                crawl_url = url + "&q=" + parse.quote(query) + "&sd=" + s_date + "000000" + "&ed=" + e_date + "235959" + "&p=" + str(page)
                yield scrapy.Request(url=crawl_url, callback=self.parse_link)
            #time.sleep(5)

    def parse_link(self, response):

        print('parse_link >>' + '*' * 100)
        for link in response.xpath('//*[@id="clusterResultUL"]/li/div[2]/div/span[1]/a/@href').extract():
            print(link)
            yield scrapy.Request(url=link, callback=self.parse_news)

        # print('출력전')
        # print(response.xpath('//*[@id="resultCntArea"]/text()').extract())
        # for next_page in response.xpath('//*[@id="newsColl"]/div[4]/span/span[3]/a/@href').extract():
        #     print('넥스트!!! >> ' + next_page)
            # if next_page is not None:
            #     next_page = response.urljoin(next_page)
            #     yield scrapy.Request(url=next_page, callback=self.parse_news)

    def parse_news(self, response):
        item = NewsItem()
        print('parse_news >>' + '*' * 100)
        #제목 //*[@id="cSub"]/div/h3
        item['title'] = response.xpath('//*[@id="cSub"]/div/h3/text()').extract()[0]
        #print(response.xpath('//*[@id="cSub"]/div[1]/h3/text()').extract()[0])
        #내용 //*[@id="harmonyContainer"]
        item['article'] = response.xpath('//*[@id="harmonyContainer"]/section/p[contains(@dmcf-ptype, "general")]/text()').extract()
        #print(response.xpath('//*[@id="harmonyContainer"]/section/p[contains(@dmcf-ptype, "general")]/text()').extract())

        item['date'] = response.xpath('/html/head/meta[contains(@property, "og:regDate")]/@content').extract()[0][:8]

        yield item


#//*[@id="clusterResultUL"]/li[1]/div[2]/div/div[2]/dl/dd[1]/span[2]/a
#//*[@id="clusterResultUL"]/li[2]/div[2]/div/span[1]/a
#//*[@id="clusterResultUL"]/li[1]/div[2]/div/span[1]/a

#//*[@id="clusterResultUL"]/li[1]/div[2]/div/span[1]/a
#//*[@id="clusterResultUL"]/li[4]/div[2]/div/span[1]/a
#//*[@id="clusterResultUL"]/li[1]/div[2]/div/span[1]/a
#//*[@id="clusterResultUL"]/li[5]/div[2]/div/span[1]/a

#//*[@id="cSub"]/div/span/span
# //*[@id="resultCntArea"]

#//*[@id="newsColl"]/div[4]/span/span[3]/a
# //*[@id="newsColl"]/div[4]/span/span[3]/a
# //*[@id="newsColl"]/div[4]/span/span[3]/a
##newsColl > div.paging_comm > span > span:nth-child(3) > a
##newsColl > div.paging_comm > span > span:nth-child(2) > em
#document.querySelector("#newsColl > div.paging_comm > span > span:nth-child(3) > a")


