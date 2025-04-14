import pygame
import math
import numpy as np
from numba import njit, prange
import time


pygame.init()
WIDTH, HEIGHT = 600, 400 
window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Optimization constants
ASPECT_RATIO = WIDTH / HEIGHT
INV_WIDTH = 1.0 / WIDTH
INV_HEIGHT = 1.0 / HEIGHT

# Scene parameters
SPHERE_CENTER = np.array([0.0 - 0.8, 0.0 - 0.8, 0.0])
SPHERE_RADIUS = 1.0
CAMERA_POS = np.array([0.0, 0.0, -3.0]) 


LIGHT_DISTANCE = 2.0
light_angle = 0.0
LIGHT_SPEED = 0.05

@njit(fastmath=True)
def normalize(v):
    norm = math.sqrt(v[0]**2 + v[1]**2 + v[2]**2)
    return v / norm if norm != 0 else v

@njit(fastmath=True)
def calculate_light_pos(angle):
    x = math.sin(angle) * LIGHT_DISTANCE
    z = math.cos(angle) * LIGHT_DISTANCE
    return normalize(np.array([x, -1.0, z]))

@njit(fastmath=True)
def ray_sphere_intersection(ray_origin, ray_dir, sphere_center, sphere_radius):
    oc = ray_origin - sphere_center
    a = np.dot(ray_dir, ray_dir)
    b = 2.0 * np.dot(oc, ray_dir)
    c = np.dot(oc, oc) - sphere_radius**2
    discriminant = b**2 - 4*a*c

    if discriminant < 0:
        return (np.inf, np.inf)
    sqrt_discr = math.sqrt(discriminant)
    t1 = (-b - sqrt_discr) / (2.0 * a)
    t2 = (-b + sqrt_discr) / (2.0 * a)
    return (t1, t2)

@njit(parallel=True, fastmath=True)
def render_frame(width, height, light_dir, frame_buffer):
    for y in prange(height):
        for x in prange(width):

            nx = (2.0 * (x + 0.5) * INV_WIDTH - 1.0)
            ny = (1.0 - 2.0 * (y + 0.5) * INV_HEIGHT) * (height / width)

            ray_dir = normalize(np.array([nx, ny, 1.0]))
            t1, t2 = ray_sphere_intersection(CAMERA_POS, ray_dir, SPHERE_CENTER, SPHERE_RADIUS)

            if t1 > 0 and t1 != np.inf:
                hit_point = CAMERA_POS + t1 * ray_dir
                normal = normalize(hit_point - SPHERE_CENTER)


                light_vec = -light_dir


                light_intensity = max(0.0, np.dot(normal, light_vec))
                diffuse = light_intensity * 0.8


                ambient = 0.2

 
                if light_intensity > 0:
                    reflect = 2.0 * np.dot(normal, light_vec)
                    reflected_light = normalize(light_vec - normal * reflect)
                    view_dir = -ray_dir
                    specular = max(0.0, np.dot(reflected_light, view_dir))**32
                    metallic = 0.3 * specular
                else:
                    metallic = 0.0

                intensity = min(1.0, diffuse + ambient + metallic)
                col_val = int(255 * intensity)
                color = (col_val, col_val, col_val)
            else:
                color = (0, 0, 0)

            frame_buffer[y, x] = color

def main():
    global light_angle
    frame_buffer = np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint8)

    run = True
    while run:
        start_time = time.time()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        light_angle += LIGHT_SPEED
        light_dir = calculate_light_pos(light_angle)

        render_frame(WIDTH, HEIGHT, light_dir, frame_buffer)

        surf = pygame.surfarray.make_surface(frame_buffer)
        window.blit(surf, (0, 0))
        pygame.display.flip()

        pygame.display.set_caption(f"Raytraced Sphere - {int(clock.get_fps())}FPS")
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()
