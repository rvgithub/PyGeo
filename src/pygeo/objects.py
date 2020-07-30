import numpy as np


class Point:
    """Class representing a point."""

    #method to pass information on the object of the class
    def __init__(self, point):
        self._point = np.array(point, dtype=float)

    def __repr__(self):
        return f"Point({self._point.tolist()})"

    def __add__(self, other):
        if isinstance(other, Vector):
            return Point(self._point + other._vector)
        return NotImplemented

    def __radd__(self, other):
        if isinstance(other, Vector):
            return Point(other._vector + self._point)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Point):
            return Vector(self._point - other._point)
        return NotImplemented

    #method to check if two points are equal
    def __eq__(self, other):
        if isinstance(other, Point):
            return np.array_equal(other._point, self._point)
        return False


class Vector:
    """A vector."""

    #method to pass information on the object of the class
    def __init__(self, vector):
        self._vector = np.array(vector, dtype=float)

    #method that represents the output format of the class
    def __repr__(self):
        return f"Point({self._vector.tolist()})"

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self._vector + other._vector)
        return NotImplemented

    

    #method to check if two vectors are equal
    def __eq__(self, other):
        if isinstance(other, Vector):
            return np.array_equal(other._vector, self._vector)
        return False

    def __mul__(self,other):
        if isinstance(other, Vector):
            return np.dot(self._vector, other._vector)
        if isinstance(other, Point):
            return np.dot(self._vector, other._point)
        if isinstance(other, float) or isinstance(other, int) :
            return Vector(self._vector * other)
        return NotImplemented
    
    
    
#Tasks 1: Implement Ray class.
class Ray (Point, Vector):
    """Class representing a Ray. A ray may be represented as its origin and a direction."""
    
    #__init__ method takes the origin and direction as arguments
    def __init__(self, origin, direction): 
        if not isinstance(origin, Point) :
            if Point(origin) == Point(direction):
                self._origin = ()
                self._direction = ()
                raise Exception("The end point and direction should not be same")
            else:
                self._origin = Point(origin)
                self._direction = Point(direction)
                self._t = self._direction - self._origin
        else:
            if origin == direction:
                self._origin = ()
                self._direction = ()
                raise Exception("The end point and direction should not be same")
            else:
                self._origin = origin
                self._direction = direction
                self._t = self._direction - self._origin

    def __repr__(self):
        return f"Ray{self._origin, self._direction}"

    def __eq__(self,other):
        if isinstance(other, Ray):
            return np.array_equal(other._origin, self._origin) & np.array_equal(other._direction,self._direction)
        return False


#Tasks 2: Implement Sphere class.
class Sphere(Point):
    """Class representing a sphere. A sphere may be represented by its center and a radius."""

    #__init__ method takes the center and radius as arguments
    def __init__(self, center, radius:float):
        if radius<=0:
            return Exception("Radius should be greater than zero.")
        else:
            if not isinstance(center, Point):
                self._center = Point(center)
                self._radius = radius
            elif isinstance(center, Point):
                self._center = center
                self._radius = radius
       
    #method that represents the output format of the class
    def __repr__(self):
        return f"Sphere{self._center,self._radius}"

    #method that compares two spheres by comparing both the center and radius of the other sphere
    def __eq__(self, other):
        if isinstance(other, Sphere):
            return np.array_equal(other._center, self._center) & (other._radius == self._radius)
        return