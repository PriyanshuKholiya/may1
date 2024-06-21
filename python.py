import datetime

class Book:
    def __init__(self, title, author, isbn, genre):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.genre = genre
        self.available = True
        self.borrower = None
        self.due_date = None
        self.ratings = []  # List to store ratings
        self.reviews = []  # List to store reviews

    def add_rating(self, rating):
        self.ratings.append(rating)

    def add_review(self, review):
        self.reviews.append(review)

class User:
    def _init_(self, username, password):
        self.username = username
        self.password = password

class Library:
    def _init_(self):
        self.books = []
        self.users = []
        self.current_user = None

    def add_book(self, title, author, isbn, genre):
        book = Book(title, author, isbn, genre)
        self.books.append(book)

    def display_books(self):
        print("List of Books:")
        for book in self.books:
            print(f"Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}, Genre: {book.genre}, Available: {book.available}")

    def lend_book(self, title, borrower):
        for book in self.books:
            if book.title == title and book.available:
                book.available = False
                book.borrower = borrower
                book.due_date = datetime.datetime.now() + datetime.timedelta(days=14)
                print(f"Book '{title}' successfully borrowed by {borrower}.")
                return
        print(f"Book '{title}' is not available for borrowing.")

    def return_book(self, title):
        for book in self.books:
            if book.title == title and not book.available:
                book.available = True
                print(f"Book '{title}' successfully returned.")
                return
        print(f"Book '{title}' was not borrowed or does not exist in the library.")

    def add_user(self, username, password):
        user = User(username, password)
        self.users.append(user)
        print(f"User '{username}' successfully added.")

    def authenticate_user(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                self.current_user = user
                print(f"Welcome, {username}!")
                return
        print("Invalid username or password.")

    def search_book(self, query):
        found_books = []
        for book in self.books:
            if query.lower() in book.title.lower() or query.lower() in book.author.lower() or query.lower() in book.genre.lower():
                found_books.append(book)
        if found_books:
            print(f"Found {len(found_books)} matching books:")
            for book in found_books:
                print(f"Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}, Genre: {book.genre}, Available: {book.available}")
        else:
            print("No matching books found.")

    def calculate_fine(self, title, return_date):
        for book in self.books:
            if book.title == title and not book.available:
                due_date = book.due_date
                if return_date > due_date:
                    days_overdue = (return_date - due_date).days
                    fine = days_overdue * 0.50  # Assuming a fine of $0.50 per day
                    print(f"Fine for '{title}' is ${fine:.2f}.")
                    return
        print(f"No fine for '{title}'.")

    def rate_book(self, title, rating):
        for book in self.books:
            if book.title == title:
                book.add_rating(rating)
                print(f"Rating of {rating} added for '{title}'.")
                return
        print(f"Book '{title}' not found.")

    def review_book(self, title, review):
        for book in self.books:
            if book.title == title:
                book.add_review(review)
                print(f"Review added for '{title}'.")
                return
        print(f"Book '{title}' not found.")

    def display_reviews_and_ratings(self, title):
        for book in self.books:
            if book.title == title:
                if book.ratings:
                    print(f"Ratings for '{title}': {', '.join(str(rating) for rating in book.ratings)}")
                else:
                    print(f"No ratings for '{title}'.")
                if book.reviews:
                    print(f"Reviews for '{title}':")
                    for review in book.reviews:
                        print(review)
                else:
                    print(f"No reviews for '{title}'.")
                return
        print(f"Book '{title}' not found.")

    def reset_library(self):
        self.books = []
        self.users = []
        self.current_user = None
        print("Library has been reset.")

    def search_books_by_genre(self, genre):
        found_books = [book for book in self.books if genre.lower() in book.genre.lower()]
        if found_books:
            print(f"Found {len(found_books)} books in the genre '{genre}':")
            for book in found_books:
                print(f"Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}, Genre: {book.genre}, Available: {book.available}")
        else:
            print(f"No books found in the genre '{genre}'.")

def main():
    library = Library()
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Add User")
        print("6. Login")
        print("7. Search Book")
        print("8. Calculate Fine")
        print("9. Rate Book")
        print("10. Review Book")
        print("11. Display Reviews and Ratings")
        print("12. Search Books by Genre")
        print("13. Logout")
        print("14. Reset Library")
        print("15. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            isbn = input("Enter ISBN: ")
            genre = input("Enter genre: ")
            library.add_book(title, author, isbn, genre)
        
        elif choice == '2':
            library.display_books()
        
        elif choice == '3':
            if library.current_user:
                title = input("Enter book title to borrow: ")
                library.lend_book(title, library.current_user.username)
            else:
                print("Please login to borrow a book.")
        
        elif choice == '4':
            if library.current_user:
                title = input("Enter book title to return: ")
                library.return_book(title)
            else:
                print("Please login to return a book.")
        
        elif choice == '5':
            if library.current_user:
                print("Only admin can add users.")
            else:
                username = input("Enter username: ")
                password = input("Enter password: ")
                library.add_user(username, password)
        
        elif choice == '6':
            if library.current_user:
                print("You are already logged in.")
            else:
                username = input("Enter username: ")
                password = input("Enter password: ")
                library.authenticate_user(username, password)
        
        elif choice == '7':
            query = input("Enter search query: ")
            library.search_book(query)
        
        elif choice == '8':
            if library.current_user:
                title = input("Enter book title: ")
                return_date = datetime.datetime.strptime(input("Enter return date (YYYY-MM-DD): "), '%Y-%m-%d')
                library.calculate_fine(title, return_date)
            else:
                print("Please login to calculate fine.")
        
        elif choice == '9':
            if library.current_user:
                title = input("Enter book title: ")
                rating = float(input("Enter rating (1-5): "))
                library.rate_book(title, rating)
            else:
                print("Please login to rate a book.")
        
        elif choice == '10':
            if library.current_user:
                title = input("Enter book title: ")
                review = input("Enter review: ")
                library.review_book(title, review)
            else:
                print("Please login to review a book.")
        
        elif choice == '11':
            title = input("Enter book title: ")
            library.display_reviews_and_ratings(title)
        
        elif choice == '12':
            genre = input("Enter genre to search: ")
            library.search_books_by_genre(genre)
        
        elif choice == '13':
            if library.current_user:
                library.current_user = None
                print("Logged out successfully.")
            else:
                print("You are not logged in.")
        
        elif choice == '14':
            if library.current_user:
                print("Only admin can reset the library.")
            else:
                library.reset_library()
        
        elif choice == '15':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "_main_":
    main()
