# Cat/Dog Classifier

Welcome to the **Cat/Dog Classifier** project! This project is a deep learning application developed using **Streamlit** that classifies images into two categories: cats and dogs. Below, you will find details on the setup process, required files, and usage instructions.

---

## Features
- Classifies uploaded images as either a **cat** or a **dog**.
- Built using **Streamlit** for an interactive user interface.
- Utilizes a pre-trained model for high accuracy in classification.

---

## Prerequisites

1. **Python**: Ensure you have Python 3.7 or later installed.
2. **Required Libraries**: Install the dependencies listed in the `requirements.txt` file.

---

## Required Files

The model file required for classification (`model.h5`) is not stored on GitHub due to size limitations. Instead, it is available at the following Google Drive link:

[Google Drive - Cat Dog Classifier Folder](https://drive.google.com/drive/folders/1vmIo1fBBkf7hxCmg50Y2ErcSg5063fDL?usp=sharing)

### Steps to Access the Model File:
1. Open the provided link.
2. Navigate to the folder named `Cat Dog Classifier`.
3. Download the `model.h5` file.
4. Place the `model.h5` file in the same directory as the other project files downloaded from this repository.

---

## Setup Instructions

Follow the steps below to set up and run the project:

### 1. Clone the Repository
```bash
git clone https://github.com/tejas-130704/Deep-Learning-Projects.git
cd Deep-Learning-Projects/Cat_Dog_Classifier
```

### 2. Install Dependencies
Install the required Python libraries:
```bash
pip install -r requirements.txt
```

### 3. Add the Model File
Download the `model.h5` file from the [Google Drive link](https://drive.google.com/drive/folders/1vmIo1fBBkf7hxCmg50Y2ErcSg5063fDL?usp=sharing) and place it in the `Cat_Dog_Classifier` directory.

### 4. Run the Application
Start the Streamlit application by running the following command:
```bash
streamlit run app.py
```

This will launch the application in your default web browser.

---

## Usage

1. Open the application in your browser.
2. Upload an image of a cat or a dog.
3. View the prediction result displayed on the page.

---

## File Structure

```
Cat_Dog_Classifier/
├── main.py                # Main Streamlit application
├── model.h5              # Pre-trained model file (download separately)
├── requirements.txt      # List of dependencies
└── Readme.md             # Project documentation
```

---

## Screenshots


![Screenshot 2025-01-21 115226](https://github.com/user-attachments/assets/2ef0b991-6a1b-48e7-8ca2-6d0bc5bb2c82)


![Screenshot 2025-01-21 115250](https://github.com/user-attachments/assets/e5229f80-bed4-43a3-be4b-db90fd3a2588)

---

![Screenshot 2025-01-21 115408](https://github.com/user-attachments/assets/f8a523f0-6510-49ac-8b99-f58ff3cbb8c2)


![Screenshot 2025-01-21 115417](https://github.com/user-attachments/assets/c8d82512-8fc8-472a-81c5-49d53c48c801)


---

## Acknowledgments
- Thanks to the contributors and community for their support.
- Model training and evaluation inspired by TensorFlow/Keras documentation.

For any issues or suggestions, feel free to open an issue in this repository.

