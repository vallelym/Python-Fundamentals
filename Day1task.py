print("Published Authors")
print()

# Dictionary to store authors and their books
authors_books = {
    "J.K. Rowling": ["Harry Potter and the Philosopher's Stone", "Harry Potter and the Chamber of Secrets", "Harry Potter and the Prisoner of Azkaban"],
    "J.R.R. Tolkien": ["The Hobbit", "The Fellowship of the Ring", "The Adventures of Tom Bombadil"],
    "Stephen King": ["The Shining", "IT", "Christine"]
}

# Function to get books by author
def get_books_by_author(author_name):
    books = authors_books.get(author_name)
    if books:
        return f"{author_name} has written the following books: {', '.join(books)}."
    else:
        return f"Sorry, we don't have information on books by {author_name}."

# Main program
if __name__ == "__main__":
    author_name = input("Enter the author's name: ")
    print(get_books_by_author(author_name))