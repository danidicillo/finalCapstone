# T21 - COMPULSORY TASK 2:

print(" ")
print(" T21 - COMPULSORY TASK 2: ")

# Let us build a system that will tell you what to watch next based on the word vector similarity of the description of movies.

# 1) Create a file called watch_next.py
# DONE!

# 2) Read in the movies.txt file. Each separate line is a description of a different movie:

# 3) Your task is to create a function to return which movies a user would watch next if they have watched Planet Hulk with the
# description “Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick
# Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the
# planet Sakaar where he is sold into slavery and trained as a gladiator.”

# 4) The function should take in the description as a parameter and return the title of the most similar movie:

# **************** SOLUTION ******************

# Import the library:
import spacy

# Load the language model:
nlp = spacy.load("en_core_web_lg")

# Store the movie's description in a variable:
Planet_Hulk_movie = '''“Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and
launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into 
slavery and trained as a gladiator.'''

# Create the function:

def next_movie_to_watch(parameter_movie_description):

        # Create a dictionary to store the data from the text file:
        movies_dict = {}
        movies_dict_1 = {}

        # Create a variable to store the Text file:
        movies_list = "movies.txt"

        # Read the contents of the movies.txt file and split them into lines:

        with open(movies_list, "r") as file:
            movie_descriptions = file.read().splitlines()

        # Iterate over the lines and split into movie name and description:
            for description in movie_descriptions:
                movie_info = description.split(":")          # Split the text lines from the txt file
                movie_name = movie_info[0].strip()           # Strip movie info's name
                movie_description = movie_info[1].strip()    # Strip movie info's description
                movies_dict[movie_name] = movie_description  # Create a dictionary entry for each movie     
                
            # For validation, print the resulting dictionary showing the contents as they are shown in the text file:
            ''' print(" ")
                for movie, description in movies_dict.items():
                movies_dict_1 = f"{movie}: {description}"
                print(movies_dict_1)'''
                
            print(" ")

            # Compare the description of any movie with the description of every available movie on the movies.txt file:
            model_movie = nlp(parameter_movie_description)
            movie_similarities = []         # declare this list to store the movies similarity values in descending order:

            # Find the score of similarity for every movie and the maximum one:
            for movie, description in movies_dict.items():
                similarity = nlp(description).similarity(model_movie)
                movie_similarities.append((movie, similarity))   # Save the movies and their correspondent score in the list created above.

            # Sort the movie similarities in descending order based on similarity value (I have made research in Google and ChatGPT to learn about this sort and lambda functions):
            movie_similarities.sort(key=lambda x: x[1], reverse=True)

            print("Recommended Movies: \n")

            for movie, similarity in movie_similarities:
                print(f"{movie}: {similarity}")

            # Define a max_similarity_movie variable to store the name of the movie with maximum similarity:
            max_similarity_movie = " "
            # Define a max_similarity variable to store the maximum score for similarity:
            max_similarity = 0

            # Find the value of similarity for every movie and the maximum:
            for movie, description in movies_dict.items():
                similarity = nlp(description).similarity(model_movie)
                #For validation, print the correspondent similarity values along with every movie's name:
                # print(f"{movie}: {similarity}")
                # Check the maximum value of similarity:
                if similarity > max_similarity:
                    max_similarity = similarity
                    max_similarity_movie = movie 
        print(" ")
        print("NEXT MOVIE TO WATCH ---> " + max_similarity_movie + " (" + str(max_similarity) + ")\n")


# Call the function for the movie description provided above to show the required results:
next_movie_to_watch(Planet_Hulk_movie)