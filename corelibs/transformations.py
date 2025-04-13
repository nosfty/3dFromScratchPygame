
import math
import numpy as np

### Moved from Vectors.py beacuse i have bug with importing
class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y



class Vector3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
###


def transform3dto2d(vector3, fov):


    ## Transform World Space coordinates to Camera Space Coordinates
    ## bugfixes and improvements are required.




    angleRadians = math.radians(fov)
    tan_half_fov = math.tan(angleRadians / 2)


    x_proj = vector3.x / (vector3.z * tan_half_fov)
    y_proj = vector3.y / (vector3.z * tan_half_fov)


    x_normalized = (x_proj + 1) / 2
    y_normalized = (1 - y_proj) / 2

    return Vector2(x_normalized, y_normalized)



def rotate(vector3, axis, angle):

    ## Rotation of 3D Vector3 around a given axis.

    # Using: Rotate(Vector3[x,y,z], 'x' or 'y' or 'z', angle)

    rotationMatrixX = np.array([[1, 0, 0], [0, math.cos(angle), -math.sin(angle)], [0, math.sin(angle), math.cos(angle)]])
    rotationMatrixY = np.array([[math.cos(angle), 0, math.sin(angle)], [0, 1, 0], [-math.sin(angle), 0, math.cos(angle)]])
    rotationMatrixz = np.array([[math.cos(angle), -math.sin(angle), 0], [math.sin(angle), math.cos(angle), 0], [0, 0, 1]])

    vector3 = np.array([vector3.x, vector3.y, vector3.z])

    if axis == 'x':
        return Vector3(vector3.dot(rotationMatrixX)[0], vector3.dot(rotationMatrixX)[1], vector3.dot(rotationMatrixX)[2])
    if axis == 'y':
        return Vector3(vector3.dot(rotationMatrixY)[0], vector3.dot(rotationMatrixY)[1], vector3.dot(rotationMatrixY)[2])
    if axis == 'z':
        return Vector3(vector3.dot(rotationMatrixz)[0], vector3.dot(rotationMatrixz)[1], vector3.dot(rotationMatrixz)[2])



def sstopgcord(vector2, screenwidth, screenheight):

    ## Screen Space to PygameGame Coordinates
    ## Like [-1,1] to [600,400]

    return Vector2(int(vector2.x * screenwidth),
            int(vector2.y * screenheight))



def translate3d(vector3:Vector3, cortVec3:Vector3):


    # Translate the 3D vector3 around the cartesian origin

    # Honestly we need to get positions of vertecies, buy it low level library i wont touch this

    translatematrix = np.array([[1, 0, 0, cortVec3.x], [0, 1, 0, cortVec3.y], [0, 0, 1, cortVec3.z], [0, 0, 0, 1]])

    return vector3(vector3.dot(translatematrix)[0], vector3.dot(translatematrix)[1], vector3.dot(translatematrix)[2])



