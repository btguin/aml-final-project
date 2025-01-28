# Claim Predictor: A Machine Learning Approach to Insurance Claim Likelihood

Policy Risk Predictor explores the prediction of insurance claim likelihood using a stacked ensemble model that combines Random Forest, XGBoost, and CatBoost using Logistic Regression as a meta-learner.

## Data

The project utilizes two main datasets:

1.  **Medicaid Vision Claims**: This dataset (`medicaid-vision-claims.csv`, not directly present in the tree but referenced in `catboost-baseline.ipynb`) contains information on Medicaid vision claims, including patient demographics, diagnoses, procedures, and claim amounts.
2.  **Allstate Claims Severity**: This dataset, obtained from Kaggle, includes data on Allstate insurance claims and their corresponding severity. It's used for exploring insurance claim prediction in a different context.

## Models

The project primarily employs the **CatBoost** library for building predictive models. The `catboost-baseline.ipynb` notebook demonstrates the training of a CatBoost regressor on the Medicaid dataset to predict the `Data_Value` feature.

-   **Model Type**: Gradient Boosting (CatBoostRegressor)
-   **Target Variable**: `Data_Value` (Medicaid dataset)
-   **Features**: Various demographic and claim-related features (see `categorical_features` in the notebook).
-   **Evaluation Metric**: Root Mean Squared Error (RMSE)
-   **Feature Importance**: The `catboost-baseline.ipynb` notebook includes an analysis of feature importance derived from the trained CatBoost model.

Additionally, the project uses **OpenAI's language models** (specifically `gpt-4o-mini`) for natural language processing tasks. The `insurance_data_parser.py` file defines a function `extract_vehicle_insurance_info` that leverages OpenAI's API to extract structured information (e.g., subscription length, vehicle age, customer age, fuel type) from unstructured text descriptions of insurance claims.

## Streamlit Application

The `app/` directory contains a Streamlit application that allows users to interactively predict the likelihood of a vehicle insurance claim.

### Features

-   **Reference Data**: Displays a table of dummy insurance data for context.
-   **Claim Description**: Allows users to input a textual description of an insurance claim.
-   **Information Extraction**: Uses OpenAI's API (via `insurance_data_parser.py`) to extract structured data from the user's input.
-   **Prediction**: Displays a dummy claim likelihood prediction (currently a placeholder value of 0.75).
-   **Risk Level**: Indicates whether the predicted claim likelihood is considered "High Risk" or "Low Risk".

### Usage

1.  Ensure the required libraries are installed (see `requirements.txt`).
2.  Set the `OPEN_AI_API_KEY` environment variable with your OpenAI API key.
3.  Navigate to the `code/app/` directory.
4.  Run the application using `streamlit run main.py`.

## Notebooks

The `code/` directory contains several Jupyter notebooks:

-   **`medicaid-data-explore.ipynb`**: This notebook explores the Medicaid claims data, providing insights into its structure and features.
-   **`catboost-baseline.ipynb`**: This notebook demonstrates the training of a CatBoost model on the Medicaid data to predict claim values. It includes data preprocessing, model training, evaluation, and feature importance analysis.
-   **`insurance_claims.ipynb`**: This notebook explores the Allstate claims severity data (not fully implemented).

## Requirements

The project requires the following Python libraries:

-   `openai==1.54.3`
-   `pandas==2.2.2`
-   `pydantic==2.5.3`
-   `pydantic-core==2.14.6`
-   `python-dotenv==0.21.0`
-   `streamlit==1.40.0`
-   `catboost`
-   `scikit-learn`
-   `numpy`

These can be installed using:

```bash
pip install -r requirements.txt
