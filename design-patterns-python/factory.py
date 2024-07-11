class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class PersonFactory:
    def __init__(self):
        self.index = 0
    
    def create_person(self, name):
        p = Person(self.index, name)
        self.index += 1
        return p