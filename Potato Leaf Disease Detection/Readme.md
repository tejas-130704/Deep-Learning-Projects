
# Potato Leaf Disease Prediction

This project uses a convolutional neural network (CNN) model to predict diseases in potato leaves. It is implemented using **Streamlit** for the user interface and provides an interactive way to classify the health of potato leaves. The trained models are stored externally due to size limitations and need to be downloaded from the provided link.

---

![Screenshot 2025-01-21 111111](https://github.com/user-attachments/assets/d3c0816e-4361-4b37-ad02-64bf72ed0d10)

![Screenshot 2025-01-21 111123](https://github.com/user-attachments/assets/6e7a01f7-7740-49ee-972a-a271a7a6454d)

---

![Screenshot 2025-01-21 111211](https://github.com/user-attachments/assets/0f6a5305-6788-4db6-9d2f-ca79db747f90)


![Screenshot 2025-01-21 111222](https://github.com/user-attachments/assets/2e24379b-025d-45ad-82dc-c06dfc27d180)


---

![Screenshot 2025-01-21 111302](https://github.com/user-attachments/assets/37a333d1-cb21-488b-916e-988dc8edd3cd)


![Screenshot 2025-01-21 111310](https://github.com/user-attachments/assets/52821233-33d4-4cc3-8591-cd8bdfe94b1b)

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
   git clone https://github.com/tejas-130704/Deep-Learning-Projects/potato-leaf-disease-prediction.git
   cd potato-leaf-disease-prediction
   ```

2. Download the pretrained models from the provided Google Drive link:
   [Potato Leaf Disease Prediction Models](https://drive.google.com/drive/folders/1vmIo1fBBkf7hxCmg50Y2ErcSg5063fDL?usp=sharing)
   - Locate the folder **Potato leaf disease prediction**.
   - Download the files `cnn_pretrained_model.h5`.
   - Place the downloaded `.h5` file in the project folder.

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

You can use either model based on your requirements. Place the file in the project directory and ensure it is loaded correctly in `app.py`.

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

**Note**: Ensure you have downloaded the required model file from the Google Drive link and placed it in the project folder before running the application.

