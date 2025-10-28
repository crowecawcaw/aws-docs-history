# Resources for using R with Amazon SageMaker AI

This document lists resources that can help you learn how to use Amazon SageMaker AI features with the
R software environment. The following sections introduce SageMaker AI's built-in R kernel, explain how
to get started with R on SageMaker AI, and provide several example notebooks.

The examples are organized in three levels: beginner, intermediate, and advanced. They
start with [Getting Started with R on SageMaker AI](https://sagemaker-examples.readthedocs.io/en/latest/r_examples/r_sagemaker_hello_world/r_sagemaker_hello_world.html "https://sagemaker-examples.readthedocs.io/en/latest/r_examples/r_sagemaker_hello_world/r_sagemaker_hello_world.html"), continue with end-to-end machine learning with R on
SageMaker AI, and then finish with more advanced topics such as SageMaker Processing with R script, and
bring-your-own R algorithm to SageMaker AI.

For information on how to bring your own custom R image to Studio, see [Custom Images in Amazon SageMaker Studio Classic](studio-byoi.md "studio-byoi.md"). For a similar blog article, see [Bringing your own R environment to Amazon SageMaker Studio](https://aws.amazon.com/blogs/machine-learning/bringing-your-own-r-environment-to-amazon-sagemaker-studio/ "https://aws.amazon.com/blogs/machine-learning/bringing-your-own-r-environment-to-amazon-sagemaker-studio/").

###### Topics

- [RStudio support in SageMaker AI](#rstudio-for-r "#rstudio-for-r")
- [R kernel in SageMaker AI](#r-sagemaker-kernel-ni "#r-sagemaker-kernel-ni")
- [Example notebooks](#r-sagemaker-example-notebooks "#r-sagemaker-example-notebooks")
- [Get started with R in SageMaker AI](r-sagemaker-get-started.md "r-sagemaker-get-started.md")

## RStudio support in SageMaker AI

Amazon SageMaker AI supports RStudio as a fully-managed integrated development
environment (IDE) integrated with Amazon SageMaker AI domain. With
RStudio integration, you can launch an RStudio environment in the domain to run your RStudio
workflows on SageMaker AI resources. For more information, see [RStudio on Amazon SageMaker AI](rstudio.md "rstudio.md").

## R kernel in SageMaker AI

SageMaker notebook instances support R using a pre-installed R kernel. Also, the R kernel has
the reticulate library, an R to Python interface, so you can use the features of SageMaker AI Python
SDK from within an R script.

- [reticulatelibrary](https://rstudio.github.io/reticulate/ "https://rstudio.github.io/reticulate/"): provides
  an R interface to the [Amazon SageMaker Python SDK](https://sagemaker.readthedocs.io/en/stable "https://sagemaker.readthedocs.io/en/stable"). The reticulate package translates between R
  and Python objects.

## Example notebooks

**Prerequisites**

- [Getting Started with R on SageMaker AI](https://sagemaker-examples.readthedocs.io/en/latest/r_examples/r_sagemaker_hello_world/r_sagemaker_hello_world.html "https://sagemaker-examples.readthedocs.io/en/latest/r_examples/r_sagemaker_hello_world/r_sagemaker_hello_world.html") – This sample notebook describes how you can
  develop R scripts using Amazon SageMaker AI‘s R kernel. In this notebook you set up your SageMaker AI
  environment and permissions, download the [abalone dataset](https://archive.ics.uci.edu/ml/datasets/abalone "https://archive.ics.uci.edu/ml/datasets/abalone") from the
  [UCI Machine Learning Repository](https://archive.ics.uci.edu/datasets "https://archive.ics.uci.edu/datasets"),
  do some basic processing and visualization on the data, then save the data as .csv format
  to S3.

**Beginner Level**

- [SageMaker AI Batch Transform using R Kernel](https://sagemaker-examples.readthedocs.io/en/latest/r_examples/r_batch_transform/r_xgboost_batch_transform.html "https://sagemaker-examples.readthedocs.io/en/latest/r_examples/r_batch_transform/r_xgboost_batch_transform.html") – This sample Notebook describes how to
  conduct a batch transform job using SageMaker AI’s Transformer API and the [XGBoost
  algorithm](xgboost.md "xgboost.md"). The notebook also uses the Abalone dataset.

**Intermediate Level**

- [Hyperparameter Optimization for XGBoost in R](https://sagemaker-examples.readthedocs.io/en/latest/r_examples/r_xgboost_hpo_batch_transform/r_xgboost_hpo_batch_transform.html "https://sagemaker-examples.readthedocs.io/en/latest/r_examples/r_xgboost_hpo_batch_transform/r_xgboost_hpo_batch_transform.html") – This sample notebook extends the
  previous beginner notebooks that use the abalone dataset and XGBoost. It describes how to
  do model tuning with [hyperparameter optimization](https://sagemaker.readthedocs.io/en/stable/tuner.html "https://sagemaker.readthedocs.io/en/stable/tuner.html"). You will also learn how to use batch transform for
  batching predictions, as well as how to create a model endpoint to make real-time
  predictions.
- [Amazon SageMaker Processing with R](https://sagemaker-examples.readthedocs.io/en/latest/r_examples/r_in_sagemaker_processing/r_in_sagemaker_processing.html "https://sagemaker-examples.readthedocs.io/en/latest/r_examples/r_in_sagemaker_processing/r_in_sagemaker_processing.html") – [SageMaker Processing](https://aws.amazon.com/blogs/aws/amazon-sagemaker-processing-fully-managed-data-processing-and-model-evaluation/ "https://aws.amazon.com/blogs/aws/amazon-sagemaker-processing-fully-managed-data-processing-and-model-evaluation/") lets you preprocess, post-process and run model evaluation
  workloads. This example shows you how to create an R script to orchestrate a Processing
  job.

**Advanced Level**

- [Train and Deploy Your Own R Algorithm in SageMaker AI](https://sagemaker-examples.readthedocs.io/en/latest/r_examples/r_byo_r_algo_hpo/tune_r_bring_your_own.html "https://sagemaker-examples.readthedocs.io/en/latest/r_examples/r_byo_r_algo_hpo/tune_r_bring_your_own.html") – Do you already have an R
  algorithm, and you want to bring it into SageMaker AI to tune, train, or deploy it? This example
  walks you through how to customize SageMaker AI containers with custom R packages, all the way to
  using a hosted endpoint for inference on your R-origin model.
