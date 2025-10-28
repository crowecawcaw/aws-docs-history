# Running Feature Store Feature

Processor remotely

To run your Feature Processors on large data sets that require hardware more powerful than
what is locally available, you can decorate your code with the `@remote`
decorator to run your local Python code as a single or multi-node distributed SageMaker training
job. For more information on running your code as a SageMaker training job, see [Run your local code as a SageMaker training job](train-remote-decorator.md "train-remote-decorator.md").

The following is a usage example of the `@remote` decorator along with the
`@feature_processor` decorator.

```
from sagemaker.remote_function.spark_config import SparkConfig
from sagemaker.remote_function import remote
from sagemaker.feature_store.feature_processor import CSVDataSource, feature_processor

CSV_DATA_SOURCE = CSVDataSource('s3://bucket/prefix-to-csv/')
OUTPUT_FG = 'arn:aws:sagemaker:us-east-1:123456789012:feature-group/feature-group'

@remote(
    spark_config=SparkConfig(),
    instance_type="ml.m5.2xlarge",
    dependencies="/local/requirements.txt"
)
@feature_processor(
    inputs=[CSV_DATA_SOURCE],
    output=OUTPUT_FG,
)
def transform(csv_input_df):
   return csv_input_df

transform()
```

The `spark_config` parameter indicates that the remote job runs as a Spark
application. The `SparkConfig` instance can be used to configure the Spark
Configuration and provide additional dependencies to the Spark application such as Python
files, JARs, and files.

For faster iterations when developing your feature processing code, you can specify the
`keep_alive_period_in_seconds` argument in the `@remote` decorator
to retain configured resources in a warm pool for subsequent training jobs. For more
information on warm pools, see `KeepAlivePeriodInSeconds` in the API Reference guide.

The following code is an example of local `requirements.txt:`

```
sagemaker>=2.167.0
```

This will install the corresponding SageMaker SDK version in remote job which is required for
executing the method annotated by `@feature-processor`.
