from sys import displayhook
import pygame
from spots import *
from algorithms import *

WIDTH = 500

WIN = pygame.display.set_mode((WIDTH, WIDTH))
BG = pygame.image.load("maze525.png").convert()
pygame.display.set_caption("Pacman Maze Solver")
sprite_sheet_image = pygame.image.load("pacman.png").convert_alpha()    
aniamtion_list = []

def get_image(sheet, width, height):
	image = pygame.Surface((width,height)).convert_alpha()
	image.blit(sheet, (0,0),(0,0,25,25))
	return image

frame_0 = get_image(sprite_sheet_image,25,25)
frame_1 = get_image(sprite_sheet_image,25,25)
frame_2 = get_image(sprite_sheet_image,25,25)

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
					print("Time taken for DFS: ", et-st)

				if event.key == pygame.K_a and start and end:
					for row in grid:
						for spot in row:
							spot.update_neighbors(grid)

					st = time.time()
					Astar(lambda: draw(win, grid, ROWS, width),grid, start, end)
					et = time.time()
					print("Time taken for A*: ", et-st)

				if event.key == pygame.K_b and start and end:
					for row in grid:
						for spot in row:
							spot.update_neighbors(grid)

					st = time.time()
					BFS(lambda: draw(win, grid, ROWS, width), start, end)
					et = time.time()
					print("Time taken for BFS: ", et-st)

				if event.key == pygame.K_u and start and end:
					for row in grid:
						for spot in row:
							spot.update_neighbors(grid)

					st = time.time()
					UCS(lambda: draw(win, grid, ROWS, width), grid,start, end)
					et = time.time()
					print("Time taken for UCS: ", et-st)

				if event.key == pygame.K_g and start and end:
					for row in grid:
						for spot in row:
							spot.update_neighbors(grid)

					st = time.time()
					GBFS(lambda: draw(win, grid, ROWS, width), grid, start, end)
					et = time.time()
					print("Time taken for GBFS: ", et-st)

				if event.key == pygame.K_c:
					start = None
					end = None
					grid = make_grid(ROWS, width)


	pygame.quit()

main(WIN, WIDTH)
