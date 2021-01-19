import re
from re import Match
from typing import Tuple

import scrapy
from scrapy import Request
from scrapy.http import Response

from scrapydemo.items import ScrapydemoItem


class QsbkSpider(scrapy.Spider):
    name = 'qsbk'
    # allowed_domains = ['qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/text/page/1/']

    @staticmethod
    def data_clean(data: str) -> str:
        return re.sub('\n', '', data)

    def parse(self, response: Response):
        # 找到一页上所有文章
        articles = response.xpath("//div[starts-with(@class, 'article')]")

        for article in articles:
            author = article.xpath('.//div[@class="author clearfix"]//h2/text()').get('')
            content = article.xpath('.//div[@class="content"]/span[1]').xpath('string(.)').get('')
            data = {
                'author': self.data_clean(author),
                'content': self.data_clean(content)
            }
            item = ScrapydemoItem(**data)
            yield item
        has_next_page, next_page_url = self.get_next_page(response)
        if has_next_page:
            yield Request(url=next_page_url, callback=self.parse)

    def get_next_page(self, response: Response) -> Tuple[bool, str]:
        # 判断是否有下一页
        next_page = response.xpath('//span[@class="next"]').get('')
        if not next_page:
            return False, ''
        current_url = response.url
        next_page = re.sub(r'\d+', self.re_callback, current_url)
        return True, next_page

    @staticmethod
    def re_callback(data: Match) -> str:
        return str(int(data.group()) + 1)
