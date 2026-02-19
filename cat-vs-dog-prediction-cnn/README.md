# Cat vs. Dog Prediction CNN

## Overview

This project is a Convolutional Neural Network (CNN) designed to classify images of cats and dogs. The project includes both a Tkinter-based GUI application and a Streamlit web-based application for predictions.

## Features

- **GUI Application**: Tkinter-based interface for local predictions (`prediction.py`).
- **Streamlit Application**: Web-based interface for predictions (`cat_dog_classifier.py`).
- **Data Preprocessing**: Includes data augmentation and normalization.

## Prerequisites

Ensure you have the following installed:

- Python 3.6+
- Tkinter (for GUI application)
- TensorFlow 2.x
- Keras
- NumPy
- Pandas
- Matplotlib
- scikit-learn
- Streamlit (for web-based application)

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/HarshShinde0/cat-vs-dog-prediction-cnn.git
   cd cat-vs-dog-prediction-cnn
   ```

2. **Create and activate a virtual environment (optional but recommended)**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages**:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Tkinter GUI Application

1. **Run the Tkinter-based GUI application**:

   ```bash
   python prediction.py
   ```

   This script provides a local GUI for making predictions on images using the trained model.

### Streamlit Web-Based Application

1. **Run the Streamlit web-based application**:

   ```bash
   streamlit run cat_dog_classifier.py
   ```

   You can now view your Streamlit app in your browser at [http://localhost:8501](http://localhost:8501).

## Dataset

Get the dataset from Kaggle:

- [Cat vs. Dog Image Classification Dataset](https://www.kaggle.com/datasets/vishallazrus/cat-vs-dog-image-classification-making-prediction)

## Kaggle Notebook

Update and explore the Kaggle Notebook here:

- [Cat vs. Dog Prediction CNN Notebook](https://www.kaggle.com/harshshinde8/cat-vs-dog-prediction-cnn)

## Project Structure

- `prediction.py`: Tkinter-based GUI application for local predictions.
- `cat_dog_classifier.py`: Streamlit-based web application for predictions.
- `requirements.txt`: List of dependencies required for the project.
- `README.md`: This file.

## Contributing

Contributions are welcome! Please fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
