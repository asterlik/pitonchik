
import math

def volume(a):
    """объём правильного тетраэдра"""
    return a**3 / (6 * math.sqrt(2))

def surface_area(a):
    """площадь поверхности (4 равност треугольника)"""
    return math.sqrt(3) * a**2

def mass(vol, density):
    return vol * density