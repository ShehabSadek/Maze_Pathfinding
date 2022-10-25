import pygame
import sys

screen = pygame.display.set_mode((556,556))
pygame.display.set_caption("Pac Man")

maze = pygame.image.load("maze.png")
maze.convert()
maze_rect= maze.get_rect(topleft=(0,0))
#maze = pygame.transform.laplacian(maze)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.blit(maze,maze_rect)
    pygame.display.update()