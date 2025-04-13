import pygame
import math
import time
from vectors import *
from transformations import *
from cube import *

pygame.init()
sc = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()

def calculate_normal(polygon):
    if len(polygon) < 3: return None
    u = Vector3(polygon[1].x-polygon[0].x, polygon[1].y-polygon[0].y, polygon[1].z-polygon[0].z)
    v = Vector3(polygon[2].x-polygon[0].x, polygon[2].y-polygon[0].y, polygon[2].z-polygon[0].z)
    normal = Vector3(u.y*v.z-u.z*v.y, u.z*v.x-u.x*v.z, u.x*v.y-u.y*v.x)
    length = math.sqrt(normal.x**2 + normal.y**2 + normal.z**2)
    if length > 0: normal.x /= length; normal.y /= length; normal.z /= length
    return normal

def is_face_visible(polygon, camera_position=Vector3(0, 0, 0)):
    normal = calculate_normal(polygon)
    if not normal:
        return False

    center = Vector3(0, 0, 0)
    for vertex in polygon:
        center.x += vertex.x
        center.y += vertex.y
        center.z += vertex.z
    center.x /= len(polygon)
    center.y /= len(polygon)
    center.z /= len(polygon)

    view_vector = Vector3(center.x - camera_position.x,
                          center.y - camera_position.y,
                          center.z - camera_position.z)

    length = math.sqrt(view_vector.x**2 + view_vector.y**2 + view_vector.z**2)
    if length > 0:
        view_vector.x /= length
        view_vector.y /= length
        view_vector.z /= length

    dot_product = normal.x * view_vector.x + normal.y * view_vector.y + normal.z * view_vector.z
    return dot_product < 0

def draw_step_by_step():
    angle = 0
    cube_faces = [[3,2,1,0],[4,5,6,7],[4,0,1,5],[6,2,3,7],[7,3,0,4],[5,1,2,6]]
    face_colors = [(255,0,0),(0,255,0),(0,0,255),(255,255,0),(0,255,255),(255,0,255)]
    cube_edges = [(0,1),(1,2),(2,3),(3,0),(4,5),(5,6),(6,7),(7,4),(0,4),(1,5),(2,6),(3,7)]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        sc.fill((0,0,0))
        angle += 0.01

        rotated = [rotate(rotate(rotate(vertex, 'x', angle), 'y', angle*0.7), 'z', angle*0.3) for vertex in cube_vertices]
        projected = [sstopgcord(transform3dto2d(Vector3(v.x, v.y, v.z+3), 60), 600, 400) for v in rotated]
        screen_vertices = [(p.x, p.y) for p in projected]

        delay = 0.05

        sc.fill((0,0,0))
        for edge in cube_edges:
            start = screen_vertices[edge[0]]
            time.sleep(delay)
            end = screen_vertices[edge[1]]
            pygame.draw.line(sc, (255,255,255), start, end, 1)
            pygame.display.flip()
        time.sleep(delay)


        visible_faces = []
        for i, face in enumerate(cube_faces):
            face_3d = [rotated[idx] for idx in face]
            if is_face_visible(face_3d):
                depth = sum(v.z for v in face_3d)/len(face_3d)
                visible_faces.append((depth, i, face))

        visible_faces.sort(reverse=True)

        for depth, i, face in visible_faces:
            polygon = [screen_vertices[idx] for idx in face]
            pygame.draw.polygon(sc, face_colors[i], polygon)
            pygame.draw.polygon(sc, (255,255,255), polygon, 1)
            pygame.display.flip()
            time.sleep(delay)


        sc.fill((0,0,0))
        for depth, i, face in visible_faces:
            polygon = [screen_vertices[idx] for idx in face]
            pygame.draw.polygon(sc, face_colors[i], polygon)
            pygame.draw.polygon(sc, (255,255,255), polygon, 1)

        for edge in cube_edges:
            start = screen_vertices[edge[0]]
            end = screen_vertices[edge[1]]

            pygame.draw.line(sc, (255,255,255), start, end, 1)

        pygame.display.flip()
        time.sleep(delay)
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    draw_step_by_step()