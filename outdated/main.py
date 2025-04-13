import pygame
import math

from vectors import *
from transformations import *
from cube import *

def main():
    pygame.init()
    sc = pygame.display.set_mode((600, 400))
    FPS = 60
    clock = pygame.time.Clock()
    fov = 60
    angle = 0
    cube_edges = [
        (0, 1), (1, 2), (2, 3), (3, 0),
        (4, 5), (5, 6), (6, 7), (7, 4),
        (0, 4), (1, 5), (2, 6), (3, 7)
    ]
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        sc.fill((0, 0, 0))
        angle += 0.01
        rotated_vertices = []
        for vertex in cube_vertices:
            v = rotate(vertex, 'x', angle)
            v = rotate(v, 'y', angle*0.7)
            v = rotate(v, 'z', angle*0.3)
            rotated_vertices.append(v)
        projected_vertices = []
        for vertex in rotated_vertices:
            vertex_with_offset = Vector3(vertex.x, vertex.y, vertex.z + 3)
            projected = transform3dto2d(vertex_with_offset, fov)
            screen_pos = sstopgcord(projected, 600, 400)
            projected_vertices.append(screen_pos)
        for edge in cube_edges:
            start = projected_vertices[edge[0]]
            end = projected_vertices[edge[1]]
            if (0 <= start.x <= 600 and 0 <= start.y <= 400 and
                    0 <= end.x <= 600 and 0 <= end.y <= 400):
                pygame.draw.line(sc, (255, 255, 255), (start.x, start.y), (end.x, end.y), 1)
        for vertex in projected_vertices:
            if 0 <= vertex.x <= 600 and 0 <= vertex.y <= 400:
                pygame.draw.circle(sc, (255, 255, 255), (vertex.x, vertex.y), 3)
        pygame.display.flip()
        clock.tick(FPS)
if __name__ == "__main__":
    main()