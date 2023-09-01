class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        
    def __str__(self):
        return f'{self.title} by {self.author} {self.pages}'
    
    
book1 = Book("Some Title of the Book", 189)
book2 = Book("Some other Title of the Book", 200)
print (book1)
print (book2)