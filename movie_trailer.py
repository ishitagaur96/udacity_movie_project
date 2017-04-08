# -*- coding: cp1252 -*-

import media
import fresh_tomatoes
# following code creates 6 instances of class movie from media.py
# each instance has four variables title,storyline,poster and youtube trailer
Ballerina = media.Movie("Ballerina",
                        "Ballerina is a 2016 English-language Canadian-French"
                        "3D computer-animated musical dance adventure comedy"
                        "film", "https://upload.wikimedia.org/wikipedia/en/d/"
                        "da/Ballerina_%282016_film%29.png",
                        "https://www.youtube.com/watch?v=fmK7X0swHrE")

Logan = media.Movie("Logan",
                    "Logan is a 2017 American superhero film featuring the"
                    "Marvel Comics character Wolverine",
                    "https://upload.wikimedia.org/wikipedia/en/3/37/"
                    "Logan_2017_poster.jpg",
                    "https://www.youtube.com/watch?v=RH3OxVFvTeg")

Frozen = media.Movie("Frozen",
                     "the film tells the story of a fearless princess who sets"
                     "off on a journey alongside a rugged iceman,"
                     "his loyal pet reindeer, and a naïve snowman to find her"
                     "estranged sister, whose icy powers have"
                     "inadvertently trapped the kingdom in eternal winter.",
                     "https://upload.wikimedia.org/wikipedia/en/0/05/Frozen_"
                     "%28201"
                     "3_film%29_poster.jpg",
                     "https://www.youtube.com/watch?v=TbQm5doF_Uc")

Interstellar = media.Movie("Interstellar",
                           "Set in a dystopian future where humanity is"
                           "struggling to survive,"
                           "it follows a group of astronauts who travel"
                           "through a wormhole in search of a new home for"
                           "humanity.",
                           "https://upload.wikimedia.org/wikipedia/en/b/bc/"
                           "Interstellar_film_poster.jpg",
                           "https://www.youtube.com/watch?v=0vxOhd4qlnA")

Pirates_of_the_caribbean = media.Movie("Pirates of the caribbean",
                                       "Captain Jack Sparrow is pursued by an"
                                       "old rival, Armando Salazar,"
                                       "who along with his Spanish Navy ghost"
                                       "crew has escaped from the Devil's"
                                       "Triangle,and is determined to kill"
                                       "every pirate at sea."
                                       "Jak seeks the Trident of Poseidon, a"
                                       "powerful artifact that grants its"
                                       "possessor total control over the seas,"
                                       " in order to defeat Salazar",
                                       "https://upload.wikimedia.org/"
                                       "wikipedia/"
                                       "en/2/21/Pirates_of_the_Caribbean%2C_"
                                       "Dead_Men_Tell_No_Tales.jpg",
                                       "https://www.youtube.com/watch?v"
                                       "w69ZgDfmKcA")

The_Circle = media.Movie("The circle",
                         "A young tech worker (Emma Watson) takes a job at a"
                         "powerful Internet corporation,"
                         "quickly rises up the company's ranks, and soon finds"
                         "herself in a perilous situation concerning privacy,"
                         "surveillance and freedom. She comes to learn that"
                         "her"
                         "decisions and actions will determine the future of"
                         "humanity.",
                         "https://upload.wikimedia.org/wikipedia/en/8/80"
                         "/The_Circle_%282017_film%29.png",
                         "https://www.youtube.com/watch?v=QCOXARv6J9k")


# list named movies is created that consists of above instances
movies = [Ballerina, Logan, Frozen, Interstellar, Pirates_of_the_caribbean,
          The_Circle]
# list is then passed as argument to open_movies_page function of
# fresh_tomatoes.
fresh_tomatoes.open_movies_page(movies)
