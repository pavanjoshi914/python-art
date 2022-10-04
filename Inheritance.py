class Employee:
    company = "google"

    def setDetails(self):
        print(f"all employee are very cool .")

class programer(Employee):
    language = "python"

    def getDetails(self):
        print(f"all {self.language} programers are very dangeous .")
print("program 1...................................................")
e = Employee() #very important to call informations from class
e.setDetails()
p = programer() #very important to call informations from class
p.setDetails() # setDetails is not present in "''class programer(Employee):"'' but u can call it , because "programer(Employee)" is subset:
print(p.company)# this will call 1st class (class Employee) 
print(p.language)
p.getDetails()

# again same program but we will give setDetails both side
class Employee:
    company = "google"

    def setDetails(self):
        print(f"all employee are very cool .")

class programer(Employee):
    language = "python"

    def getDetails(self):
        print(f"all {self.language} programers are very dangeous .")
    
    def setDetails(self):
        print(f"never undrestimate any programer .")    
print("program 2...................................................")
e = Employee() #very important to call informations from class
e.setDetails()
p = programer() #very important to call informations from class
p.setDetails()
print(p.company)# this will call 1st class (class Employee) 
print(p.language)
p.getDetails()
