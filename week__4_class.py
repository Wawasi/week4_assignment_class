class Person:
 def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

 def introduce(self):
        print("Hello this is", self.name, "aged", self.age,"years old. They are", self.gender,".")

person1 = Person ("Micah", 43 , "Male")
person1.introduce()