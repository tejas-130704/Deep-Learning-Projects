import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image

# Load your trained model
model = load_model('model.h5')  # Change this to the path where your model is saved

# Set up the Streamlit interface
st.title("Cat vs Dog Classifier")

st.write(
    "This web app predicts whether the uploaded image is a Cat or a Dog using a trained classifier model."
)

# Image uploader
uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_image is not None:
    # Open the image
    img = Image.open(uploaded_image)
    st.image(img, caption="Uploaded Image", use_column_width=True)

    # Preprocessing the image
    img = img.resize((224, 224))  # Resize to match model's input size
    img_array = np.array(img) / 255.0  # Normalize the image
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension

    # Prediction
    prediction = model.predict(img_array)

    # Display prediction
    if prediction[0] > 0.5:
        st.success(f"Prediction: Dog")
    else:
        st.success(f"Prediction: Cat")
