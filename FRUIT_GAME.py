import pygame
import random
import sys
import math

pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 60
FRUIT_SIZE = 50  
FRUIT_TYPES = ['apple', 'banana', 'orange']
FRUIT_IMAGES = {}

for fruit in FRUIT_TYPES:
    image = pygame.image.load(f'{fruit}.png')
    FRUIT_IMAGES[fruit] = pygame.transform.scale(image, (FRUIT_SIZE, FRUIT_SIZE))

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fruit Cutting Game")

fruits = []
score = 0
attempts = 0
max_attempts = 10
game_over = False

font = pygame.font.Font(None, 36)

class Fruit:
    def __init__(self, fruit_type):
        self.type = fruit_type
        self.image = FRUIT_IMAGES[fruit_type]
        self.rect = self.image.get_rect()
        self.rect.x = random.choice([-FRUIT_SIZE, WIDTH]) 
        self.rect.y = random.randint(HEIGHT // 2, HEIGHT) 
        self.direction = random.choice([-1, 1]) 

    def move(self):
        self.rect.y -= 5  
        self.rect.x += self.direction * 2  
        if self.rect.y < 0:  
            self.rect.y = HEIGHT
            self.rect.x = random.choice([-FRUIT_SIZE, WIDTH])

    def draw(self):
        screen.blit(self.image, self.rect)

def main():
    global score, attempts, game_over
    clock = pygame.time.Clock()
    spawn_timer = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                mouse_pos = event.pos
                for fruit in fruits:
                    if fruit.rect.collidepoint(mouse_pos):
                        fruits.remove(fruit)
                        score += 1
                        attempts += 1
                        print(f'Score: {score}')
                        break
                else:
                    attempts += 1

        spawn_timer += 1
        if spawn_timer > 30 and not game_over:
            fruit_type = random.choice(FRUIT_TYPES)
            fruits.append(Fruit(fruit_type))
            spawn_timer = 0

        for fruit in fruits:
            fruit.move()
            if fruit.rect.y < 0:  
                fruits.remove(fruit)

        if attempts >= max_attempts:
            game_over = True

        screen.fill((255, 255, 255)) 
        for fruit in fruits:
            fruit.draw()

        score_text = font.render(f'Score: {score}', True, (0, 0, 0))
        screen.blit(score_text, (10, 10))

        if game_over:
            game_over_text = font.render('Game Over!', True, (255, 0, 0))
            accuracy = (score / attempts) * 100 if attempts > 0 else 0
            accuracy_text = font.render(f'Accuracy: {accuracy:.2f}%', True, (0, 0, 0))
            attempts_text = font.render(f'Attempts: {attempts}', True, (0, 0, 0))
            screen.blit(game_over_text, (WIDTH // 2 - 50, HEIGHT // 2 - 50))
            screen.blit(accuracy_text, (WIDTH // 2 - 50, HEIGHT // 2))
            screen.blit(attempts_text, (WIDTH // 2 - 50, HEIGHT // 2 + 50))

        pygame.display.flip() 
        clock.tick(FPS) 

if __name__ == "__main__":
    main()
