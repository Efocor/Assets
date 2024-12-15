#..... Código simple de FERI para rotaciones (referencia de las mismas y sus coordenadas) .....
import matplotlib.pyplot as plt
import numpy as np

def rotamos_coordenadas(coords, ang):
    """
    Rota las coordenadas de acuerdo al ángulo (90, 180, 270 grados).
    Básicamente tomamos una matriz o vector y las giramos.
    """
    if ang == 90:
        return [(y, -x) for x, y in coords]
    elif ang == 180:
        return [(-x, -y) for x, y in coords]
    elif ang == 270:
        return [(-y, x) for x, y in coords]
    else:
        return coords  # No rotation (original)

def normalizamos_coordenadas(coords):
    """
    Normalizo las coordenadas para que siempre se mantengan dentro del cuadrante positivo
    y con la base en el eje y = 0.
    """
    #Las desplazamos a las coordenadas para que el punto más bajo quede en el eje y = 0 (para mi referencia)
    min_y = min(y for _, y in coords)
    normalizadas_coords = [(x, y - min_y) for x, y in coords]
    
    #Aseguro de que todas las coordenadas estén en el cuadrante positivo
    min_x = min(x for x, _ in normalizadas_coords)
    normalizadas_coords = [(x - min_x, y) for x, y in normalizadas_coords]
    
    return normalizadas_coords

def plot_coordenadas(coords, titulito):
    """
    Muestra esas coordenadas en un gráfico.
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
    plt.title(titulito)
    plt.grid(True)
    plt.show()

#Matrices de una letra "F" y "I grande"
letra_F_coords = [
    [(1, 0), (1, 1), (0, 2), (1, 2), (2, 2)], # Original o sea sin giro.
    [(0, 0), (0, 1), (1, 1), (0, 2), (0, 3)], # 90°
    [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)], # 180°
    [(0, 0), (1, 0), (0, 1), (0, 2), (0, 3)]  # 270°
]

letra_E_coords = [
    [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)], # Original
    [(2, 0), (2, 1), (2, 2), (2, 3), (2, 4)], # 90°
    [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)], # 180°
    [(2, 0), (2, 1), (2, 2), (2, 3), (2, 4)]  # 270°
]

#.....Aquí la letra F y sus rotaciones
for idx, coords in enumerate(letra_F_coords):
    normalizadas_coords = normalizamos_coordenadas(coords)
    plot_coordenadas(normalizadas_coords, f"F Rotada {90*idx}°")

#.....Aquí el caso de la letra E grande y sus rotaciones
for idx, coords in enumerate(letra_E_coords):
    normalizadas_coords = normalizamos_coordenadas(coords)
    plot_coordenadas(normalizadas_coords, f"E Grande Rotada {90*idx}°")

#...... Uso para referencia ......
