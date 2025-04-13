![image](https://github.com/user-attachments/assets/bdc49986-b80d-4e94-bfb4-0ff9963d226a)# 🚀 Pygame 3D Renderer  

**Pure 3D Rendering with Pygame (No OpenGL)** — A simple and efficient library for 3D graphics from scratch  

[![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)  
[![Pygame](https://img.shields.io/badge/pygame-2.0+-green.svg)](https://www.pygame.org/news)  

## 🌟 Features  

- 🐍 Fully written in Python (no OpenGL dependencies)  
- 🎨 Simple API for quick 3D graphics development  
- 📦 Core 3D primitives support (starting with triangles)  
- 🔄 Built-in transformations (rotation, translation)  
- 🖌️ Flexible object appearance customization  
- 👁️‍🗨️ Camera with perspective projection  

## 🛠 Installation  

1. Ensure you have Python 3.7+ installed  
2. Install Pygame:  

```bash  
pip install pygame  
```  

3. Clone the repository or add the `corelibs` files to your project  

## 🏁 Quick Start  

```python  
import pygame  
from corelibs import core  
from corelibs.transformations import Vector3  

# Initialization  
pygame.init()  
screen = pygame.display.set_mode((800, 600))  
camera = core.Camera(Vector3(0, 0, -5), 60)  

# Create a 3D triangle  
triangle = core.Triangle(  
    Vector3(-1, -1, 0),  
    Vector3(1, -1, 0),  
    Vector3(0, 1, 0)  
)  

# Configure appearance  
triangle.configure(  
    shaded=True,               # Enable shading  
    color=(255, 0, 0),        # Red color  
    outlinded=True,           # Enable outline  
    outline_color=(255, 255, 255)  # White outline  
)  

# Main loop  
running = True  
while running:  
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            running = False  
    
    screen.fill((0, 0, 0))  # Clear screen  
    
    # Rotate and render  
    triangle.rotate(Vector3(0, 0.01, 0))  
    triangle.draw(screen, camera)  
    
    pygame.display.flip()  
    pygame.time.Clock().tick(60)  

pygame.quit()  
```  

## 📚 API Documentation  

### `Triangle(v1: Vector3, v2: Vector3, v3: Vector3)`  
Creates a 3D triangle with specified vertices.  

**Parameters:**  
- `v1`, `v2`, `v3`: Triangle vertices in 3D space  

### `configure(shaded: bool, color: tuple, outlinded: bool, outline_color: tuple)`  
Configures the triangle's appearance.  

**Parameters:**  
- `shaded`: Enable/disable shading  
- `color`: Fill color (RGB)  
- `outlinded`: Enable/disable outline  
- `outline_color`: Outline color (RGB)  

### `rotate(angle_vector: Vector3)`  
Rotates the triangle around axes.  

**Parameters:**  
- `angle_vector`: Rotation angles for X, Y, Z axes  

### `draw(screen: pygame.Surface, camera: Camera)`  
Renders the triangle on screen.  

**Parameters:**  
- `screen`: Pygame surface for rendering  
- `camera`: Camera for projection  

### `Camera(position: Vector3, fov: float)`  
Creates a camera for 3D scenes.  

**Parameters:**  
- `position`: Camera position in 3D space  
- `fov`: Field of view (in degrees)  

## 🎯 Usage Examples  

### Creating a Cube from Triangles  
```python  
# Create 12 triangles (2 per cube face)  
# ... cube creation code ...  

# In the main loop:  
for triangle in cube_triangles:  
    triangle.rotate(Vector3(0.01, 0.02, 0.005))  
    triangle.draw(screen, camera)  
```  

### Camera Control  
```python  
camera.position.z += 0.1  # Zoom in  
camera.position.y -= 0.1  # Move up  
```  

## 🤝 Contributing  
1. Fork the repository  
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)  
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)  
4. Push to the branch (`git push origin feature/AmazingFeature`)  
5. Open a Pull Request  

## 📜 License  
Distributed under the MIT License. See `LICENSE` for details.

## Gallery 

`Triangle.py (Latest)`

![image](https://github.com/user-attachments/assets/929f0341-72dd-4fe0-b905-9d77a8712872)


`Vertices coordinates`

![Component 1](https://github.com/user-attachments/assets/a0236825-a15e-4e4b-a671-f723759bf587)

`outdated/cubeshaded.py`

![image](https://github.com/user-attachments/assets/5ea9d77f-b18c-424b-841f-a7424d2e3827)

`outdated/render_q.py`

![image](https://github.com/user-attachments/assets/d9502b04-747e-4b32-9a36-d0340381dfa5)

![image](https://github.com/user-attachments/assets/b53ac122-89c5-4fe0-80fe-ec2fda2e131b)

![image](https://github.com/user-attachments/assets/0eb44e9f-781b-4e93-b9b9-50fd569a5816)

`outdated/main.py`

![image](https://github.com/user-attachments/assets/9224a29e-d032-4d4f-adbd-3432f298e701)




