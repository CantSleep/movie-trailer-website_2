import fresh_tomatoes
import media
# create instances of the Movie class
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

marigold = media.Movie("The Second Best Exotic Marigold Hotel",
                     "Mature british folk retire to india",
                     "http://upload.wikimedia.org/wikipedia/en/9/9e/Second_Best_poster.jpg",
                     "https://www.youtube.com/watch?v=O96og_f-Omk")

theory = media.Movie("The Theory of Everything",
                        "Story of Stephen Hawkings Life",
                        "http://upload.wikimedia.org/wikipedia/en/b/b8/Theory_of_Everything.jpg",
                        "https://www.youtube.com/watch?v=Salz7uGp72c")

inception = media.Movie("Inception",
                        "Thought Robbers",
                        "http://upload.wikimedia.org/wikipedia/en/7/7f/Inception_ver3.jpg",
                        "https://www.youtube.com/watch?v=YoHD9XEInc0")

sleuth = media.Movie("Sleuth",
                    "Brainy Thriller",
                    "http://upload.wikimedia.org/wikipedia/en/e/e2/Sleuth_movie.jpg",
                    "https://www.youtube.com/watch?v=DGz1QTj9-d4")

amadeus = media.Movie("Amadeus",
                        "A story of Mozarts demise",
                        "http://upload.wikimedia.org/wikipedia/en/2/2f/Amadeusmov.jpg",
                        "https://www.youtube.com/watch?v=0F8_qdd8iho")

# save the instances in list to pass to fresh_tomatoes
movies = [inception, sleuth, amadeus, toy_story, marigold, theory]

# Generate the fresh_tomatoes HTML file
fresh_tomatoes.open_movies_page(movies)

# print statements to test code
#print media.Movie.VALID_RATINGS
#print (media.Movie.__doc__)
#print (media.Movie.__name__, media.Movie.__module__)
#print amadeus.__module__
#print(amadeus.__class__)

