import pygame
import math
from vectors import *
from transformations import *
from cube import *

def calculate_normal(polygon):
    if len(polygon) < 3:
        return None

    p0 = polygon[0]
    p1 = polygon[1]
    p2 = polygon[2]

    u = Vector3(p1.x - p0.x, p1.y - p0.y, p1.z - p0.z)
    v = Vector3(p2.x - p0.x, p2.y - p0.y, p2.z - p0.z)

    normal = Vector3(
        u.y * v.z - u.z * v.y,
        u.z * v.x - u.x * v.z,
        u.x * v.y - u.y * v.x
    )

    length = math.sqrt(normal.x**2 + normal.y**2 + normal.z**2)
    if length > 0:
        normal.x /= length
        normal.y /= length
        normal.z /= length

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

def calculate_face_depth(face_vertices):
    return sum(v.z for v in face_vertices) / len(face_vertices)

def main():
    pygame.init()
    sc = pygame.display.set_mode((600, 400))
    FPS = 60
    clock = pygame.time.Clock()
    fov = 60
    angle = 0

    cube_faces = [
        [3, 2, 1, 0],
        [4, 5, 6, 7],
        [4, 0, 1, 5],
        [6, 2, 3, 7],
        [7, 3, 0, 4],
        [5, 1, 2, 6]
    ]

    face_colors = [
        (255, 0, 0),
        (0, 255, 0),
        (0, 0, 255),
        (255, 255, 0),
        (0, 255, 255),
        (255, 0, 255)
    ]

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
            projected_vertices.append((screen_pos.x, screen_pos.y))

        visible_faces = []
        for i, face in enumerate(cube_faces):
            face_3d = [rotated_vertices[idx] for idx in face]
            if is_face_visible(face_3d):
                depth = calculate_face_depth(face_3d)
                visible_faces.append((depth, i, face))

        visible_faces.sort(reverse=True, key=lambda x: x[0])

        for depth, i, face in visible_faces:
            polygon_points = [projected_vertices[idx] for idx in face]
            pygame.draw.polygon(sc, face_colors[i], polygon_points)
            pygame.draw.polygon(sc, (255, 255, 255), polygon_points, 1)

        for edge in cube_edges:
            start = projected_vertices[edge[0]]
            end = projected_vertices[edge[1]]
            pygame.draw.line(sc, (255, 255, 255), start, end, 1)

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
