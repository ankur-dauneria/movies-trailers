# Movies Trailer Website

> Movies Trailer webpage is a project, comprising of a front end and a backend. Based on user provided list of movies, movies trailer webpage is constructed. User can click on movie tile to play its corresponding YouTube trailer. This project backend comprises of python classes to store the movie information. The objects are instantiated (of different user choice movies) to construct a trailer webpage.

# Quickstart

### Installation

```
    $ git clone {repository}
    $ cd <repository_folder>
    $ python entertainment_media.py
```

### Technologies

- Frontend: HTML/CSS/JS

- Backend: Python

- Web Framework: Bootstrap

# Resources

## media.py

This file contains classes which are used to build the complete backend of this projects. It has two classes `Video` and `Movie`.
Video is parent class and Movie is a child class.


```python
    class Video
    class Movie(Video)
```

### Class Structure

#### class `Video`

 - `title` {String} tile of the video

 - `duration` {String} time duration of the video

#### class `Movie(Video)`

 - `year` {String} year of movie release
 
 - `rating` {String} valid rating of the movie

 - `storyline` {String} storyline of the movie

 - `poster_image_url` {String} URL of the image poster

 - `trailer_youtube_url` {String} URL of the YouTube trailer


## entertainment_media.py

This file imports the `media` module and instantiates class `Movie` objects with details of different movies. It supplies the list of movie to build the HTML webpage
Sample object is instantiated as below:

```python
    import media
    movie_object = media.Movie(movie_title, movie_year, movie_duration, movie_rating, movie_storyline, movie_poster_image, movie_youtube_trailer)
```

## fresh_tomatoes.py

It has task to build the HTML webpage based on the movie objects details supplied to it. It uses `bootstrap` web framework to build the webpage.

# API

`def title(self)` returns the title of the movie

`def title(self, title)` sets the title of the movie

`def duration(self)` returns the time duration (in minutes) of the movie

`def duration(self, duration)` sets the time duration (in minutes) of the movie

`def rating(self)` returns the valid rating of the movie

`def rating(self, rating)` sets the valid rating of the movie

`def storyLine(self)` returns the storyline of the movie

`def storyLine(self, storyline)` sets the storyline of the movie

`def year(self)` returns of the year of movie release

`def year(self, year)` sets the year of the movie release

`def poster_image_URL(self)` returns URL of the poster image of the movie

`def poster_image_URL(self, poster_image_url)` sets the URL of the poster image of the movie

`def youtube_trailer_URL(self)` returns the URL of the YouTube trailer of the movie

`def youtube_trailer_URL(self, youtube_trailer_url)` sets the URL of the YouTube trailer of the movie

# How to use it 

New movies can be added to the webpage via `entertainment_media.py` file.

To instantiate a new movie object, first import the `media` module

```python
    import media
    movie_object = media.Movie(movie_title, movie_year, movie_duration, movie_rating, movie_storyline, movie_poster_image, movie_youtube_trailer)
```

To add/update an API, classes (`Movie`, `Video`) under `media.py` file can be edited.

`fresh_tomatoes.py` can be edited to support new APIs carring movie information to display

# Credits

Udacity: for providing the starting version of fresh_tomatoes.py

# License

The contents of this repository are covered under the [MIT License](LICENSE).