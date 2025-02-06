import pygame
import sys

pygame.init()

# Настройки окна
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Динозаврик')

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Шрифты
font = pygame.font.Font(None, 74)
small_font = pygame.font.Font(None, 48)

# Функция для отображения текста на экране
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

# Основной цикл меню
def menu():
    while True:
        screen.fill(WHITE)

        draw_text('Меню', font, BLACK, screen, 320, 50)
        draw_text('Играть', small_font, BLACK, screen, 350, 150)
        draw_text('Выход', small_font, BLACK, screen, 350, 250)
        draw_text('Разработчики', small_font, BLACK, screen, 350, 350)
        draw_text('Помощь', small_font, BLACK, screen, 350, 450)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 350 <= x <= 450:
                    if 150 <= y <= 200:
                        run_game()  # Функция запуска игры
                    elif 250 <= y <= 300:
                        pygame.quit()
                        sys.exit()
                    elif 350 <= y <= 400:
                        show_developers()
                    elif 450 <= y <= 500:
                        show_help()

# Функция для запуска игры
def run_game():
    # Здесь должен быть ваш код из файла dino.py
    # Например:
    import dino
    dino.main()  # Предполагая, что в dino.py есть функция main()

# Функция, отображающая информацию о разработчиках
def show_developers():
    while True:
        screen.fill(WHITE)
        draw_text('Дикунов Даниил и Марк Дорошенко', font, BLACK, screen, 50, 200)
        draw_text('Нажмите любую клавишу, чтобы вернуться', small_font, GRAY, screen, 50, 300)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                return  # Возвращаемся в меню

# Функция, отображающая помощь
def show_help():
    while True:
        screen.fill(WHITE)
        draw_text('Telegramm: Даниил-@yhppkh, Марк-@balance0811', font, BLACK, screen, 50, 200)
        draw_text('Нажмите любую клавишу, чтобы вернуться', small_font, GRAY, screen, 50, 300)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                return  # Возвращаемся в меню

# Запуск главного меню
if __name__ == '__main__':
    menu()
