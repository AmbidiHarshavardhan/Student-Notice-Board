"""Defines the Movie class that contains the details of a movie."""
import webbrowser

class Info(object):
    """This class provides a way to store movie related information.

    Attributes:
        title: A string to store the title of the movie.
        storyline: A string to store the basic plot of the movie.
        poster_image_url: A string to store the URL of the movie poster.
        trailer_youtube_url: A string to store the URL of the movie trailer.
        release_date: A string to store the release date of the movie.
    """

    def __init__(self, title, description, image_url,
                 link, da_te):
        """Initialises Movie class instance variables."""
        self.title = title
        self.description = description
        self.image_url = image_url
        self.link = link
        self.da_te = da_te

    def show_trailer(self):
        """Plays the movie trailer in the web browser."""
        webbrowser.open(self.link)
