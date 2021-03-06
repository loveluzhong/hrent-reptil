# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from abc import ABCMeta, abstractmethod


class BaseItem(metaclass=ABCMeta):
    pass


class EsItem(BaseItem):
    @abstractmethod
    def save(self):
        """
        保存数据
        :return:
        """
        pass

class UrlItem(scrapy.Item):
    url = scrapy.Field()

