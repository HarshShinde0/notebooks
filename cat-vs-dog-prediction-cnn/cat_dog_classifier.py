import streamlit as st
from PIL import Image
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image

# Load the pre-trained model (ensure this path points to your actual model weights)
model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(filters=32, kernel_size=3, activation='relu', input_shape=(64, 64, 3)),
    tf.keras.layers.MaxPooling2D(pool_size=2, strides=2),
    tf.keras.layers.Conv2D(filters=32, kernel_size=3, activation='relu'),
    tf.keras.layers.MaxPooling2D(pool_size=2, strides=2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(units=128, activation='relu'),
    tf.keras.layers.Dense(units=1, activation='sigmoid')
])

model.load_weights('/home/hks/ml/Predictions/cnn_weights.weights.h5')

# Function to classify the image
def classify_image(image_path):
    test_image = image.load_img(image_path, target_size=(64, 64))
    test_image_array = image.img_to_array(test_image)
    test_image_array = np.expand_dims(test_image_array, axis=0)
    test_image_array /= 255.0
    
    result = model.predict(test_image_array)
    confidence = result[0][0]
    
    if confidence > 0.5:
        prediction = 'dog'
        confidence_percentage = confidence * 100
    else:
        prediction = 'cat'
        confidence_percentage = (1 - confidence) * 100
        
    return prediction, confidence_percentage

# Streamlit app
st.title("Cat vs Dog Classifier")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    # Display the image
    img = Image.open(uploaded_file)
    st.image(img, caption='Uploaded Image.', use_column_width=True)
    
    # Get prediction and confidence
    prediction, confidence = classify_image(uploaded_file)
    st.write(f'Prediction: **{prediction}** ({confidence:.2f}%)')