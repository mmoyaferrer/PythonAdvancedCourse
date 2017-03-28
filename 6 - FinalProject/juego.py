#!/usr/bin/env python
# -*- coding: utf-8 -*-
from gi.repository import Gtk, GObject
import pygame
import MySQLdb
import time
import sys

from pygame.locals import *
from random import randint


#################################
#################################
###    MANUEL MOYA FERRER     ###
#################################
#################################


class Nave(pygame.sprite.Sprite):

    def __init__(self, coordenadas, imagen, vidasNave):
    	
    	self.coordenadas=coordenadas
        pygame.sprite.Sprite.__init__(self)
        
        self.ImgCompleta = imagen
        self.actualizado = pygame.time.get_ticks()

        self.image = self.ImgCompleta.subsurface((275,620,350-275,700-620))
        transparente = self.image.get_at((0, 0))
        self.image.set_colorkey(transparente)

        self.rect = self.image.get_rect()
        self.rect.center = coordenadas
        self.vidasNave=vidasNave


    def update(self, nuevas_coordenadas):

        self.rect.center = nuevas_coordenadas
        self.coordenadas=nuevas_coordenadas

        self.actualizado= pygame.time.get_ticks()

    def getCoordenadas(self):
    	return self.coordenadas

    def getVidas(self):
   		return self.vidasNave

class Misil(pygame.sprite.Sprite):

    def __init__(self, coordenadas, imagen):
    	
    	self.coordenadas=coordenadas
        pygame.sprite.Sprite.__init__(self)
        
        self.ImgCompleta = imagen
        self.actualizado = pygame.time.get_ticks()

        self.image = self.ImgCompleta.subsurface((295,665,300-295,690-665))
        transparente = self.image.get_at((0, 0))
        self.image.set_colorkey(transparente)

        self.rect = self.image.get_rect()
        self.rect.center = coordenadas


    def update(self, nuevas_coordenadas):

        self.rect.center = nuevas_coordenadas
        self.coordenadas=nuevas_coordenadas

        self.actualizado= pygame.time.get_ticks()

    def getCoordenadas(self):
    	return self.coordenadas

class SoldadoImperial(pygame.sprite.Sprite):

    def __init__(self, coordenadas, imagen):
    	
    	self.coordenadas=coordenadas
        pygame.sprite.Sprite.__init__(self)
        
        self.ImgCompleta = imagen
        self.actualizado = pygame.time.get_ticks()

        self.image = self.ImgCompleta.subsurface((50,380,100-50,430-380))
        transparente = self.image.get_at((0, 0))
        self.image.set_colorkey(transparente)

        self.rect = self.image.get_rect()
        self.rect.center = coordenadas

        self.vidas=1


    def update(self, nuevas_coordenadas):

        self.rect.center = nuevas_coordenadas
        self.coordenadas=nuevas_coordenadas

        self.actualizado= pygame.time.get_ticks()

    def getCoordenadas(self):
    	return self.coordenadas

    def getVidas(self):
    	return self.vidas

