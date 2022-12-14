class Book:
    def __init__(self, page, time, img):
        self.page = page
        self.time = time
        self.img = img


    def __str__(self):
        return f'количество страниц {self.page}\n' \
               f'время чтения одной страницы в секундах {self.time}\n' \
               f'количество картинок {self.img}\n' \
               f'время чтения {self.time_r()}\n' \
               f'количество статей/номеров на страницу {self.count()}'

    def __add__(self, other):
        return Book(self.page + other.page, self.time, self.img)

    def time_r(self):
        return (self.page * self.time) / 360

    def count(self):
        return self.img / self.page

class encyclopedia(Book):
    def __init__(self, color):
        super().__init__(1000, 60, 30)
        self.color = color

    def recolor(self):
        self.color = self.color[::-1]

    def __str__(self):
        return super().__str__() + f'\nцвет {self.color}'

class phonebook(Book):
    def __init__(self, page_d):
        super().__init__(60, 15, 30)
        self.page_d = page_d

    def delete(self):
        self.page = 30
        self.img = 15
        self.page_d /= 2

    def __str__(self):
        return super().__str__() + f'\nвырывание страниц {self.page_d}'



o = encyclopedia ("red")
print(type(o), o, sep='\n')
y = phonebook(60)
print(type(y), y, sep='\n')
i = o + y
print('результат сложения:')
print(type(i), i, sep='\n')
print(f'меняем цвет для {type(o)}')
o.recolor()
print(o)
print("Вырываем ненужные страницы")
y.delete()
print(y)
