import numpy as np
import math
from point import *


class Shape:
    start_position = Point(0, 0)
    points = []
    anchors = []

    def __init__(self):
        self.start_position = Point(0, 0)
        self.anchors = []
        self.points = []

    def transform(self, i_hat, j_hat):
        linear_trans = self.__matriculated([i_hat.get_list(), j_hat.get_list()])
        vectors = []
        for vector in self.anchors:
            vectors.append(vector.get_list())
        base_matrix = self.__matriculated(vectors)
        res_matrix = np.dot(linear_trans, base_matrix)
        pos = self.__dismatriculated(res_matrix)
        index = 0
        while index < len(self.anchors):
            self.anchors[index] = pos[index]
            index += 1
        self.build_point_by_anchors()

    def build_point_by_anchors(self):
        i = 0
        self.points.clear()
        while i < len(self.anchors):
            self.points.append(Point(self.anchors[i].x + self.start_position.x, self.anchors[i].y + self.start_position.y))
            i += 1

    def __matriculated(self, vectors):
        up = []
        bottom = []
        for vector in vectors:
            up.append(vector[0])
            bottom.append(vector[1])
        return np.array([up, bottom])

    def __dismatriculated(self, matrix):
        vecs = []
        index = 0
        while index < len(self.anchors):
            vecs.append(Point(matrix[0][index], matrix[1][index]))
            index += 1
        return vecs

    def __str__(self):
        a_str = ""
        for a in self.anchors:
            a_str += str(a) + ","
        p_str = ""
        for p in self.points:
            p_str += str(p) + ","
        return "anchors:" + a_str + "\npoints:"+p_str

    def get_point_list(self):
        res = []
        for p in self.points:
            res.append(p.x)
            res.append(p.y)
        return res

    def move_x(self, step):
        self.start_position.x += step
        self.build_point_by_anchors()

    def move_y(self, step):
        self.start_position.y += step
        self.build_point_by_anchors()

    def move(self, x, y):
        self.start_position.x += x
        self.start_position.y += y
        self.build_point_by_anchors()

    def clone(self):
        return Shape()


class Triangle(Shape):

    @property
    def length(self):
        return self.__length

    def __init__(self, start_position, length):
        Shape.__init__(self)
        self.start_position = start_position
        self.__length = length
        self.anchors.append(Point(0, 0.5*length/math.cos(math.pi/6)))
        self.anchors.append(Point(0, 0.5*length/math.cos(math.pi/6)))
        self.anchors.append(Point(-0.5*length, -0.5*length*math.tan(math.pi/6)))
        self.anchors.append(Point(0.5*length, -0.5*length*math.tan(math.pi/6)))
        self.build_point_by_anchors()

    def clone(self):
        ct = Triangle(self.start_position.clone(), self.__length)
        ct.anchors.clear()
        ct.points.clear()
        for a in self.anchors:
            ct.anchors.append(a.clone())
        for p in self.points:
            ct.points.append(p.clone())
        return ct


class Rectangle(Shape):
    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    def __init__(self, start_position, width, height):
        Shape.__init__(self)
        self.start_position = start_position
        self.__width = width
        self.__height = height
        self.anchors.append(Point(width*(-0.5), height*0.5))
        self.anchors.append(Point(width*0.5, height*0.5))
        self.anchors.append(Point(width*0.5, height*(-0.5)))
        self.anchors.append(Point(width*(-0.5), height*(-0.5)))
        self.build_point_by_anchors()

    def clone(self):
        cr = Rectangle(self.start_position.clone(), self.width, self.height)
        cr.anchors.clear()
        cr.points.clear()
        for a in self.anchors:
            cr.anchors.append(a.clone())
        for p in self.points:
            cr.points.append(p.clone())
        return cr


class Oval(Shape):
    @property
    def major_axis(self):
        return self.__major_axis

    @property
    def minor_axis(self):
        return self.__minor_axis

    def __init__(self, start_position, major_axis, minor_axis):
        Shape.__init__(self)
        self.start_position = start_position
        self.__major_axis = major_axis
        self.__minor_axis = minor_axis
        self.anchors.append(Point(major_axis*(-0.5), minor_axis*0.5))
        self.anchors.append(Point(major_axis*0.5, minor_axis*(-0.5)))
        self.build_point_by_anchors()

    def clone(self):
        co = Oval(self.start_position.clone(), self.major_axis, self.minor_axis)
        co.anchors.clear()
        co.points.clear()
        for a in self.anchors:
            co.anchors.append(a.clone())
        for p in self.points:
            co.points.append(p.clone())
        return co

