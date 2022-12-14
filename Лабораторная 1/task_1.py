import doctest

class Laptop:
    def __init__(self, current_percentage: int, genshin: bool):
        if (genshin == 1) and (current_percentage < 100):
            print("Надо поставить ноутбук на зарядку, сейчас разрядится.")
        else: print ("Ноутбук еще долго будет работать.")
        #genshin - включена ли одноименная игра

    def drop(self):
        ...
    def take_to_uni(self):
        ...

class Phys_exam:
    def __init__(self, tutor: str, lessons_attended: int, board: int):
        if (tutor == "Кожевников") and (lessons_attended < 15) and (board == 0):
            print ("Ты отчислен, какой экзамен по физике?")
        else: print("Иди на экзамен за своей троечкой.")
        #tutor - фамилия преподавателя
        #lessons_attended - кол-во посещенных пар
        #board - кол-во раз у доски
        #Я не смогла не написать это, уж слишком жизненно:)
    def pass_exam(self):
        ...
    def be_ill(self):
        ...


class Hunger:
    def __init__(self, hungry_or_not: bool, food_in_fridge: bool):
        if (food_in_fridge == 0) and (hungry_or_not == 0):
            print("А почему такая ситуация? В магазин надо:(")
        elif (hungry_or_not == 1):
            print("Ну а какая тогда разница, сколько еды в холодильнике?")
        else: print("Тогда приятиного аппетита:)")
        #hungry_or_not == 1 человек сыт
    def eat(self):
        ...
    def die_from_hunger(self):
        ...


if __name__ == "__main__":
    situation1 = Laptop(98, 1)
    situation2 = Laptop(45, 0)
    tutor1 = Phys_exam("Кожевников",15,1)
    tutor2 = Phys_exam("Кожевников",10,0)
    tutor3 = Phys_exam("Романов", 7, 0)
    hunger1 = Hunger(1, 0)
    hubger2 = Hunger(0, 0)
    doctest.testmod()
    pass
