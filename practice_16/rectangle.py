#Откройте сайт «Дом питомца» и на основе имеющихся в нем данных создайте конструктор класса Cat со следующими параметрами:
# имя, пол, возраст.
#В отдельный файл импортируйте и создайте объект Cat, который выводит имеющихся на сайте котов, с одинаковыми параметрами, но с разными значениями.

#Исходники с кодом выкладывайте в репозиторий Github, призывайте для проверки ментора в Slack.


class Cat:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def getName(self):
        return self.name

    def getGender(self):
        return self.gender

    def getAge(self):
        return self.age

