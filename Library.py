class library:
    def __init__(self, listofbook):
        self.books = listofbook

    def displayAvailableBook(self):
        print("name of books present in library are := ")
        for books in self.books:
            print("\t*"+books)
    def borrowbook(self,bookname):
        if bookname in self.books:
            print(f"you have been issued {bookname}. please return it into 30 days. ")
            self.books.remove(bookname)
            return True
        else:
            print("sorry book is not available.") 
    def returnbook(self,bookname):
        self.books.append(bookname)
        print("thanks to return this book ............")

class student:
    def requestbook(self):
        self.book = input("enter the name of the book you needed :=")
        return self.book

    def returnbook(self):
        self.book = input("enter the name of book you returned := ")
        return self.book

if __name__ == "__main__":
    centrallibraary = library(["python", "java", "tata","dango","todem"])
    student = student()
    while(True):
        WelcomeMSG = ''' === welcome to our centralibrary===
        please choose an option
        1). list of all book 
        2). request a book
        3). return a book 
        4). exit the library
        '''
        print(WelcomeMSG)
        a = int(input("enter your choice = "))
        if a == 1:
            centrallibraary.displayAvailableBook()
        elif a == 2:
            centrallibraary.borrowbook(student.requestbook())   
        elif a == 3:
            centrallibraary.returnbook(student.returnbook())
        elif a == 4:
            print("thanks to choose central library ")
            print("you are exit ")
            exit()
        else:
            print("invalid choise")   
