import pygame
pygame.mixer.init() #Para Iniciar o Mixer precisa dar um input
pygame.init()
pygame.mixer.music.load('Inesperado.mp3')
pygame.mixer.music.play()
pygame.event.wait()