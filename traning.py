class Astashenkov():
    """Create new Atashenkov man"""

    def __init__(self, name):
        """Setting name and surname"""
        self.surname = 'Astashenkov'
        self.name = name

    def sayHello(self):
        """Introduсe himself"""
        print('My name is ', self.name, ', my surname is ', self.surname)


saveliy = Astashenkov('Saveliy')
egor = Astashenkov('Egor')

saveliy.sayHello()
egor.sayHello()
print(saveliy.surname, saveliy.name)