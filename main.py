from selectors import SelectSelector

import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 60
window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

fontItem = pygame.font.Font(None, 50)
fontItemSelect = pygame.font.Font(None, 60)

items = ['Играть', 'Разработчики', 'Выход']
select = 0
timer = 0

play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP: select -= 1
            elif event.key == pygame.K_DOWN: select += 1
            elif event.key in [pygame.K_RETURN, pygame.K_SPACE]:
                if items[select] == 'Выход': play = False #Задаем кнопкy

            select = select % len(items)  #выбор иконок

    timer += 1


    window.fill('white')
    for i in range(len(items)):
        if i == select and timer % 30 < 15:
            text = fontItemSelect.render(items[i], 1, 'blue')
        else:
            text = fontItem.render(items[i],1, 'gray')

        rect = text.get_rect(center = (WIDTH // 2, 200 + 50 * i))
        window.blit(text, rect)

    pygame.display.update()
    clock.tick(FPS)


pygame.quit()
