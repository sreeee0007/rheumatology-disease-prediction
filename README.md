Rheumatology Disease Prediction System

About the Project

The Rheumatology Disease Prediction System is a machine learning-based project developed using Python to predict rheumatological disease categories based on symptom-related data.

The project uses machine learning classification algorithms to analyze symptom data and predict potential disease categories. It demonstrates the application of machine learning techniques in healthcare.

Objectives

* Develop a machine learning-based disease prediction system.
* Analyze rheumatological symptom data.
* Implement and explore machine learning classification algorithms.
* Predict disease categories based on symptom-related features.
* Demonstrate the application of machine learning in healthcare.

Technologies Used

* Programming Language: Python
* Data Processing: Pandas, NumPy
* Machine Learning: Scikit-learn
* Dataset: CSV

Machine Learning Algorithms

1. Decision Tree Classifier

Decision Tree is a supervised machine learning algorithm that uses decision rules to classify data into different categories based on input features.

In this project, it is used to identify patterns in symptom-related data and predict rheumatological disease categories.

2. Gaussian Naive Bayes

Gaussian Naive Bayes is a probabilistic machine learning algorithm based on Bayes’ theorem. It assumes that numerical features follow a Gaussian distribution within each class.

In this project, it is used to estimate the probabilities of different disease categories based on the available symptom features.

Dataset

The project uses the following dataset:

data/dataset_rheumatology_symptoms.csv

The dataset contains symptom-related features and corresponding disease labels used for machine learning-based classification.

Project Structure

Rheumatology-Disease-Prediction/
│
├── data/
│   └── dataset_rheumatology_symptoms.csv
│
├── screenshots/
│   ├── Screenshot1.png
│   └── Screenshot2.png
│
├── src/
│   └── main.py
│
├── requirements.txt
└── README.md

Installation and Execution

Prerequisites

* Python 3.9 or later
* pip package manager

1. Install Dependencies

Open a terminal in the project’s root directory and run:

pip install -r requirements.txt

2. Run the Project

Execute the following command from the root directory:

python src/main.py

Ensure that the dataset path in the Python code points to the correct CSV file inside the data directory.

Methodology

1. Data Loading: Load the symptom dataset from the CSV file.
2. Data Preprocessing: Prepare the data for machine learning.
3. Model Training: Train the Decision Tree and Gaussian Naive Bayes classifiers.
4. Disease Prediction: Generate predictions based on the symptom features.
5. Model Evaluation: Assess model performance using suitable evaluation metrics, if implemented.

Screenshots

Screenshot 1

Screenshot 2

Applications

* Machine learning-based symptom classification.
* Educational exploration of healthcare data analysis.
* Demonstration of supervised learning algorithms.
* Exploration of predictive modeling using Python.

Limitations

* Prediction performance depends on the quality and quantity of the dataset.
* Results may vary depending on the input features and model used.
* Predictions may not generalize to real-world clinical situations.

Future Enhancements

* Expand the dataset with validated medical data.
* Compare model performance using appropriate evaluation metrics.
* Explore additional machine learning algorithms.
* Develop a user-friendly interface for symptom input.
* Improve model validation and deployment.

Disclaimer

This project is intended for educational and research purposes only. Its predictions are not medical diagnoses and must not replace professional medical advice or treatment.

Author

Developed as a machine learning project focused on rheumatological disease prediction using Python.
