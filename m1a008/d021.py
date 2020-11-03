import os, pygame
musica = os.path.join(os.path.dirname(__file__), 'd021.mp3')
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load(musica)
pygame.mixer.music.play()
pygame.event.wait()
