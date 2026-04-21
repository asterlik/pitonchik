
import math

def volume(a, b, c):
    """объём"""
    return a * b * c

def surface_area(a, b, c):
    """площадь пп"""
    return 2 * (a*b + a*c + b*c)

def mass(vol, density):
    """масса = объём * плотность"""
    return vol * density