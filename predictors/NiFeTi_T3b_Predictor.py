import numpy as np
import joblib
from pathlib import Path

# Locate the model files relative to the project directory.
PROJECT_ROOT = Path(__file__).resolve().parents[1]
MODEL_PATH = PROJECT_ROOT / "models" / "NiFeTi"

scaler = joblib.load(MODEL_PATH / "NiFeTi_T3b_scaler.pkl")

models = {
    "poly": joblib.load(MODEL_PATH / "NiFeTi_T3b_poly_model.pkl"),
    "linear": joblib.load(MODEL_PATH / "NiFeTi_T3b_linear_model.pkl"),
    "rf": joblib.load(MODEL_PATH / "NiFeTi_T3b_rf_model.pkl")
}

poly = joblib.load(MODEL_PATH / "NiFeTi_T3b_poly_transform.pkl")

train_mean = scaler["mean"].to_numpy()
train_std = scaler["std"].to_numpy()


def predict_ratio(cc, ab, bc, model_type="poly"):
    X = np.array([[cc, ab, bc]])

    X_scaled = (X - train_mean[:-1]) / train_std[:-1]

    if model_type == "poly":
        X_scaled = poly.transform(X_scaled)

    ratio_scaled = models[model_type].predict(X_scaled)

    ratio = ratio_scaled * train_std[-1] + train_mean[-1]

    return float(np.asarray(ratio).ravel()[0])
