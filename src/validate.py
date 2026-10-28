from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib


def validate_model():

    # Load dataset
    iris = load_iris()
    X = iris.data
    y = iris.target

    # Same split used during training
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    # Load trained model
    model = joblib.load("models/model.pkl")

    # Make predictions
    predictions = model.predict(X_test)

    # Calculate accuracy
    accuracy = accuracy_score(y_test, predictions)

    print(f"Validation Accuracy: {accuracy:.4f}")

    # Validation threshold
    if accuracy >= 0.80:
        print("MODEL VALIDATION PASSED")
        return True
    else:
        print("MODEL VALIDATION FAILED")
        return False


if __name__ == "__main__":
    validate_model()