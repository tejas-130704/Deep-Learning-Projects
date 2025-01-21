# Movie Recommendation System

A **Movie Recommendation System** built using **Streamlit** that recommends movies based on a selected movie. This project uses preprocessed data and a machine learning model stored in pickle files for generating movie recommendations. 

---

![Screenshot 2025-01-21 104026](https://github.com/user-attachments/assets/3008ca0d-a304-48a2-bce4-ade39940870f)


![Screenshot 2025-01-21 104052](https://github.com/user-attachments/assets/7e95d9ca-1816-4d7d-b226-18b59c7cbea5)

![Screenshot 2025-01-21 104625](https://github.com/user-attachments/assets/19c904a4-c99a-4948-9ffb-646714b9e405)


![Screenshot 2025-01-21 104705](https://github.com/user-attachments/assets/ff6a6617-3a87-47d9-bb66-136bea6977e8)


---

## Features
- Provides movie recommendations based on cosine similarity.
- User-friendly interface built using **Streamlit**.
- Utilizes preprocessed datasets and vectorized data for fast and efficient recommendations.

---

## Project Structure
```
├── app.py                 # Main Streamlit application
├── requirements.txt       # Required Python packages
├── Files/                 # Folder with preprocessed files (to be downloaded separately)
│   ├── reduced_vector.pkl # Dimensionality-reduced vectors for cosine similarity
│   ├── new_data.csv       # Preprocessed movie data
└── README.md              # Project documentation
```

---

## Setup Instructions

### Prerequisites
Ensure you have the following installed on your system:
- Python 3.7 or later
- pip (Python package manager)

### Step 1: Clone the Repository
Clone the project repository from GitHub:
```bash
git clone <repository_url>
cd <repository_name>
```

### Step 2: Download the Required Files
1. Go to the following Google Drive link:
   [Download Files Folder](https://drive.google.com/drive/folders/1vmIo1fBBkf7hxCmg50Y2ErcSg5063fDL?usp=sharing)
2. Navigate to the `Movie Recommendation` folder.
3. Download the `Files` folder.
4. Place the `Files` folder in the root directory of the cloned repository.

Your project structure should now look like this:
```
├── app.py
├── requirements.txt
├── Files/
│   ├── reduced_vector.pkl
│   ├── new_data.csv
└── README.md
```

### Step 3: Install Dependencies
Install the required Python libraries using the `requirements.txt` file:
```bash
pip install -r requirements.txt
```

### Step 4: Run the Application
Launch the Streamlit application:
```bash
streamlit run app.py
```

The application will start running locally, and you can access it at `http://localhost:8501/` in your browser.

---

## How It Works
1. Select a movie from the dropdown menu on the Streamlit interface.
2. The system calculates similarity scores based on the preloaded vector data (`reduced_vector.pkl`).
3. Recommended movies are displayed on the screen.

---

## Dataset and Preprocessing
- The **new_data.csv** file contains preprocessed movie data, including titles and metadata.
- The **reduced_vector.pkl** file stores dimensionality-reduced TF-IDF vectors for faster similarity computation.

---

## Troubleshooting
- **ModuleNotFoundError**: Ensure all dependencies are installed correctly using the `requirements.txt` file.
- **FileNotFoundError**: Confirm that the `Files` folder with `reduced_vector.pkl` and `new_data.csv` is in the root directory.

---

## Acknowledgments
- The project uses cosine similarity and TF-IDF techniques for recommendations.
- Built using **Streamlit** for an intuitive user interface.

---

### Note
The link to the files contains a `Movie Recommendation` folder. Make sure you download the folder titled `Files` and place it in the project directory as described above.

---

Enjoy exploring movies with this recommendation system!

