from .base import GeometricBody

class Parallelepiped(GeometricBody):
    def __init__(self, a, b, c, material, density):
        super().__init__(material, density)
        self._a, self._b, self._c = a, b, c
    
    @property
    def a(self):
        return self._a
    @a.setter
    def a(self, v):
        if v <= 0: raise ValueError("Длина > 0")
        self._a = v
        self._invalidate_cache()
    
    @property
    def b(self):
        return self._b
    @b.setter
    def b(self, v):
        if v <= 0: raise ValueError("Ширина > 0")
        self._b = v
        self._invalidate_cache()
    
    @property
    def c(self):
        return self._c
    @c.setter
    def c(self, v):
        if v <= 0: raise ValueError("Высота > 0")
        self._c = v
        self._invalidate_cache()
    
    def calculate_volume(self):
        if self._cached_volume is None:
            self._cached_volume = self.a * self.b * self.c
        return self._cached_volume
    
    def calculate_surface_area(self):
        if self._cached_area is None:
            self._cached_area = 2 * (self.a*self.b + self.a*self.c + self.b*self.c)
        return self._cached_area
    
    def __str__(self):
        return f"Параллелепипед({self.a}x{self.b}x{self.c} см)"