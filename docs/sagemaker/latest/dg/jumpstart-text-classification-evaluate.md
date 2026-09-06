

# Evaluate and compare model performance
<a name="jumpstart-text-classification-evaluate"></a>

Evaluate your deployed text classification models using the evaluation framework. The framework supports both supervised and unsupervised evaluation modes through a notebook-based approach.

## Using built-in datasets
<a name="w2aac37c15c23b5"></a>

**We recommend using the built-in supervised evaluation dataset** for this tutorial, as most users don't have labeled evaluation data readily available. The built-in datasets provide comprehensive performance analysis across different scenarios:
+ **Balanced datasets**: Equal class distribution for baseline performance.
+ **Skewed datasets**: Imbalanced classes for real-world testing.
+ **Challenging datasets**: Edge cases to stress-test model robustness.

The evaluation generates key metrics including accuracy, precision, recall, F1-score, Matthews Correlation Coefficient (MCC), and Area Under the Curve Receiver Operating Characteristic scores with visual curves for model comparison.

## Using custom data
<a name="w2aac37c15c23b7"></a>

If you have your own labeled dataset, you can substitute it in the notebook. The framework automatically adapts to your data format and generates the same comprehensive metrics.

**Supported data formats:**
+ **CSV format:** Two columns: `text` and `label`
+ **Label formats:** "positive"/"negative", "LABEL\_0"/"LABEL\_1", "True"/"False", or "0"/"1"
+ **Unsupervised:** Single `text` column for confidence analysis

## Set up your evaluation environment
<a name="w2aac37c15c23b9"></a>

Create a JupyterLab space in SageMaker Amazon SageMaker Studio to run the evaluation notebook.

1. In Studio, choose **JupyterLab** from the home screen.

1. If you don't have a space:

   1. Choose **Create space**.

   1. Enter a descriptive name (for example, **TextModelEvaluation)**.

   1. Keep the default instance type.

   1. Choose **Run space**.

   1. When the space has been created, choose **Open JupyterLab**.

### Access the evaluation notebook
<a name="w2aac37c15c23b9b7"></a>

Download the [zip file](samples/sagemaker-text-classification-evaluation-2.zip) and extract it to your local machine. Upload the entire extracted folder to your JupyterLab space to begin testing your models. The package contains the main evaluation notebook, sample datasets, supporting Python modules, and detailed instructions for the complete evaluation framework.

**Note**  
After extracting the package, review the README file for detailed setup instructions and framework overview.

Continue to [Interpret your results](jumpstart-text-classification-interpret.md) to learn how to analyze the evaluation output and make data-driven model selection decisions.