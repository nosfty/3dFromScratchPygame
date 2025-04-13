import pygame
from corelibs import core
from corelibs.transformations import Vector3


def main():
    pygame.init()
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("3D Triangle Rendering")
    clock = pygame.time.Clock()
    FPS = 60

    # Create camera
    camera = core.Camera(Vector3(0, 0, -5), 60)

    # Create triangle
    triangle = core.Triangle(
        Vector3(-1, -1, 0),
        Vector3(1, -1, 0),
        Vector3(0, 1, 0)
    )
    triangle.configure(
        shaded=True,
        color=(255, 0, 0),  # Red
        outlinded=True,
        outline_color=(255, 255, 255)  # White outline
    )

    angle = 0
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear screen
        screen.fill((0, 0, 0))

        # Rotate triangle
        angle += 0.001
        triangle.rotate(Vector3(0, 0.01, 0))

        # Draw triangle
        triangle.draw(screen, camera)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()