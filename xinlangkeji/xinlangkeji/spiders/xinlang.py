# -*- coding: utf-8 -*-
import scrapy
import re

class XinlangSpider(scrapy.Spider):
    name = 'xinlang'
    allowed_domains = []
    start_urls = ['https://cre.mix.sina.com.cn/api/v3/get?&&cre=tianyi&mod=pctech&statics=1&up=6&top_id=%2CA1u1J%2CA1rkN%2CA1s5b%2CA1mJl%2CA1PbX%2CA1MSP%2CA1fbh%2CA1Rzi%2CA1MWO%2CA1MEd%2C%2C9Eux1%2C%2C&offset=0&ad=%7B%22rotate_count%22%3A100%2C%22platform%22%3A%22pc%22%2C%22channel%22%3A%22tianyi_pctech%22%2C%22page_url%22%3A%22https%3A%2F%2Ftech.sina.com.cn%2F%22%2C%22timestamp%22%3A1543491917683%7D']

    def parse(self, response):
        # print(response.text)
        url_list = re.findall('"url_https":"(.*?)",',response.text,re.S)
        # print(url_list)
        for url in url_list:
            url1 = url.replace('\\','')
            # print(url1)
            yield scrapy.Request(url1,self.info)
    #
    def info(self,response):
        try:
            # 标题
            title = response.xpath('//h1[@class="main-title"]/text()').extract_first().strip()
            # print(title)
            # 时间
            time = response.xpath('//span[@class="date"]/text()').extract_first().strip()
            # 来源
            if response.xpath('//span[@class="source"]/a/text()'):
                laiyuan = response.xpath('//span[@class="source"]/a/text()').extract_first().strip()
            else:
                laiyuan = '来源不明'
            # 关键字
            if response.xpath('//meta[@name="keywords"]/@content'):
                keyword = response.xpath('//meta[@name="keywords"]/@content').extract_first().strip()
            else:
                keyword = '暂无关键字'
            # 导读
            if response.xpath('//meta[@name="description"]/@content'):
                intro = response.xpath('//meta[@name="description"]/@content').extract_first().strip()
            else:
                intro = '暂无导读'
            # 内容
            if response.xpath('//div[@class="article"]/p/text()'):
                content = ''.join(response.xpath('//div[@class="article"]/p/text()').extract()).strip()
            else:
                content = '暂无内容'
            # 作者
            if response.xpath('//meta[@property="article:author"]/@content'):
                author = response.xpath('//meta[@property="article:author"]/@content').extract_first().strip()
            else:
                author = '作者不明'
            # 图片
            if response.xpath('///div[@class="img_wrapper"]/img/@src'):
                pic = response.xpath('//div[@class="img_wrapper"]/img/@src').extract()
            else:
                pic = '暂无内容'
            # print(title,time,laiyuan,keyword,intro,content,author)
        except:
            pass