import matplotlib.pyplot as plt
import numpy as np

def rotate_coordinates(coords, angle):
    """
    Rota las coordenadas de acuerdo al ángulo (90, 180, 270 grados).
    """
    if angle == 90:
        return [(y, -x) for x, y in coords]
    elif angle == 180:
        return [(-x, -y) for x, y in coords]
    elif angle == 270:
        return [(-y, x) for x, y in coords]
    else:
        return coords  # No rotation (original)

def normalize_coordinates(coords):
    """
    Normaliza las coordenadas para que siempre se mantengan dentro del cuadrante positivo
    y con la base en el eje y = 0.
    """
    # Desplazar las coordenadas para que el punto más bajo quede en el eje y = 0
    min_y = min(y for _, y in coords)
    normalized_coords = [(x, y - min_y) for x, y in coords]
    
    # Asegurarse de que todas las coordenadas estén en el cuadrante positivo
    min_x = min(x for x, _ in normalized_coords)
    normalized_coords = [(x - min_x, y) for x, y in normalized_coords]
    
    return normalized_coords

def plot_coordinates(coords, title):
    """
    Muestra las coordenadas en un gráfico.
    """
    coords = np.array(coords)
    plt.figure(figsize=(5, 5))
    plt.scatter(coords[:, 0], coords[:, 1], color='blue')
    for i, txt in enumerate(coords):
        plt.annotate(f"{txt}", (coords[i, 0] + 0.1, coords[i, 1] + 0.1))
    
    plt.xlim(0, 6)
    plt.ylim(0, 6)
    plt.axhline(0, color='black',linewidth=1)
    plt.axvline(0, color='black',linewidth=1)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.title(title)
    plt.grid(True)
    plt.show()

# Matrices de las letras "F" y "E grande"
letter_F_coords = [
    [(1, 0), (1, 1), (0, 2), (1, 2), (2, 2)], # Original
    [(0, 0), (0, 1), (1, 1), (0, 2), (0, 3)], # 90°
    [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)], # 180°
    [(0, 0), (1, 0), (0, 1), (0, 2), (0, 3)]  # 270°
]

letter_E_coords = [
    [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)], # Original
    [(2, 0), (2, 1), (2, 2), (2, 3), (2, 4)], # 90°
    [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)], # 180°
    [(2, 0), (2, 1), (2, 2), (2, 3), (2, 4)]  # 270°
]

# Mostrar la letra F y sus rotaciones
for idx, coords in enumerate(letter_F_coords):
    normalized_coords = normalize_coordinates(coords)
    plot_coordinates(normalized_coords, f"F Rotated {90*idx}°")

# Mostrar la letra E grande y sus rotaciones
for idx, coords in enumerate(letter_E_coords):
    normalized_coords = normalize_coordinates(coords)
    plot_coordinates(normalized_coords, f"E Grande Rotated {90*idx}°")
