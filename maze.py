import pygame
import sys


def draw(window, size, rows):
    distance_between_rows = size // rows
    x=0
    y=0
    for i in range(rows):

        x+= distance_between_rows
        y+= distance_between_rows
        pygame.draw.line(window,(0,0,0),(x,0),(x,size))
        pygame.draw.line(window,(0,0,0),(0,y),(size,y))

def main():
    size=556
    row=35
    screen = pygame.display.set_mode((size,size))
    pygame.display.set_caption("Pac Man")

    maze = pygame.image.load("maze.png")
    maze.convert()
    maze_rect= maze.get_rect(topleft=(0,0))
    #maze = pygame.transform.laplacian(maze)
    while True:
        screen.blit(maze,maze_rect)
        draw(screen,size,row)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()

if __name__=="__main__":
    main()