import math


class Shape:
    def area(self):
        return 0

    def perimeter(self):
        return 0

    def vertices(self):
        return 0


class Triangle(Shape):
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1, self.y1 = x1, y1
        self.x2, self.y2 = x2, y2
        self.x3, self.y3 = x3, y3

    def area(self):
        return abs((self.x1 * (self.y2 - self.y3) + self.x2 * (self.y3 - self.y1) + self.x3 * (self.y1 - self.y2)) / 2)

    def perimeter(self):
        side1 = math.sqrt((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2)
        side2 = math.sqrt((self.x3 - self.x2) ** 2 + (self.y3 - self.y2) ** 2)
        side3 = math.sqrt((self.x1 - self.x3) ** 2 + (self.y1 - self.y3) ** 2)
        return side1 + side2 + side3

    def vertices(self):
        return 3


class Rectangle(Shape):
    def __init__(self, x1, y1, x2, y2):
        self.x1, self.y1 = x1, y1
        self.x2, self.y2 = x2, y2

    def area(self):
        width = abs(self.x2 - self.x1)
        height = abs(self.y2 - self.y1)
        return width * height

    def perimeter(self):
        width = abs(self.x2 - self.x1)
        height = abs(self.y2 - self.y1)
        return 2 * (width + height)

    def vertices(self):
        return 4


class Circle(Shape):
    def __init__(self, x, y, radius):
        self.x, self.y = x, y
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

    def perimeter(self):
        return 2 * math.pi * self.radius

    def vertices(self):
        return 0


class Polygon(Shape):
    def __init__(self, x, y, radius, sides):
        self.x, self.y = x, y
        self.radius = radius
        self.sides = sides

    def area(self):
        side = 2 * self.radius * math.sin(math.pi / self.sides)
        return (self.sides * side * side) / (4 * math.tan(math.pi / self.sides))

    def perimeter(self):
        import math
        side = 2 * self.radius * math.sin(math.pi / self.sides)
        return self.sides * side

    def vertices(self):
        return self.sides


class ShapeCollection:
    def __init__(self):
        self.shapes = []

    def add_shape(self, shape):
        self.shapes.append(shape)

    def total_area(self):
        total = 0
        for shape in self.shapes:
            total += shape.area()
        return total

    def total_perimeter(self):
        total = 0
        for shape in self.shapes:
            total += shape.perimeter()
        return total

    def total_vertices(self):
        total = 0
        for shape in self.shapes:
            total += shape.vertices()
        return total


def main():
    collection = ShapeCollection()

    print("Вводите фигуры в формате: тип параметры")
    print("Доступные типы: triangle, rectangle, circle, polygon")
    print("Примеры:")
    print("triangle 0 0 1 0 0 1")
    print("rectangle 0 0 3 2")
    print("circle 1 1 5")
    print("polygon 0 0 5 10")
    print("Для завершения ввода нажмите enter")
    print()

    while True:
        try:
            input_str = input("Введите фигуру: ").strip()

            if input_str.lower() == '':
                break

            if not input_str:
                continue

            parts = input_str.split()
            shape_type = parts[0].lower()

            if shape_type == 'triangle':
                if len(parts) != 7:
                    print("Ошибка: для треугольника нужно 6 координат (x1 y1 x2 y2 x3 y3)")
                    continue

                x1, y1, x2, y2, x3, y3 = map(float, parts[1:7])
                triangle = Triangle(x1, y1, x2, y2, x3, y3)
                if triangle.area() == 0:
                    print("Ошибка: точки не образуют треугольник")
                    continue
                collection.add_shape(triangle)
                print("Треугольник добавлен")

            elif shape_type == 'rectangle':
                if len(parts) != 5:
                    print("Ошибка: для прямоугольника нужно 4 координаты (x1 y1 x2 y2)")
                    continue

                x1, y1, x2, y2 = map(float, parts[1:5])
                if x1 == x2 or y1 == y2:
                    print("Ошибка: прямоугольник вырожден в линию")
                    continue
                rectangle = Rectangle(x1, y1, x2, y2)
                collection.add_shape(rectangle)
                print("Прямоугольник добавлен")

            elif shape_type == 'circle':
                if len(parts) != 4:
                    print("Ошибка: для круга нужно 3 параметра (x y radius)")
                    continue

                x, y, radius = map(float, parts[1:4])
                if radius <= 0:
                    print("Ошибка: радиус должен быть положительным")
                    continue
                circle = Circle(x, y, radius)
                collection.add_shape(circle)
                print("Круг добавлен")

            elif shape_type == 'polygon':
                if len(parts) != 5:
                    print("Ошибка: для многоугольника нужно 4 параметра (x y radius sides)")
                    continue

                x, y, radius, sides = map(float, parts[1:5])
                if radius <= 0:
                    print("Ошибка: радиус должен быть положительным")
                    continue
                if sides < 3:
                    print("Ошибка: количество сторон должно быть не меньше 3")
                    continue
                polygon = Polygon(x, y, radius, int(sides))
                collection.add_shape(polygon)
                print("Многоугольник добавлен")

            else:
                print(f"Ошибка: неизвестный тип фигуры '{shape_type}'")

        except ValueError:
            print("Ошибка: некорректные числовые значения")
        except Exception as e:
            print(f"Ошибка: {e}")

    print()
    print("Введите команду для подсчета:")
    print("1. area - общая площадь всех фигур")
    print("2. perimeter - суммарный периметр")
    print("3. vertices - суммарное количество углов")
    print("4. all - все показатели")
    print("0. exit - выход")
    print()

    while True:
        command = input("Команда: ").strip().lower()

        if command == '0':
            break

        elif command == '1':
            area = collection.total_area()
            print(f"Total area: {area:.2f}")

        elif command == '2':
            perimeter = collection.total_perimeter()
            print(f"Total perimeter: {perimeter:.2f}")

        elif command == '3':
            vertices = collection.total_vertices()
            print(f"Total vertices: {vertices}")

        elif command == '4':
            area = collection.total_area()
            perimeter = collection.total_perimeter()
            vertices = collection.total_vertices()
            print(f"Total area: {area:.2f}")
            print(f"Total perimeter: {perimeter:.2f}")
            print(f"Total vertices: {vertices}")

        else:
            print("Неизвестная команда")

        print()


if __name__ == "__main__":
    main()
