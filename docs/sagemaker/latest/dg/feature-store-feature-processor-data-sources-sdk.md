# Feature Processor SDK data

sources

The Amazon SageMaker Feature Store Feature Processor SDK for Python (Boto3) provides constructs to load data from feature groups
or objects stored in Amazon S3. For a full list of Feature Store provided data source definitions, see the
[Feature Processor data source Feature Store Python SDK](https://github.com/aws/sagemaker-python-sdk/blob/master/src/sagemaker/feature_store/feature_processor/_data_source.py "https://github.com/aws/sagemaker-python-sdk/blob/master/src/sagemaker/feature_store/feature_processor/_data_source.py").

For examples on how to use the Feature Store Python SDK data source definitions, see [Example Feature Processing code
for common use cases](feature-store-feature-processor-examples.md "feature-store-feature-processor-examples.md").

## FeatureGroupDataSource

The `FeatureGroupDataSource` is used to specify a feature group as an input data
source for a Feature Processor. Data can be loaded from an offline store feature group.
Attempting to load your data from an online store feature group will result in a validation
error. You can specify start and end offsets to limit the data that is loaded to a specific time
range. For example, you can specify a start offset of ‘14 days' to load only the last two weeks
of data, and you can additionally specify an end offset of '7 days' to limit the input to the
previous week of data.

## Feature Store provided

data source definitions

The Feature Store Python SDK contain data source definitions that can be used to specify various
input data sources for a Feature Processor. These include CSV, Parquet, and Iceberg table
sources. For a full list of Feature Store provided data source definitions, see the [Feature Processor data source Feature Store Python SDK](https://github.com/aws/sagemaker-python-sdk/blob/master/src/sagemaker/feature_store/feature_processor/_data_source.py "https://github.com/aws/sagemaker-python-sdk/blob/master/src/sagemaker/feature_store/feature_processor/_data_source.py").
