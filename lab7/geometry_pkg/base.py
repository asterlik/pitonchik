from abc import ABC, abstractmethod

class GeometricBody(ABC):
    def __init__(self, material: str, density: float):
        self._material = material
        self._density = density
        self._cached_volume = None
        self._cached_area = None
    
    @property
    def material(self):
        return self._material
    
    @material.setter
    def material(self, value):
        if not value:
            raise ValueError("Материал не может быть пустым")
        self._material = value
    
    @property
    def density(self):
        return self._density
    
    @density.setter
    def density(self, value):
        if value <= 0:
            raise ValueError("Плотность должна быть > 0")
        self._density = value
    
    def _invalidate_cache(self):
        self._cached_volume = None
        self._cached_area = None
    
    @abstractmethod
    def calculate_volume(self) -> float:
        pass
    
    @abstractmethod
    def calculate_surface_area(self) -> float:
        pass
    
    def calculate_mass(self) -> float:
        return self.calculate_volume() * self.density
    
    def __str__(self):
        return f"{self.__class__.__name__}({self.material}, {self.density} г/см³)"
    
    def __repr__(self):
        return f"<{self.__class__.__name__} at {id(self)}>"
    
    def to_dict(self):
        return {
            'body_type': self.__class__.__name__,
            'material': self.material,
            'density': self.density,
            'volume': self.calculate_volume(),
            'surface_area': self.calculate_surface_area(),
            'mass': self.calculate_mass()
        }