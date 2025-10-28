# Evaluate and compare model performance

Evaluate your deployed text classification models using the evaluation framework. The framework supports both supervised and unsupervised evaluation modes through a notebook-based approach.

## Using built-in datasets

**We recommend using the built-in supervised evaluation dataset** for this tutorial, as most users don't have labeled evaluation data readily available. The built-in datasets provide comprehensive performance analysis across different scenarios:

- **Balanced datasets**: Equal class distribution for baseline performance.
- **Skewed datasets**: Imbalanced classes for real-world testing.
- **Challenging datasets**: Edge cases to stress-test model robustness.

The evaluation generates key metrics including accuracy, precision, recall, F1-score, Matthews Correlation Coefficient (MCC), and Area Under the Curve Receiver Operating Characteristic scores with visual curves for model comparison.

## Using custom data

If you have your own labeled dataset, you can substitute it in the notebook. The framework automatically adapts to your data format and generates the same comprehensive metrics.

**Supported data formats:**

- **CSV format:** Two columns: `text` and `label`
- **Label formats:** "positive"/"negative", "LABEL_0"/"LABEL_1", "True"/"False", or "0"/"1"
- **Unsupervised:** Single `text` column for confidence analysis

## Set up your evaluation environment

Create a JupyterLab space in SageMaker Amazon SageMaker Studio to run the evaluation notebook.

1. In Studio, choose **JupyterLab** from the home screen.
2. If you don't have a space:
   1. Choose **Create space**.
   2. Enter a descriptive name (for example, `TextModelEvaluation)`.
   3. Keep the default instance type.
   4. Choose **Run space**.
   5. When the space has been created, choose **Open JupyterLab**.

### Access the evaluation notebook

Download the [zip file](samples/sagemaker-text-classification-evaluation-2.md "samples/sagemaker-text-classification-evaluation-2.md") and extract it to your local machine. Upload the entire extracted folder to your JupyterLab space to begin testing your models. The package contains the main evaluation notebook, sample datasets, supporting Python modules, and detailed instructions for the complete evaluation framework.

###### Note

After extracting the package, review the README file for detailed setup instructions and framework overview.

Continue to [Interpret your results](jumpstart-text-classification-interpret.md "jumpstart-text-classification-interpret.md") to learn how to analyze the evaluation output and make data-driven model selection decisions.
