
import math

def volume(r):
    return (4/3) * math.pi * r**3

def surface_area(r):
    return 4 * math.pi * r**2

def mass(vol, density):
    return vol * density