'''
    main.py
    Created by Nicholas Ramsay

    This file takes data from a data.csv file and displays via 
    pygame the data points alongside a simple moving average 
    and a weighted moving average.
'''

import pygame
import csv
from myutils import utils

# get data from data.csv
data = []
with open('data.csv', 'r+') as file:
    reader = csv.reader(file)

    for row in reader:
        data.append(float(row[1]))

def moving_average(data, l = 1):
    new_data = []

    for i, num in enumerate(data):
        total, count = num, 0
        for back in data[i-l if i-l > 0 else 0 : i]:
            total += back
            count += 1
        for forward in data[i : i+l if i+l < len(data) else len(data) - 1]:
            total += forward
            count += 1
        new_data.append(total/count)

    return new_data

def weighted_moving_average(data, l = 1):
    new_data = []

    for i, num in enumerate(data):
        total, count = num * l, l

        weight = l - 1
        for back in data[i-l if i-l > 0 else 0 : i]:
            total += back * weight
            count += 1 * weight
            weight -= 1
        
        weight = l - 1
        for forward in data[i : i+l if i+l < len(data) else len(data) - 1]:
            total += forward * weight
            count += 1 * weight
            weight -= 1
        new_data.append(total/count)

    return new_data
        
# setup pygame display
pygame.init()

display = (500,500)
screen = pygame.display.set_mode(display)
pygame.display.set_caption('Moving averages')

# Begin main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Default data
    for x, y in enumerate(data):

        nx = int(utils.map2range(x - 100, -101, 101, 100, 400)) + 50
        ny = 450 - int(utils.map2range(y, min(data) - 1, max(data) + 1, 100, 400))

        pygame.draw.circle(screen, (0,0,0), (nx,ny), 2)

    # Moving average data
    ma_data = moving_average(data, 10)
    for x, y in enumerate(ma_data):
    
        nx = int(utils.map2range(x - 100, -101, 101, 100, 400)) + 50
        ny = 450 - int(utils.map2range(y, min(ma_data) - 1, max(ma_data) + 1, 100, 400))

        pygame.draw.circle(screen, (255,0,0), (nx,ny), 2)

    # weighted moving average data
    ma_data = weighted_moving_average(data, 10)
    for x, y in enumerate(ma_data):
    
        nx = int(utils.map2range(x - 100, -101, 101, 100, 400)) + 50
        ny = 450 - int(utils.map2range(y, min(ma_data) - 1, max(ma_data) + 1, 100, 400))

        pygame.draw.circle(screen, (0,0,255), (nx,ny), 2)

    pygame.display.update()
    screen.fill((255,255,255))
