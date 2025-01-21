import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np

# Load the trained model
MODEL_PATH = "cnn_model4.h5"  # Replace with your model's file path
model = load_model(MODEL_PATH)

# Class labels for predictions
CLASS_LABELS = {
    2: "Healthy",
    0: "Early Blight",
    1: "Late Blight"
}

# Function to preprocess the uploaded image
def preprocess_image(image, target_size=(256, 256)):
    """Preprocess the image for prediction."""
    image = image.resize(target_size)
    image = img_to_array(image) / 255.0  # Normalize the image
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    return image

# Streamlit interface
st.title("Potato Leaf Disease Detection")
st.write("Upload an image of a potato leaf to identify its health status.")

# Image uploader
uploaded_file = st.file_uploader("Choose a potato leaf image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display uploaded image
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

    # Preprocess the image
    with st.spinner("Processing image..."):
        image = load_img(uploaded_file)
        processed_image = preprocess_image(image)

    # Predict the class
    with st.spinner("Making prediction..."):
        predictions = model.predict(processed_image)
        predicted_class = np.argmax(predictions, axis=1)[0]
        confidence = np.max(predictions) * 100

    # Display prediction result
    st.success(f"Prediction: {CLASS_LABELS[predicted_class]} (Confidence: {confidence:.2f}%)")

st.write("---")
st.info("Ensure the uploaded image is clear and contains only the leaf for accurate results.")
