from keras.models import load_model
import numpy as np

def load_trained_model(model_path):
    """Load a trained model."""
    return load_model(model_path)

def make_predictions(model, X):
    """Make predictions with a trained model."""
    predictions = model.predict(X)
    predicted_classes = (predictions > 0.5).astype(int)

    return predictions, predicted_classes

