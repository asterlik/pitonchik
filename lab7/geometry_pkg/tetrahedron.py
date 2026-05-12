from .base import GeometricBody
import math

class Tetrahedron(GeometricBody):
    def __init__(self, edge, material, density):
        super().__init__(material, density)
        self._edge = edge
    
    @property
    def edge(self):
        return self._edge
    @edge.setter
    def edge(self, v):
        if v <= 0: raise ValueError("Ребро > 0")
        self._edge = v
        self._invalidate_cache()
    
    def calculate_volume(self):
        if self._cached_volume is None:
            self._cached_volume = self.edge**3 / (6 * math.sqrt(2))
        return self._cached_volume
    
    def calculate_surface_area(self):
        if self._cached_area is None:
            self._cached_area = math.sqrt(3) * self.edge**2
        return self._cached_area
    
    def __str__(self):
        return f"Тетраэдр(ребро={self.edge} см)"