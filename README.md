# Movie Recommendation System

## Overview

This project is a movie recommendation system that provides personalized movie recommendations based on content analysis. It utilizes the TMDB movie database, which contains information about 5000 movies, available on Kaggle.

The recommendation system is built using content-based filtering techniques, including TF-IDF vectorization and cosine similarity analysis. The goal is to help users discover new movies that are similar to the ones they have enjoyed in the past.

## Files

- `Movie_Recommender_System.ipynb`: This Jupyter Notebook contains the code for building and training the content-based recommendation model.

- `app.py`: This file contains the code for the Streamlit web application. Users can access the movie recommendation system through this web app.

- `movie.pkl`: This is a pickle file containing the movie data and features used by the recommendation system.

- `similarity_matrix.pkl`: This pickle file stores the similarity matrix generated for the movies.

## How it Works

1. **Model Building**: The `Movie_Recommender_System.ipynb` notebook is where the content-based recommendation model is created. It uses the TMDB movie database as the source of movie information.

2. **Web Application**: The recommendation system is deployed as a web app using the Streamlit library. Users can input their preferences, and the system will recommend movies based on their choices.

3. **Poster Fetching**: The web application uses the TMDB API to fetch movie posters for display in the recommendations.

## Getting Started

To get started with the movie recommendation system, follow these steps:

1. Clone this repository to your local machine:

   ```bash
   git clone 
   ```

2. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit web app:

   ```bash
   streamlit run app.py
   ```

4. Access the web app by opening a web browser and navigating to the provided URL.

5. Explore and enjoy personalized movie recommendations!

## Contribute

Contributions to this project are welcome. If you'd like to make enhancements, fix issues, or improve the recommendations, please feel free to submit a pull request.

## License

This project is open-source and available under the [MIT License](LICENSE.txt).
