from shapes import *
from point import *


class ShapePainter:
    @property
    def shapes(self):
        return self.__shapes

    @shapes.setter
    def shapes(self, value):
        if type(value) == list:
            self.__shapes = value
        else:
            self.__shapes = [value]
        self.__draw(self.__pen_color)

    @property
    def canvas(self):
        return self.__canvas

    @canvas.setter
    def canvas(self, value):
        self.__canvas = value

    def __init__(self, canvas, shapes, pen_color="black"):
        self.__canvas = canvas
        self.__ids = []
        self.__pen_color = pen_color
        self.shapes = shapes

    def __draw(self, pen_color, color_str="white"):
        for shape in self.shapes:
            points = shape.get_point_list()
            if type(shape) == Oval:
                self.__ids.append(self.canvas.create_oval(*points, outline=pen_color, fill=color_str))
            else:
                self.__ids.append(self.canvas.create_polygon(*points, outline=pen_color, fill=color_str))

    def drop(self):
        for id in self.__ids:
            self.canvas.delete(id)
        self.__ids.clear()

    def fill(self, color_str="white"):
        pen_color = "black" if color_str == "white" else color_str
        self.drop()
        self.__draw(color_str, pen_color)

    def move_x(self, step):
        for shape in self.shapes:
            shape.move_x(step)
        for id in self.__ids:
            self.canvas.move(id, step, 0)

    def move_y(self, step):
        for shape in self.shapes:
            shape.move_y(step)
        for id in self.__ids:
            self.canvas.move(id, 0, step)

    def move(self, x, y):
        for shape in self.shapes:
            shape.move(x, y)
        for id in self.__ids:
            self.canvas.move(id, x, y)
