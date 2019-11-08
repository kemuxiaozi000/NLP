# -*- coding: utf-8 -*-
from urllib import parse

import scrapy


class LiyiSpider(scrapy.Spider):
    name = 'liyi'
    allowed_domains = ['tieba.baidu.com']
    start_urls = ['https://tieba.baidu.com/f?ie=utf-8&kw=%E6%9D%8E%E6%AF%85']

    def parse(self, response):
        data = response.css(".j_th_tit::attr(href)").extract()
        for url in data:
            print(url)
            yield scrapy.Request(url=parse.urljoin(response.url, url), callback=self.parse_detail)

    def parse_detail(self, response):
        # 帖子的主题
        title = response.css(".core_title_txt.pull-left.text-overflow::text").extract()
        # 作者们
        author = response.css(".p_author_name.j_user_card::text").extract()
        # 帖子回复的内容，需要进一步处理
        content_list = response.css(".d_post_content.j_d_post_content").extract()
        pass
