# Tutorial for building models with Notebook Instances

This Get Started tutorial walks you through how to create a SageMaker notebook instance,
open a Jupyter notebook with a preconfigured kernel with the Conda environment for
machine learning, and start a SageMaker AI session to run an end-to-end ML cycle. You'll learn
how to save a dataset to a default Amazon S3 bucket automatically paired with the SageMaker AI
session, submit a training job of an ML model to Amazon EC2, and deploy the trained model for
prediction by hosting or batch inferencing through Amazon EC2.

This tutorial explicitly shows a complete ML flow of training the XGBoost model from
the SageMaker AI built-in model pool. You use the [US Adult Census dataset](https://archive.ics.uci.edu/ml/datasets/adult "https://archive.ics.uci.edu/ml/datasets/adult"),
and you evaluate the performance of the trained SageMaker AI XGBoost model on predicting
individuals' income.

- [SageMaker AI
  XGBoost](xgboost.md "xgboost.md") – The [XGBoost](https://xgboost.readthedocs.io/en/latest/ "https://xgboost.readthedocs.io/en/latest/") model is
  adapted to the SageMaker AI environment and preconfigured as Docker containers. SageMaker AI
  provides a suite of [built-in algorithms](algos.md "algos.md") that are
  prepared for using SageMaker AI features. To learn more about what ML algorithms are
  adapted to SageMaker AI, see [Choose an Algorithm](algorithms-choose.md "algorithms-choose.md")
  and [Use Amazon
  SageMaker Built-in Algorithms](algos.md "algos.md"). For the SageMaker AI built-in algorithm API
  operations, see [First-Party Algorithms](https://sagemaker.readthedocs.io/en/stable/algorithms/index.html "https://sagemaker.readthedocs.io/en/stable/algorithms/index.html") in the [Amazon SageMaker Python SDK](https://sagemaker.readthedocs.io/en/stable "https://sagemaker.readthedocs.io/en/stable").
- [Adult Census
  dataset](https://archive.ics.uci.edu/ml/datasets/adult "https://archive.ics.uci.edu/ml/datasets/adult") – The dataset from the [1994 Census bureau database](http://www.census.gov/en.html "http://www.census.gov/en.html") by
  Ronny Kohavi and Barry Becker (Data Mining and Visualization, Silicon Graphics).
  The SageMaker AI XGBoost model is trained using this dataset to predict if an individual
  makes over $50,000 a year or less.

###### Topics

- [Create an Amazon SageMaker Notebook Instance for the
  tutorial](gs-setup-working-env.md "gs-setup-working-env.md")
- [Create a Jupyter notebook in the SageMaker notebook
  instance](ex1-prepare.md "ex1-prepare.md")
- [Prepare a
  dataset](ex1-preprocess-data.md "ex1-preprocess-data.md")
- [Train a Model](ex1-train-model.md "ex1-train-model.md")
- [Deploy the model to Amazon EC2](ex1-model-deployment.md "ex1-model-deployment.md")
- [Evaluate the model](ex1-test-model.md "ex1-test-model.md")
- [Clean up Amazon SageMaker notebook instance resources](ex1-cleanup.md "ex1-cleanup.md")
