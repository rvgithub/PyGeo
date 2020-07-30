from pygeo.intersect import (intersect, _intersect_ray_with_sphere,)
from pygeo.objects import Point, Vector, Ray, Sphere
import pytest

#Task 3: Implement _intersect_ray_and_sphere function
# _intersect_ray_with_sphere

def test__intersect__ray_with_sphere__return_true():
    r1 = Ray((0, 0, 0), (1, 0, 0))
    s1 = Sphere((0, 0, 0), 3)
    d, intersections = intersect(r1, s1)
    calculated_intersections = [Point([3.0, 0.0, 0.0]), Point([-3.0, 0.0, 0.0])]
    d_analytical = 2
    assert ((intersections == calculated_intersections) and (d_analytical == d) ) is True

def test__intersect__ray_with_sphere__return_false():
    r1 = Ray((0, 0, 0), (1, 1, 1))
    s1 = Sphere((10, 10, 10), 3)
    d, intersections = intersect(r1, s1)
    calculated_intersections = [Point([3.0, 0.0, 0.0]), Point([-3.0, 0.0, 0.0])]
    d_analytical = 2
    assert ((intersections == calculated_intersections) and (d_analytical == d) ) is False

  
def test__intersect__ray_not_intersect_with_sphere__return_true():
    r1 = Ray((100, 100, 100), (200, 200, 100))
    s1 = Sphere((0, 0, 0), 5)
    d, intersections = intersect(r1, s1)
    calculated_intersections =[0]
    d_analytical = 0
    assert ((intersections == calculated_intersections) and (d_analytical == d) ) is True
