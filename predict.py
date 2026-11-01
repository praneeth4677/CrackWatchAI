import numpy as np
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.models import load_model

# Constants
MODEL_PATH = "MOBILENET.h5"
IMG_SIZE = (224, 224)  # Same size used during training

# Load the trained model
model = load_model(MODEL_PATH)

# Class labels (same order as used during training)
class_names = [
    "Defective",
    "Non_Defective"
]

def predict_model(image_path):
    """Predicts the class label for a single image."""
    try:
        # Load and preprocess the image
        img = load_img(image_path, target_size=IMG_SIZE)
        img_array = img_to_array(img) / 255.0  # Normalize the image
        img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension

        # Make prediction
        prediction = model.predict(img_array, verbose=0)
        predicted_class = np.argmax(prediction, axis=1)[0]
        confidence = np.max(prediction) * 100

        # Return the predicted label
        return class_names[predicted_class],confidence

    except Exception as e:
        return f"Error processing image: {e}"

