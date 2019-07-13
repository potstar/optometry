class Person():
    def __init__(self,name):
        self.name=name
Person.age=None
def eat(self):
    print(self.name)
li=Person('li')
import types
li.eat=types.MethodType(eat,li)
li.eat()
print(li.age)