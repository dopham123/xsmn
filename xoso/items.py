# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class XosoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Tây_Ninh = scrapy.Field()
    An_Giang = scrapy.Field()
    Bình_Thuận = scrapy.Field()
    pass

class GiaiItem(scrapy.Item):
    Mã_Tỉnh = scrapy.Field()
    Tên_Tỉnh = scrapy.Field()
    Giải_Tám = scrapy.Field()
    Giải_Bảy = scrapy.Field()
    Giải_Sáu = scrapy.Field()
    Giải_Năm = scrapy.Field()
    Giải_Tư = scrapy.Field()
    Giải_Ba = scrapy.Field()
    Giải_Nhì = scrapy.Field()
    Giải_Nhất = scrapy.Field()
    Giải_Đặc_Biệt = scrapy.Field()
