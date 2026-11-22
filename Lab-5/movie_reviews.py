"""A local movie board with ratings, reviews and stable review identifiers."""
import hashlib
import json
import secrets

STREAM_HOST = "127.0.0.1"
STREAM_PORT = 8000


class MovieBoard:
    """Maintain one independent catalogue and its reviews."""

    def __init__(self):
        self.movies = {}

    def add_movie(self, title, genre, year):
        """Add an unrated title to this catalogue."""
        self.movies[title] = {"genre": genre, "year": year,
                              "ratings": [], "reviews": []}

    def rate_movie(self, title, stars, review_text=""):
        """Record a valid integer rating and its optional review."""
        if (isinstance(stars, bool) or not isinstance(stars, int)
                or not 1 <= stars <= 5):
            print("Rating must be between 1 and 5, got", stars)
            return False
        if title not in self.movies:
            return False
        self.movies[title]["ratings"].append(stars)
        if review_text:
            self.movies[title]["reviews"].append(review_text)
        return True

    def average_rating(self, title):
        """Round the mean to one decimal; unrated titles start at zero."""
        ratings = self.movies[title]["ratings"]
        return round(sum(ratings) / len(ratings), 1) if ratings else 0.0

    def top_movies(self, count=2):
        """Return the highest-rated titles, with stable ties."""
        ranked = sorted(self.movies, key=self.average_rating, reverse=True)
        return ranked[:count]

    def pick_featured(self):
        """Select a featured title from the catalogue."""
        return secrets.choice(sorted(self.movies)) if self.movies else None


def review_id(title, review_text):
    """Hash an unambiguous pair of title and review strings."""
    encoded = json.dumps([title, review_text], ensure_ascii=False).encode()
    return hashlib.sha256(encoded).hexdigest()


def main():
    """Run the example catalogue and print its results."""
    board = MovieBoard()
    board.add_movie("The Long Road", "Drama", 2021)
    board.add_movie("Laugh Track", "Comedy", 2019)
    board.add_movie("Star Drift", "Sci-Fi", 2023)
    board.rate_movie("The Long Road", 5, "Beautiful story")
    board.rate_movie("The Long Road", 4, "A bit slow but worth it")
    board.rate_movie("Laugh Track", 2, "Not very funny")
    board.rate_movie("Star Drift", 6, "Out of range rating")
    board.rate_movie("Star Drift", 4)
    for number, title in enumerate(board.movies, start=1):
        print(number, title, board.average_rating(title))
    print("Top movies:", board.top_movies())
    print("Featured today:", board.pick_featured())
    print("Review id:", review_id("Laugh Track", "Not very funny"))
    print(f"Streaming from {STREAM_HOST}:{STREAM_PORT}")
    print("Genres:", sorted(movie["genre"] for movie in board.movies.values()))


if __name__ == "__main__":
    main()
