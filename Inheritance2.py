#we will use -- init-- function..................................
class Person:                                          # grandfather
    country = "India"
    
    def __init__(self):
        print("initializing person ........")

    def takeBreath(self ):
        print(f"I am a person so i am breathing ")

class Employee(Person):                                # father
    company ="Honda "
    salary = 23432

    def __init__(self):
        super().__init__()
        print("initializing employee ........")

    def getSalary(self):
        print(f"salary of a person is {self.salary}")
    
    def takeBreath(self):
        print(f"i am programer so i am teaking breath ")

class Programer(Employee):                              #son
    company = "testman"

    def __init__(self):
        super().__init__()
        print("initializing programer ........")

    def getSalary(self):
        print(f"company dont give salary to programer ")
    
    def takeBreath(self ):
        super().takeBreath() 
        print(f" nahi lene ka hai merko sass")
p = Programer()      #  def __init__(self): call all three class and print 
                    # with help of p = programer() we can operate all class
                    
