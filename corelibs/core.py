from corelibs.transformations import Vector3
from corelibs import transformations
import pygame


class Camera:

    def __init__(self, position:Vector3, fov:float):
        self.position = position
        self.fov = fov



class Triangle:

    def __init__(self, v1:Vector3, v2:Vector3, v3:Vector3):
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3

        self.shaded = False
        self.color = None
        self.outlinded = False
        self.outline_color = None

    def configure(self, shaded:bool, color:Vector3, outlinded:bool, outline_color:Vector3):

        # I'll be honest. the shading and outlining settings are not working. I fucked up. todolist.append("please fix this")

        self.shaded = shaded
        self.color = color
        self.outlinded = outlinded
        self.outline_color = outline_color

    def rotate(self, anglevector3:Vector3):

        self.v1 = transformations.rotate(self.v1, "x", anglevector3.x)
        self.v2 = transformations.rotate(self.v2, "x", anglevector3.x)
        self.v3 = transformations.rotate(self.v3, "x", anglevector3.x)

        self.v1 = transformations.rotate(self.v1, "y", anglevector3.y)
        self.v2 = transformations.rotate(self.v2, "y", anglevector3.y)
        self.v3 = transformations.rotate(self.v3, "y", anglevector3.y)

        self.v1 = transformations.rotate(self.v1, "z", anglevector3.z)
        self.v2 = transformations.rotate(self.v2, "z", anglevector3.z)
        self.v3 = transformations.rotate(self.v3, "z", anglevector3.z)


    def draw(self, screen: pygame.Surface, camera: Camera):
        vec_with_camera = Vector3(self.v1.x - camera.position.x, self.v1.y - camera.position.y, self.v1.z - camera.position.z)
        vec_with_camera2 = Vector3(self.v2.x - camera.position.x, self.v2.y - camera.position.y, self.v2.z - camera.position.z)
        vec_with_camera3 = Vector3(self.v3.x - camera.position.x, self.v3.y - camera.position.y, self.v3.z - camera.position.z)

        point1 = transformations.transform3dto2d(vec_with_camera, camera.fov)
        point2 = transformations.transform3dto2d(vec_with_camera2, camera.fov)
        point3 = transformations.transform3dto2d(vec_with_camera3, camera.fov)

        screen_width = screen.get_width()
        screen_height = screen.get_height()

        final_points = [
            [transformations.sstopgcord(point1, screen_width, screen_height).x,
             transformations.sstopgcord(point1, screen_width, screen_height).y],
            [transformations.sstopgcord(point2, screen_width, screen_height).x,
             transformations.sstopgcord(point2, screen_width, screen_height).y],
            [transformations.sstopgcord(point3, screen_width, screen_height).x,
             transformations.sstopgcord(point3, screen_width, screen_height).y]
        ]

        pygame.draw.polygon(screen, self.color, final_points)


    # To Do add more configurations, get_posX, get_posY, get_rotation, get_face_visibility/normal for backface culling. But it works for now. Yay!


    # well, finally, according to the idea, you can already do something low-polygonal.









