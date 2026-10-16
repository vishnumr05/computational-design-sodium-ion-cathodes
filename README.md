# Ratio Prediction Using Machine Learning

## Project Overview

This project contains the datasets, trained machine-learning models, prediction scripts, and analysis notebooks developed to predict the Na_f-site **to** Na_e-site **ratio** for three material systems:

- **ZnYGe**
- **NiFeTi**
- **NiCoMn**

The machine-learning models use **transition-metal pair percentages (pair PCTs)** as input features. The original representation contains six pair-PCT variables, which are reduced to **three input variables** for the prediction models.

The purpose of this package is to provide a reproducible collection of the datasets, preprocessing methods, trained models, and prediction code so that the analysis can be reviewed and the trained models can be used for further predictions.

---

## 1. Scientific Objective

The objective of the machine-learning analysis is to establish a relationship between the **transition-metal pair percentages** and the resulting Na_f-site / Na_e-site ratio.

### Target Variable

The target variable predicted by the models is:

**Na_f-site / Na_e-site ratio**

### Input Variables

The input variables are **transition-metal pair percentages (pair PCTs)**.

Initially, six pair-PCT variables are available. These are reduced to three pair-PCT features for use as the machine-learning inputs.

Thus, the overall prediction problem can be represented as:

```text
Six transition-metal pair PCTs
            │
            ▼
    Feature reduction
            │
            ▼
Three pair-PCT input variables
            │
            ▼
    Machine-learning model
            │
            ▼
Na_f-site / Na_e-site ratio
```

The exact three retained pair-PCT variables are system-dependent and should be interpreted in accordance with the corresponding dataset and analysis notebook.

---

## 2. Material Systems

Three material systems are investigated:

### ZnYGe

The ZnYGe predictor uses three reduced pair-PCT inputs:

```text
cc, bb, aa
```

These are supplied to the prediction function in this order.

The available trained models are:

- Linear Regression
- Polynomial Regression
- Random Forest Regression

### NiFeTi

The NiFeTi predictor uses three reduced pair-PCT inputs:

```text
cc, ab, bc
```

These are supplied to the prediction function in this order.

The available trained models are:

- Linear Regression
- Polynomial Regression
- Random Forest Regression

### NiCoMn

The NiCoMn predictor uses three reduced pair-PCT inputs:

```text
aa, ab, bb
```

These are supplied to the prediction function in this order.

The available trained models are:

- Linear Regression
- Polynomial Regression
- Random Forest Regression

The predictor scripts confirm that the three reduced input variables are assembled into a three-feature input array before scaling and model prediction.

---

## 3. Dataset Structure

For each material system, two datasets are provided.

### Complete Dataset

```text
ZnYGe_dataset_complete.csv
NiFeTi_dataset_complete.csv
NiCoMn_dataset_complete.csv
```

These contain the complete datasets used in the model-development workflow.

### T3b Test Dataset

```text
ZnYGe_T3b_dataset_test.csv
NiFeTi_T3b_dataset_test.csv
NiCoMn_T3b_dataset_test.csv
```

These datasets are used to test and evaluate the trained models for T3b-related predictions.

---

## 4. Feature Reduction

The original input representation consists of **six transition-metal pair PCT variables**.

For the machine-learning prediction, these six variables are reduced to **three pair-PCT variables**.

The resulting three variables are used as the model inputs for each material system.

This reduction is important because the trained prediction functions expect exactly three input features.

The feature ordering must therefore be preserved when using the supplied predictor scripts.

---

## 5. Machine-Learning Models

Three regression approaches were developed and saved for each material system.

### 5.1 Linear Regression

Linear regression provides a baseline relationship between the three reduced pair-PCT inputs and the Na_f-site / Na_e-site ratio.

### 5.2 Polynomial Regression

Polynomial regression is used to model nonlinear relationships between the reduced pair-PCT inputs and the target ratio.

A separate polynomial feature transformer is saved with each polynomial model.

### 5.3 Random Forest Regression

Random Forest regression provides a nonlinear, tree-based machine-learning approach to predicting the Na_f-site/Na_e-site ratio.

The three approaches allow comparison of the relationship between the pair-PCT inputs and the target ratio using the model-evaluation procedure in the notebooks.

---

## 6. Preprocessing

The three pair-PCT input variables are standardised using statistics obtained from the training data.

The supplied scaler stores the training mean and standard deviation.

During prediction:

1. The three pair-PCT inputs are assembled in the required order.
2. The inputs are standardised using the saved training statistics.
3. For polynomial regression, the polynomial feature transformation is applied.
4. The selected trained model generates a prediction.
5. The predicted standardised target is converted back to the original target scale.

