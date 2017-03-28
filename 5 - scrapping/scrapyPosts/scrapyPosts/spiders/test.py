from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

class MySpider(BaseSpider):
	name="spyder"
	allowed_domains = ["ugr.es"]
	start_urls = [  "http://osl.ugr.es/2016/06/27/taller-donacion-colegios/"
					"http://osl.ugr.es/2016/06/13/informe-sobre-tasas-de-rendimiento-academico/"
					"http://osl.ugr.es/2016/06/30/informe-de-experiencia-de-usuario-en-open-data-ugr/"
					"http://osl.ugr.es/2016/06/06/entrega-de-premios-del-certamen-de-proyectos-libres-de-la-ugr/"
					
					]

	def parse(self,response):
		hxs=HtmlXPathSelector(response)
		titles=hxs.select("//header")  ##Es un vector con los contenidos de cada bloque html que contiene dicha sentencia
		for titulo in titles:
			title = titulo.select(".//h1/text()").extract()
			link=titulo.select("//a/@href").extract()
			contenido=titulo.select("//p/text()").extract()
			autor=titulo.select("//span//a/text(")
			print "TITULO: "
			print "\n"
			print title
			print "\n"
			print "CONTENIDO: "
			print "\n"
			print contenido
			print "\n"
			print "\n"
			print "AUTOR: "
			print "\n"
			print autor
			print "\n"
		pass