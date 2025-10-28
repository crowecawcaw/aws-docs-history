# Custom data

source examples

This section provides examples of custom data sources implementations for Feature
Processors. For more information on custom data sources, see [Custom data
sources](feature-store-feature-processor-data-sources-custom.md "feature-store-feature-processor-data-sources-custom.md").

Security is a shared responsibility between AWS and our customers. AWS is responsible
for protecting the infrastructure that runs the services in the AWS Cloud. Customers are
responsible for all of their necessary security configuration and management tasks. For example,
secrets such as access credentials to data stores should not be hard coded in your custom data
sources. You can use AWS Secrets Manager to manage these credentials. For information about Secrets Manager, see
[What is
AWS Secrets Manager?](../../../secretsmanager/latest/userguide/intro.md "../../../secretsmanager/latest/userguide/intro.md") in the AWS Secrets Manager user guide. The following examples will use Secrets Manager for your
credentials.

###### Topics

- [Amazon Redshift Clusters (JDBC) custom data source examples](#feature-store-feature-processor-data-sources-custom-examples-redshift "#feature-store-feature-processor-data-sources-custom-examples-redshift")
- [Snowflake custom data source examples](#feature-store-feature-processor-data-sources-custom-examples-snowflake "#feature-store-feature-processor-data-sources-custom-examples-snowflake")
- [Databricks (JDBC) custom data source examples](#feature-store-feature-processor-data-sources-custom-examples-databricks "#feature-store-feature-processor-data-sources-custom-examples-databricks")
- [Streaming custom data source examples](#feature-store-feature-processor-data-sources-custom-examples-streaming "#feature-store-feature-processor-data-sources-custom-examples-streaming")

## Amazon Redshift Clusters (JDBC) custom data source examples

Amazon Redshift offers a JDBC driver that can be used to read data with Spark. For information
about how to download the Amazon Redshift JDBC driver, see [Download the Amazon Redshift JDBC driver,
version 2.1](../../../redshift/latest/mgmt/jdbc20-download-driver.md "../../../redshift/latest/mgmt/jdbc20-download-driver.md").

To create the custom Amazon Redshift data source class, you will need to overwrite the
`read_data` method from the [Custom data
sources](feature-store-feature-processor-data-sources-custom.md "feature-store-feature-processor-data-sources-custom.md").

To connect with an Amazon Redshift cluster you need your:

- Amazon Redshift JDBC URL (`jdbc-url`)

For information about obtaining your Amazon Redshift JDBC URL, see [Getting the JDBC URL](../../../redshift/latest/mgmt/jdbc20-obtain-url.md "../../../redshift/latest/mgmt/jdbc20-obtain-url.md") in the
Amazon Redshift Database Developer Guide.

- Amazon Redshift user name (`redshift-user`) and password
  (`redshift-password`)

For information about how to create and manage database users using the Amazon Redshift SQL
commands, see [Users](../../../redshift/latest/dg/r_Users.md "../../../redshift/latest/dg/r_Users.md") in the Amazon Redshift Database Developer Guide.

- Amazon Redshift table name (`redshift-table-name`)

For information about how to create a table with some examples, see [CREATE
TABLE](../../../redshift/latest/dg/r_CREATE_TABLE_NEW.md "../../../redshift/latest/dg/r_CREATE_TABLE_NEW.md") in the Amazon Redshift Database Developer Guide.

- (Optional) If using Secrets Manager, you’ll need the secret name
  (`secret-redshift-account-info`) where you store
  your Amazon Redshift access username and password on Secrets Manager.

For information about Secrets Manager, see [Find secrets in
AWS Secrets Manager](../../../secretsmanager/latest/userguide/manage_search-secret.md "../../../secretsmanager/latest/userguide/manage_search-secret.md") in the AWS Secrets Manager User Guide.

- AWS Region (`your-region`)

For information about obtaining your current session’s region name using SDK for Python (Boto3),
see [region_name](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/core/session.html#boto3.session.Session.region_name "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/core/session.html#boto3.session.Session.region_name") in the Boto3 documentation.

The following example demonstrates how to retrieve the JDBC URL and personal access token
from Secrets Manager and override the `read_data` for your custom data source class,
`DatabricksDataSource`.

```
from sagemaker.feature_store.feature_processor import PySparkDataSource
import json
import boto3


class RedshiftDataSource(PySparkDataSource):

    data_source_name = "Redshift"
    data_source_unique_id = "`redshift-resource-arn`"

    def read_data(self, spark, params):
        url = "`jdbc-url`?user=`redshift-user`&password=`redshift-password`"
        aws_iam_role_arn = "`redshift-command-access-role`"
        secret_name = "`secret-redshift-account-info`"
        region_name = "`your-region`"

        session = boto3.session.Session()
        sm_client = session.client(
            service_name='secretsmanager',
            region_name=region_name,
        )

        secrets = json.loads(sm_client.get_secret_value(SecretId=secret_name)["SecretString"])
        jdbc_url = url.replace("`jdbc-url`", secrets["jdbcurl"]).replace("`redshift-user`", secrets['username']).replace("`redshift-password`", secrets['password'])

        return spark.read \
             .format("jdbc") \
             .option("url", url) \
             .option("driver", "com.amazon.redshift.Driver") \
             .option("dbtable", "`redshift-table-name`") \
             .option("tempdir", "s3a://`your-bucket-name`/`your-bucket-prefix`") \
             .option("aws_iam_role", aws_iam_role_arn) \
             .load()
```

The following example shows how to connect `RedshiftDataSource` to your
`feature_processor` decorator.

```
from sagemaker.feature_store.feature_processor import feature_processor

@feature_processor(
    inputs=[RedshiftDataSource()],
    output="`feature-group-arn`",
    target_stores=["OfflineStore"],
    spark_config={"spark.jars.packages": "com.amazon.redshift:redshift-jdbc42:2.1.0.16"}
)
def transform(input_df):
    return input_df
```

To run the feature processor job remotely, you need to provide the jdbc driver by defining
`SparkConfig` and pass it to the `@remote` decorator.

```
from sagemaker.remote_function import remote
from sagemaker.remote_function.spark_config import SparkConfig

config = {
    "Classification": "spark-defaults",
    "Properties": {
      "spark.jars.packages": "com.amazon.redshift:redshift-jdbc42:2.1.0.16"
    }
}

@remote(
    spark_config=SparkConfig(configuration=config),
    instance_type="ml.m5.2xlarge",
)
@feature_processor(
    inputs=[RedshiftDataSource()],
    output="`feature-group-arn`",
    target_stores=["OfflineStore"],
)
def transform(input_df):
    return input_df
```

## Snowflake custom data source examples

Snowflake provides a Spark connector that can be used for your
`feature_processor` decorator. For information about Snowflake connector for
Spark, see [Snowflake
Connector for Spark](https://docs.snowflake.com/en/user-guide/spark-connector "https://docs.snowflake.com/en/user-guide/spark-connector") in the Snowflake documentation.

To create the custom Snowflake data source class, you will need to override the
`read_data` method from the [Custom data
sources](feature-store-feature-processor-data-sources-custom.md "feature-store-feature-processor-data-sources-custom.md") and add the Spark
connector packages to the Spark classpath.

To connect with a Snowflake data source you need:

- Snowflake URL (`sf-url`)

For information about URLs for accessing Snowflake web interfaces, see [Account
Identifiers](https://docs.snowflake.com/en/user-guide/admin-account-identifier "https://docs.snowflake.com/en/user-guide/admin-account-identifier") in the Snowflake documentation.

- Snowflake database (`sf-database`)

For information about obtaining the name of your database using Snowflake, see [CURRENT_DATABASE](https://docs.snowflake.com/en/sql-reference/functions/current_database "https://docs.snowflake.com/en/sql-reference/functions/current_database") in the Snowflake documentation.

- Snowflake database schema (`sf-schema`)

For information about obtaining the name of your schema using Snowflake, see [CURRENT_SCHEMA](https://docs.snowflake.com/en/sql-reference/functions/current_schema "https://docs.snowflake.com/en/sql-reference/functions/current_schema") in the Snowflake documentation.

- Snowflake warehouse (`sf-warehouse`)

For information about obtaining the name of your warehouse using Snowflake, see [CURRENT_WAREHOUSE](https://docs.snowflake.com/en/sql-reference/functions/current_warehouse "https://docs.snowflake.com/en/sql-reference/functions/current_warehouse") in the Snowflake documentation.

- Snowflake table name (`sf-table-name`)
- (Optional) If using Secrets Manager, you’ll need the secret name
  (`secret-snowflake-account-info`) where you
  store your Snowflake access username and password on Secrets Manager.

For information about Secrets Manager, see [Find secrets in
AWS Secrets Manager](../../../secretsmanager/latest/userguide/manage_search-secret.md "../../../secretsmanager/latest/userguide/manage_search-secret.md") in the AWS Secrets Manager User Guide.

- AWS Region (`your-region`)

For information about obtaining your current session’s region name using SDK for Python (Boto3),
see [region_name](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/core/session.html#boto3.session.Session.region_name "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/core/session.html#boto3.session.Session.region_name") in the Boto3 documentation.

The following example demonstrates how to retrieve the Snowflake user name and password
from Secrets Manager and override the `read_data` function for your custom data source class
`SnowflakeDataSource`.

```
from sagemaker.feature_store.feature_processor import PySparkDataSource
from sagemaker.feature_store.feature_processor import feature_processor
import json
import boto3


class SnowflakeDataSource(PySparkDataSource):

    sf_options = {
        "sfUrl" : "`sf-url`",
        "sfDatabase" : "`sf-database`",
        "sfSchema" : "`sf-schema`",
        "sfWarehouse" : "`sf-warehouse`",
    }

    data_source_name = "Snowflake"
    data_source_unique_id = "`sf-url`"

    def read_data(self, spark, params):
        secret_name = "`secret-snowflake-account-info`"
        region_name = "`your-region`"

        session = boto3.session.Session()
        sm_client = session.client(
            service_name='secretsmanager',
            region_name=region_name,
        )

        secrets = json.loads(sm_client.get_secret_value(SecretId=secret_name)["SecretString"])
        self.sf_options["sfUser"] = secrets.get("username")
        self.sf_options["sfPassword"] = secrets.get("password")

        return spark.read.format("net.snowflake.spark.snowflake") \
                        .options(**self.sf_options) \
                        .option("dbtable", "`sf-table-name`") \
                        .load()
```

The following example shows how to connect `SnowflakeDataSource` to your
`feature_processor` decorator.

```
from sagemaker.feature_store.feature_processor import feature_processor

@feature_processor(
    inputs=[SnowflakeDataSource()],
    output=`feature-group-arn`,
    target_stores=["OfflineStore"],
    spark_config={"spark.jars.packages": "net.snowflake:spark-snowflake_2.12:2.12.0-spark_3.3"}
)
def transform(input_df):
    return input_df
```

To run the feature processor job remotely, you need to provide the packages via defining
`SparkConfig` and pass it to `@remote` decorator. The Spark packages
in the following example are such that `spark-snowflake_2.12` is the Feature
Processor Scala version, `2.12.0` is the Snowflake version you wish to use, and
`spark_3.3` is the Feature Processor Spark version.

```
from sagemaker.remote_function import remote
from sagemaker.remote_function.spark_config import SparkConfig

config = {
    "Classification": "spark-defaults",
    "Properties": {
      "spark.jars.packages": "net.snowflake:spark-snowflake_2.12:2.12.0-spark_3.3"
    }
}

@remote(
    spark_config=SparkConfig(configuration=config),
    instance_type="ml.m5.2xlarge",
)
@feature_processor(
    inputs=[SnowflakeDataSource()],
    output="`feature-group-arn>`",
    target_stores=["OfflineStore"],
)
def transform(input_df):
    return input_df
```

## Databricks (JDBC) custom data source examples

Spark can read data from Databricks by using the Databricks JDBC driver. For information
about the Databricks JDBC driver, see [Configure the Databricks ODBC and JDBC drivers](https://docs.databricks.com/en/integrations/jdbc-odbc-bi.html#configure-the-databricks-odbc-and-jdbc-drivers "https://docs.databricks.com/en/integrations/jdbc-odbc-bi.html#configure-the-databricks-odbc-and-jdbc-drivers") in the Databricks
documentation.

###### Note

You can read data from any other database by including the corresponding JDBC driver in
Spark classpath. For more information, see [JDBC To Other
Databases](https://spark.apache.org/docs/latest/sql-data-sources-jdbc.html "https://spark.apache.org/docs/latest/sql-data-sources-jdbc.html") in the Spark SQL Guide.

To create the custom Databricks data source class, you will need to override the
`read_data` method from the [Custom data
sources](feature-store-feature-processor-data-sources-custom.md "feature-store-feature-processor-data-sources-custom.md") and add the JDBC jar
to the Spark classpath.

To connect with a Databricks data source you need:

- Databricks URL (`databricks-url`)

For information about your Databricks URL, see [Building the connection URL for the Databricks driver](https://docs.databricks.com/en/integrations/jdbc-odbc-bi.html#building-the-connection-url-for-the-databricks-driver "https://docs.databricks.com/en/integrations/jdbc-odbc-bi.html#building-the-connection-url-for-the-databricks-driver") in the Databricks
documentation.

- Databricks personal access token
  (`personal-access-token`)

For information about your Databricks access token, see [Databricks personal access
token authentication](https://docs.databricks.com/en/dev-tools/auth.html#pat "https://docs.databricks.com/en/dev-tools/auth.html#pat") in the Databricks documentation.

- Data catalog name (`db-catalog`)

For information about your Databricks catalog name, see [Catalog name](https://docs.databricks.com/en/sql/language-manual/sql-ref-names.html#catalog-name "https://docs.databricks.com/en/sql/language-manual/sql-ref-names.html#catalog-name") in the Databricks documentation.

- Schema name (`db-schema`)

For information about your Databricks schema name, see [Schema name](https://docs.databricks.com/en/sql/language-manual/sql-ref-names.html#schema-name "https://docs.databricks.com/en/sql/language-manual/sql-ref-names.html#schema-name") in the Databricks documentation.

- Table name (`db-table-name`)

For information about your Databricks table name, see [Table name](https://docs.databricks.com/en/sql/language-manual/sql-ref-names.html#table-name "https://docs.databricks.com/en/sql/language-manual/sql-ref-names.html#table-name") in the Databricks documentation.

- (Optional) If using Secrets Manager, you’ll need the secret name
  (`secret-databricks-account-info`) where you
  store your Databricks access username and password on Secrets Manager.

For information about Secrets Manager, see [Find secrets in
AWS Secrets Manager](../../../secretsmanager/latest/userguide/manage_search-secret.md "../../../secretsmanager/latest/userguide/manage_search-secret.md") in the AWS Secrets Manager User Guide.

- AWS Region (`your-region`)

For information about obtaining your current session’s region name using SDK for Python (Boto3),
see [region_name](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/core/session.html#boto3.session.Session.region_name "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/core/session.html#boto3.session.Session.region_name") in the Boto3 documentation.

The following example demonstrates how to retrieve the JDBC URL and personal access token
from Secrets Manager and overwrite the `read_data` for your custom data source class,
`DatabricksDataSource`.

```
from sagemaker.feature_store.feature_processor import PySparkDataSource
import json
import boto3


class DatabricksDataSource(PySparkDataSource):

    data_source_name = "Databricks"
    data_source_unique_id = "`databricks-url`"

    def read_data(self, spark, params):
        secret_name = "`secret-databricks-account-info`"
        region_name = "`your-region`"

        session = boto3.session.Session()
        sm_client = session.client(
            service_name='secretsmanager',
            region_name=region_name,
        )

        secrets = json.loads(sm_client.get_secret_value(SecretId=secret_name)["SecretString"])
        jdbc_url = secrets["jdbcurl"].replace("`personal-access-token`", secrets['pwd'])

        return spark.read.format("jdbc") \
                        .option("url", jdbc_url) \
                        .option("dbtable","``db-catalog``.``db-schema``.``db-table-name``") \
                        .option("driver", "com.simba.spark.jdbc.Driver") \
                        .load()
```

The following example shows how to upload the JDBC driver jar,
``jdbc-jar-file-name`.jar`, to Amazon S3 in order to add it
 to the Spark classpath. For information about downloading the Spark JDBC driver
 (``jdbc-jar-file-name`.jar`) from Databricks, see
[Download JDBC
Driver](https://www.databricks.com/spark/jdbc-drivers-download "https://www.databricks.com/spark/jdbc-drivers-download")in the Databricks website.

```
from sagemaker.feature_store.feature_processor import feature_processor

@feature_processor(
    inputs=[DatabricksDataSource()],
    output=`feature-group-arn`,
    target_stores=["OfflineStore"],
    spark_config={"spark.jars": "s3://`your-bucket-name`/`your-bucket-prefix`/`jdbc-jar-file-name`.jar"}
)
def transform(input_df):
    return input_df
```

To run the feature processor job remotely, you need to provide the jars by defining
`SparkConfig` and pass it to the `@remote` decorator.

```
from sagemaker.remote_function import remote
from sagemaker.remote_function.spark_config import SparkConfig

config = {
    "Classification": "spark-defaults",
    "Properties": {
      "spark.jars": "s3://`your-bucket-name`/`your-bucket-prefix`/`jdbc-jar-file-name`.jar"
    }
}

@remote(
    spark_config=SparkConfig(configuration=config),
    instance_type="ml.m5.2xlarge",
)
@feature_processor(
    inputs=[DatabricksDataSource()],
    output="`feature-group-arn`",
    target_stores=["OfflineStore"],
)
def transform(input_df):
    return input_df
```

## Streaming custom data source examples

You can connect to streaming data sources like Amazon Kinesis, and author transforms with Spark
Structured Streaming to read from streaming data sources. For information about the Kinesis
connector, see [Kinesis Connector for
Spark Structured Streaming](https://github.com/roncemer/spark-sql-kinesis "https://github.com/roncemer/spark-sql-kinesis") in GitHub. For information about Amazon Kinesis, see [What Is Amazon Kinesis Data
Streams?](../../../streams/latest/dev/introduction.md "../../../streams/latest/dev/introduction.md") in the Amazon Kinesis Developer Guide.

To create the custom Amazon Kinesis data source class, you will need to extend the
`BaseDataSource` class and override the `read_data` method from [Custom data
sources](feature-store-feature-processor-data-sources-custom.md "feature-store-feature-processor-data-sources-custom.md").

To connect to an Amazon Kinesis data stream you need:

- Kinesis ARN (`kinesis-resource-arn`)

For information on Kinesis data stream ARNs, see [Amazon
Resource Names (ARNs) for Kinesis Data Streams](../../../streams/latest/dev/controlling-access.md#kinesis-using-iam-arn-format "../../../streams/latest/dev/controlling-access.md#kinesis-using-iam-arn-format") in the Amazon Kinesis Developer
Guide.

- Kinesis data stream name
  (`kinesis-stream-name`)
- AWS Region (`your-region`)

For information about obtaining your current session’s region name using SDK for Python (Boto3),
see [region_name](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/core/session.html#boto3.session.Session.region_name "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/core/session.html#boto3.session.Session.region_name") in the Boto3 documentation.

```
from sagemaker.feature_store.feature_processor import BaseDataSource
from sagemaker.feature_store.feature_processor import feature_processor

class KinesisDataSource(BaseDataSource):

    data_source_name = "Kinesis"
    data_source_unique_id = "`kinesis-resource-arn`"

    def read_data(self, spark, params):
        return spark.readStream.format("kinesis") \
            .option("streamName", "`kinesis-stream-name`") \
            .option("awsUseInstanceProfile", "false") \
            .option("endpointUrl", "https://kinesis.``your-region``.amazonaws.com")
            .load()
```

The following example demonstrates how to connect `KinesisDataSource` to your
`feature_processor` decorator.

```
from sagemaker.remote_function import remote
from sagemaker.remote_function.spark_config import SparkConfig
import feature_store_pyspark.FeatureStoreManager as fsm

def ingest_micro_batch_into_fg(input_df, epoch_id):
    feature_group_arn = "`feature-group-arn`"
    fsm.FeatureStoreManager().ingest_data(
        input_data_frame = input_df,
        feature_group_arn = feature_group_arn
    )

@remote(
    spark_config=SparkConfig(
        configuration={
            "Classification": "spark-defaults",
            "Properties":{
                "spark.sql.streaming.schemaInference": "true",
                "spark.jars.packages": "com.roncemer.spark/spark-sql-kinesis_2.13/1.2.2_spark-3.2"
            }
        }
    ),
    instance_type="ml.m5.2xlarge",
    max_runtime_in_seconds=2419200 # 28 days
)
@feature_processor(
    inputs=[KinesisDataSource()],
    output="`feature-group-arn`"
)
def transform(input_df):
    output_stream = (
        input_df.selectExpr("CAST(rand() AS STRING) as partitionKey", "CAST(data AS STRING)")
        .writeStream.foreachBatch(ingest_micro_batch_into_fg)
        .trigger(processingTime="1 minute")
        .option("checkpointLocation", "`s3a://checkpoint-path`")
        .start()
    )
    output_stream.awaitTermination()
```

In the example code above we use a few Spark Structured Streaming options while streaming
micro-batches into your feature group. For a full list of options, see the [Structured Streaming Programming Guide](https://spark.apache.org/docs/latest/structured-streaming-programming-guide.html "https://spark.apache.org/docs/latest/structured-streaming-programming-guide.html") in the Apache Spark documentation.

- The `foreachBatch` sink mode is a feature that allows you to apply
  operations and write logic on the output data of each micro-batch of a streaming query.

For information on `foreachBatch`, see [Using Foreach and ForeachBatch](https://spark.apache.org/docs/latest/structured-streaming-programming-guide.html#using-foreach-and-foreachbatch "https://spark.apache.org/docs/latest/structured-streaming-programming-guide.html#using-foreach-and-foreachbatch") in the Apache Spark Structured Streaming
Programming Guide.

- The `checkpointLocation` option periodically saves the state of the
  streaming application. The streaming log is saved in checkpoint location
  `s3a://checkpoint-path`.

For information on the `checkpointLocation` option, see [Recovering from Failures with Checkpointing](https://spark.apache.org/docs/latest/structured-streaming-programming-guide.html#recovering-from-failures-with-checkpointing "https://spark.apache.org/docs/latest/structured-streaming-programming-guide.html#recovering-from-failures-with-checkpointing") in the Apache Spark Structured
Streaming Programming Guide.

- The `trigger` setting defines how often the micro-batch processing is
  triggered in a streaming application. In the example, the processing time trigger type is
  used with one-minute micro-batch intervals, specified by `trigger(processingTime="1
minute")`. To backfill from a stream source, you can use the available-now trigger
  type, specified by `trigger(availableNow=True)`.

For a full list of `trigger` types, see [Triggers](https://spark.apache.org/docs/latest/structured-streaming-programming-guide.html#triggers "https://spark.apache.org/docs/latest/structured-streaming-programming-guide.html#triggers") in the Apache Spark Structured Streaming Programming Guide.

**Continuous streaming and automatic retries using event based
triggers**

The Feature Processor uses SageMaker Training as compute infrastructure and it has a maximum
runtime limit of 28 days. You can use event based triggers to extend your continuous streaming
for a longer period of time and recover from transient failures. For more information on
schedule and event based executions, see [Scheduled and event
based executions for Feature Processor pipelines](feature-store-feature-processor-schedule-pipeline.md "feature-store-feature-processor-schedule-pipeline.md").

The following is an example of setting up an event based trigger to keep the streaming
Feature Processor pipeline running continuously. This uses the streaming transform function
defined in the previous example. A target pipeline can be configured to be triggered when a
`STOPPED` or `FAILED` event occurs for a source pipeline execution.
Note that the same pipeline is used as the source and target so that it run
continuously.

```
import sagemaker.feature_store.feature_processor as fp
from sagemaker.feature_store.feature_processor import FeatureProcessorPipelineEvent
from sagemaker.feature_store.feature_processor import FeatureProcessorPipelineExecutionStatus

streaming_pipeline_name = "`streaming-pipeline`"
streaming_pipeline_arn = fp.to_pipeline(
    pipeline_name = streaming_pipeline_name,
    step = transform # defined in previous section
)

fp.put_trigger(
    source_pipeline_events=FeatureProcessorPipelineEvents(
        pipeline_name=source_pipeline_name,
        pipeline_execution_status=[
            FeatureProcessorPipelineExecutionStatus.STOPPED,
            FeatureProcessorPipelineExecutionStatus.FAILED]
    ),
    target_pipeline=target_pipeline_name
)
```
