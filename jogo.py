import pygame
import sys
import random

# Inicialização do Pygame
pygame.init()

# Configurações da janela
window_size = (400, 400)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption('Jogo da Cobra')

# Cores
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)

# Tamanho da grade
grid_size = 20

# Inicialização da cobra
snake = [(100, 50), (90, 50), (80, 50)]
snake_direction = 'RIGHT'

# Comida
food = (random.randrange(1, (window_size[0] // grid_size)) * grid_size,
        random.randrange(1, (window_size[1] // grid_size)) * grid_size)

# Velocidade da cobra
speed = 15

# Função para desenhar a cobra
def draw_snake(snake):
    for segment in snake:
        pygame.draw.rect(window, green, (segment[0], segment[1], grid_size, grid_size))

# Loop principal do jogo
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Controles da cobra
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and snake_direction != 'RIGHT':
                snake_direction = 'LEFT'
            if event.key == pygame.K_RIGHT and snake_direction != 'LEFT':
                snake_direction = 'RIGHT'
            if event.key == pygame.K_UP and snake_direction != 'DOWN':
                snake_direction = 'UP'
            if event.key == pygame.K_DOWN and snake_direction != 'UP':
                snake_direction = 'DOWN'

    # Movimento da cobra
    new_head = list(snake[0])

    if snake_direction == 'RIGHT':
        new_head[0] += grid_size
    if snake_direction == 'LEFT':
        new_head[0] -= grid_size
    if snake_direction == 'UP':
        new_head[1] -= grid_size
    if snake_direction == 'DOWN':
        new_head[1] += grid_size

    snake.insert(0, tuple(new_head))

    # Verifica colisão com a comida
    if snake[0] == food:
        food = (random.randrange(1, (window_size[0] // grid_size)) * grid_size,
                random.randrange(1, (window_size[1] // grid_size)) * grid_size)
    else:
        snake.pop()

    # Verifica colisão com as bordas
    if (snake[0][0] < 0 or snake[0][0] >= window_size[0] or
        snake[0][1] < 0 or snake[0][1] >= window_size[1]):
        running = False

    # Verifica colisão com o próprio corpo
    if snake[0] in snake[1:]:
        running = False

    # Limpeza da tela
    window.fill(black)

    # Desenho da comida
    pygame.draw.rect(window, white, (food[0], food[1], grid_size, grid_size))

    # Desenho da cobra
    draw_snake(snake)

    # Atualização da tela
    pygame.display.update()

    # Controle de velocidade
    pygame.time.Clock().tick(speed)

# Encerramento do Pygame
pygame.quit()
sys.exit() 