#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
import math
import time

import sys

from pygame.locals import *

def main():

    pygame.init()

    Reloj= pygame.time.Clock()

    Ventana = pygame.display.set_mode((1024, 768))
    pygame.display.set_caption("Juego carreras")

    Fondo = pygame.image.load("circuit.png")



    Nitro1Imagen=pygame.image.load("fuel.png").convert()
    nitro1Trans=Nitro1Imagen.get_at((0,0))
    Nitro1Imagen.set_colorkey(nitro1Trans)
    coorN1=(150,75)
    Nitro1=Nitro(Nitro1Imagen,coorN1)

    Nitro2Imagen=pygame.image.load("fuel.png").convert()
    nitro2Trans=Nitro2Imagen.get_at((0,0))
    Nitro2Imagen.set_colorkey(nitro2Trans)
    coorN2=(800,100)
    Nitro2=Nitro(Nitro2Imagen,coorN2)

    Nitro3Imagen=pygame.image.load("fuel.png").convert()
    nitro3Trans=Nitro3Imagen.get_at((0,0))
    Nitro3Imagen.set_colorkey(nitro3Trans)
    coorN3=(700,650)
    Nitro3=Nitro(Nitro3Imagen,coorN3)

    Nitro4Imagen=pygame.image.load("fuel.png").convert()
    nitro4Trans=Nitro4Imagen.get_at((0,0))
    Nitro4Imagen.set_colorkey(nitro4Trans)
    coorN4=(600,400)
    Nitro4=Nitro(Nitro4Imagen,coorN4)

    Nitro5Imagen=pygame.image.load("fuel.png").convert()
    nitro5Trans=Nitro5Imagen.get_at((0,0))
    Nitro5Imagen.set_colorkey(nitro5Trans)
    coorN5=(100,600)
    Nitro5=Nitro(Nitro5Imagen,coorN5)

    ImagenCochePrincipal = pygame.image.load("car_red.png").convert()
    transparente = ImagenCochePrincipal.get_at((0, 0))
    ImagenCochePrincipal.set_colorkey(transparente)

    cochePrincipal = Coche((200, 650), ImagenCochePrincipal,0)
    coordenadaX,coordenadaY=cochePrincipal.getCoordenadas()
    direccion=0


    terrenoAsfalto0=Fondo.get_at((150,100))
    terrenoAsfalto1=Fondo.get_at((151,100))
    terrenoAsfalto2=Fondo.get_at((152,100))
    terrenoAsfalto3=Fondo.get_at((153,100))
    terrenoAsfalto4=Fondo.get_at((154,100))
    terrenoAsfalto5=Fondo.get_at((155,100))
    terrenoAsfalto6=Fondo.get_at((156,100))
    terrenoAsfalto7=Fondo.get_at((157,100))
    terrenoAsfalto8=Fondo.get_at((158,100))
    terrenoAsfalto9=Fondo.get_at((159,100))
    terrenoAsfalto10=Fondo.get_at((160,100))
    print terrenoAsfalto0
    print terrenoAsfalto1
    print terrenoAsfalto2
    print terrenoAsfalto3
    print terrenoAsfalto4
    print terrenoAsfalto5
    print terrenoAsfalto6
    print terrenoAsfalto7
    print terrenoAsfalto8
    print terrenoAsfalto9
    print terrenoAsfalto10

    #Muestras terreno asfalto, para despues saber si el coche circula por asfalto
    #(109, 109, 109, 255)
    #(111, 111, 111, 255)
    #(106, 106, 106, 255)
    #(103, 103, 103, 255)
    #(104, 104, 104, 255)
    #(110, 110, 110, 255)
    #(109, 109, 109, 255)
    #(101, 101, 101, 255)
    #(103, 103, 103, 255)
    #(104, 104, 104, 255)
    #(102, 102, 102, 255)

    velocidadMuyRapida=20
    velocidadRapida=8
    velocidadBaja=2

    ##Contador antes de empezar
    contadorComienzo(Ventana,Fondo,cochePrincipal)
    tInicio=time.clock()  #Tiempo en el que se inicia la vuelta

    while True:
    	
        #### AL PASAR POR LINEA DE META SE PARA EL CONTADOR Y SE MUESTRA EL TIEMPO
        if (int(coordenadaX)>180 and int(coordenadaX)<200 and int(coordenadaY)>560):
            tFinal=time.clock()
            tVuelta=tFinal-tInicio
            tVuelta=str(tVuelta)
            
            cochePrincipal = Coche((200, 650), ImagenCochePrincipal,0)
            coordenadaX,coordenadaY=cochePrincipal.getCoordenadas()
            #Mostramos lo que se ha tardado
            Fuente= pygame.font.Font(None, 50)
            Mensaje = Fuente.render("Has tardado "+tVuelta+" segundos", 0, (0,0,0)) 
            #Mostramos menú de opciones
            Mensaje2 = Fuente.render("Repetir -> Espacio, Salir -> Esc", 0, (0,0,0))
            Ventana.blit(Fondo, (0, 0))
            Ventana.blit(Nitro1.image, Nitro1.rect)
            Ventana.blit(Nitro2.image, Nitro2.rect)
            Ventana.blit(Nitro3.image, Nitro3.rect)
            Ventana.blit(Nitro4.image, Nitro4.rect)
            Ventana.blit(Nitro5.image, Nitro5.rect)
            Ventana.blit(cochePrincipal.image, cochePrincipal.rect)
            Ventana.blit(Mensaje, (160, 80))  
            Ventana.blit(Mensaje2, (160, 120)) 
            pygame.display.flip() 
            

            accionCaptada=0
            while accionCaptada==0:
                for evento in pygame.event.get():
                    if evento.type == pygame.KEYDOWN:
                        if evento.key == pygame.K_SPACE:
                            tInicio=time.clock()
                            accionCaptada=1
                        if evento.key == pygame.K_ESCAPE:
                            sys.exit()
                            accionCaptada=2
                if evento.type == pygame.QUIT:
                    sys.exit()
                    accionCaptada=2
                pass
            #Captamos si quiere repetir o salir
            
            
            if accionCaptada==1:
                ##Volvemos a mostrar el tiempo que queda y se inicia de nuevo
                contadorComienzo(Ventana,Fondo,cochePrincipal)
                tInicio=time.clock()  #Tiempo en el que se inicia la vuelta
                pass


            Ventana.blit(Fondo, (0, 0))
            Ventana.blit(cochePrincipal.image, cochePrincipal.rect)
            Ventana.blit(Mensaje, (160, 100))  
            pygame.display.flip() 
            

        cochePrincipal.update((coordenadaX,coordenadaY))
        Ventana.blit(Fondo, (0, 0))
        Ventana.blit(Nitro1.image, Nitro1.rect)
        Ventana.blit(Nitro2.image, Nitro2.rect)
        Ventana.blit(Nitro3.image, Nitro3.rect)
        Ventana.blit(Nitro4.image, Nitro4.rect)
        Ventana.blit(Nitro5.image, Nitro5.rect)
        Ventana.blit(cochePrincipal.image, cochePrincipal.rect)

        pygame.display.flip()

        keyState=pygame.key.get_pressed()

        (a,b,c,d)=Fondo.get_at((cochePrincipal.getCoordenadas()))
        
        #Aunque hemos tomado más medidas, solo con este atributo detecta si esta en el asfalto de una manera correcta
        

        if (a>100 and (pygame.sprite.collide_rect(cochePrincipal,Nitro1) or pygame.sprite.collide_rect(cochePrincipal,Nitro2) or pygame.sprite.collide_rect(cochePrincipal,Nitro3) or pygame.sprite.collide_rect(cochePrincipal,Nitro4) or pygame.sprite.collide_rect(cochePrincipal,Nitro5))):
            velocidad=velocidadMuyRapida
            pass
        elif (a>100 and (pygame.sprite.collide_rect(cochePrincipal,Nitro1)==False and pygame.sprite.collide_rect(cochePrincipal,Nitro2)==False and pygame.sprite.collide_rect(cochePrincipal,Nitro3)==False and pygame.sprite.collide_rect(cochePrincipal,Nitro4)==False and pygame.sprite.collide_rect(cochePrincipal,Nitro5)==False)):
            velocidad=velocidadRapida
            pass
        else:
            velocidad=velocidadBaja
               
        if keyState[pygame.K_UP]:
            direccion=cochePrincipal.getDireccion()
            coordenadaX, coordenadaY=cochePrincipal.getCoordenadas()
            #Pasamos la direccion a radianes
            direccionRad=(direccion*math.pi)/180
            coordenadaX=coordenadaX+velocidad*math.cos(direccionRad)
            coordenadaY=coordenadaY+velocidad*math.sin(direccionRad)
            pass

        if keyState[pygame.K_RIGHT]:
            cochePrincipal.incDirDerecha()

        if keyState[pygame.K_LEFT]:
            cochePrincipal.incDirIzquierda()

        if keyState[pygame.K_DOWN]:
            direccion=cochePrincipal.getDireccion()
            coordenadaX, coordenadaY=cochePrincipal.getCoordenadas()
            #Pasamos la direccion a radianes
            direccionRad=(direccion*math.pi)/180
            coordenadaX=coordenadaX-velocidad*math.cos(direccionRad)
            coordenadaY=coordenadaY-velocidad*math.sin(direccionRad)
            pass
            pass


        for evento in pygame.event.get():
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    sys.exit()

            if evento.type == pygame.QUIT:
                sys.exit()



        #Reloj.tick(200)
