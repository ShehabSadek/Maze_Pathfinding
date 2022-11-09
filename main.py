import pygame
from spots import *
from algorithms import *
from sprite import *
import time
from termcolor import colored
import pickle

WIDTH = 500
WIN = pygame.display.set_mode((WIDTH, WIDTH))
ICON = pygame.image.load('icon.png')
maze=[]
pygame.display.set_icon(ICON)
pygame.display.set_caption("Pacman Maze Solver")

sprite_sheet_image = pygame.image.load("pacman.png").convert_alpha()    
sprite_sheet= SpriteSheet(sprite_sheet_image)


animation_list=[]
aniamtion_steps=3
for x in range(aniamtion_steps):
	animation_list.append(sprite_sheet.get_image(x,25,25,1,BLACK))

def draw_pacman(path,grid,rows,width,start):
	current_time = pygame.time.get_ticks()
	frame = 0 
	animation_cd = 100
	last_update = pygame.time.get_ticks()
	curr_pos = start.get_pos()
	while path:
		next_pos=path.pop()
		nxt_pos=tuple(ti*25 for ti in next_pos)

		flipped_surface = animation_list[frame]

		if next_pos[0] < curr_pos[0]:
			flipped_surface = pygame.transform.flip(animation_list[frame], True, False)

		if next_pos[1] < curr_pos[1]:
			flipped_surface = pygame.transform.rotate(animation_list[frame],90)

		if next_pos[1] > curr_pos[1]:
			flipped_surface = pygame.transform.rotate(animation_list[frame],-90)
			
		draw(WIN, grid, rows, width)

		WIN.blit(flipped_surface,nxt_pos,special_flags=pygame.BLEND_RGBA_ADD)
		pygame.display.update()
		time.sleep(0.15)

		# if  current_time - last_update >= animation_cd:
		# 	frame += 1
		# if frame >= len(animation_list):
		# 	frame = 0
		frame+=1
		if frame>2:
			frame = 0
		last_update= current_time
		curr_pos=next_pos

def write_preset(maze,number):
	try:
		with open('maze{}.pckl'.format(number), 'wb') as fp:
			pickle.dump(maze,fp)

		print(colored('Wrote preset to file','cyan'))
	except Exception as e:
		print("Oops!", e.__class__, "occurred.")

def load_preset_maze(grid,number):
	try:
		with open('maze{}.pckl'.format(number), 'rb') as fp:
			maze=pickle.load(fp)
		for i in range (len(maze)):
			x,y = maze[i]
			spot = grid[x][y]
			spot.make_barrier()
	except Exception as e:
		print("Oops!", e.__class__, "occurred.")

def reset(grid):

	for row in grid:
		for spot in row:
			spot.reset()

def get_score(grid):
	count=0
	for row in grid:
		for spot in row:
			if spot.is_path():
				count+=1
	print("Cost:",colored(count,'yellow'))


		

def main(win, width):
	ROWS = 20
	grid = make_grid(ROWS, width)

	start = None
	end = None

	run = True
	first_run = True
	while run:
		if first_run:
			draw(win, grid, ROWS, width)
		if (get_path()):
			first_run=False
			draw_pacman(get_path(),grid,ROWS,width,start)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

			if pygame.mouse.get_pressed()[0]: # LEFT
				first_run=True
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
				first_run=True
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
					get_score(grid)
					print("Time taken for {}: ".format(colored('DFS', 'green')), colored(et-st, 'blue'))

				if event.key == pygame.K_a and start and end:
					for row in grid:
						for spot in row:
							spot.update_neighbors(grid)

					st = time.time()
					Astar(lambda: draw(win, grid, ROWS, width),grid, start, end)
					et = time.time()
					get_score(grid)
					print("Time taken for {}: ".format(colored('A*', 'green')), colored(et-st, 'blue'))

				if event.key == pygame.K_b and start and end:
					for row in grid:
						for spot in row:
							spot.update_neighbors(grid)

					st = time.time()
					BFS(lambda: draw(win, grid, ROWS, width), start, end)
					et = time.time()
					get_score(grid)
					print("Time taken for {}: ".format(colored('BFS', 'green')), colored(et-st, 'blue'))

				if event.key == pygame.K_u and start and end:
					for row in grid:
						for spot in row:
							spot.update_neighbors(grid)

					st = time.time()
					UCS(lambda: draw(win, grid, ROWS, width), grid,start, end)
					et = time.time()
					get_score(grid)
					print("Time taken for {}: ".format(colored('UCS', 'green')), colored(et-st, 'blue'))

				if event.key == pygame.K_g and start and end:
					for row in grid:
						for spot in row:
							spot.update_neighbors(grid)

					st = time.time()
					GBFS(lambda: draw(win, grid, ROWS, width), grid, start, end)
					et = time.time()
					get_score(grid)
					print("Time taken for {}: ".format(colored('GBFS', 'green')), colored(et-st, 'blue'))

				if event.key == pygame.K_c:
					first_run=True
					start = None
					end = None
					grid = make_grid(ROWS, width)

				if event.key == pygame.K_r and start and end:
					first_run=True
					for row in grid:
						for spot in row:
							if spot.is_open() or spot.is_closed() or spot.is_path():
								spot.reset()
					print(colored('Reset path', 'red'))
				if event.key == pygame.K_4 :
					for row in grid:
						for spot in row:
							if(spot.is_barrier()):
								maze.append(spot.get_pos())
					write_preset(maze,0)
				if event.key == pygame.K_5 :
					for row in grid:
						for spot in row:
							if(spot.is_barrier()):
								maze.append(spot.get_pos())
					write_preset(maze,1)
				if event.key == pygame.K_6 :
					for row in grid:
						for spot in row:
							if(spot.is_barrier()):
								maze.append(spot.get_pos())
					write_preset(maze,2)
				if event.key == pygame.K_1 :
					first_run=True
					start = None
					end = None
					reset(grid)
					print(colored('Loaded preset', 'green'))
					load_preset_maze(grid,0)
				if event.key == pygame.K_2 :
					first_run=True
					start = None
					end = None
					reset(grid)
					print(colored('Loaded preset', 'green'))
					load_preset_maze(grid,1)
				if event.key == pygame.K_3 :
					first_run=True
					start = None
					end = None
					reset(grid)
					print(colored('Loaded preset', 'green'))
					load_preset_maze(grid,2)			


	pygame.quit()

main(WIN, WIDTH)
