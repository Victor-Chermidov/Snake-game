import pygame
import random

SPEED = 5
snake = 15
food = 8
game_over = False
# инициализируем библиотеку Pygame
pygame.init()

# определяем размеры окна
window_size = (300, 300)
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 300
x = SCREEN_WIDTH / 2
y = SCREEN_HEIGHT / 2
dx, dy = 0, 0
food_x, food_y = random.randint(0, SCREEN_WIDTH - food), random.randint(0, SCREEN_HEIGHT - food)
snake_seg = [(x, y)]
# задаем название окна
pygame.display.set_caption("Змейка")

clock = pygame.time.Clock()  # Подключение часов и таймера в программу

# создаем окно
screen = pygame.display.set_mode(window_size)

# задаем цвет фона
background_color = (0, 0, 255)  # синий


# Функция для отображения текста на экране
def display_message(message, size):
    font = pygame.font.Font(None, size)  # Переменная с шрифтом
    text = font.render(message, True, WHITE)  # Переменная с текстом готовым
    screen.blit(text, (SCREEN_WIDTH / 4, SCREEN_HEIGHT / 2))


# заполняем фон заданным цветом
screen.fill(background_color)
# обновляем экран для отображения изменений
pygame.display.flip()
# показываем окно, пока пользователь не нажмет кнопку "Закрыть"
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx = -SPEED
                dy = 0
            if event.key == pygame.K_RIGHT:
                dx = SPEED
                dy = 0
            if event.key == pygame.K_DOWN:
                dy = SPEED
                dx = 0
            if event.key == pygame.K_UP:
                dy = -SPEED
                dx = 0
    x += dx
    y += dy

    # Отрисовка еды
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (0, 255, 0), (food_x, food_y, food, food))

    snake_seg.append((x, y))
    if len(snake_seg) > 1:
        if snake_seg[0] == snake_seg[-1]:
            snake_seg.pop(0)
    if x+15 > SCREEN_WIDTH or x < 0 or y+15 > SCREEN_HEIGHT or y < 0 or (x, y) in snake_seg[:-1]:
        game_over = True

    for pr_snake in snake_seg:
        pygame.draw.rect(screen, (255, 255, 255), (pr_snake[0], pr_snake[1], snake, snake))

    pygame.display.update()

    if (food_x - food / 2 < x-snake/2 < food_x + food / 2 or food_x - food / 2< x-snake/2< food_x + food / 2) and (food_y - food / 2 < y+snake/2 < food_y + food / 2 or  food_y - food / 2 < y-snake/2 < food_y + food / 2):
        food_x, food_y = random.randint(0, SCREEN_WIDTH - food), random.randint(0, SCREEN_HEIGHT - food)
    else:
        snake_seg.pop(0)

    clock.tick(15)