def contadorComienzo(Ventana,Fondo,cochePrincipal):
        # Elegimos la fuente y el tamaño
    Fuente= pygame.font.Font(None, 50)    

    t0=time.clock()
    while (time.clock()-t0<1):
        
        Mensaje = Fuente.render("Cuenta atras para comenzar: 5 segundos ", 0, (0,0,0)) 
        Ventana.blit(Fondo, (0, 0))
        Ventana.blit(cochePrincipal.image, cochePrincipal.rect)
        Ventana.blit(Mensaje, (160, 100))
        pygame.display.flip()
    
        pass
    t0=time.clock()
    while (time.clock()-t0<1):
        
        Mensaje = Fuente.render("Cuenta atras para comenzar: 4 segundos ", 0, (0,0,0)) 
        Ventana.blit(Fondo, (0, 0))
        Ventana.blit(cochePrincipal.image, cochePrincipal.rect)
        Ventana.blit(Mensaje, (160, 100))
        pygame.display.flip()
    
        pass
    t0=time.clock()
    while (time.clock()-t0<1):
        
        Mensaje = Fuente.render("Cuenta atras para comenzar: 3 segundos ", 0, (0,0,0)) 
        Ventana.blit(Fondo, (0, 0))
        Ventana.blit(cochePrincipal.image, cochePrincipal.rect)
        Ventana.blit(Mensaje, (160, 100))
        pygame.display.flip()
    
        pass
    t0=time.clock()
    while (time.clock()-t0<1):
        
        Mensaje = Fuente.render("Cuenta atras para comenzar: 2 segundos ", 0, (0,0,0)) 
        Ventana.blit(Fondo, (0, 0))
        Ventana.blit(cochePrincipal.image, cochePrincipal.rect)
        Ventana.blit(Mensaje, (160, 100))
        pygame.display.flip()
    
        pass
    
    t0=time.clock()
    while (time.clock()-t0<1):
        
        Mensaje = Fuente.render("Cuenta atras para comenzar: 1 segundos ", 0, (0,0,0)) 
        Ventana.blit(Fondo, (0, 0))
        Ventana.blit(cochePrincipal.image, cochePrincipal.rect)
        Ventana.blit(Mensaje, (160, 100))
        pygame.display.flip()
    
        pass

    Mensaje = Fuente.render("YA!!", 0, (0,0,0)) 
    Ventana.blit(Fondo, (0, 0))
    Ventana.blit(cochePrincipal.image, cochePrincipal.rect)
    Ventana.blit(Mensaje, (160, 100))
    pygame.display.flip()
    pass

