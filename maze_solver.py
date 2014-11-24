#!/usr/bin/env python

import sys
import os
import shutil

from Queue import Queue
from PIL import Image

# maze_image_path = 'maze-1.png'
# start_coords = (1,378)
# end_coords = (507,2)
# progress_interval = 10000

maze_image_path = 'maze-2.png'
start_coords = (1,59)
end_coords = (119,1)
progress_interval = 500

visited_color = (255,242,0) # color to mark visited pixels
threshold_color = (255,255,255) # anything this bright or brighter is considered clear
path_color = (255,0,0) # solved path color

# Deletes path if exists, then creates path. Has some race conditions that I'm ignoring
def create_empty_dir(path):
    if os.path.exists(path):
        shutil.rmtree(path)
    os.makedirs(path)

# Is pixel traversable, or is it a wall
def is_clear(pixel_coords, maze_pixels):
    x,y = pixel_coords
    pixel_color = maze_pixels[x,y]
    if all(c > 225 for c in pixel_color):
        return True

def mark_visited(pixel_coords, maze_pixels):
    x,y = pixel_coords
    maze_pixels[x,y] = visited_color

def get_adjacent_pixel_coords(pixel_coords):
    x,y = pixel_coords
    return [(x-1,y),(x,y-1),(x+1,y),(x,y+1)]

def print_path(path, dir_name):
    path_maze_image = Image.open(maze_image_path)
    path_maze_pixels = path_maze_image.load()
    for position in path:
        x,y = position
        path_maze_pixels[x,y] = path_color
    path_maze_image.save(dir_name + '/solved.png')

def BFS(start_coords, end_coords, maze_image_path):
    # Create output directory
    bfs_dir_name = 'bfs'
    create_empty_dir(bfs_dir_name)

    # Load maze from image
    bfs_maze_image = Image.open(maze_image_path)
    bfs_maze_pixels = bfs_maze_image.load()

    queue = Queue() # lists of pixel_coord tuples
    queue.put([start_coords]) # wrap the start tuple in a list

    # For saving progress snapshots
    saved_progress_count = 0
    while_loop_count = 0

    while not queue.empty():
        path = queue.get() # path is a list of pixel_coord tuples
        pixel_coords = path[-1] # get last pixel_coord tuple

        if pixel_coords == end_coords:
            print_path(path, bfs_dir_name)
            return path

        for adjacent_pixel_coords in get_adjacent_pixel_coords(pixel_coords):
            if is_clear(adjacent_pixel_coords, bfs_maze_pixels):
                mark_visited(adjacent_pixel_coords, bfs_maze_pixels)
                new_path = list(path) # force copy, not reference
                new_path.append(adjacent_pixel_coords)
                queue.put(new_path)            
        
        # print progress snapshots    
        if while_loop_count == progress_interval:
            bfs_maze_image.save(bfs_dir_name + '/' + `saved_progress_count` + '_progress.png')
            saved_progress_count += 1
            while_loop_count = 0
        while_loop_count += 1

    print 'End of queue, no path found.'

def DFS(start_coords, end_coords, maze_image_path):
    # Create output directory
    dfs_dir_name = 'dfs'
    create_empty_dir(dfs_dir_name)

    # Load maze from image
    dfs_maze_image = Image.open(maze_image_path)
    dfs_maze_pixels = dfs_maze_image.load()

    stack = [] # lists of pixel_coord tuples
    stack.append([start_coords]) # wrap the start tuple in a list

    # For saving progress snapshots
    saved_progress_count = 0
    while_loop_count = 0

    while stack:
        path = stack.pop()
        pixel_coords = path[-1]

        if pixel_coords == end_coords:
            print_path(path, dfs_dir_name)
            return path

        for adjacent_pixel_coords in get_adjacent_pixel_coords(pixel_coords):
            if is_clear(adjacent_pixel_coords, dfs_maze_pixels):
                mark_visited(adjacent_pixel_coords, dfs_maze_pixels)
                new_path = list(path) # force copy, not reference
                new_path.append(adjacent_pixel_coords)
                stack.append(new_path)   

        # print progress snapshots    
        if while_loop_count == progress_interval:
            dfs_maze_image.save(dfs_dir_name + '/' + `saved_progress_count` + '_progress.png')
            saved_progress_count += 1
            while_loop_count = 0
        while_loop_count += 1

    print 'End of stack, no path found.'

BFS(start_coords, end_coords, maze_image_path)
DFS(start_coords, end_coords, maze_image_path)
