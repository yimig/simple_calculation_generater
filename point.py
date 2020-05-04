class Point:
    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    def __init__(self, x, y=0):
        if type(x) == list:
            y = x[1]
            x = x[0]
        self.x = x
        self.y = y

    def __str__(self):
        return "("+str(self.x)+","+str(self.y)+")"

    def get_list(self):
        return [self.x, self.y]

    def get_vector(self):
        return [[self.x], [self.y]]

    def clone(self):
        return Point(self.x, self.y)
