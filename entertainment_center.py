import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story", 
						"A story of a boy and his toys that come to life",
						"https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
						"www.youtube.com/watch?v=vwyZH85NQC4")

avatar = media.Movie("Avatar",
					 "A marine on an alien planet",
					 "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
					 "https://www.youtube.com/watch?v=5PSNL1qE6VY")

fight_club = media.Movie("Fight Club",
						 "An everyman and an unreliable narrator who feels trapped with his white-collar position in society",
						 "https://upload.wikimedia.org/wikipedia/en/f/fc/Fight_Club_poster.jpg",
						 "https://www.youtube.com/watch?v=J8FRBYOFu2w")

bronson = media.Movie("Bronson",
					  "In this drama based on a true story, there's no one tougher or more brutal in the English penal system than prison Michael Peterson, aka Charles Bronson",
					  "https://upload.wikimedia.org/wikipedia/en/e/e0/Bronson_poster.jpg",
					  "https://www.youtube.com/watch?v=GMJ1c3qxOWc")

dark_skies = media.Movie("Dark Skies",
						 "A thriller centered on an alien disguised as a human and a boy tagged for abduction",
						 "https://upload.wikimedia.org/wikipedia/en/7/7f/Dark_Skies_Poster.jpg",
						 "https://www.youtube.com/watch?v=K8iLp1xQtPQ")

mirage_men = media.Movie("Mirage Men",
						 "Former government agents discuss their involvement in shaping UFO mythology during the Cold War",
						 "http://www.gstatic.com/tv/thumb/dvdboxart/10644572/p10644572_d_v8_aa.jpg",
						 "https://www.youtube.com/watch?v=rvAYSucaPRI")

the_conversation = media.Movie("The Conversation",
	                           "Surveillance expert Harry Caul (Gene Hackman) is hired by a mysterious client's brusque aide (Harrison Ford) to tail a young couple, Mark (Frederic Forrest) and Ann (Cindy Williams)",
	                           "https://upload.wikimedia.org/wikipedia/en/e/e0/Theconversation.jpg",
	                           "https://www.youtube.com/watch?v=VD_CAJHIIQE")

dark_city = media.Movie("Dark City",
						"A man struggles with memories of his past, including a wife he cannot remember, in a nightmarish world with no sun and run by beings with telekinetic powers who seek the souls of humans",
						"https://upload.wikimedia.org/wikipedia/en/9/9c/Dark_City_poster.jpg",
						"https://www.youtube.com/watch?v=jSpowoKqSzc")

talladega_nights = media.Movie("Talladega Nights",
							 "Talladega Nights: The Ballad of Ricky Bobby is a 2006 film about the #1 NASCAR driver, who stays atop the heap thanks to a pact with his best friend and teammate. But when a French Formula One driver makes his way up the ladder, his talent and devotion are put to the test.",
							 "https://upload.wikimedia.org/wikipedia/en/e/e7/Talladega_nights.jpg",
							 "https://www.youtube.com/watch?v=-zPcMma_C7A")

movies = [toy_story, avatar, fight_club, bronson, dark_skies, mirage_men, the_conversation, dark_city, talladega_nights]

fresh_tomatoes.open_movies_page(movies)

print(media.Movie.__doc__)





