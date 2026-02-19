# Chatbot using Wikipedia URL in Python (using NLTK)

A simple yet effective chatbot built with Python and NLTK that leverages web content from a given URL to answer user queries. This project demonstrates natural language processing (NLP) techniques for building conversational agents using real-world data.

## 🧠 Project Overview

This project allows you to:
- Scrape and process text from a provided URL
- Apply NLP techniques using NLTK
- Build a chatbot that can respond to user queries based on the scraped content

The core logic is presented in a Jupyter Notebook for easy experimentation and learning.

## 🚀 Features

- Web scraping to extract content from a URL
- Text cleaning and preprocessing
- Tokenization, lemmatization, and vectorization (NLTK)
- TF-IDF similarity matching for answering user questions
- Interactive chatbot interface (in notebook)

## 📁 Files

- `chatbot using url with python using nltk harshinde.ipynb` — Main Jupyter Notebook containing all code, explanations, and sample interactions.

## 🛠️ Installation & Setup


2. **Install Required Packages**
    ```bash
    pip install nltk requests beautifulsoup4 scikit-learn
    ```

3. **Download NLTK Data (First Run Only)**
    ```python
    import nltk
    nltk.download('punkt')
    nltk.download('wordnet')
    ```

4. **Run the Notebook**
    ```bash
    jupyter notebook "chatbot using url with python using nltk harshinde.ipynb"
    ```

## 💡 How It Works

1. **Provide a URL:**  
   The chatbot scrapes the text content from the provided URL.

2. **NLP Processing:**  
   The scraped text is cleaned and processed using NLTK (tokenization, lemmatization).

3. **User Query:**  
   The user can ask questions about the content of the page.

4. **Response Generation:**  
   The chatbot uses TF-IDF and cosine similarity to find and return the most relevant answer from the page content.

## 📝 Example

- Paste a URL (such as a Wikipedia article) in the notebook.
- Ask questions related to the page.
- Get relevant, context-aware answers from the chatbot!