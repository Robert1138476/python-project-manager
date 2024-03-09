import pygame
import os
import sys

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Object management
objects = []


# Load objects from scripts in the "objects" folder
def load_objects():
    objects_folder = "objects"
    for file_name in os.listdir(objects_folder):
        if file_name.endswith(".py"):
            module_name = file_name[:-3]
            module = __import__(
                f"{objects_folder}.{module_name}", fromlist=[module_name]
            )
            objects.append(module.Object())


# Main game loop
def main():
    running = True
    load_objects()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update objects
        for obj in objects:
            obj.update()

        # Render objects
        screen.fill(WHITE)
        for obj in objects:
            obj.render(screen)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
