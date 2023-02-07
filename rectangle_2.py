from rectangle import Rectangle, Square, Circle

# создаём два прямоугольника

rect_1 = Rectangle(3, 4)
rect_2 = Rectangle(12, 5)
# Вывод площади двух прямоугольников
print(rect_1.get_area())
print(rect_2.get_area())

# Считаем площать квадратов
square_1 = Square(5)
square_2 = Square(10)

print(square_1.get_area_square(),
      square_2.get_area_square())

# Находим площадь круга
circ_1 = Circle(3)

print(circ_1.get_circle_area())

figures = [rect_1, rect_2, square_1, square_2, circ_1]
for figure in figures:
    if isinstance(figure, Square):
        print(figure.get_area_square())
    elif isinstance(figure, Circle):
        print(figure.get_circle_area())
    else:
        print(figure.get_area())