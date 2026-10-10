import pandas as pd
from sklearn.model_selection import train_test_split

# Load the dataset
data = pd.read_csv("dataset_rheumatology_symptoms.csv")

# Separate symptoms and disease
X = data.drop("disease", axis=1)
y = data["disease"]

# Split the dataset into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Display the results
print("Total records:", len(data))
print("Training records:", len(X_train))
print("Testing records:", len(X_test))

print("\nSymptoms used by the model:")
print(list(X.columns))

print("\nTraining data shape:", X_train.shape)
print("Testing data shape:", X_test.shape)
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

# -------------------------------
# Decision Tree Model
# -------------------------------

decision_tree = DecisionTreeClassifier(random_state=42)

decision_tree.fit(X_train, y_train)

dt_predictions = decision_tree.predict(X_test)

dt_accuracy = accuracy_score(y_test, dt_predictions)

print("\nDecision Tree Accuracy:", dt_accuracy)
from sklearn.metrics import classification_report

print("\nDecision Tree Classification Report:")
print(classification_report(y_test, dt_predictions))


# -------------------------------
# Naive Bayes Model
# -------------------------------

naive_bayes = GaussianNB()

naive_bayes.fit(X_train, y_train)

nb_predictions = naive_bayes.predict(X_test)

nb_accuracy = accuracy_score(y_test, nb_predictions)

print("Naive Bayes Accuracy:", nb_accuracy)


# -------------------------------
# Select the better model
# -------------------------------

if dt_accuracy >= nb_accuracy:
    model = decision_tree
    print("\nSelected Model: Decision Tree")
else:
    model = naive_bayes
    print("\nSelected Model: Naive Bayes")
# Get symptoms from the user
print("\n" + "=" * 60)
print("        RHEUMATOLOGY DISEASE PREDICTION SYSTEM")
print("=" * 60)
print("        AI-Based Symptom Classification")
print("=" * 60)
print("Answer each question with yes or no.\n")

user_symptoms = []

for symptom in X.columns:
    answer = input(f"Do you have {symptom.replace('_', ' ')}? (yes/no): ")
    
    if answer.lower() == "yes":
        user_symptoms.append(1)
    else:
        user_symptoms.append(0)

# Convert the symptoms into the format expected by the model
user_input = pd.DataFrame([user_symptoms], columns=X.columns)

# Make prediction
prediction = model.predict(user_input)

# Get prediction confidence
probabilities = model.predict_proba(user_input)
confidence = max(probabilities[0]) * 100

# Display result
print("\n" + "=" * 50)
print("              PREDICTION RESULT")
print("=" * 50)

print(f"Predicted Disease     : {prediction[0]}")
print(f"Prediction Confidence : {confidence:.2f}%")

print("\nNote: This system is for educational purposes only.")
print("It does not replace professional medical diagnosis.")
print("=" * 50)
