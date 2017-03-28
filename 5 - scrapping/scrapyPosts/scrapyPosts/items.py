# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapypostsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    title = Field()
    autor = Field()
    contenido = Field()
    listaDeCategorias = Field()
    listaDeEtiquetas = Field()
    link = Field()


    pass
