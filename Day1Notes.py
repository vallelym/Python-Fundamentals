#Day1 Task
#Solution1
books = {"author1": ["book1", "book2"], "author2": ["book1", "book2"], "author3": ["book1", "book2"]}

x = input("enter an author name: ")

print(", ".join(books[x]))

#Solution2

y = input("enter author name: ")

x = books.get(y)

print(", ".join(x) or "author not found")

