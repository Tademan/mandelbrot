import math
import sys
import pygame
from mandela import *
from mpmath import mp
mp.dps = 50

class Kartta:
    def __init__(self, koko, alku_arvo=0):
        self.maze = [[alku_arvo for i in range(koko[0])]for i in range(koko[0])]
    def anna(self,x,y):
        return self.maze[x][y]
    def aseta(self,x,y,arvo):
        self.maze[x][y] = arvo
    def piirrä(self, näyttö, paikka=[0,0], koko=1):

        for x in range(koko[0]):
            for y in range(koko[1]):
                pygame.draw.rect(näyttö,väri,pygame.rect(x*zoom,y*zoom,zoom,zoom),5)
def anna_väri(a):
    if a == 0:
        return (0,0,0)
    d = (1231243*a+43728462378)%255
    e = (7895039 * a + 865930478543) % 255
    f = (42974892 * a + 786979272043) % 255
    return (d,e,f)
def piirrä(näyttö, x, y, tarkkuus,paikka,zoom,font):
    #näyttö.fill((255, 255, 255))
    korkeus = näyttö.get_height()
    leveys = näyttö.get_width()
    xd = paikka[0] + x * tarkkuus / leveys / zoom
    yd = paikka[1] + y * tarkkuus / korkeus / zoom
    a = mandela(xd,yd,500)
    pygame.draw.rect(näyttö, anna_väri(a), pygame.Rect(x * tarkkuus, y * tarkkuus, tarkkuus, tarkkuus))


    text = font.render(str(math.log2(zoom)), 1, (0,0,0))
    textpos = text.get_rect()
    textpos.x = 0
    textpos.y = 50
    näyttö.blit(text, textpos)

    if x == 0:
        pygame.display.flip()

def main():
    pygame.init()
    näyttö = pygame.display.set_mode((1500, 1000), pygame.RESIZABLE)
    pygame.display.set_caption('Pygame Window')
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 50)

    Hiiri = [0, 0, 0]
    aika = 0
    x = 0
    y = 0
    tarkkuus = 8
    paikka = [-1.3, -0.4]
    zoom = 1
    while True:
        # Näppäimet
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                m = pygame.mouse.get_pos()

                if event.button == 4:
                    zoom *= 2
                    paikka[0]+=1/zoom*(m[0]/leveys)
                    paikka[1] += 1 / zoom *(m[1]/korkeus)
                    tarkkuus = 128
                elif event.button == 5:
                    zoom /= 2
                    tarkkuus = 128
                    if tarkkuus == 0:
                        tarkkuus = 1
            if event.type == pygame.VIDEORESIZE:
                old_surface_saved = näyttö
                näyttö = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                # On the next line, if only part of the window
                # needs to be copied, there's some other options.
                näyttö.blit(old_surface_saved, (0, 0))
                del old_surface_saved
            if event.type == pygame.QUIT:
                sys.exit(0)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    paikka[1] -= 1/(zoom*10)
                if event.key == pygame.K_s:
                    paikka[1] += 1/(zoom*10)
                if event.key == pygame.K_a:
                    paikka[0] -= 1/(zoom*10)
                if event.key == pygame.K_d:
                    paikka[0] += 1/(zoom*10)
                if event.key == pygame.K_z:
                    tarkkuus += 1
                if event.key == pygame.K_x:
                    tarkkuus = max(tarkkuus-1,1)
            if event.type == pygame.KEYUP:
                tarkkuus = 128

        piirrä(näyttö,x,y,tarkkuus,paikka,zoom,font)
        korkeus = näyttö.get_height()
        leveys = näyttö.get_width()
        x = (x+1)
        if x > leveys//tarkkuus:
            x = 0
            y += 1
            clock.tick(1200)
        if y > korkeus // tarkkuus:
            y = 0
            tarkkuus//=2
            if tarkkuus == 0:
                tarkkuus = 1

        if pygame.mouse.get_pressed()[0]:
            if Hiiri[0]:
                Hiiri[0] = 0
                pass
        else:
            Hiiri[0] = 1


if __name__ == "__main__":
    main()
