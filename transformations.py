from vectors import *
import math
import numpy as np

def transform3dto2d(vector3, fov):
    angleRadians = math.radians(fov)
    tan_half_fov = math.tan(angleRadians / 2)
    x_proj = vector3.x / (vector3.z * tan_half_fov)
    y_proj = vector3.y / (vector3.z * tan_half_fov)  
    x_normalized = (x_proj + 1) / 2 
    y_normalized = (1 - y_proj) / 2  
    return Vector2(x_normalized, y_normalized)
    
def rotate(vector3, axis, angle):
    rotationMatrixX = np.array([[1, 0, 0], [0, math.cos(angle), -math.sin(angle)], [0, math.sin(angle), math.cos(angle)]])
    rotationMatrixY = np.array([[math.cos(angle), 0, math.sin(angle)], [0, 1, 0], [-math.sin(angle), 0, math.cos(angle)]])
    rotationMatrixz = np.array([[math.cos(angle), -math.sin(angle), 0], [math.sin(angle), math.cos(angle), 0], [0, 0, 1]])
    vector3 = np.array([vector3.x, vector3.y, vector3.z])
    if axis == 'x':
        return Vector3(vector3.dot(rotationMatrixX)[0], vector3.dot(rotationMatrixX)[1], vector3.dot(rotationMatrixX)[2])
    if axis == 'y':
        return Vector3(vector3.dot(rotationMatrixY)[0], vector3.dot(rotationMatrixY)[1], vector3.dot(rotationMatrixY)[2])
    if axis == 'z':
        return Vector3(vector3.dot(rotationMatrixz)[0], vector3.dot(rotationMatrixz)[1], vector3.dot(rotationMatrixz)[2]

def sstopgcord(vector2, screenwidth, screenheight):
    return Vector2(int(vector2.x * screenwidth),
            int(vector2.y * screenheight))