class Coche(pygame.sprite.Sprite):

    def __init__(self, coordenadas, imagen,direccion):
        pygame.sprite.Sprite.__init__(self)
    	
        self.coordenadas=coordenadas
    	self.direccion=direccion
        self.ImgCompleta = imagen
        self.actualizado = pygame.time.get_ticks()
        ##La direccion se medirá en grados, comenzando en 0º, hacia la derecha.
        #El movimiento se produce hacia dicha direccion
        self.image = imagen
        self.rect = self.image.get_rect()
        self.rect.center = coordenadas


    def update(self, nuevas_coordenadas):
        self.rect.center = nuevas_coordenadas
        self.coordenadas=nuevas_coordenadas
        self.actualizado= pygame.time.get_ticks()
        

    def incDirDerecha(self):
        self.direccion=self.direccion+7
        
        self.image=pygame.transform.rotate(self.ImgCompleta,-self.direccion)
        if self.direccion==360:
            self.direccion=0
            pass
    def incDirIzquierda(self):
        self.direccion=self.direccion-7
        self.image=pygame.transform.rotate(self.ImgCompleta,-self.direccion)

        if self.direccion==-360:
            self.direccion=0
            pass
    def getDireccion(self):
        return self.direccion
    def getCoordenadas(self):
        cx,cy=self.coordenadas
        cx=int(cx)
        cy=int(cy)
        return (cx,cy)

class Nitro(pygame.sprite.Sprite):

    def __init__(self, imagen,coordenadas):
        self.coordenadas=coordenadas
        pygame.sprite.Sprite.__init__(self)
        self.ImgCompleta = imagen
        self.actualizado = pygame.time.get_ticks()
        ##La direccion se medirá en grados, comenzando en 0º, hacia la derecha.
        #El movimiento se produce hacia dicha direccion
        
        self.image = imagen
        self.rect = self.image.get_rect()
        self.rect.center = coordenadas



main()