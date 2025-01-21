import streamlit as st
import pandas as pd
import pickle
from sklearn.metrics.pairwise import cosine_similarity

# Load data and pre-trained vector
@st.cache_resource
def load_data():
    # Load the CSV file containing movie data
    new_data = pd.read_csv('Files/new_data.csv')
    # Load the reduced vector file
    with open('Files/reduced_vector.pkl', 'rb') as file:
        reduced_vector = pickle.load(file)
    return new_data, reduced_vector

# Movie recommendation function
def movierec(title, new_data, reduced_vector):
    all_movie = []
    try:
        isx = new_data[new_data['title'] == title].index
        cosine_sim = cosine_similarity(reduced_vector, reduced_vector[[isx[0]]])
        new_cosine = list(enumerate(cosine_sim))
        new_cosine = sorted(new_cosine, key=lambda x: x[1], reverse=True)
        for i in new_cosine[:20]:  # Top 20 recommendations
            mtitle = new_data['title'][i[0]]
            poster = new_data['poster_path'][i[0]]
            all_movie.append({'title': mtitle, 'poster': f"https://image.tmdb.org/t/p/w500{poster}"})
        return all_movie
    except:
        return [{"title": "Not Found!!", "poster": ""}]

# Streamlit app
def main():
    st.title("Movie Recommendation System 🎥")
    st.write("Select a movie, and we’ll recommend similar movies!")

    # Load data
    new_data, reduced_vector = load_data()

    # Dropdown for movie selection
    selected_movie = st.selectbox("Choose a movie", new_data['title'],placeholder="Choose an option")

    # Recommend movies
    if st.button("Recommend"):
        recommendations = movierec(selected_movie, new_data, reduced_vector)
        if recommendations[0]["title"] == "Not Found!!":
            st.error("Movie not found!")
        else:
            st.subheader(f"Movies similar to {selected_movie}:")
            num_cols = 5  # Number of columns in the grid
            for i in range(0, len(recommendations), num_cols):
                cols = st.columns(num_cols)  # Create columns dynamically
                for col, movie in zip(cols, recommendations[i:i+num_cols]):
                    with col:
                        st.image(movie['poster'], use_column_width=True)
                        st.caption(movie['title'])

if __name__ == '__main__':
    main()
