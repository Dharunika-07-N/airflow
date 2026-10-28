import joblib
import os


def deploy_model():

    model_path = "models/model.pkl"

    if os.path.exists(model_path):
        model = joblib.load(model_path)

        print("Model loaded successfully.")
        print("Model type:", type(model).__name__)
        print("MODEL DEPLOYMENT READY")

        return True

    else:
        print("Model file not found.")
        return False


if __name__ == "__main__":
    deploy_model()