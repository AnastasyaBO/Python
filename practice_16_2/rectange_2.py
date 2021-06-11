from rectange import Rectange, Square, Round

rec_1 = Rectange(3, 4)
rec_2 = Rectange(12, 5)

square_1 = Square(5)
square_2 = Square(10)

round_1 = Round(2)
round_2 = Round(3)


figures = [rec_1, rec_2, square_1, square_2, round_1, round_2]

for figure in figures:
    if isinstance(figure, Square):
        print(figure.get_area_square())

    elif isinstance(figure, Round):
        print(figure.get_area_round())

    else:
        print(figure.get_area())
