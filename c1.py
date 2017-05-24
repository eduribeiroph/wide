# -*- coding: utf-8 -*-
import scrapy


class C1Spider(scrapy.Spider):
    name = "c1"
    allowed_domains = ["http://www.comprasnasantaifigenia.com.br"]
    start_urls = ['http://www.comprasnasantaifigenia.com.br/interna.asp?depto=cartuchos/']

    def parse(self, response):
        divs = response.xpath("/html/body/div[1]/div[2]/div[2]/div[1]/div")
        for div in divs:
            title = div.xpath('.//h5/strong/text()').extract_first()
            yield{
                'title' : title,
            }