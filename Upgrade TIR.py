import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Установка заголовка и иконки окна
pygame.display.set_caption("Игра ТИР")
icon = pygame.image.load("image/11.png")
pygame.display.set_icon(icon)

# Загрузка изображения мишени
target_image = pygame.image.load("image/target.png")
target_width = 180
target_height = 180

# Начальные координаты мишени
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

# Скорость движения мишени по осям X и Y
target_speed_x = random.choice([-3, -2, -1, 1, 2, 3])
target_speed_y = random.choice([-3, -2, -1, 1, 2, 3])

# Случайный цвет фона
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Инициализация шрифта для отображения счета
font = pygame.font.SysFont('Arial', 24)

# Начальное количество очков
score = 0

running = True
while running:
    screen.fill(color)

    # Перемещение мишени
    target_x += target_speed_x
    target_y += target_speed_y

    # Проверка столкновения с границами экрана и изменение направления движения
    if target_x <= 0 or target_x >= SCREEN_WIDTH - target_width:
        target_speed_x = -target_speed_x
    if target_y <= 0 or target_y >= SCREEN_HEIGHT - target_height:
        target_speed_y = -target_speed_y

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                # Увеличиваем счет при попадании
                score += 1
                # Перемещаем мишень в случайное место
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
                # Изменяем скорость мишени
                target_speed_x = random.choice([-3, -2, -1, 1, 2, 3])
                target_speed_y = random.choice([-3, -2, -1, 1, 2, 3])

    # Отрисовка мишени
    screen.blit(target_image, (target_x, target_y))

    # Отображение счета
    score_text = font.render(f"Очки: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    pygame.display.update()

pygame.quit()