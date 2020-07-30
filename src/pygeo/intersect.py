from pygeo.objects import Point, Ray, Vector, Sphere
import numpy as np

def intersect(first_object, second_object):
    """Function checks if first_object is a Ray and second_object is a sphere.
    And if that is true then _intersect_ray_with_sphere is called."""
    if isinstance(first_object, Ray) & isinstance(second_object, Sphere):
        d, intercepts = _intersect_ray_with_sphere(first_object, second_object)
        return d, intercepts
    else:
        print("Intersection could not be executeed")
        return NotImplemented

def _intersect_ray_with_sphere(ray, sphere):
    """
    A line and a sphere can intersect in three ways:    no intersection at all (delta < 0), 
                                                        at exactly one point i.e. tangent (delta = 0)
                                                        or in two points (delta > 0)
    A function to get intersection of a ray and a sphere and returns points of intersection and number of intersections.
    """
    ray_origin = ray._origin
    ray_direction = ray._direction
    circle_center = sphere._center
    radius = sphere._radius 
    line = ray_direction - ray_origin
        
    a = (circle_center - ray_origin)
    b = (a*a) - ((radius) ** 2)
    delta = ((2 * (line * a))**2) - 4 *((line*line)* b)

    if delta < 0: #no intersection between ray and sphere
        return 0, [0]

    elif delta > 0: #ray intersects the sphere
        d = 2
        d1 = (-2 * b + (np.sqrt(delta)))/(2*a)
        d2 = (-2 * b - (np.sqrt(delta)))/(2*a)
        intersection1 = ray_origin + ((ray_direction - ray_origin) * d1)
        intersection2 = ray_origin + ((ray_direction - ray_origin) * d2)
        intersections = [intersection1, intersection2]
        return d, intersections
    else : #delta =0, one point intersection, ray is a tangent to the sphere
        d = 1
        d1 = (-2*b+(np.sqrt(delta)))/2*a
        intersections = [ray_origin+((ray_direction-ray_origin) * d1)]
        return d, intersections