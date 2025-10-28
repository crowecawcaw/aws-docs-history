# Feature Store Feature Processor SDK

Declare a Feature Store Feature Processor definition by decorating your transformation functions with
the `@feature_processor` decorator. The SageMaker AI SDK for Python (Boto3) automatically loads data from
the configured input data sources, applies the decorated transformation function, and then
ingests the transformed data to a target feature group. Decorated transformation functions must
conform to the expected signature of the `@feature_processor` decorator. For more
information about the `@feature_processor` decorator, see [@feature_processor Decorator](https://sagemaker.readthedocs.io/en/stable/api/prep_data/feature_store.html#feature-processor-decorator "https://sagemaker.readthedocs.io/en/stable/api/prep_data/feature_store.html#feature-processor-decorator") in the Amazon SageMaker Feature Store Read the Docs.

With the `@feature_processor` decorator, your transformation function runs in a
Spark runtime environment where the input arguments provided to your function and its return
value are Spark DataFrames. The number of input parameters in your transformation function must
match the number of inputs configured in the `@feature_processor` decorator.

For more information on the `@feature_processor` decorator, see the [Feature Processor Feature Store SDK for Python (Boto3)](https://github.com/aws/sagemaker-python-sdk/tree/master/src/sagemaker/feature_store/feature_processor "https://github.com/aws/sagemaker-python-sdk/tree/master/src/sagemaker/feature_store/feature_processor").

The following code are basic examples on how to use the `@feature_processor`
decorator. For more specific example usage cases, see [Example Feature Processing code
for common use cases](feature-store-feature-processor-examples.md "feature-store-feature-processor-examples.md").

The Feature Processor SDK can be installed from the SageMaker Python SDK and its extras using the
following command.

```
pip install sagemaker[feature-processor]
```

In the following examples, `us-east-1` is
the region of the resource, `111122223333` is
the resource owner account ID, and
`your-feature-group-name` is the feature group
name.

The following is a basic feature processor definition, where the
`@feature_processor` decorator configures a CSV input from Amazon S3 to be
loaded and provided to your transformation function (for example, `transform`), and
prepares it for ingestion to a feature group. The last line runs it.

```
from sagemaker.feature_store.feature_processor import CSVDataSource, feature_processor

CSV_DATA_SOURCE = CSVDataSource('s3://`your-bucket`/`prefix-to-csv`/')
OUTPUT_FG = 'arn:aws:sagemaker:`us-east-1`:`111122223333`:feature-group/`your-feature-group-name`'

@feature_processor(inputs=[CSV_DATA_SOURCE], output=OUTPUT_FG)
def transform(csv_input_df):
   return csv_input_df

transform()
```

The `@feature_processor` parameters include:

- `inputs` (List[str]): A list of data sources that are used in your Feature Store
  Feature Processor. If your data sources are feature groups or stored in Amazon S3 you may be able
  to use Feature Store provided data source definitions for feature processor. For a full list of Feature Store
  provided data source definitions, see the [Feature Processor Data Source](https://sagemaker.readthedocs.io/en/stable/api/prep_data/feature_store.html#feature-processor-data-source "https://sagemaker.readthedocs.io/en/stable/api/prep_data/feature_store.html#feature-processor-data-source") in the Amazon SageMaker Feature Store Read the Docs.
- `output` (str): The ARN of the feature group to ingest the output of the
  decorated function.
- `target_stores` (Optional[List[str]]): A list of stores (for example,
  `OnlineStore` or `OfflineStore`) to ingest to the output. If
  unspecified, data is ingested to all of the output feature group’s enabled stores.
- `parameters` (Dict[str, Any]): A dictionary to be provided to your
  transformation function.
- `enable_ingestion` (bool): A flag to indicate whether the transformation
  function’s outputs are ingested to the output feature group. This flag is useful during the
  development phase. If unspecified, ingestion is enabled.
  Optional wrapped function parameters (provided as an argument if provided in the function
  signature) include:

- `params` (Dict[str, Any]): The dictionary defined in the
  `@feature_processor` parameters. It also contains system configured parameters
  that can be referenced with the key `system`, such as the
  `scheduled_time` parameter.
- `spark` (SparkSession): A reference to the SparkSession instance initialized
  for the Spark Application.
  The following code is an example of using the `params` and `spark`
  parameters.

```
from sagemaker.feature_store.feature_processor import CSVDataSource, feature_processor

CSV_DATA_SOURCE = CSVDataSource('s3://`your-bucket`/`prefix-to-csv`/')
OUTPUT_FG = 'arn:aws:sagemaker:`us-east-1`:`111122223333`:feature-group/`your-feature-group-name`'

@feature_processor(inputs=[CSV_DATA_SOURCE], output=OUTPUT_FG)
def transform(csv_input_df, params, spark):

   scheduled_time = params['system']['scheduled_time']
   csv_input_df.createOrReplaceTempView('csv_input_df')
   return spark.sql(f'''
        SELECT *
        FROM csv_input_df
        WHERE date_add(event_time, 1) >= {scheduled_time}
   ''')

transform()
```

The `scheduled_time` system parameter (provided in the `params`
argument to your function) is an important value to support retrying each execution. The value
can help to uniquely identify the Feature Processor’s execution and can be used as a reference
point for daterange–based inputs (for example, only loading the last 24 hours worth of
data) to guarantee the input range independent of the code’s actual execution time. If the
Feature Processor runs on a schedule (see [Scheduled and event
based executions for Feature Processor pipelines](feature-store-feature-processor-schedule-pipeline.md "feature-store-feature-processor-schedule-pipeline.md")) then its value is fixed
to the time it is scheduled to run. The argument can be overridden during synchronous execution
using the SDK’s execute API to support use cases such as data backfills or re-running a missed
past execution. Its value is the current time if the Feature Processor runs any other
way.

For information about authoring Spark code, see the [Spark SQL Programming
Guide](https://spark.apache.org/docs/latest/sql-programming-guide.html "https://spark.apache.org/docs/latest/sql-programming-guide.html").

For more code samples for common use-cases, see the [Example Feature Processing code
for common use cases](feature-store-feature-processor-examples.md "feature-store-feature-processor-examples.md").

Note that transformation functions decorated with `@feature_processor` do not
return a value. To programmatically test your function, you can remove or monkey patch the
`@feature_processor` decorator such that it acts as a pass-through to the wrapped
function. For more details on the `@feature_processor` decorator, see [Amazon SageMaker Feature Store
Python SDK](https://sagemaker.readthedocs.io/en/stable/amazon_sagemaker_featurestore.html "https://sagemaker.readthedocs.io/en/stable/amazon_sagemaker_featurestore.html").