class menuGUI:

	
	def __init__(self):

		##POR DEFECTO Y SI NO SE CAMBIA
		self.tasaGeneracionSoldadosImperialesBaja=3
		self.tasaGeneracionSoldadosImperialesMedia=2
		self.tasaGeneracionSoldadosImperialesAlta=1
		self.tasaGeneracionSoldadosImperialesMuyAlta=1



		self.builder=Gtk.Builder()
		self.builder.add_from_file("guiGladeStarsWarsInvaders.glade")
		self.handlers={"onDeleteWindow":Gtk.main_quit,
				        "onIniciarJuego":self.onIniciarJuego,
				        "difBaja":self.difBaja,
				        "difMedia":self.difMedia,
				        "difAlta":self.difAlta,
				        "onAcercaDe":self.onAcercaDe,
				        "guardarPuntuacion":self.guardarPuntuacion,
				        "obtenerPuntuaciones":self.obtenerPuntuaciones
					       	}
		self.builder.connect_signals(self.handlers)

		self.window=self.builder.get_object("window1")
		self.window.show_all()


		

		self.about=self.builder.get_object("aboutdialog")




		tTotal=0


	def onIniciarJuego(self,menuitem):
		self.bucleJuego()
		pass

	def difBaja(self,menuitem):
		self.tasaGeneracionSoldadosImperialesBaja=5
		self.tasaGeneracionSoldadosImperialesMedia=4
		self.tasaGeneracionSoldadosImperialesAlta=3
		self.tasaGeneracionSoldadosImperialesMuyAlta=2
		print "Dificultad Baja"
		pass
	def difMedia(self,menuitem):
		self.tasaGeneracionSoldadosImperialesBaja=3
		self.tasaGeneracionSoldadosImperialesMedia=2
		self.tasaGeneracionSoldadosImperialesAlta=1
		self.tasaGeneracionSoldadosImperialesMuyAlta=1
		print "Dificultad Media"
		pass
	def difAlta(self,menuitem):
		self.tasaGeneracionSoldadosImperialesBaja=1
		self.tasaGeneracionSoldadosImperialesMedia=0.5
		self.tasaGeneracionSoldadosImperialesAlta=0.5
		self.tasaGeneracionSoldadosImperialesMuyAlta=0.5
		print "Dificultad Alta"
		pass

	def onAcercaDe(self,menuitem):
		self.about.show()
		pass

	def guardarPuntuacion(self,menuitem):
		global tTotal
		entryNombre=self.builder.get_object("entryNombre")
		nombre=entryNombre.get_text()
		
		self.Conexion = MySQLdb.connect(host='localhost', user='manuel',passwd='moya', db='DBSWSI')
		#Creamos el cursor
		self.micursor = self.Conexion.cursor(MySQLdb.cursors.DictCursor)
		self.Conexion.commit()

		print "guardarPuntuacion"
		

		query= "INSERT INTO Ranking (Nombre,Puntuacion) VALUES (%s,%s);"%("\""+nombre+"\"","\""+(str(tTotal))[:5]+"\"")
		self.micursor.execute(query)
		self.Conexion.commit()

	def obtenerPuntuaciones(self,menuitem):
		# Establecemos la conexión
		
		self.Conexion = MySQLdb.connect(host='localhost', user='manuel',passwd='moya', db='DBSWSI')
		#Creamos el cursor
		self.micursor = self.Conexion.cursor(MySQLdb.cursors.DictCursor)
		self.Conexion.commit()

		print "obtenerPuntuaciones"
		#Creamos el cursor
		query= "SELECT * FROM Ranking WHERE 1;"
		self.micursor.execute(query)
		self.Conexion.commit()

		registros= self.micursor.fetchall()
		
		puntuaciones=""
		for registro in registros:
			puntuaciones = puntuaciones + registro["Nombre"] + ": " + registro["Puntuacion"] + ", "
			pass

		entryPuntuaciones=self.builder.get_object("entryPuntuaciones")
		entryPuntuaciones.set_text(puntuaciones)

		print registro

	def bucleJuego(self):

		global tTotal


		pygame.init()
		Reloj= pygame.time.Clock()

		Ventana = pygame.display.set_mode((600, 700))
		pygame.display.set_caption("Stars War Invaders")

		Fondo = pygame.image.load("fondo.png")

		Imagen = pygame.image.load("SWSI.png").convert()
		transparente = Imagen.get_at((0, 0))
		Imagen.set_colorkey(transparente)

		vidasNave=3
		misiles=[]
		soldados=[]
		velocidadSoldados=2

		tG=self.tasaGeneracionSoldadosImperialesBaja

		nave = Nave((300, 640), Imagen,3)
		coordenadaX,coordenadaY=nave.coordenadas
		direccion=3

		t0=time.clock()
		tTotal=0

		while True:

			nave.update((coordenadaX,coordenadaY))
			coordenadaX,coordenadaY=nave.getCoordenadas()

			Ventana.blit(Fondo, (0, 0))
			Ventana.blit(nave.image, nave.rect)
			pygame.display.flip()

			##CAPTURA DE TECLADO#################
			keyState=pygame.key.get_pressed()

			if keyState[pygame.K_UP]:
				coordenadaX, coordenadaY=nave.getCoordenadas()
				if coordenadaY>50:
					coordenadaY=coordenadaY-5
				
			if keyState[pygame.K_RIGHT]:
				coordenadaX, coordenadaY=nave.getCoordenadas()
				if coordenadaX<565:
					coordenadaX=coordenadaX+5

			if keyState[pygame.K_LEFT]:
				coordenadaX, coordenadaY=nave.getCoordenadas()
				if coordenadaX>35:
					coordenadaX=coordenadaX-5

			if keyState[pygame.K_DOWN]:
				coordenadaX, coordenadaY=nave.getCoordenadas()
				if coordenadaY<650:
					coordenadaY=coordenadaY+5

			for evento in pygame.event.get():
				if evento.type == pygame.KEYDOWN:
					if evento.key == pygame.K_ESCAPE:
						pygame.display.quit()
						pygame.quit()
					if evento.key == pygame.K_SPACE:
						misiles.append(Misil(nave.getCoordenadas(),Imagen))
						pass

			if evento.type == pygame.QUIT:
				pygame.display.quit()
				pygame.quit()


			##ACTUALICACION DE LOS MISILES
			if len(misiles)>0:
				for misil in misiles:
					coordenadaXMisil,coordenadaYMisil=misil.getCoordenadas()
					coordenadaYMisil=coordenadaYMisil-10
					
					if coordenadaYMisil<0:
						misiles.remove(misil)
						pass
					else:
						misil.update((coordenadaXMisil,coordenadaYMisil))
						Ventana.blit(misil.image,misil.rect)
						pygame.display.flip()
					pass
			pass

			##GENERACION, ACTUALIZACION DE LOS SOLDADOS IMPERIALES Y COLISIONES
			if ((time.clock()-t0)>tG):
				tTotal=tTotal+time.clock()-t0
				t0=time.clock()
				cxRandom=randint(50,550)
				soldados.append(SoldadoImperial((cxRandom,50),Imagen))
				pass

			if tTotal>5 and tTotal<15:
				tG=self.tasaGeneracionSoldadosImperialesMedia
				
			if tTotal>15 and tTotal<30:
				tG=self.tasaGeneracionSoldadosImperialesAlta
				velocidadSoldados=3

			if tTotal>30 and tTotal<45:
				velocidadSoldados=4
			if tTotal>45 and tTotal<60:
				velocidadSoldados=5
			if tTotal>60:
				tG=self.tasaGeneracionSoldadosImperialesMuyAlta
				velocidadSoldados=7

			if len(soldados)>0:
				#misil.update((coordenadaXMisil,coordenadaYMisil))
				for soldado in soldados:
					cXsoldado,cYsoldado=soldado.getCoordenadas()
					cYsoldado=cYsoldado+velocidadSoldados
					soldado.update((cXsoldado,cYsoldado))
					Ventana.blit(soldado.image,soldado.rect)
					

					if cYsoldado>700:
						soldados.remove(soldado)
						vNave=nave.getVidas()
						nave.vidasNave=vNave-1
						pass
					if soldado.getVidas()==0:
						soldados.remove(soldado)

					for misil in misiles:

						if pygame.sprite.collide_rect(soldado,misil):
							v=soldado.getVidas()
							soldado.vidas=v-1
							pass

					pass


				

			##mMOSTRAMOS VIDAS

			if nave.getVidas()==3:
				Fuente= pygame.font.Font(None, 50)  
				Mensaje = Fuente.render("Vidas: 3", 0, (255,255,255)) 
				Ventana.blit(Mensaje, (450, 10))
				pygame.display.flip()
				pass
			if nave.getVidas()==2:
				Fuente= pygame.font.Font(None, 50)  
				Mensaje = Fuente.render("Vidas: 2", 0, (255,255,255)) 
				Ventana.blit(Mensaje, (450, 10))
				pygame.display.flip()
				pass
			if nave.getVidas()==1:
				Fuente= pygame.font.Font(None, 50)  
				Mensaje = Fuente.render("Vidas: 1", 0, (255,255,255)) 
				Ventana.blit(Mensaje, (450, 10))
				pygame.display.flip()
				pass

			if (nave.getVidas()==0):
				Fuente= pygame.font.Font(None, 30)  
				tiempoString=str(tTotal)
				tiempoString=tiempoString[:5]
				Mensaje = Fuente.render("GAME OVER, TIEMPO: "+tiempoString+" SEGUNDOS", 0, (255,255,255)) 
				Ventana.blit(Mensaje, (110, 100))
				pygame.display.flip()
				time.sleep(3)
				pygame.display.quit()
				pygame.quit()



menu=menuGUI()
Gtk.main()