This preprocessing is implemented directly in the supplied predictor scripts.

---

## 7. Prediction Scripts

The following scripts are provided:

```text
predictors/
├── ZnYGe_T3b_Predictor.py
├── NiFeTi_T3b_Predictor.py
└── NiCoMn_T3b_Predictor.py
```

Each predictor contains a `predict_ratio()` function.

### ZnYGe

```python
predict_ratio(cc, bb, aa, model_type="linear")
```

### NiFeTi

```python
predict_ratio(cc, ab, bc, model_type="poly")
```

### NiCoMn

```python
predict_ratio(aa, ab, bb, model_type="poly")
```

The default model type differs between systems, so the desired model should be specified explicitly when comparing model predictions.

---

## 8. Saved Model Files

For each material system, the following trained objects are provided:

```text
*_T3b_linear_model.pkl
*_T3b_poly_model.pkl
*_T3b_poly_transform.pkl
*_T3b_rf_model.pkl
*_T3b_scaler.pkl
```

The scaler and polynomial transformer are part of the prediction pipeline and must be retained alongside the corresponding models.

---

## 9. Prediction Workflow

The complete prediction workflow is:

```text
Six transition-metal pair PCTs
                │
                ▼
       Feature reduction
                │
                ▼
Three selected pair-PCT inputs
                │
                ▼
       Feature standardization
                │
       ┌────────┼─────────┐
       ▼        ▼         ▼
    Linear   Polynomial    RF
                │
                ▼
       Target prediction
                │
                ▼
   Inverse transformation
                │
                ▼
Na_f-site / Na_e-site ratio
```

---

## 10. Notebooks

Two notebooks are included:

```text
notebooks/
├── training_file.ipynb
└── testing_file.ipynb
```

### `training_file.ipynb`

This notebook contains the model development and training workflow.

It should be used to understand how the datasets were processed and how the trained models were generated.

### `testing_file.ipynb`

This notebook contains the final analysis/submission workflow and should be used as the primary reference for the reported findings and model evaluation.

---

## 11. Results and Findings

The final analysis compares the performance of the Linear Regression, Polynomial Regression, and Random Forest models for predicting the Na_f-site / Na_e-site ratio.

The final numerical results, model-performance metrics, plots, and conclusions should be taken from:

```text
notebooks/testing_file.ipynb
```

### Summary of Model Performance

| Material System | Linear R² | Polynomial R² | Random Forest R² | Best Performing Model |
|---|---:|---:|---:|---|
| NiCoMn | 0.6336 | **0.8368** | 0.7308 | **Polynomial Regression** |
| NiFeTi | 0.8404 | **0.8690** | 0.7810 | **Polynomial Regression** |
| ZnYGe | **0.8939** | **0.8939** | 0.8242 | **Linear / Polynomial Regression** |

The results indicate that Polynomial Regression provides the highest R² for the NiCoMn and NiFeTi systems. For ZnYGe, Linear and Polynomial Regression produce the same reported R² of 0.8939, while Random Forest gives a lower R² of 0.8242.

### Feature Importance

The Random Forest feature importances provide an indication of the relative contribution of the three reduced pair-PCT inputs.

- **NiCoMn:** AA_pct is the most influential feature (0.5328), followed by AB_pct (0.3280) and BB_pct (0.1392).
- **NiFeTi:** CC_pct is the most influential feature (0.4899), followed by BC_pct (0.2633) and AB_pct (0.2468).
- **ZnYGe:** CC_pct strongly dominates the feature importance (0.9339), with AA_pct (0.0392) and BB_pct (0.0269) contributing substantially less.

These feature-importance values are specific to the Random Forest models and should not be interpreted as regression coefficients.
---

## 12. Running the Project

### Step 1 — Install Python

Use a compatible Python environment with the packages specified in:

```text
requirements.txt
```

### Step 2 — Install dependencies

```bash
pip install -r requirements.txt
```

### Step 3 — Launch Jupyter

```bash
jupyter notebook
```

### Step 4 — Review the notebooks

Open:

```text
notebooks/training_file.ipynb
```

to inspect the training workflow.

Then open:

```text
notebooks/testing_file.ipynb
```

to review the final analysis and findings.

### Step 5 — Use the trained predictors

The predictor scripts can be used to generate predictions without retraining the models, provided that the corresponding `.pkl` Files are present.

---

## 13. Important Reproducibility Note

The original predictor scripts contain an absolute path referring to the original development computer:

```python
BASE_PATH = "D:/College/Research Intern Applications/UNSW/Code/"
```

This path should be replaced with a project-relative path before distributing the final ZIP.

The final version should allow the project to be extracted to any directory and run without requiring modification of personal/local file paths.


