import pygame
import random
import copy

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TILE_SIZE = 20
SPEED = 10
DIRECTIONS = {'l': -20, 'r': 20, 'u': -20, 'd': 20, 'q': 0}
INDEX = {'l': 0, 'r': 0, 'u': 1, 'd': 1, 'q': 0}

COLORS = {'red': (255, 0, 0), 'white': (255, 255, 255), 'black': (0, 0, 0), 'blue': (0, 0, 255), 'green': (0, 255, 0)}

snake_dir = 'q'

food_x = random.randrange(0, int(SCREEN_WIDTH/10), 2) * 10 + 1
food_y = random.randrange(0, int(SCREEN_HEIGHT/10), 2) * 10 + 1
# print(food_x, food_y)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
snake_head = pygame.Rect(1, 1, TILE_SIZE-1, TILE_SIZE-1)
food = pygame.Rect(food_x, food_y, TILE_SIZE-1, TILE_SIZE-1)
tail = []
score = 0

def draw_board():
    screen.fill(COLORS['white'])
    pygame.draw.rect(screen, COLORS['red'], snake_head)
    pygame.draw.rect(screen, COLORS['blue'], food)
    for block in tail:
        pygame.draw.rect(screen, COLORS['green'], block)
        # print("head", snake_head.x, snake_head.y)
        # print("tails", block.x, block.y)
    i = 0
    while i < SCREEN_WIDTH:
        pygame.draw.line(screen, COLORS['black'], (i, 0), (i, SCREEN_HEIGHT))
        i += TILE_SIZE

    i = 0
    while i < SCREEN_HEIGHT:
        pygame.draw.line(screen, COLORS['black'], (0, i), (SCREEN_WIDTH, i))
        i += TILE_SIZE

def ate_food():
    if snake_head.x == food.x and snake_head.y == food.y:
        tail.append(copy.deepcopy(snake_head))
        food.x = random.randrange(0, int(SCREEN_WIDTH/10), 2) * 10 + 1
        food.y = random.randrange(0, int(SCREEN_HEIGHT/10), 2) * 10 + 1

def game_over():
    if snake_head in tail:
        return True
    return False

isRunning = True

while isRunning:

    pygame.time.Clock().tick(SPEED)
    draw_board()
    if game_over():
        isRunning = False
        break
    ate_food()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a and snake_dir != 'r':
                snake_dir = 'l'
            if event.key == pygame.K_d and snake_dir != 'l':
                snake_dir = 'r'
            if event.key == pygame.K_w and snake_dir != 'd':
                snake_dir = 'u'
            if event.key == pygame.K_s and snake_dir != 'u':
                snake_dir = 'd'
    
    move_x = DIRECTIONS[snake_dir] if snake_dir in ['l', 'r'] else 0
    move_y = DIRECTIONS[snake_dir] if snake_dir in ['u', 'd'] else 0

    if len(tail) > 0:
        for i in range(len(tail)-1, 0, -1):
            tail[i] = copy.deepcopy(tail[i-1])
        tail[0] = copy.deepcopy(snake_head)
        # tail.pop()
        # tail.append(snake_head)

    snake_head.move_ip(move_x, move_y)

    if snake_head.x < 0:
        snake_head.x = SCREEN_WIDTH - TILE_SIZE + 1
    elif snake_head.x > SCREEN_WIDTH:
        snake_head.x = 1

    if snake_head.y < 0:
        snake_head.y = SCREEN_HEIGHT - TILE_SIZE + 1
    elif snake_head.y > SCREEN_HEIGHT:
        snake_head.y = 1
    

    # update_screen()
    # pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(snake_pos[0], snake_pos[1], TILE_SIZE-1, TILE_SIZE-1))
    # snake_pos[1] += 20
    # pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(30, 30, 60, 60))
    pygame.display.update()

pygame.quit()