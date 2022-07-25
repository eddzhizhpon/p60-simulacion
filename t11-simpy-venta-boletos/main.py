import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SIZE = (800, 500)

pygame.init()
screen = pygame.display.set_mode(SIZE)

# FPS control
clock = pygame.time.Clock()

def main():
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        
        screen.fill(WHITE)

        pygame.display.flip()
        clock.tick(20)

    pygame.quit()

if __name__ == '__main__':
    main()