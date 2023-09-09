
class Person:
  name = "abeer"
  age = 18
  
  def is_adult ():
   if Person.age >= 18:
        print("You have too much responsibilities")
   else:
        print("Lucky you")
   

print(Person.name)
print(Person.age)    
Person.is_adult()

class person1:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def __str__(self):
    return f"My name is {self.name} and I am {self.age} years old "
  
first_person = person1("khawater", 21)
print(first_person)


  