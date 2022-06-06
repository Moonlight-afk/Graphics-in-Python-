import pygame

pygame.init()  # Запускаем pygame
screen = pygame.display.set_mode((500, 500))  # Устанавливаем размер экрана
clock = pygame.time.Clock()  # Чтобы программа работала с заданной частотой кадров
running = True
fps = 60

x1,y1,x2,y2 = 50,0,60,200

def brez(screen: screen):
    del_y = abs(y2 - y1)
    del_x = abs(x2 - x1)
    bet = 0
    # Первая четверть
    if x1 < x2 and y1 < y2:
        start_x = x1
        finish_x = x2
        start_y = y1
        finish_y = y2
        z = 1
        y = y1
        x_x = x1
    # Вторая четверть
    elif x1 > x2 and y1 < y2:
        start_x = x2
        finish_x = x1
        start_y = y1
        finish_y = y2
        z = -1
        y = y2
        x_x = x1
    # Третья четверть
    elif x1 > x2 and y1 > y2:
        start_x = x2
        finish_x = x1
        start_y = y2
        finish_y = y1
        z = 1
        y = y2
        x_x = x2
    # Четвертая четверть
    else:
        start_x = x1
        finish_x = x2
        start_y = y2
        finish_y = y1
        z = -1
        y = y1
        x_x = x2

    if del_x >= del_y:
        # Рисует линию, пока линия больше горизонтальная,чем вертикальная
        for x in range(start_x, finish_x):
            bet += 2 * del_y #bet - 
            if bet >= del_x:
                y += z
                bet -= 2 * del_x
            screen.set_at((250 + x, 250 - y),(0,0,0))
    else:
        # Рисует линию, пока линия больше вертикальная,чем горизонтальная
        for y in range(start_y, finish_y):
            bet += 2 * del_x
            if bet >= del_y:
                x_x += z
                bet -= 2 * del_y
            screen.set_at((250 + x_x, 250 - y),(0,0,0))


while running:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255, 255, 255))
    pygame.draw.line(screen, (0, 0, 0), [10, 250], [490, 250], 2) #Горизонтальная ось
    pygame.draw.line(screen, (0, 0, 0), [250, 10], [250, 490], 2) #Вертикальная ось
    brez(screen)
    pygame.display.flip()  # Переворачиваем экран, при использовании двойной буферезаци
pygame.quit()
