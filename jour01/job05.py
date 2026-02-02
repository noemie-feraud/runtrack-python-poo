# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y 
#     def afficher_points(self):
#         print(f"x = {self.x}, y = {self.y}")

#     def afficher_x(self):
#         print(self.x)

#     def afficher_y(self):
#         print(self.y)

#     def changer_x(self, nouveau_x):
#         self.x = nouveau_x
#         nouveau_x += 2

#     def changer_y(self, nouveau_y):
#         self.y = nouveau_y
#         nouveau_y += 5
# points = Point(3, 5)
# points.afficher_points()

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def afficher_points(self):
        print (f" x = {self.x}, y = {self.y}")

    def afficher_x(self):
        print(f" x = {self.x}")

    def afficher_y(self):
        print(f" y = {self.y}")

    def changer_x(self, nouveau_x):
        self.x = nouveau_x

    def changer_y(self, nouveau_y):
        self.y = nouveau_y

points = Point(5,6)
points.afficher_points()

points.changer_x(20)
points.afficher_x()

points.changer_y(32)
points.afficher_y()

