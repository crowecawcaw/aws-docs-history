# Batch ingestion with Amazon SageMaker Feature Store

Spark

Amazon SageMaker Feature Store Spark is a Spark connector that connects the Spark library to Feature Store. Feature Store Spark
simplifies data ingestion from Spark `DataFrame`s to feature groups. Feature Store supports
batch data ingestion with Spark, using your existing ETL pipeline, on Amazon EMR, GIS, an AWS Glue job,
an Amazon SageMaker Processing job, or a SageMaker notebook.

Methods for installing and implementing batch data ingestion are provided for Python and
Scala developers. Python developers can use the open-source
`sagemaker-feature-store-pyspark` Python library for local development,
installation on Amazon EMR, and for Jupyter Notebooks by following the instructions in the [Amazon SageMaker Feature Store Spark GitHub
repository](https://github.com/aws/sagemaker-feature-store-spark "https://github.com/aws/sagemaker-feature-store-spark"). Scala developers can use the Feature Store Spark connector available in the [Amazon SageMaker Feature Store Spark SDK Maven central repository](https://mvnrepository.com/artifact/software.amazon.sagemaker.featurestore/sagemaker-feature-store-spark-sdk "https://mvnrepository.com/artifact/software.amazon.sagemaker.featurestore/sagemaker-feature-store-spark-sdk").

You can use the Spark connector to ingest data in the following ways, depending on if the
online store, offline store, or both are enabled.

1. Ingest by default – If the online store is enabled, Spark connector first ingests
   your dataframe into the online store using the [PutRecord](../APIReference/API_feature_store_PutRecord.md "../APIReference/API_feature_store_PutRecord.md")
   API. Only the record with the largest event time remains in the online store. If the offline
   store is enabled, within 15 minutes Feature Store ingests your dataframe into the offline store. For
   more information about how the online and offline stores work, see [Feature Store concepts](feature-store-concepts.md "feature-store-concepts.md").

You can accomplish this by not specifying `target_stores` in the
`.ingest_data(...)` method. 2. Offline store direct ingestion – If offline store is enabled, Spark connector
batch ingests your dataframe directly into the offline store. Ingesting the dataframe
directly into the offline store doesn't update the online store.

You can accomplish this by setting `target_stores=["OfflineStore"]` in the
`.ingest_data(...)` method. 3. Online store only – If online store is enabled, Spark connector ingests your
dataframe into the online store using the [PutRecord](../APIReference/API_feature_store_PutRecord.md "../APIReference/API_feature_store_PutRecord.md")
API. Ingesting the dataframe directly into the online store doesn't update the offline
store.

You can accomplish this by setting `target_stores=["OnlineStore"]` in the
`.ingest_data(...)` method.
For information about using the different ingestion methods, see [Example implementations](#batch-ingestion-spark-connector-example-implementations "#batch-ingestion-spark-connector-example-implementations").

###### Topics

- [Feature Store Spark
  installation](#batch-ingestion-spark-connector-installation "#batch-ingestion-spark-connector-installation")
- [Retrieving the JAR for Feature Store Spark](#retrieve-jar-spark-connector "#retrieve-jar-spark-connector")
- [Example implementations](#batch-ingestion-spark-connector-example-implementations "#batch-ingestion-spark-connector-example-implementations")

## Feature Store Spark

installation

**Scala users**

The Feature Store Spark SDK is available in the [Amazon SageMaker Feature Store Spark SDK Maven central repository](https://mvnrepository.com/artifact/software.amazon.sagemaker.featurestore/sagemaker-feature-store-spark-sdk "https://mvnrepository.com/artifact/software.amazon.sagemaker.featurestore/sagemaker-feature-store-spark-sdk") for Scala users.

\***\*Requirements\*\***

- Spark >= 3.0.0 and <= 3.3.0
- `iceberg-spark-runtime` >= 0.14.0
- Scala >= 2.12.x
- Amazon EMR >= 6.1.0 (only if you are using Amazon EMR)

**Declare the dependency in POM.xml**

The Feature Store Spark connector has a dependency on the `iceberg-spark-runtime`
library. You must therefore add corresponding version of the
`iceberg-spark-runtime` library to the dependency if you're ingesting data into a
feature group that you've auto-created with the Iceberg table format. For example, if you're
using Spark 3.1, you must declare the following in your project’s `POM.xml`:

```

 <dependency>
 <groupId>software.amazon.sagemaker.featurestore</groupId>
 <artifactId>sagemaker-feature-store-spark-sdk_2.12</artifactId>
 <version>1.0.0</version>
 </dependency>

 <dependency>
   <groupId>org.apache.iceberg</groupId>
   <artifactId>iceberg-spark-runtime-3.1_2.12</artifactId>
   <version>0.14.0</version>
</dependency>

```

**Python users**

The Feature Store Spark SDK is available in the open-source [Amazon SageMaker Feature Store Spark GitHub
repository](https://github.com/aws/sagemaker-feature-store-spark "https://github.com/aws/sagemaker-feature-store-spark").

\***\*Requirements\*\***

- Spark >= 3.0.0 and <= 3.3.0
- Amazon EMR >= 6.1.0 (only if you are using Amazon EMR)
- Kernel = `conda_python3`

We recommend setting the `$SPARK_HOME` to the directory where you have Spark
installed. During installation, Feature Store uploads the required JAR to `SPARK_HOME`, so
that the dependencies load automatically. Spark starting a JVM is required to make this
PySpark library work.

**Local installation**

To find more info about the installation, enable verbose mode by appending
`--verbose` to the following installation command.

```

pip3 install sagemaker-feature-store-pyspark-`3.1` --no-binary :all:

```

**Installation on Amazon EMR**

Create an Amazon EMR cluster with the release version 6.1.0 or later. Enable SSH to help you
troubleshoot any issues.

You can do one of the following to install the library:

- Create a custom step within Amazon EMR.
- Connect to your cluster using SSH and install the library from there.

###### Note

The following information uses Spark version 3.1, but you can specify any version that
meets the requirements.

```

export SPARK_HOME=/usr/lib/spark
sudo -E pip3 install sagemaker-feature-store-pyspark-`3.1` --no-binary :all: --verbose

```

###### Note

If you want to install the dependent JARs automatically to SPARK_HOME, do not use the
bootstrap step.

**Installation on a SageMaker notebook instance**

Install a version of PySpark that's compatible with the Spark connector using the
following commands:

```
!pip3 install pyspark==`3.1.1`
!pip3 install sagemaker-feature-store-pyspark-`3.1` --no-binary :all:

```

If you're performing batch ingestion to the offline store, the dependencies aren't within
the notebook instance environment.

```
from pyspark.sql import SparkSession
import feature_store_pyspark

extra_jars = ",".join(feature_store_pyspark.classpath_jars())

spark = SparkSession.builder \
    .config("spark.jars", extra_jars) \
    .config("spark.jars.packages", "org.apache.hadoop:hadoop-aws:3.2.1,org.apache.hadoop:hadoop-common:3.2.1") \
    .getOrCreate()

```

**Installation on notebooks with GIS**

###### Important

You must use AWS Glue Version 2.0 or later.

Use the following information to help you install the PySpark connector in an AWS Glue
Interactive Session (GIS).

Amazon SageMaker Feature Store Spark requires a specific Spark connector JAR during the initialization of the
session to be uploaded to your Amazon S3 bucket. For more information on uploading the required JAR
to your S3 bucket, see [Retrieving the JAR for Feature Store Spark](#retrieve-jar-spark-connector "#retrieve-jar-spark-connector").

After you’ve uploaded the JAR, you must provide the GIS sessions with the JAR using the
following command.

```
%extra_jars s3:/`<YOUR_BUCKET>`/spark-connector-jars/sagemaker-feature-store-spark-sdk.jar

```

To install Feature Store Spark in the AWS Glue runtime, use the
`%additional_python_modules` magic command within the GIS notebook. AWS Glue runs
`pip` to the modules that you’ve specified under
`%additional_python_modules`.

```
%additional_python_modules sagemaker-feature-store-pyspark-`3.1`
```

Before you start the AWS Glue session, you must use both of the preceding magic
commands.

**Installation on an AWS Glue job**

###### Important

You must use AWS Glue Version 2.0 or later.

To install the Spark connector on a AWS Glue job, use the `--extra-jars` argument
to provide the necessary JARs and `--additional-python-modules` to install the
Spark Connector as job parameters when you create the AWS Glue job as shown in the following
example. For more information on uploading the required JAR to your S3 bucket, see [Retrieving the JAR for Feature Store Spark](#retrieve-jar-spark-connector "#retrieve-jar-spark-connector").

```
glue_client = boto3.client('glue', region_name=region)
response = glue_client.create_job(
    Name=pipeline_id,
    Description='Feature Store Compute Job',
    Role=glue_role_arn,
    ExecutionProperty={'MaxConcurrentRuns': max_concurrent_run},
    Command={
        'Name': 'glueetl',
        'ScriptLocation': script_location_uri,
        'PythonVersion': '3'
    },
    DefaultArguments={
        '--TempDir': temp_dir_location_uri,
        '--additional-python-modules': 'sagemaker-feature-store-pyspark-3.1',
        '--extra-jars': "s3:/`<YOUR_BUCKET>`/spark-connector-jars/sagemaker-feature-store-spark-sdk.jar",
        ...
    },
    MaxRetries=3,
    NumberOfWorkers=149,
    Timeout=2880,
    GlueVersion='3.0',
    WorkerType='G.2X'
)

```

**Installation on an Amazon SageMaker Processing job**

To use Feature Store Spark with Amazon SageMaker Processing jobs, bring your own image. For more information about
bringing your image, see [Custom Images in Amazon SageMaker Studio Classic](studio-byoi.md "studio-byoi.md"). Add the
installation step to a Dockerfile. After you've pushed the Docker image to an Amazon ECR
repository, you can use the PySparkProcessor to create the processing job. For more
information about creating a processing job with the PySpark processor, see [Run a Processing Job with Apache Spark](use-spark-processing-container.md "use-spark-processing-container.md").

The following is an example of adding an installation step to the Dockerfile.

```
FROM `<ACCOUNT_ID>`.dkr.ecr.`<AWS_REGION>`.amazonaws.com/sagemaker-spark-processing:3.1-cpu-py38-v1.0

RUN /usr/bin/python3 -m pip install sagemaker-feature-store-pyspark-3.1 --no-binary :all: --verbose


```

## Retrieving the JAR for Feature Store Spark

To retrieve the Feature Store Spark dependency JAR, you must install the Spark connector from the
Python Package Index (PyPI) repository using `pip` in any Python environment with
network access. A SageMaker Jupyter Notebook is an example of a Python environment with network
access.

The following command installs the Spark connector.

```

!pip install sagemaker-feature-store-pyspark-`3.1`

```

After you've installed Feature Store Spark, you can retrieve the JAR location and upload the JAR to
Amazon S3.

The `feature-store-pyspark-dependency-jars` command provides the location of
the necessary dependency JAR that Feature Store Spark added. You can use the command to retrieve the
JAR and upload it to Amazon S3.

```
jar_location = !feature-store-pyspark-dependency-jars
jar_location = jar_location[0]

s3_client = boto3.client("s3")
s3_client.upload_file(jar_location, "`<YOUR_BUCKET>`","spark-connector-jars/sagemaker-feature-store-spark-sdk.jar")

```

## Example implementations

Example Python script

_FeatureStoreBatchIngestion.py_

```
from pyspark.sql import SparkSession
from feature_store_pyspark.FeatureStoreManager import FeatureStoreManager
import feature_store_pyspark

spark = SparkSession.builder \
                    .getOrCreate()

# Construct test DataFrame
columns = ["RecordIdentifier", "EventTime"]
data = [("1","2021-03-02T12:20:12Z"), ("2", "2021-03-02T12:20:13Z"), ("3", "2021-03-02T12:20:14Z")]

df = spark.createDataFrame(data).toDF(*columns)

# Initialize FeatureStoreManager with a role arn if your feature group is created by another account
feature_store_manager= FeatureStoreManager("arn:aws:iam::111122223333:role/role-arn")

# Load the feature definitions from input schema. The feature definitions can be used to create a feature group
feature_definitions = feature_store_manager.load_feature_definitions_from_schema(df)

feature_group_arn = "arn:aws:sagemaker:`<AWS_REGION>`:`<ACCOUNT_ID>`:feature-group/`<YOUR_FEATURE_GROUP_NAME>`"

# Ingest by default. The connector will leverage PutRecord API to ingest your data in stream
# https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_feature_store_PutRecord.html
feature_store_manager.ingest_data(input_data_frame=df, feature_group_arn=feature_group_arn)

# To select the target stores for ingestion, you can specify the target store as the paramter
# If OnlineStore is selected, the connector will leverage PutRecord API to ingest your data in stream
feature_store_manager.ingest_data(input_data_frame=df, feature_group_arn=feature_group_arn, target_stores=["OfflineStore", "OnlineStore"])

# If only OfflineStore is selected, the connector will batch write the data to offline store directly
feature_store_manager.ingest_data(input_data_frame=df, feature_group_arn=feature_group_arn, target_stores=["OfflineStore"])

# To retrieve the records failed to be ingested by spark connector
failed_records_df = feature_store_manager.get_failed_stream_ingestion_data_frame()

```

**Submit a Spark job with example Python script**

The PySpark version requires an extra dependent JAR to be imported, so extra steps
are needed to run the Spark application.

If you did not specify `SPARK_HOME` during installation, then you have
to load required JARs in JVM when running
`spark-submit`. `feature-store-pyspark-dependency-jars` is a
Python script installed by the Spark library to automatically fetch the path to all JARs
for you.

```

spark-submit --jars `feature-store-pyspark-dependency-jars` FeatureStoreBatchIngestion.py

```

If you are running this application on Amazon EMR, we recommended that you run the
application in client mode, so that you do not need to distribute the dependent JARs to
other task nodes. Add one more step in Amazon EMR cluster with Spark argument similar to the
following:

```

spark-submit --deploy-mode client --master yarn s3:/`<PATH_TO_SCRIPT>`/FeatureStoreBatchIngestion.py

```

Example Scala script

_FeatureStoreBatchIngestion.scala_

```
import software.amazon.sagemaker.featurestore.sparksdk.FeatureStoreManager
import org.apache.spark.sql.types.{StringType, StructField, StructType}
import org.apache.spark.sql.{Row, SparkSession}

object TestSparkApp {
  def main(args: Array[String]): Unit = {

    val spark = SparkSession.builder().getOrCreate()

    // Construct test DataFrame
    val data = List(
      Row("1", "2021-07-01T12:20:12Z"),
      Row("2", "2021-07-02T12:20:13Z"),
      Row("3", "2021-07-03T12:20:14Z")
    )

    val schema = StructType(
      List(StructField("RecordIdentifier", StringType), StructField("EventTime", StringType))
    )

    val df = spark.createDataFrame(spark.sparkContext.parallelize(data), schema)

    // Initialize FeatureStoreManager with a role arn if your feature group is created by another account
    val featureStoreManager = new FeatureStoreManager("arn:aws:iam::111122223333:role/role-arn")

    // Load the feature definitions from input schema. The feature definitions can be used to create a feature group
    val featureDefinitions = featureStoreManager.loadFeatureDefinitionsFromSchema(df)

    val featureGroupArn = "arn:aws:sagemaker:`<AWS_REGION>`:`<ACCOUNT_ID>`:feature-group/`<YOUR_FEATURE_GROUP_NAME>`"

    // Ingest by default. The connector will leverage PutRecord API to ingest your data in stream
    // https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_feature_store_PutRecord.html
    featureStoreManager.ingestData(df, featureGroupArn)

    // To select the target stores for ingestion, you can specify the target store as the paramter
    // If OnlineStore is selected, the connector will leverage PutRecord API to ingest your data in stream
    featureStoreManager.ingestData(df, featureGroupArn, List("OfflineStore", "OnlineStore"))

    // If only OfflineStore is selected, the connector will batch write the data to offline store directly
    featureStoreManager.ingestData(df, featureGroupArn, ["OfflineStore"])

    // To retrieve the records failed to be ingested by spark connector
    val failedRecordsDf = featureStoreManager.getFailedStreamIngestionDataFrame()
  }
}

```

**Submit a Spark job**

**Scala**

You should be able to use Feature Store Spark as a normal dependency. No extra instruction is
needed to run the application on all platforms.
