import pygame

# Inicializando o mixer PyGame
pygame.mixer.init()

# Iniciando o Pygame
pygame.init()

pygame.mixer.music.load('C:\Users\Erika\PycharmProjects\pythonexercicios.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()

