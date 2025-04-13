def parse_obj(file_path):
    vertices = []
    faces = []

    with open(file_path, 'r') as f:
        for line in f:
            if line.startswith('v '):  # вершина
                parts = line.split()
                vertices.append([float(parts[1]), float(parts[2]), float(parts[3])])
            elif line.startswith('f '):  # полигон
                parts = line.split()
                face = []
                for part in parts[1:]:
                    # Обрезаем текстуры/нормали (если есть f v1/vt1/vn1)
                    vertex_index = part.split('/')[0]
                    face.append(int(vertex_index) - 1)  # в OBJ индексы с 1
                faces.append(face)

    return vertices


