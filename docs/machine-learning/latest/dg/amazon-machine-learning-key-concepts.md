We are no longer updating the Amazon Machine Learning service or accepting
new users for it. This documentation is available for existing users, but we are
no longer updating it. For more information, see [What is Amazon Machine Learning](what-is-amazon-machine-learning.md "what-is-amazon-machine-learning.md").

# Amazon Machine Learning Key Concepts

This section summarizes the following key concepts and describes in greater
detail how they are used within Amazon ML:

- [Datasources](#datasources "#datasources") contain
  metadata associated with data inputs to Amazon ML
- [ML Models](#ml-models "#ml-models") generate
  predictions using the patterns extracted from the input data
- [Evaluations](#evaluations "#evaluations") measure the
  quality of ML models
- [Batch Predictions](#batch-predictions "#batch-predictions") _asynchronously_
  generate predictions for multiple input data
  observations
- [Real-time Predictions](#real-time-predictions "#real-time-predictions") _synchronously_ generate
  predictions for individual data observations

## Datasources

A datasource is an object that contains metadata about your
input data. Amazon ML reads your input data, computes
descriptive statistics on its attributes, and stores the
statistics—along with a schema and other information—as part of
the datasource object. Next, Amazon ML uses the datasource to
train and evaluate an ML model and generate batch predictions.

###### Important

A datasource does not store a copy of your input data.
Instead, it stores a reference to the Amazon S3 location where
your input data resides. If you move or change the Amazon S3
file, Amazon ML cannot access or use it to create a ML model,
generate evaluations, or generate predictions.

The following table defines terms that are related to
datasources.

| **Term**         | **Definition**                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Attribute        | A unique, named property within an observation. In<br>tabular-formatted data such as spreadsheets or<br>comma-separated values (CSV) files, the column<br>headings represent the attributes, and the rows<br>contain values for each attribute.<br>Synonyms: variable, variable name, field, column                                                                                                                                        |
| Datasource Name  | (Optional) Allows you to define a human-readable name<br>for a datasource. These names enable you to find and<br>manage your datasources in the Amazon ML console.                                                                                                                                                                                                                                                                         |
| Input Data       | Collective name for all the observations that are<br>referred to by a datasource.                                                                                                                                                                                                                                                                                                                                                          |
| Location         | Location of input data. Currently, Amazon ML can use<br>data that is stored within Amazon S3 buckets, Amazon<br>Redshift databases, or MySQL databases in Amazon<br>Relational Database Service (RDS).                                                                                                                                                                                                                                     |
| Observation      | A single input data unit. For example, if you are<br>creating an ML model to detect fraudulent<br>transactions, your input data will consist of many<br>observations, each representing an individual<br>transaction.<br>Synonyms: record, example, instance, row                                                                                                                                                                          |
| Row ID           | (Optional) A flag that, if specified, identifies an<br>attribute in the input data to be included in the<br>prediction output. This attribute makes it easier to<br>associate which prediction corresponds with which<br>observation.<br>Synonyms: row identifier                                                                                                                                                                          |
| Schema           | The information needed to interpret the input data,<br>including attribute names and their assigned data types,<br>and names of special attributes.                                                                                                                                                                                                                                                                                        |
| Statistics       | Summary statistics for each attribute in the input<br>data. These statistics serve two purposes:<br>The Amazon ML console displays them in graphs to help<br>you understand your data at-a-glance and identify<br>irregularities or errors.<br>Amazon ML uses them during the training process to<br>improve the quality of the resulting ML model.                                                                                        |
| Status           | Indicates the current state of the datasource, such as<br>**In Progress**,<br>**Completed**, or<br>**Failed**.                                                                                                                                                                                                                                                                                                                             |
| Target Attribute | In the context of training an ML model, the target<br>attribute identifies the name of the attribute in the<br>input data that contains the "correct"<br>answers. Amazon ML uses this to discover patterns in<br>the input data and generate an ML model. In the<br>context of evaluating and generating predictions, the<br>target attribute is the attribute whose value will be<br>predicted by a trained ML model.<br>Synonyms: target |

## ML Models

An ML model is a mathematical model that generates predictions
by finding patterns in your data. Amazon ML supports three types
of ML models: binary classification, multiclass classification
and regression.

The following table defines terms that are related to ML models.

| **Term**         | **Definition**                                                                                                                                                                                                                                                          |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Regression       | The goal of training a regression ML model is to predict<br>a numeric value.                                                                                                                                                                                            |
| Multiclass       | The goal of training a multiclass ML model is to predict<br>values that belong to a limited, pre-defined set of<br>permissible values.                                                                                                                                  |
| Binary           | The goal of training a binary ML model is to predict<br>values that can only have one of two states, such as true or false.                                                                                                                                             |
| Model Size       | ML models capture and store patterns. The more patterns<br>a ML model stores, the bigger it will be. ML model size<br>is described in Mbytes.                                                                                                                           |
| Number of Passes | When you train an ML model, you use data from a<br>datasource. It is sometimes beneficial to use each data<br>record in the learning process more than once. The<br>number of times that you let Amazon ML use the same data<br>records is called the number of passes. |
| Regularization   | Regularization is a machine learning technique that you<br>can use to obtain higher-quality models. Amazon ML<br>offers a default setting that works well for most cases.                                                                                               |

## Evaluations

An evaluation measures the quality of your ML model and
determines if it is performing well.

The following table defines terms that are related to
evaluations.

| **Term**                | **Definition**                                                                                                                                                                                                                           |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Model Insights          | Amazon ML provides you with a metric and a number of<br>insights that you can use to evaluate the predictive<br>performance of your model.                                                                                               |
| AUC                     | Area Under the ROC Curve (AUC) measures the ability of a<br>binary ML model to predict a higher score for positive<br>examples as compared to negative examples.                                                                         |
| Macro-averaged F1-score | The macro-averaged F1-score is used to evaluate the<br>predictive performance of multiclass ML models.                                                                                                                                   |
| RMSE                    | The Root Mean Square Error (RMSE) is a metric used to<br>evaluate the predictive performance of regression ML<br>models.                                                                                                                 |
| Cut-off                 | ML models work by generating numeric prediction scores.<br>By applying a cut-off value, the system converts these<br>scores into 0 and 1 labels.                                                                                         |
| Accuracy                | Accuracy measures the percentage of correct predictions.                                                                                                                                                                                 |
| Precision               | Precision shows the percentage of actual positive instances<br>(as opposed to false positives) among those instances that have been retrieved (those predicted to be positive). In other<br>words, how many selected items are positive? |
| Recall                  | Recall shows the percentage of actual positives among the total number of relevant instances (actual positives). In other words,<br>how many positive items are selected?                                                                |

## Batch Predictions

Batch predictions are for a set of observations that can run all
at once. This is ideal for predictive analyses that do not have
a real-time requirement.

The following table defines terms that are related to batch
predictions.

| **Term**        | **Definition**                                                                                                                            |
| --------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| Output Location | The results of a batch prediction are stored in an S3<br>bucket output location.                                                          |
| Manifest File   | This file relates each input data file with its<br>associated batch prediction results. It is stored in the<br>S3 bucket output location. |

## Real-time Predictions

Real-time predictions are for applications with a low latency
requirement, such as interactive web, mobile, or desktop
applications. Any ML model can be queried for predictions by
using the low latency real-time prediction API.

The following table defines terms that are related to real-time
predictions.

| **Term**                      | **Definition**                                                                                                                                                                                                    |
| ----------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Real-time Prediction API      | The Real-time Prediction API accepts a single input<br>observation in the request payload and returns the<br>prediction in the response.                                                                          |
| Real-time Prediction Endpoint | To use an ML model with the real-time prediction API,<br>you need to create a real-time prediction endpoint. Once<br>created, the endpoint contains the URL that you can use<br>to request real-time predictions. |
