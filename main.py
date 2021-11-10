import random
import pygame
import sys


def main():
    window_size = total_width, total_height = 600, 650
    playable_area_size = width, height = 600, 600
    x_max = int(width / 10)
    y_max = int(height / 10)

    black = 0, 0, 0
    green = 0, 255, 0
    red = 255, 0, 0
    white = 255, 255, 255

    game_over = False
    score = 0

    snake_x = [x_max - 3, x_max - 2, x_max - 1]
    snake_y = [int(y_max / 2), int(y_max / 2), int(y_max / 2)]
    fruit = [random.randint(0, x_max - 1), random.randint(0, y_max - 1)]
    direction = "left"

    pygame.init()
    window = pygame.display.set_mode(window_size)
    window_background = pygame.Surface(window_size)
    window_background = window_background.convert()
    window_background.fill(white)
    pygame.display.set_caption("Snake Game")

    background = pygame.Surface(playable_area_size)
    background = background.convert()
    background.fill(black)

    pygame.font.init()
    score_space = pygame.Surface((total_width, total_height - height))
    score_font = pygame.font.Font(None, 40)
    score_text = score_font.render(f"Score: {score}", True, black)
    score_space.fill(white)
    score_space.blit(score_text, score_text.get_rect(center=((total_width - width) // 2 + score_text.get_size()[0] // 2,
                                                             (total_height - height) // 2)))
    print(score_text.get_size())

    game_over_font = pygame.font.Font(None, 50)
    game_over_text = game_over_font.render("Game Over!", True, green)

    clock = pygame.time.Clock()
    speed = 10

    window.blit(window_background, (0, 0))
    window.blit(background, (total_width - width, total_height - height))
    window.blit(score_text, (0, 0))
    pygame.display.flip()

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    direction = "up"
                elif event.key == pygame.K_DOWN:
                    direction = "down"
                elif event.key == pygame.K_LEFT:
                    direction = "left"
                elif event.key == pygame.K_RIGHT:
                    direction = "right"
                elif event.key == pygame.K_RETURN:
                    if game_over:
                        game_over = False
                        snake_x = [x_max - 3, x_max - 2, x_max - 1]
                        snake_y = [int(y_max / 2), int(y_max / 2), int(y_max / 2)]
                        fruit = [random.randint(0, x_max - 1), random.randint(0, y_max - 1)]
                        direction = "left"
                        speed = 10
                        score = 0

        if game_over:
            background.blit(game_over_text, game_over_text.get_rect(center=(int(width / 2), int(height / 2))))
            window.blit(background, (total_width - width, total_height - height))
            pygame.display.flip()
        else:
            if direction == "up":
                snake_y.insert(0, snake_y[0] - 1)
                snake_x.insert(0, snake_x[0])
            elif direction == "down":
                snake_y.insert(0, snake_y[0] + 1)
                snake_x.insert(0, snake_x[0])
            elif direction == "left":
                snake_x.insert(0, snake_x[0] - 1)
                snake_y.insert(0, snake_y[0])
            else:
                snake_x.insert(0, snake_x[0] + 1)
                snake_y.insert(0, snake_y[0])

            for i in range(1, len(snake_x)):
                if snake_x[0] == snake_x[i] and snake_y[0] == snake_y[i]:
                    game_over = True
                    break
            if snake_x[0] < 0 or snake_y[0] < 0 or snake_x[0] >= x_max or snake_y[0] >= y_max:
                game_over = True

            if snake_x[0] != fruit[0] or snake_y[0] != fruit[1]:
                snake_x.pop()
                snake_y.pop()
            else:
                while snake_x[0] == fruit[0] and snake_y[0] == fruit[1]:
                    fruit = [random.randint(0, x_max - 1), random.randint(0, y_max - 1)]
                speed += 1
                score += 1

            background.fill(black)
            window_background.fill(white)
            score_space.fill(white)

            score_text = score_font.render(f"Score: {score}", True, black)
            score_space.blit(score_text,
                             score_text.get_rect(center=((total_width - width) // 2 + score_text.get_size()[0],
                                                         (total_height - height) // 2)))

            fruit_icon = pygame.Rect(fruit[0] * 10, fruit[1] * 10, 10, 10)
            for i in range(0, len(snake_x)):
                pygame.draw.rect(background, green, pygame.Rect(snake_x[i] * 10, snake_y[i] * 10, 10, 10))
            pygame.draw.rect(background, red, fruit_icon)
            window.blit(background, (total_width - width, total_height - height))
            window.blit(score_space, (0, 0))
            pygame.display.flip()
            clock.tick(speed)


if __name__ == '__main__':
    main()

