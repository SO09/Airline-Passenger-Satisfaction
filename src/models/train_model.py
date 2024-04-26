import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import Adam
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from keras.models import load_model

def build_model(input_dim):
    """Build and compile a neural network model."""
    model = Sequential([
        Dense(128, activation='relu', input_shape=(input_dim,)),
        Dropout(0.5),
        Dense(64, activation='relu'),
        Dropout(0.5),
        Dense(32, activation='relu'),
        Dropout(0.5),
        Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer=Adam(learning_rate=0.001), loss='binary_crossentropy', metrics=['accuracy'])
    return model

def train_model(X_train, y_train, X_val, y_val):
    """Train the model."""
    model = build_model(X_train.shape[1])
    history = model.fit(X_train, y_train, epochs=25, batch_size=64, validation_data=(X_val, y_val), verbose=2)
    model.save('models/mon_modele.h5')
    return model, history


