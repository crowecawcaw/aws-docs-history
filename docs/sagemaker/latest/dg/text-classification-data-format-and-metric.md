# Datasets format and objective

metric for text classification

In this section we learn about the available formats for datasets used in text
classification as well as the metric used to evaluate the predictive quality of machine
learning model candidates. The metrics calculated for candidates are specified using an array
of [MetricDatum](../APIReference/API_MetricDatum.md "../APIReference/API_MetricDatum.md") types.

## Datasets formats

Autopilot supports tabular data formatted as CSV files or as Parquet files. For tabular
data, each column contains a feature with a specific data type and each row contains an
observation. The properties of these two file formats differ considerably.

- **CSV** (comma-separated-values) is a row-based file
  format that stores data in human readable plaintext which a popular choice for data
  exchange as they are supported by a wide range of applications.
- **Parquet** is a column-based file format where the
  data is stored and processed more efficiently than row-based file formats. This makes
  them a better option for big data problems.

The **data types** accepted for columns include numerical,
categorical, text.

Autopilot supports building machine learning models on large datasets up to hundreds of
GBs. For details on the default resource limits for input datasets and how to increase them,
see [Amazon SageMaker Autopilot
quotas](autopilot-quotas.md "autopilot-quotas.md").

## Objective metric

The following list contains the names of the metrics that are currently available to
measure the performance of models for text classification.

**`Accuracy`**

The ratio of the number of correctly classified items to the total number of
(correctly and incorrectly) classified items. Accuracy measures how close the
predicted class values are to the actual values. Values for accuracy metrics vary
between zero (0) and one (1). A value of 1 indicates perfect accuracy, and 0 indicates
perfect inaccuracy.
