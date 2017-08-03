# Class video tells about the video properties
class Video():
    """This class provides a way to store video related information.
       Its a parent class.

    Attributes: \n
        title: Title of the video\n
        duration: Time duration of the video (in minutes)\n
    """

    def __init__(self, video_title, video_duration):
        """Video class constructor

        Args: \n
            video_title: title of the video\n
            video_duration: time duration of the video (in minutes)\n

        Returns: nothing
        """
        self._title = video_title
        self._duration = video_duration

    @property
    def title(self):
        """Returns the title of the movie

        Returns: title of the movie
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of the video

        Args: \n
            title: title of the video

        Returns: nothing
        """
        self._title = title

    @property
    def duration(self):
        """Returns the time duration of the video in minutes

        Returns: time duration of the video.
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the time duration

        Args: \n
            duration: time duration

        Returns: nothing
        """
        self._duration = duration

# Class Movie inherited from video. It stores the Movie properties


class Movie(Video):
    """This class provides a way to store the movie related information.
       Inherits from Video Class.

    Attributes: \n
        rating: rating of the movie\n
        year: Year of the movie release\n
        storyline: storyline of the movie\n
        poster_image_url: URL of the poster image ofthe movie\n
        trailer_youtube_url: URL of the trailer youtube video of the movie\n
    """

    def __init__(self, movie_title, movie_year, movie_duration, movie_rating,
                 movie_storyline, movie_poster_image, movie_youtube_trailer):
        """Movie class constructor

        Args: \n
            movie_title: title of the movie \n
            movie_year: year of the movie release\n
            movie_duration: time duration of the movie\n
            movie_rating: rating of the movie\n
            movie_storyline: story line of the movie\n
            movie_poster_image: URL of the poster image of the movie\n
            movie_youtube_trailer: URL of the youtube trailer of the movie\n

        Returns: nothing
        """
        Video.__init__(self, movie_title, movie_duration)
        self._rating = movie_rating
        self._storyline = movie_storyline
        self._year = movie_year
        self._poster_image_url = movie_poster_image
        self._trailer_youtube_url = movie_youtube_trailer

    @property
    def rating(self):
        """Returns the rating of the movie

        Returns: rating of the movie.
        """
        return self._rating

    @rating.setter
    def rating(self, rating):
        """Sets the rating of the movie

        Args: \n
            rating: rating of the movie

        Returns: nothing
        """
        self._rating = rating

    @property
    def storyLine(self):
        """Returns the storyline of the movie

        Returns: storyline of the movie
        """
        return self._storyline

    @storyLine.setter
    def storyLine(self, storyline):
        """Sets the storyline of the movie

        Args: \n
            storyline: storyline of the movie

        Returns: nothing
        """
        self._storyline = storyline

    @property
    def year(self):
        """Returns the year of release of the movie

        Returns: year of release of the movie.
        """
        return self._year

    @year.setter
    def year(self, year):
        """Sets the year of the movie

        Args: \n
            year: year of the movie

        Returns: nothing
        """
        self._year = year

    @property
    def poster_image_URL(self):
        """Returns the poster image URL of the movie

        Returns: image URL of the movie
        """
        return self._poster_image_url

    @poster_image_URL.setter
    def poster_image_URL(self, poster_image_url):
        """Sets the poster image URL of the movie

        Args: \n
            poster_image_url: poster image URL of the movie

        Returns: nothing
        """
        self._poster_image_url = poster_image_url

    @property
    def youtube_trailer_URL(self):
        """Returns the YouTube trailer URL of the movie

        Returns: YouTube trailer URL
        """
        return self._trailer_youtube_url

    @youtube_trailer_URL.setter
    def youtube_trailer_URL(self, youtube_trailer_url):
        """Sets the Youtube trailer URL of the movie

        Args: \n
            youtube_trailer_url: youtube trailer URL of the movie

        Returns: nothing
        """
        self._trailer_youtube_url = youtube_trailer_url
