from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# 1. Prepare a mock dataset
emails = [
    "Win a free iPhone now! Click here", 
    "Meeting schedule for tomorrow", 
    "Congratulations! You've been selected for a cash prize", 
    "Project update and deployment notes", 
    "Claim your $1000 Amazon gift card today",
    "Let's grab lunch at 12 PM",
    "URGENT: Your account has been compromised",
    "Please review the attached pull request"
]
labels = [1, 0, 1, 0, 1, 0, 1, 0] # 1 = Spam, 0 = Ham

# 2. Vectorize the text
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(emails)

# 3. Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.25, random_state=42)

# 4. Train Naive Bayes Classifier
model = MultinomialNB()
model.fit(X_train, y_train)

# 5. Evaluate and Predict
predictions = model.predict(X_test)
print(f"Model Accuracy: {accuracy_score(y_test, predictions) * 100:.2f}%")

# Test a new email
test_email = ["Get a free loan instantly!"]
test_vec = vectorizer.transform(test_email)
result = model.predict(test_vec)

print(f"\nTest Email: '{test_email[0]}'")
print("Classification:", "SPAM" if result[0] == 1 else "NOT SPAM")
