import pygame
import sys
import random


WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
GRID_SIZE = 20
GRID_WIDTH = WINDOW_WIDTH // GRID_SIZE
GRID_HEIGHT = WINDOW_HEIGHT // GRID_SIZE


WHITE = (255, 255, 255)
GREEN = (0, 150, 0)
ORANGE = (250, 150, 0)
GRAY = (100, 100, 100)


UP, DOWN, LEFT, RIGHT = (0, -1), (0, 1), (-1, 0), (1, 0)


class Snake:
    def __init__(self):
        self.length = 2
        self.positions = [(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.color = GREEN

    def control(self, xy):
        if (xy[0] * -1, xy[1] * -1) == self.direction:
            return
        self.direction = xy

    def move(self):
        cur = self.positions[0]
        x, y = self.direction
        new = ((cur[0] + (x * GRID_SIZE)) % WINDOW_WIDTH, (cur[1] + (y * GRID_SIZE)) % WINDOW_HEIGHT)


        if len(self.positions) > 2 and new in self.positions[2:]:
            self.__init__()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()

    def draw(self, surface):
        for p in self.positions:
            rect = pygame.Rect((p[0], p[1]), (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(surface, self.color, rect)


class Food:
    def __init__(self):
        self.position = (0, 0)
        self.color = ORANGE
        self.randomize()

    def randomize(self):
        self.position = (random.randint(0, GRID_WIDTH - 1) * GRID_SIZE,
                         random.randint(0, GRID_HEIGHT - 1) * GRID_SIZE)

    def draw(self, surface):
        rect = pygame.Rect((self.position[0], self.position[1]), (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(surface, self.color, rect)


def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Snake Game')
    clock = pygame.time.Clock()


    font = pygame.font.SysFont("arial", 25)

    snake = Snake()
    food = Food()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.control(UP)
                elif event.key == pygame.K_DOWN:
                    snake.control(DOWN)
                elif event.key == pygame.K_LEFT:
                    snake.control(LEFT)
                elif event.key == pygame.K_RIGHT:
                    snake.control(RIGHT)

        snake.move()


        if snake.positions[0] == food.position:
            snake.length += 1
            food.randomize()


        screen.fill(WHITE)
        snake.draw(screen)
        food.draw(screen)


        speed = (10 + snake.length) // 2
        info = font.render(f"Length: {snake.length}  Speed: {speed}", True, GRAY)
        screen.blit(info, (10, 10))

        pygame.display.update()
        clock.tick(speed)


if __name__ == '__main__':
    main()