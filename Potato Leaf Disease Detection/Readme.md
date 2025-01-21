
# Potato Leaf Disease Prediction

This project uses a convolutional neural network (CNN) model to predict diseases in potato leaves. It is implemented using **Streamlit** for the user interface and provides an interactive way to classify the health of potato leaves. The trained models are stored externally due to size limitations and need to be downloaded from the provided link.

---




---

## Features
- Interactive user interface built with Streamlit.
- Predicts whether a potato leaf is healthy or diseased.
- Utilizes pretrained CNN models for high accuracy.

## Getting Started

### Prerequisites
Make sure you have the following installed on your system:
- Python 3.7+
- Streamlit
- TensorFlow
- NumPy
- OpenCV
- PIL (Pillow)

### Installation
1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/potato-leaf-disease-prediction.git
   cd potato-leaf-disease-prediction
   ```

2. Download the pretrained models from the provided Google Drive link:
   [Potato Leaf Disease Prediction Models](https://drive.google.com/drive/folders/1vmIo1fBBkf7hxCmg50Y2ErcSg5063fDL?usp=sharing)
   - Locate the folder **Potato leaf disease prediction**.
   - Download the files `cnn_pretrained_model.h5` and `cnn_model.h5`.
   - Place the downloaded `.h5` files in the project folder.

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Usage
1. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```

2. Open the provided local URL in your browser (e.g., `http://localhost:8501`).

3. Upload an image of a potato leaf through the interface to get predictions about its health status.

### Directory Structure
```
Potato-leaf-disease-prediction/
├── main.py
├── cnn_pretrained_model.h5   # Place downloaded file here
├── cnn_model.h5              # Place downloaded file here
├── requirements.txt
├── README.md
└── ... (other files)
```

## Process Flow
1. **Image Upload**:
   - Users upload an image of a potato leaf.
   - Supported formats: JPG, PNG, JPEG.

2. **Preprocessing**:
   - The image is resized and normalized for compatibility with the CNN model.

3. **Prediction**:
   - The model classifies the leaf as healthy or diseased.
   - If diseased, the type of disease is also specified (e.g., early blight, late blight).

4. **Results**:
   - The result is displayed in the Streamlit interface, along with the uploaded image.

### Models
- `cnn_pretrained_model.h5`: Trained on a larger dataset for enhanced performance.
- `cnn_model.h5`: Alternative model for prediction.

You can use either model based on your requirements. Place both files in the project directory and ensure they are loaded correctly in `app.py`.

### Notes
- You can extend this project by using a custom-trained model for specific datasets.
- If you encounter issues with the pretrained models, retraining or fine-tuning the model with additional data may improve performance.

## Dependencies
Make sure to install the dependencies listed in `requirements.txt`. Key libraries include:
- Streamlit
- TensorFlow
- NumPy
- OpenCV

## Resources
- [Streamlit Documentation](https://docs.streamlit.io/)
- [TensorFlow Documentation](https://www.tensorflow.org/)

## Contributing
Contributions are welcome! Feel free to fork the repository and submit a pull request.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

**Note**: Ensure you have downloaded the required model files from the Google Drive link and placed them in the project folder before running the application.

