import os

import joblib
import pandas as pd

SELECTED_SEPAL_FEATURES = [
    "sepal length (cm)",
    "sepal width (cm)",
    "petal length (cm)",
    "petal width (cm)",
]


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
    df = pd.DataFrame(
        [
            {
                "sepal length (cm)": data_dictionary["sepal_length"],
                "sepal width (cm)": data_dictionary["sepal_width"],
                "petal length (cm)": data_dictionary["petal_length"],
                "petal width (cm)": data_dictionary["petal_width"],
            }
        ]
    )
    features = df[SELECTED_SEPAL_FEATURES]
    prediction_index = model.predict(features)[0]
    target_names = ["setosa", "versicolor", "virginica"]
    return target_names[prediction_index]
