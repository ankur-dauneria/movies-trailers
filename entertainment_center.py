# !/usr/bin/env python

# import modules
import fresh_tomatoes
import media

# Class Movie objects are instantiated for different movies.
toy_story = media.Movie(
    "Toy Story",
    "1995",
    "81 min",
    "G",
    "A cowboy doll is profoundly threatened and jealous when a new "
    "spaceman figure supplants him as top toy in a boys room",
    "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
    "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie(
    "Avatar",
    "2009",
    "162 min",
    "PG-13",
    "A paraplegic marine dispatched to the moon Pandora on a unique mission"
    "becomes torn between following his orders and protecting the world he "
    "feels is his home",
    "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
    "https://www.youtube.com/watch?v=5PSNL1qE6VY")

dangal = media.Movie(
    "Dangal",
    "2016",
    "161 min",
    "PG-13",
    "Former wrestler Mahavir Singh Phogat and his two wrestler daughters "
    "struggle towards glory at the Commonwealth Games in the face of "
    "societal oppression.",
    "https://upload.wikimedia.org/wikipedia/en/9/99/Dangal_Poster.jpg",
    "https://www.youtube.com/watch?v=x_7YlGv9u1g")

threeIdiots = media.Movie(
    "3 Idiots ",
    "2009",
    "170 min",
    "PG-13",
    "Two friends are searching for their long lost companion. They "
    "revisit their college days and recall the memories of their friend "
    "who inspired them to think differently, even as the rest of the "
    "world called them 'idiots'",
    "https://upload.wikimedia.org/wikipedia/en/d/df/3_idiots_poster.jpg",
    "https://www.youtube.com/watch?v=K0eDlFX9GMc")

bahubaliTwo = media.Movie(
    "Bahubali 2: The Conclusion",
    "2017",
    "167 min",
    "UA",
    "When Shiva, the son of Bahubali, learns about his heritage, he begins to "
    "look for answers. His story is juxtaposed with past events that unfolded "
    "in the Mahishmati Kingdom.",
    "https://upload.wikimedia.org/wikipedia/en/f/f9/"
    "Baahubali_the_Conclusion.jpg",
    "https://www.youtube.com/watch?v=G62HrubdD6o")

sultan = media.Movie(
    "Sultan ",
    "2016",
    "170 min",
    "PG-13",
    "Sultan is a classic underdog tale about a wrestler's journey",
    "https://upload.wikimedia.org/wikipedia/en/1/1f/Sultan_film_poster.jpg",
    "https://www.youtube.com/watch?v=wPxqcq6Byq0")

# populating the movies objects into a list
movies = [toy_story, sultan, threeIdiots, avatar, dangal, bahubaliTwo]

# Supply the list of movies to create a HTML webpage
fresh_tomatoes.open_movies_page(movies)
