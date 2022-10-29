from ast import Starred
from sys import displayhook
import pygame
from spots import *
from algorithms import *
from sprite import *
import time
from termcolor import colored

WIDTH = 500

WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Pacman Maze Solver")

sprite_sheet_image = pygame.image.load("pacman.png").convert_alpha()    
sprite_sheet= SpriteSheet(sprite_sheet_image)


animation_list=[]
aniamtion_steps=3
for x in range(aniamtion_steps):
	animation_list.append(sprite_sheet.get_image(x,25,25,3,BLACK))

def draw_pacman(path):
	current_time = pygame.time.get_ticks()
	frame = 0 
	animation_cd = 100
	last_update = pygame.time.get_ticks()
	while path:
		current_pos=path.pop()
		WIN.blit(animation_list[frame],(current_pos),special_flags=pygame.BLEND_RGBA_ADD)
		if  current_time - last_update >= animation_cd:
			frame += 1
		if frame >= len(animation_list):
			frame = 0
		last_update= current_time

		

def main(win, width):
	ROWS = 20
	grid = make_grid(ROWS, width)

	start = None
	end = None

	run = True
	while run:
		draw(win, grid, ROWS, width)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

			if pygame.mouse.get_pressed()[0]: # LEFT
				pos = pygame.mouse.get_pos()
				row, col = get_clicked_pos(pos, ROWS, width)
				spot = grid[row][col]
				if not start and spot != end:
					start = spot
					start.make_start()

				elif not end and spot != start:
					end = spot
					end.make_end()

				elif spot != end and spot != start:
					spot.make_barrier()

			elif pygame.mouse.get_pressed()[2]: # RIGHT
				pos = pygame.mouse.get_pos()
				row, col = get_clicked_pos(pos, ROWS, width)
				spot = grid[row][col]
				spot.reset()
				if spot == start:
					start = None
				elif spot == end:
					end = None

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_d and start and end:
					for row in grid:
						for spot in row:
							spot.update_neighbors(grid)

					st = time.time()
					DFS(lambda: draw(win, grid, ROWS, width), start, end)
					et = time.time()
					
					print("Time taken for {}: ".format(colored('DFS', 'green')), colored(et-st, 'blue'))

				if event.key == pygame.K_a and start and end:
					for row in grid:
						for spot in row:
							spot.update_neighbors(grid)

					st = time.time()
					Astar(lambda: draw(win, grid, ROWS, width),grid, start, end)
					et = time.time()
					print("Time taken for {}: ".format(colored('A*', 'green')), colored(et-st, 'blue'))

				if event.key == pygame.K_b and start and end:
					for row in grid:
						for spot in row:
							spot.update_neighbors(grid)

					st = time.time()
					BFS(lambda: draw(win, grid, ROWS, width), start, end)
					et = time.time()
					print("Time taken for {}: ".format(colored('BFS', 'green')), colored(et-st, 'blue'))

				if event.key == pygame.K_u and start and end:
					for row in grid:
						for spot in row:
							spot.update_neighbors(grid)

					st = time.time()
					UCS(lambda: draw(win, grid, ROWS, width), grid,start, end)
					et = time.time()
					print("Time taken for {}: ".format(colored('UCS', 'green')), colored(et-st, 'blue'))

				if event.key == pygame.K_g and start and end:
					for row in grid:
						for spot in row:
							spot.update_neighbors(grid)

					st = time.time()
					GBFS(lambda: draw(win, grid, ROWS, width), grid, start, end)
					et = time.time()
					print("Time taken for {}: ".format(colored('GBFS', 'green')), colored(et-st, 'blue'))

				if event.key == pygame.K_c:
					start = None
					end = None
					grid = make_grid(ROWS, width)


	pygame.quit()

main(WIN, WIDTH)
