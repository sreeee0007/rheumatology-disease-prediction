Rheumatology Disease Prediction System

Overview

The Rheumatology Disease Prediction System is a machine learning-based project developed using Python to predict rheumatological disease categories based on symptom-related data.

The project uses a symptom dataset and machine learning classification algorithms to explore how data-driven techniques can be applied to disease prediction. It demonstrates the use of supervised learning for analyzing symptom patterns and classifying potential rheumatological conditions.

Objectives

* Develop a machine learning-based rheumatology disease prediction system.
* Process and analyze symptom-related data using Python.
* Implement machine learning classification algorithms.
* Predict disease categories based on symptom-related features.
* Explore the application of machine learning in healthcare.

Technologies Used

* Programming Language: Python
* Data Processing: Pandas and NumPy
* Machine Learning: Scikit-learn
* Dataset Format: CSV
* Version Control: Git and GitHub

Machine Learning Algorithms

1. Decision Tree Classifier

The Decision Tree Classifier is a supervised machine learning algorithm that uses decision rules to classify data into different categories based on input features.

In this project, it is used to identify patterns in symptom-related data and classify potential rheumatological disease categories.

2. Gaussian Naive Bayes

Gaussian Naive Bayes is a probabilistic classification algorithm based on Bayes’ theorem. It assumes that numerical features follow a Gaussian distribution within each class.

In this project, it is used to estimate the probabilities of different disease categories based on the available symptom features.

Model Comparison

Using both algorithms allows the project to explore different approaches to symptom-based classification. Their performance can be compared using suitable evaluation metrics.

Dataset

The project uses the following dataset:

data/dataset_rheumatology_symptoms.CSV

The dataset contains symptom-related features and corresponding disease labels used for machine learning-based classification.

The dataset is processed and used by the classification algorithms according to the implementation in the Python source code.

Project Structure

rheumatology-disease-prediction/
│
├── data/
│   └── dataset_rheumatology_symptoms.CSV
│
├── screenshots/
│   ├── Screenshot1.PNG
│   └── Screenshot2.PNG
│
├── src/
│   └── main.py
│
├── README.md
└── requirements.txt

Installation and Setup

Prerequisites

* Python 3.9 or later
* pip package manager

1. Install Dependencies

Open a terminal in the project’s root directory and run:

pip install -r requirements.txt

2. Run the Project

Execute the following command from the root directory:

python src/main.py

Note: Ensure that the dataset path specified in the Python code matches the actual location and filename of the CSV file inside the data directory.

Methodology

The project follows a machine learning-based classification workflow.

1. Dataset Loading: Load the rheumatology symptom dataset from the CSV file.
2. Data Preprocessing: Prepare the symptom features and target labels for machine learning.
3. Model Training: Train the Decision Tree and Gaussian Naive Bayes classifiers using the available training data.
4. Disease Prediction: Generate predictions based on the input symptom features.
5. Model Evaluation: Evaluate model performance using suitable classification metrics, where implemented.

Screenshots

The following screenshots demonstrate the project.

Screenshot 1

Screenshot 2

Applications

* Educational exploration of machine learning in healthcare.
* Symptom-based disease classification.
* Demonstration of supervised machine learning algorithms.
* Data processing and predictive modeling using Python.

Limitations

* Prediction performance depends on the quality, size, and representativeness of the dataset.
* Results may vary depending on the input features and classification algorithm.
* Performance on unseen data may differ from performance on training data.
* Predictions should not be treated as confirmed medical diagnoses.

Future Enhancements

* Expand the dataset with additional validated medical data.
* Evaluate the models using appropriate classification metrics.
* Compare additional machine learning algorithms.
* Develop a user-friendly interface for symptom input.
* Improve data preprocessing and model validation.
* Explore deployment as a web-based application.

Disclaimer

This project is intended for educational and research purposes only. Its predictions are not medical diagnoses and must not be used as a substitute for professional medical advice, diagnosis, or treatment.

Author

Developed as a machine learning project focused on rheumatological disease prediction using Python.
