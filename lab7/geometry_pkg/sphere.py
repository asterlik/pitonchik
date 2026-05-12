from .base import GeometricBody
import math

class Sphere(GeometricBody):
    def __init__(self, radius, material, density):
        super().__init__(material, density)
        self._radius = radius
    
    @property
    def radius(self):
        return self._radius
    @radius.setter
    def radius(self, v):
        if v <= 0: raise ValueError("Радиус > 0")
        self._radius = v
        self._invalidate_cache()
    
    def calculate_volume(self):
        if self._cached_volume is None:
            self._cached_volume = (4/3) * math.pi * self.radius**3
        return self._cached_volume
    
    def calculate_surface_area(self):
        if self._cached_area is None:
            self._cached_area = 4 * math.pi * self.radius**2
        return self._cached_area
    
    def __str__(self):
        return f"Шар(радиус={self.radius} см)"