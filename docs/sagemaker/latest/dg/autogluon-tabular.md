# AutoGluon-Tabular

[AutoGluon-Tabular](https://auto.gluon.ai/stable/index.html "https://auto.gluon.ai/stable/index.html") is a
popular open-source AutoML framework that trains highly accurate machine learning models on
an unprocessed tabular dataset. Unlike existing AutoML frameworks that primarily focus on
model and hyperparameter selection, AutoGluon-Tabular succeeds by ensembling multiple models
and stacking them in multiple layers. This page includes information about Amazon EC2 instance
recommendations and sample notebooks for AutoGluon-Tabular.

## Amazon EC2 instance recommendation for the

AutoGluon-Tabular algorithm

SageMaker AI AutoGluon-Tabular supports single-instance CPU and single-instance GPU training.
Despite higher per-instance costs, GPUs train more quickly, making them more cost
effective. To take advantage of GPU training, specify the instance type as one of the
GPU instances (for example, P3). SageMaker AI AutoGluon-Tabular currently does not support multi-GPU
training.

## AutoGluon-Tabular sample

notebooks

The following table outlines a variety of sample notebooks that address different use cases of Amazon SageMaker AI AutoGluon-Tabular algorithm.

| **Notebook Title**                                                                                                                                                                                                                                                                                                                                                                                         | **Description**                                                                                                                             |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Tabular classification with Amazon SageMaker AI AutoGluon-Tabular algorithm](https://github.com/aws/amazon-sagemaker-examples/blob/main/introduction_to_amazon_algorithms/autogluon_tabular/Amazon_Tabular_Classification_AutoGluon.ipynb "https://github.com/aws/amazon-sagemaker-examples/blob/main/introduction_to_amazon_algorithms/autogluon_tabular/Amazon_Tabular_Classification_AutoGluon.ipynb") | This notebook demonstrates the use of the Amazon SageMaker AI AutoGluon-Tabular algorithm to train and host a tabular classification model. |
| [Tabular regression with Amazon SageMaker AI AutoGluon-Tabular algorithm](https://github.com/aws/amazon-sagemaker-examples/blob/main/introduction_to_amazon_algorithms/autogluon_tabular/Amazon_Tabular_Regression_AutoGluon.ipynb "https://github.com/aws/amazon-sagemaker-examples/blob/main/introduction_to_amazon_algorithms/autogluon_tabular/Amazon_Tabular_Regression_AutoGluon.ipynb")             | This notebook demonstrates the use of the Amazon SageMaker AI AutoGluon-Tabular algorithm to train and host a tabular regression model.     | For instructions on how to create and access Jupyter notebook instances that you can use to run the example in SageMaker AI, see [Amazon SageMaker notebook instances](nbi.md "nbi.md"). After you have created a notebook instance and opened it, choose the **SageMaker AI Examples** tab to see a list of all of the SageMaker AI samples. To open a notebook, choose its **Use** tab and choose **Create copy**. |
