# Use Feature Store with SDK for Python (Boto3)

The feature group is the main Feature Store resource that contains your machine learning (ML) data
and metadata stored in Amazon SageMaker Feature Store. A feature group is a logical grouping of features and records.
A feature group’s definition is composed of a configurations for its online and offline store
and a list of feature definitions that are used to describe the values of your records. The
feature definitions must include a record identifier name and an event time name. For more
information on feature store concepts, see [Feature Store concepts](feature-store-concepts.md "feature-store-concepts.md").

Prior to using a feature store you typically load your dataset, run transformations, and set
up your features for ingestion. This process has a lot of variation and is highly dependent on
your data. The example code in the following topics refer to the [Introduction to Feature Store](https://sagemaker-examples.readthedocs.io/en/latest/sagemaker-featurestore/feature_store_introduction.html "https://sagemaker-examples.readthedocs.io/en/latest/sagemaker-featurestore/feature_store_introduction.html") and [Fraud Detection with Amazon SageMaker Feature Store](https://sagemaker-examples.readthedocs.io/en/latest/sagemaker-featurestore/sagemaker_featurestore_fraud_detection_python_sdk.html "https://sagemaker-examples.readthedocs.io/en/latest/sagemaker-featurestore/sagemaker_featurestore_fraud_detection_python_sdk.html") example notebooks, respectively. Both use the
AWS SDK for Python (Boto3). For more Feature Store examples and resources, see [Amazon SageMaker Feature Store resources](feature-store-resources.md "feature-store-resources.md").

Feature Store supports the following feature types: `String`, `Fractional`
(IEEE 64-bit floating point value), and `Integral` (Int64 - 64 bit signed integral
value). The default type is set to `String`. This means that, if a column in your
dataset is not of a `float` or `long` feature type, it defaults to
`String` in your feature store.

You may use a schema to describe your data’s columns and data types. You pass this schema
into `FeatureDefinitions`, a required parameter for a `FeatureGroup`. You
can use the SDK for Python (Boto3), which has automatic data type detection when you use the
`load_feature_definitions` function.

The default behavior when a new feature record is added with an already existing record ID
is as follows. In the offline store, the new record will be appended. In the online store, if
the event time of the new record is less than the existing event time then nothing will happen,
but if the event time of the new record is greater than or equal to the existing event time, the
record will be overwritten.

When you create a new feature group you can choose one of the following table
formats:

- AWS Glue (Default)
- Apache Iceberg
  Ingesting data, especially when streaming, can result in a large number of small files
  deposited into the offline store. This can negatively impact query performance due the higher
  number of file operations required. To avoid potential performance issues, use the Apache
  Iceberg table format when creating new feature groups. With Iceberg you can compact the small
  data files into fewer large files in the partition, resulting in significantly faster queries.
  This compaction operation is concurrent and does not affect ongoing read and write operations on
  the feature group. If you choose the Iceberg option when creating new feature groups, Amazon SageMaker Feature Store
  will create the Iceberg tables using Parquet file format, and register the tables with the
  AWS Glue Data Catalog.

###### Important

Note that for feature groups in Iceberg table format, you must specify `String`
as the value for the event time. If you specify any other type, you can't create the feature
group successfully.

In the following we list some available Feature Store managed resources.

###### Topics

- [Introduction to Feature Store example
  notebook](feature-store-introduction-notebook.md "feature-store-introduction-notebook.md")
- [Fraud detection with Feature Store example
  notebook](feature-store-fraud-detection-notebook.md "feature-store-fraud-detection-notebook.md")
