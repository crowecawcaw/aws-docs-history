# Custom data

sources

On this page we will describe how to create a custom data source class and show some usage
examples. With custom data sources, you can use the SageMaker AI SDK for Python (Boto3) provided APIs in the same
way as if you are using Amazon SageMaker Feature Store provided data sources.

To use a custom data source to transform and ingest data into a feature group using
Feature Processing, you will need to extend the `PySparkDataSource` class with
the following class members and function.

- `data_source_name` (str): an arbitrary name for the data source. For
  example, Amazon Redshift, Snowflake, or a Glue Catalog ARN.
- `data_source_unique_id` (str): a unique identifier that refers to the
  specific resource being accessed. For example, table name, DDB Table ARN, Amazon S3
  prefix. All usage of the same `data_source_unique_id` in custom data
  sources will be associated to the same data source in the lineage view. Lineage
  includes information about the execution code of a feature processing workflow, what
  data sources were used, and how they are ingested into the feature group or feature.
  For information about viewing lineage of a feature group in
  **Studio**, see [View lineage
  from the console](feature-store-use-with-studio.md#feature-store-view-feature-processor-pipeline-lineage-studio "feature-store-use-with-studio.md#feature-store-view-feature-processor-pipeline-lineage-studio").
- `read_data` (func): a method used to connect with the feature
  processor. Returns a Spark data frame. For examples, see [Custom data
  source examples](feature-store-feature-processor-data-sources-custom-examples.md "feature-store-feature-processor-data-sources-custom-examples.md").
  Both `data_source_name` and `data_source_unique_id` are used to
  uniquely identify your lineage entity. The following is an example for a custom data source
  class named `CustomDataSource`.

```
from sagemaker.feature_store.feature_processor import PySparkDataSource
from pyspark.sql import DataFrame

class CustomDataSource(PySparkDataSource):

    data_source_name = "`custom-data-source-name`"
    data_source_unique_id = "`custom-data-source-id`"

    def read_data(self, parameter, spark) -> DataFrame:
        `your own code here to read data into a Spark dataframe`
        return dataframe
```
