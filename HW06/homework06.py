import math
# ------------------- 點 -------------------
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def translate(self, dx, dy):
        return Point(self.x + dx, self.y + dy)

    def scale(self, factor):
        return Point(self.x * factor, self.y * factor)

    def rotate(self, degree):
        rad = math.radians(degree)
        x_new = self.x * math.cos(rad) - self.y * math.sin(rad)
        y_new = self.x * math.sin(rad) + self.y * math.cos(rad)
        return Point(x_new, y_new)
# ------------------- 直線 -------------------
class Line:
    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        return f"Line({self.p1}, {self.p2})"

    def slope(self):
        if self.p2.x == self.p1.x:
            return None
        return (self.p2.y - self.p1.y) / (self.p2.x - self.p1.x)

    def intercept(self):
        m = self.slope()
        if m is None:
            return None
        return self.p1.y - m * self.p1.x

    def intersect_line(self, other):
        m1, b1 = self.slope(), self.intercept()
        m2, b2 = other.slope(), other.intercept()

        if m1 is None: 
            x = self.p1.x
            y = m2 * x + b2
        elif m2 is None:
            x = other.p1.x
            y = m1 * x + b1
        elif m1 == m2:
            return None 
        else:
            x = (b2 - b1) / (m1 - m2)
            y = m1 * x + b1
        return Point(x, y)

    def perpendicular_from_point(self, pt: Point):
        m = self.slope()
        if m is None:
            foot = Point(self.p1.x, pt.y)
        elif m == 0:
            foot = Point(pt.x, self.p1.y)
        else:
            m_perp = -1 / m
            b_perp = pt.y - m_perp * pt.x
            b = self.intercept()
            x = (b - b_perp) / (m_perp - m)
            y = m * x + b
            foot = Point(x, y)
        return foot
# ------------------- 圓 -------------------
class Circle:
    def __init__(self, center: Point, radius):
        self.center = center
        self.radius = radius

    def __repr__(self):
        return f"Circle(center={self.center}, r={self.radius})"

    def intersect_circle(self, other):
        x0, y0, r0 = self.center.x, self.center.y, self.radius
        x1, y1, r1 = other.center.x, other.center.y, other.radius

        dx = x1 - x0
        dy = y1 - y0
        d = math.hypot(dx, dy)
        if d > r0 + r1 or d < abs(r0 - r1):
            return [] 

        a = (r0**2 - r1**2 + d**2) / (2*d)
        h = math.sqrt(r0**2 - a**2)
        x2 = x0 + a * dx / d
        y2 = y0 + a * dy / d

        rx = -dy * (h / d)
        ry = dx * (h / d)

        p1 = Point(x2 + rx, y2 + ry)
        p2 = Point(x2 - rx, y2 - ry)
        if p1.x == p2.x and p1.y == p2.y:
            return [p1]
        return [p1, p2]

    def intersect_line(self, line: Line):
        x0, y0 = self.center.x, self.center.y
        x1, y1 = line.p1.x, line.p1.y
        x2, y2 = line.p2.x, line.p2.y

        dx = x2 - x1
        dy = y2 - y1

        a = dx**2 + dy**2
        b = 2 * (dx*(x1 - x0) + dy*(y1 - y0))
        c = (x1 - x0)**2 + (y1 - y0)**2 - self.radius**2

        disc = b**2 - 4*a*c
        if disc < 0:
            return []
        elif disc == 0:
            t = -b / (2*a)
            return [Point(x1 + t*dx, y1 + t*dy)]
        else:
            sqrt_disc = math.sqrt(disc)
            t1 = (-b + sqrt_disc) / (2*a)
            t2 = (-b - sqrt_disc) / (2*a)
            p1 = Point(x1 + t1*dx, y1 + t1*dy)
            p2 = Point(x1 + t2*dx, y1 + t2*dy)
            return [p1, p2]
# ------------------- 三角形 -------------------
class Triangle:
    def __init__(self, p1: Point, p2: Point, p3: Point):
        self.p1, self.p2, self.p3 = p1, p2, p3

    def __repr__(self):
        return f"Triangle({self.p1}, {self.p2}, {self.p3})"

    def translate(self, dx, dy):
        return Triangle(self.p1.translate(dx, dy),
                        self.p2.translate(dx, dy),
                        self.p3.translate(dx, dy))

    def scale(self, factor):
        return Triangle(self.p1.scale(factor),
                        self.p2.scale(factor),
                        self.p3.scale(factor))

    def rotate(self, degree):
        return Triangle(self.p1.rotate(degree),
                        self.p2.rotate(degree),
                        self.p3.rotate(degree))
line = Line(Point(0, 0), Point(10, 0))
pt = Point(3, 4)
foot = line.perpendicular_from_point(pt)

# 計算三角形三邊長
a = math.hypot(pt.x - foot.x, pt.y - foot.y) 
b = math.hypot(foot.x - 0, foot.y - 0) 
c = math.hypot(pt.x - 0, pt.y - 0) 

print("三角形邊長:", a, b, c)
print("驗證畢氏定理:", math.isclose(a**2 + b**2, c**2))
