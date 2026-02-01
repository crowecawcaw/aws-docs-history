Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Tutorials for Amazon Redshift ML

You can use Amazon Redshift ML to train machine learning models using SQL statements,
and then invoke the models in SQL queries for prediction. Machine learning in Amazon Redshift
trains a model with one SQL command. Amazon Redshift automatically launches a training
job in Amazon SageMaker AI and generates a model. Once a model is created, you can perform
predictions in Amazon Redshift using the model’s prediction function.

Follow the steps in these tutorials to learn about Amazon Redshift ML features:

- [Tutorial: Building customer churn
  models](tutorial_customer_churn.md "tutorial_customer_churn.md") –
  In this tutorial, you use Amazon Redshift ML to create a customer churn model with the
  CREATE MODEL command, and run prediction queries for user scenarios. Then, you implement
  queries using the SQL function that the CREATE MODEL command generates.
- [Tutorial: Building K-means clustering
  models](tutorial_k-means_clustering.md "tutorial_k-means_clustering.md") –
  In this tutorial, you use Amazon Redshift ML to create, train, and deploy a machine
  learning model based on the [K-means
  algorithm](url-sm-dev.md "url-sm-dev.md").
- [Tutorial: Building multi-class classification
  models](tutorial_multi-class_classification.md "tutorial_multi-class_classification.md") –
  In this tutorial, you use Amazon Redshift ML to create a machine learning model that
  solves multi-class classification problems. The multi-class classification
  algorithm classifies data points into one of three or more classes. Then, you
  implement queries using the SQL function that the CREATE MODEL command
  generates.
- [Tutorial: Building XGBoost models](tutorial_xgboost.md "tutorial_xgboost.md") –
  In this tutorial, you create a model with data from Amazon S3 and run prediction
  queries with the model using Amazon Redshift ML. The XGBoost algorithm is an optimized
  implementation of the gradient boosted trees algorithm.
- [Tutorial: Building regression models](tutorial_regression.md "tutorial_regression.md") –
  In this tutorial, you use Amazon Redshift ML to create a machine learning regression model
  and run prediction queries on the model. Regression models allow you to predict
  numerical outcomes, such as the price of a house, or how many people will use a city’s
  bike rental service.
- [Tutorial: Building regression models with linear learner](tutorial_linear_learner_regression.md "tutorial_linear_learner_regression.md") –
  In this tutorial, you create a linear learner model with data from Amazon S3 and run
  prediction queries with the model using Amazon Redshift ML. The SageMaker AI linear learner algorithm
  solves either regression or multi-class classification problems.
- [Tutorial: Building multi-class classification models with linear learner](tutorial_linear_learner_multi-class_classification.md "tutorial_linear_learner_multi-class_classification.md") –
  In this tutorial, you create a linear learner model with data from Amazon S3, and then
  run prediction queries with the model using Amazon Redshift ML. The SageMaker AI linear learner
  algorithm solves either regression or classification problems.
