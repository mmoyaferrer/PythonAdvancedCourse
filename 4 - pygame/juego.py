#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame

import sys

from pygame.locals import *

def main():

    pygame.init()

    Reloj= pygame.time.Clock()

    Ventana = pygame.display.set_mode((600, 400))
    pygame.display.set_caption("Monigotillo animado")

    Fondo = pygame.image.load("fondo.jpg")

    Imagen = pygame.image.load("monigotillo.png")
    transparente = Imagen.get_at((0, 0))
    Imagen.set_colorkey(transparente)



    MiMonigotillo = Monigotillo((300, 200), Imagen,3)
    coordenadaX,coordenadaY=MiMonigotillo.coordenadas
    direccion=3

    while True:
    	
        MiMonigotillo.update((coordenadaX,coordenadaY),direccion)
        coordenadaX,coordenadaY=MiMonigotillo.coordenadas

        Ventana.blit(Fondo, (0, 0))
        Ventana.blit(MiMonigotillo.image, MiMonigotillo.rect)

        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.KEYDOWN:
            	
                if evento.key == pygame.K_RIGHT:
                	coordenadaX=coordenadaX+10
                	direccion=0
                if evento.key == pygame.K_LEFT:
                	coordenadaX=coordenadaX-10
                	direccion=1
                if evento.key == pygame.K_UP:
                	coordenadaY=coordenadaY-10
                	direccion=2
                if evento.key == pygame.K_DOWN:
                	coordenadaY=coordenadaY+10
                	direccion=3
                if evento.key == pygame.K_ESCAPE:
                    sys.exit()
            if evento.type == pygame.QUIT:
                sys.exit()

        Reloj.tick(30)


class Monigotillo(pygame.sprite.Sprite):

    def __init__(self, coordenadas, imagen,direccion):
    	self.coordenadas=coordenadas
    	self.direccion=direccion
        pygame.sprite.Sprite.__init__(self)
        self.vector=[0,1,2,3,1,4,5]
        self.posicionVector=0
        self.ImgCompleta = imagen
        a=0
        self.arrayAnimAbajo=[]
        self.arrayAnimArriba=[]
        self.arrayAnimIzquierda=[]
        self.arrayAnimDerecha=[]
        while self.posicionVector < 7:
            self.arrayAnimDerecha.append(self.ImgCompleta.subsurface(((self.vector[self.posicionVector])*32,160,32,64)))
            self.arrayAnimAbajo.append(self.ImgCompleta.subsurface(((self.vector[self.posicionVector])*32,100,32,64)))
            self.arrayAnimArriba.append(self.ImgCompleta.subsurface(((self.vector[self.posicionVector])*32,30,32,64)))
            self.posicionVector= self.posicionVector + 1
        self.anim=0
        self.posicionVector=0
        self.actualizado = pygame.time.get_ticks()
        self.image = self.arrayAnimDerecha[self.anim]
        self.rect = self.image.get_rect()
        self.rect.center = coordenadas


    def update(self, nuevas_coordenadas, direccion):
        self.rect.center = nuevas_coordenadas
        self.coordenadas=nuevas_coordenadas
        self.direccion=direccion
        print direccion
        if self.actualizado + 100 < pygame.time.get_ticks():
            self.anim= self.anim + 1
            if self.anim > 6:
                self.anim= 0

            if direccion==0:	#derecha
            	self.image = self.arrayAnimDerecha[self.anim]
            	pass
            if direccion==1:	#izquierda
            	self.image = pygame.transform.flip(self.arrayAnimDerecha[self.anim],True,False)
            	pass
            if direccion==2:	#arriba
            	self.image = self.arrayAnimArriba[self.anim]
            	pass
            if direccion==3:	#abajo
            	self.image = self.arrayAnimAbajo[self.anim]
            	pass

            self.actualizado= pygame.time.get_ticks()


main()