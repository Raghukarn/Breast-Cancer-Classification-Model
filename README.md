## Project Overview
This project focuses on building and deploying a machine learning model that classifies whether a person has breast cancer based on medical data. The model uses a **RandomForest Classifier** to perform binary classification (presence or absence of breast cancer). A **Flask** application has been developed to enable deployment of the model as a web service.

## Objectives
- Develop a binary classification model for breast cancer detection.
- Deploy the model using Flask, allowing easy access to model predictions.

## Technologies Used
- **Python**: Core programming language
- **Machine Learning**: RandomForest Classifier for binary classification
- **Flask**: Framework for deploying the model as a web service
- **Pandas, NumPy**: Data manipulation and analysis
- **scikit-learn**: Model development and evaluation

## Project Structure
```
├── app.py                                     # Flask app for model deployment </br>
├── beingdatum_webinar_azure_Ml.py             # Model training script
├── requirements.txt                           # Required Python packages
├── static/                                    # Static files (if any)
├── templates/                                 # HTML templates for web interface (if applicable)
└── README.md                                  # Project overview and documentation
```

## Model Development
The machine learning model is based on the RandomForest classifier, chosen for its accuracy and ease of interpretation in medical datasets. After training on the dataset, the model achieved notable accuracy in detecting breast cancer, ensuring reliability in real-world applications.

## Deployment with Flask
The trained model was deployed using Flask, creating a simple API endpoint to make predictions based on new patient data. Flask enables a user-friendly interface for interaction with the model.
