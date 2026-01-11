# Resources for using Scikit-learn with Amazon SageMaker AI

You can use Amazon SageMaker AI to train and deploy a model using custom Scikit-learn code. The SageMaker AI Python SDK
Scikit-learn estimators and models and the SageMaker AI open-source Scikit-learn containers make writing a
Scikit-learn script and running it in SageMaker AI easier. The following section
provides reference material you can use to learn how to use Scikit-learn with SageMaker AI.

**Requirements**

Scikit-learn 1.4 has the following dependencies.

| Dependency    | Minimum version |
| ------------- | --------------- |
| Python        | 3.10            |
| NumPy         | 2.1.0           |
| SciPy         | 1.15.3          |
| joblib        | 1.5.2           |
| threadpoolctl | 3.6.0           |

The SageMaker AI Scikit-learn container supports the following Scikit-learn versions.

| Supported Scikit-learn version | Minimum Python version |
| ------------------------------ | ---------------------- |
| `1.4-2`                        | `3.10`                 |
| `1.2-1`                        | `3.8`                  |
| `1.0-1`                        | `3.7`                  |
| `0.23-1`                       | `3.6`                  |
| `0.20.0`                       | `2.7` or `3.4`         |

For general information about writing Scikit-learn training scripts and using Scikit-learn estimators
and models with SageMaker AI, see [Using
Scikit-learn with the SageMaker Python SDK](https://sagemaker.readthedocs.io/en/stable/using_sklearn.html "https://sagemaker.readthedocs.io/en/stable/using_sklearn.html").

## What do you want to do?

###### Note

Matplotlib v2.2.3 or newer is required to run the SageMaker AI Scikit-learn example notebooks.

I want to use Scikit-learn for data processing, feature engineering, or model evaluation in
SageMaker AI.

For a sample Jupyter notebook, see [https://github.com/awslabs/amazon-sagemaker-examples/tree/master/sagemaker_processing/scikit_learn_data_processing_and_model_evaluation](https://github.com/awslabs/amazon-sagemaker-examples/tree/master/sagemaker_processing/scikit_learn_data_processing_and_model_evaluation "https://github.com/awslabs/amazon-sagemaker-examples/tree/master/sagemaker_processing/scikit_learn_data_processing_and_model_evaluation").

For a blog post on training and deploying a Scikit-learn model, see [Amazon SageMaker AI adds Scikit-Learn support](https://aws.amazon.com/blogs/machine-learning/amazon-sagemaker-adds-scikit-learn-support/ "https://aws.amazon.com/blogs/machine-learning/amazon-sagemaker-adds-scikit-learn-support/").

For documentation, see [ReadTheDocs](https://sagemaker.readthedocs.io/en/stable/amazon_sagemaker_processing.html#data-pre-processing-and-model-evaluation-with-scikit-learn "https://sagemaker.readthedocs.io/en/stable/amazon_sagemaker_processing.html#data-pre-processing-and-model-evaluation-with-scikit-learn").

I want to train a custom Scikit-learn model in SageMaker AI.

For a sample Jupyter notebook, see [https://github.com/awslabs/amazon-sagemaker-examples/tree/master/sagemaker-python-sdk/scikit_learn_iris](https://github.com/awslabs/amazon-sagemaker-examples/tree/master/sagemaker-python-sdk/scikit_learn_iris "https://github.com/awslabs/amazon-sagemaker-examples/tree/master/sagemaker-python-sdk/scikit_learn_iris").

For documentation, see [Train a Model with Scikit-learn](https://sagemaker.readthedocs.io/en/stable/using_sklearn.html#train-a-model-with-sklearn "https://sagemaker.readthedocs.io/en/stable/using_sklearn.html#train-a-model-with-sklearn").

I have a Scikit-learn model that I trained in SageMaker AI, and I want to deploy it to a hosted
endpoint.

For more information, see [Deploy
Scikit-learn models](https://sagemaker.readthedocs.io/en/stable/using_sklearn.html#deploy-sklearn-models "https://sagemaker.readthedocs.io/en/stable/using_sklearn.html#deploy-sklearn-models").

I have a Scikit-learn model that I trained outside of SageMaker AI, and I want to deploy it to a SageMaker AI
endpoint

For more information, see [Deploy Endpoints from Model Data](https://sagemaker.readthedocs.io/en/stable/using_sklearn.html#deploy-endpoints-from-model-data "https://sagemaker.readthedocs.io/en/stable/using_sklearn.html#deploy-endpoints-from-model-data").

I want to see the API documentation for [Amazon SageMaker Python SDK](https://sagemaker.readthedocs.io/en/stable "https://sagemaker.readthedocs.io/en/stable") Scikit-learn classes.

For more information, see [Scikit-learn
Classes](https://sagemaker.readthedocs.io/en/stable/sagemaker.sklearn.html "https://sagemaker.readthedocs.io/en/stable/sagemaker.sklearn.html").

I want to see information about SageMaker AI Scikit-learn containers.

For more information, see [SageMaker Scikit-learn Container GitHub repository](https://github.com/aws/sagemaker-scikit-learn-container "https://github.com/aws/sagemaker-scikit-learn-container").
