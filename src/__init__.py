# src/__init__.py

# Enable imports of the submodules easily from the src package
from .data import make_dataset
from .features import build_features
from .models import train_model, predict_model
