import joblib
import os
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

data = load_iris()


def load_data():
    return load_iris()


def train_model():
    iris_data = load_data()
    X = iris_data["data"]
    y = iris_data["target"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=4)
    model = KNeighborsClassifier(n_neighbors=5)
    model.fit(X_train, y_train)
    return model


def save_model(model, filename="iris_model.joblib"):
    os.makedirs("models", exist_ok=True)
    path = os.path.join("models", filename)
    joblib.dump(model, path)


if __name__ == "__main__":
    print("Model training started")
    m = train_model()
    print("Model training completed")
    save_model(m)
    print("Model saved")
