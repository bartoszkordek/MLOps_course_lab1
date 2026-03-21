import os

import joblib


def load_model():
    path = os.path.join("models", "iris_model.joblib")
    try:
        print("Loading model started")
        if not os.path.exists(path):
            raise FileNotFoundError(f"Model not found in path {path}.")
        return joblib.load(path)
    except Exception as e:
        print(f"Failed to load model from {path}: {e}")
        raise


def predict(model, data_dictionary: dict) -> str:
    features = [
        [
            data_dictionary["sepal_length"],
            data_dictionary["sepal_width"],
            data_dictionary["petal_length"],
            data_dictionary["petal_width"],
        ]
    ]
    prediction_index = model.predict(features)[0]
    target_names = ["setosa", "versicolor", "virginica"]
    return target_names[prediction_index]
