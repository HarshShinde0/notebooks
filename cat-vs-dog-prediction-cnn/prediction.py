import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
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

# Function to handle file dialog and display the image and result
def load_and_predict():
    file_path = filedialog.askopenfilename()
    if file_path:
        # Display the image
        img = Image.open(file_path)
        img.thumbnail((250, 250))
        img_tk = ImageTk.PhotoImage(img)
        panel.config(image=img_tk)
        panel.image = img_tk
        
        # Get prediction and confidence
        prediction, confidence = classify_image(file_path)
        result_label.config(text=f'Prediction: {prediction} ({confidence:.2f}%)')

# GUI setup
root = tk.Tk()
root.title("Cat vs Dog Classifier")

panel = tk.Label(root)
panel.pack()

button = tk.Button(root, text="Select an Image", command=load_and_predict)
button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()