# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json

from scrapydemo.items import ScrapydemoItem


class ScrapydemoPipeline:

    def __init__(self) -> None:
        super().__init__()
        print('打开文件')
        self.json_file = open('data.json', 'a', encoding='utf-8')
        self.json_file.write('[')

    def process_item(self, item: ScrapydemoItem, spider):
        # print('process_item()被执行了')
        # print(item)
        json.dump(dict(item), self.json_file, ensure_ascii=False)
        self.json_file.write(',\n')
        return item

    def close_spider(self, spider):
        print('关闭文件')
        self.json_file.write(']')
        if self.json_file:
            self.json_file.close()
