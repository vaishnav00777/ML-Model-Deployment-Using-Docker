from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
import joblib

data = load_iris()
X = data.data
y = data.target

model = DecisionTreeClassifier()
model.fit(X, y)

joblib.dump(model, "model.pkl")

print("Model created successfully!")
