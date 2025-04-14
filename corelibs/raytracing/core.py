import math

class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector2(self.x * scalar, self.y * scalar)

    def __truediv__(self, scalar):
        return Vector2(self.x / scalar, self.y / scalar)

    def dot(self, other):
        return self.x * other.x + self.y * other.y

    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)

    def normalized(self):
        mag = self.magnitude()
        return Vector2(self.x / mag, self.y / mag) if mag != 0 else Vector2(0, 0)

    def __repr__(self):
        return f"Vector2({self.x}, {self.y})"


class Vector3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __neg__(self):
        return Vector3(-self.x, -self.y, -self.z)

    def __add__(self, other):
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, scalar):
        return Vector3(self.x * scalar, self.y * scalar, self.z * scalar)

    def __truediv__(self, scalar):
        return Vector3(self.x / scalar, self.y / scalar, self.z / scalar)

    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other):
        return Vector3(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )

    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def normalized(self):
        mag = self.magnitude()
        return Vector3(self.x / mag, self.y / mag, self.z / mag) if mag != 0 else Vector3(0, 0, 0)

    def __repr__(self):
        return f"Vector3({self.x}, {self.y}, {self.z})"


class Ray3D:
    def __init__(self, origin: Vector3, direction: Vector3):
        self.origin = origin
        self.direction = direction.normalized()

    def point_at_parameter(self, t: float) -> Vector3:
        return self.origin + self.direction * t

    def __repr__(self):
        return f"Ray3D(origin={self.origin}, direction={self.direction})"


def ray_sphere_intersection(ray: Ray3D, sphere_center: Vector3, sphere_radius: float):
 

    oc = ray.origin - sphere_center


    a = ray.direction.dot(ray.direction)
    b = 2.0 * oc.dot(ray.direction)
    c = oc.dot(oc) - sphere_radius * sphere_radius

    
    discriminant = b * b - 4 * a * c

    if discriminant < 0:
        # Нет пересечений
        return None, None
    elif discriminant == 0:
     
        t = -b / (2.0 * a)
        return t, t
    else:
        
        sqrt_discr = math.sqrt(discriminant)
        t1 = (-b - sqrt_discr) / (2.0 * a)
        t2 = (-b + sqrt_discr) / (2.0 * a)

     
        return (t1, t2) if t1 < t2 else (t2, t1)

