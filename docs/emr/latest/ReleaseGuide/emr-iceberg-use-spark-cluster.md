

# Use an Iceberg cluster with Spark
<a name="emr-iceberg-use-spark-cluster"></a>

Starting with Amazon EMR version 6.5.0, you can use Iceberg with your Spark cluster with no requirement to include bootstrap actions. For Amazon EMR versions 6.4.0 and earlier, you can use a bootstrap action to pre-install all necessary dependencies.

In this tutorial, you use the AWS CLI to work with Iceberg on an Amazon EMR Spark cluster. To use the console to create a cluster with Iceberg installed, follow the steps in [Build an Apache Iceberg data lake using Amazon Athena, Amazon EMR, and AWS Glue](https://aws.amazon.com/blogs/big-data/build-an-apache-iceberg-data-lake-using-amazon-athena-amazon-emr-and-aws-glue/).

## Create an Iceberg cluster
<a name="emr-iceberg-create-cluster"></a>

You can create a cluster with Iceberg installed using the AWS Management Console, the AWS CLI or the Amazon EMR API. In this tutorial, you use the AWS CLI to work with Iceberg on an Amazon EMR cluster. To use the console to create a cluster with Iceberg installed, follow the steps in [Build an Apache Iceberg data lake using Amazon Athena, Amazon EMR, and AWS Glue](https://aws.amazon.com/blogs/big-data/build-an-apache-iceberg-data-lake-using-amazon-athena-amazon-emr-and-aws-glue/). 

To use Iceberg on Amazon EMR with the AWS CLI, first create a cluster with the following steps. For information on specifying the Iceberg classification using the AWS CLI, see [Supply a configuration using the AWS CLI when you create a cluster](emr-configure-apps-create-cluster.md#emr-configure-apps-create-cluster-cli) or [Supply a configuration using the Java SDK when you create a cluster](emr-configure-apps-create-cluster.md#emr-configure-apps-create-cluster-sdk).

1. Create a `configurations.json` file with the following content:

   ```
   [{
       "Classification":"iceberg-defaults",
       "Properties":{"iceberg.enabled":"true"}
   }]
   ```

1. Next, create a cluster with the following configuration. Replace the example Amazon S3 bucket path and the subnet ID with your own.

   ```
   aws emr create-cluster --release-label emr-6.5.0 \
   --applications Name=Spark \
   --configurations file://configurations.json \
   --region us-east-1 \
   --name My_Spark_Iceberg_Cluster \
   --log-uri s3://{{amzn-s3-demo-bucket/}} \
   --instance-type m5.xlarge \
   --instance-count 2 \
   --service-role EMR_DefaultRole_V2 \ 
   --ec2-attributes InstanceProfile=EMR_EC2_DefaultRole,SubnetId={{subnet-1234567890abcdef0}}
   ```

Alternatively, you can create an Amazon EMR cluster including the Spark application and include the file `/usr/share/aws/iceberg/lib/iceberg-spark3-runtime.jar` as a JAR dependency in a Spark job. For more information, see [Submitting Applications](https://spark.apache.org/docs/latest/submitting-applications.html#submitting-applications).

To include the jar as a dependency in a Spark job, add the following configuration property to the Spark application:

```
--conf "spark.jars=/usr/share/aws/iceberg/lib/iceberg-spark3-runtime.jar"
```

For more information about Spark job dependencies, see [Dependency Management](https://spark.apache.org/docs/latest/running-on-kubernetes.html#dependency-management) in the Apache Spark document [Running Spark on Kubernetes](https://spark.apache.org/docs/latest/running-on-kubernetes.html).

## Initialize a Spark session for Iceberg
<a name="emr-iceberg-initialize-spark-session"></a>

The following examples demonstrate how to launch the interactive Spark shell, use Spark submit, or use Amazon EMR Notebooks to work with Iceberg on Amazon EMR.

------
#### [ spark-shell ]

1. Connect to the master node using SSH. For more information, see [Connect to the master node using SSH](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-connect-master-node-ssh.html) in the *Amazon EMR Management Guide*.

1. Enter the following command to launch the Spark shell. To use the PySpark shell, replace `spark-shell` with `pyspark`.

   ```
   spark-shell \
       --conf spark.sql.catalog.my_catalog=org.apache.iceberg.spark.SparkCatalog \
       --conf spark.sql.catalog.my_catalog.warehouse=s3://{{amzn-s3-demo-bucket}}/{{prefix}}/
       --conf spark.sql.catalog.my_catalog.type=glue \
       --conf spark.sql.defaultCatalog=my_catalog \
       --conf spark.sql.extensions=org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions
   ```

------
#### [ spark-submit ]

1. Connect to the master node using SSH. For more information, see [Connect to the master node using SSH](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-connect-master-node-ssh.html) in the *Amazon EMR Management Guide*.

1. Enter the following command to launch the Spark session for Iceberg.

   ```
   spark-submit \
   --conf spark.sql.catalog.my_catalog=org.apache.iceberg.spark.SparkCatalog \
   --conf spark.sql.catalog.my_catalog.warehouse=s3://{{amzn-s3-demo-bucket1}}/{{prefix}} \
   --conf spark.sql.catalog.my_catalog.type=glue \
   --conf spark.sql.defaultCatalog=my_catalog \
   --conf spark.sql.extensions=org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions
   ```

------
#### [ EMR Studio notebooks ]

To initialize a Spark session using EMR Studio notebooks, configure your Spark session using the `%%configure` magic command in your Amazon EMR notebook, as in the following example. For more information, see [Use EMR Notebooks magics](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-studio-magics.html#emr-magics) in the *Amazon EMR Management Guide*.

```
%%configure -f{
"conf":{
    "spark.sql.catalog.my_catalog":"org.apache.iceberg.spark.SparkCatalog",
    "spark.sql.catalog.my_catalog.type":"glue",
    "spark.sql.catalog.my_catalog.warehouse":"s3://{{amzn-s3-demo-bucket1}}/{{prefix}}/",
    "spark.sql.defaultCatalog":"my_catalog",
    "spark.sql.extensions":"org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions"
    }
}
```

------
#### [ CLI ]

To initialize a Spark cluster using the CLI and set all of the Spark Iceberg session default configurations, run the following sample. For more information about specifying a configuration classification using the AWS CLI and Amazon EMR API, see [Configure applications](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-configure-apps.html).

```
[
  {
    "Classification": "spark-defaults",
    "Properties": {
      "spark.sql.catalog.my_catalog":"org.apache.iceberg.spark.SparkCatalog",
      "spark.sql.catalog.my_catalog.type":"glue",
      "spark.sql.catalog.my_catalog.warehouse":"s3://{{amzn-s3-demo-bucket1}}/{{prefix}}/",
      "spark.sql.defaultCatalog":"my_catalog",
      "spark.sql.extensions":"org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions"
    }
  }
]
```

------

## Write to an Iceberg table
<a name="emr-iceberg-write-to-table"></a>

The following example shows how to create a DataFrame and write it as an Iceberg dataset. The examples demonstrate working with datasets using the Spark shell while connected to the master node using SSH as the default hadoop user.

**Note**  
To paste code samples into the Spark shell, type `:paste` at the prompt, paste the example, and then press `CTRL+D`.

------
#### [ PySpark ]

Spark includes a Python-based shell, `pyspark`, that you can use to prototype Spark programs written in Python. Invoke `pyspark` on the master node.

```
## Create a DataFrame.
data = spark.createDataFrame([
 ("100", "2015-01-01", "2015-01-01T13:51:39.340396Z"),
 ("101", "2015-01-01", "2015-01-01T12:14:58.597216Z"),
 ("102", "2015-01-01", "2015-01-01T13:51:40.417052Z"),
 ("103", "2015-01-01", "2015-01-01T13:51:40.519832Z")
],["id", "creation_date", "last_update_time"])

## Write a DataFrame as a Iceberg dataset to the Amazon S3 location.
spark.sql("""CREATE TABLE IF NOT EXISTS dev.db.iceberg_table (id string,
creation_date string,
last_update_time string)
USING iceberg
location 's3://{{amzn-s3-demo-bucket}}/{{example-prefix}}/db/iceberg_table'""")

data.writeTo("dev.db.iceberg_table").append()
```

------
#### [ Scala ]

```
import org.apache.spark.sql.SaveMode
import org.apache.spark.sql.functions._

// Create a DataFrame.
val data = Seq(
("100", "2015-01-01", "2015-01-01T13:51:39.340396Z"),
("101", "2015-01-01", "2015-01-01T12:14:58.597216Z"),
("102", "2015-01-01", "2015-01-01T13:51:40.417052Z"),
("103", "2015-01-01", "2015-01-01T13:51:40.519832Z")
).toDF("id", "creation_date", "last_update_time")

// Write a DataFrame as a Iceberg dataset to the Amazon S3 location.
spark.sql("""CREATE TABLE IF NOT EXISTS dev.db.iceberg_table (id string,
creation_date string,
last_update_time string)
USING iceberg
location 's3://{{amzn-s3-demo-bucket}}/{{example-prefix}}/db/iceberg_table'""")

data.writeTo("dev.db.iceberg_table").append()
```

------

## Read from an Iceberg table
<a name="emr-iceberg-read-from-table"></a>

------
#### [ PySpark ]

```
df = spark.read.format("iceberg").load("dev.db.iceberg_table")
df.show()
```

------
#### [ Scala ]

```
val df = spark.read.format("iceberg").load("dev.db.iceberg_table")
df.show()
```

------
#### [ Spark SQL ]

```
SELECT * from dev.db.iceberg_table LIMIT 10
```

------

## Using AWS Glue Data Catalog with Spark Iceberg
<a name="emr-iceberg-glue-catalog-config-spark"></a>

You can connect to AWS Glue Data Catalog from Spark Iceberg. This section shows different commands for connecting.

### Connect to the default AWS Glue catalog in your default region
<a name="emr-iceberg-glue-catalog-config-spark"></a>

This sample shows how to connect, using the Glue catalog type. If you don't specify a catalog ID, it uses the default:

```
spark-submit \
    --conf spark.sql.catalog.my_catalog=org.apache.iceberg.spark.SparkCatalog \
    --conf spark.sql.catalog.my_catalog.warehouse=s3://{{amzn-s3-demo-bucket1}}/{{prefix}} \
    --conf spark.sql.catalog.my_catalog.type=glue \
    --conf spark.sql.defaultCatalog=my_catalog \
    --conf spark.sql.extensions=org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions
```

### Connect to an AWS Glue catalog with a specific catalog ID
<a name="emr-iceberg-glue-catalog-config-spark"></a>

This sample shows how to connect, using a catalog ID:

```
spark-submit \
    --conf spark.sql.catalog.my_catalog=org.apache.iceberg.spark.SparkCatalog \
    --conf spark.sql.catalog.my_catalog.warehouse=s3://{{amzn-s3-demo-bucket1}}/{{prefix}} \
    --conf spark.sql.catalog.my_catalog.type=glue \
    --conf spark.sql.catalog.my_catalog.glue.id={{AWS Glue catalog ID}} \
    --conf spark.sql.defaultCatalog=my_catalog \
    --conf spark.sql.extensions=org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions
```

This command can be used for connecting to an AWS Glue catalog in a different account, or to an RMS catalog, or to a federated catalog.

## Using Iceberg REST Catalog (IRC) with Spark Iceberg
<a name="emr-iceberg-rest-catalog-config"></a>

The sections that follow detail how to configure Iceberg integration with a catalog.

### Connect to AWS Glue Data Catalog IRC endpoint
<a name="emr-iceberg-rest-catalog-config-gdc"></a>

The following shows a sample `spark-submit` command for using Iceberg REST:

```
spark-submit \
    --conf spark.sql.catalog.my_catalog=org.apache.iceberg.spark.SparkCatalog \
    --conf spark.sql.catalog.my_catalog.warehouse={{glue catalog ID}} \
    --conf spark.sql.catalog.my_catalog.type=rest \
    --conf spark.sql.catalog.my_catalog.uri={{glue endpoint URI}}/iceberg \
    --conf spark.sql.catalog.my_catalog.rest.sigv4-enabled=true \
    --conf spark.sql.catalog.my_catalog.rest.signing-name=glue \
    --conf spark.sql.defaultCatalog=my_catalog \
    --conf spark.sql.extensions=org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions
```

To use it on a runtime-role enabled cluster, the following additional spark configuration settings are necessary:

```
"spark.hadoop.fs.s3.credentialsResolverClass": "software.amazon.glue.GlueTableCredentialsResolver",
"spark.hadoop.catalog-impl": "org.apache.iceberg.aws.glue.GlueCatalog",
"spark.hadoop.glue.id": {{glue catalog ID}}
"spark.hadoop.glue.endpoint": "glue endpoint"
```

For AWS Glue endpoint URL list for each region, see [AWS Glue endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/glue.html).

### Connect to an arbitrary IRC endpoint
<a name="emr-iceberg-rest-catalog-config-arbitrary"></a>

The following shows a sample `spark-submit` command for using an IRC endpoint:

```
spark-submit \
    --conf spark.sql.catalog.my_catalog=org.apache.iceberg.spark.SparkCatalog \
    --conf spark.sql.catalog.my_catalog.warehouse={{warehouse name}} \
    --conf spark.sql.catalog.my_catalog.type=rest \
    --conf spark.sql.catalog.my_catalog.uri={{your rest endpoint}} \
    --conf spark.sql.defaultCatalog=my_catalog \
    --conf spark.sql.extensions=org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions
```

## Configuration differences when you use Iceberg SparkCatalog versus SparkSessionCatalog
<a name="emr-iceberg-spark-catalog"></a>

Iceberg makes available two ways to create Spark Iceberg catalogs. You can set the Spark configuration to either `SparkCatalog` or to `SparkSessionCatalog`. 

### Using Iceberg SparkCatalog
<a name="emr-iceberg-spark-catalog-spark-catalog"></a>

The following shows the command for using **SparkCatalog** as the Spark Iceberg catalog:

```
spark-shell \
--conf spark.sql.catalog.my_catalog=org.apache.iceberg.spark.SparkCatalog \
--conf spark.sql.catalog.my_catalog.warehouse=s3://{{amzn-s3-demo-bucket1}}/{{prefix}} \
--conf spark.sql.catalog.my_catalog.type=glue \
--conf spark.sql.defaultCatalog=my_catalog
```

Considerations for this approach:
+ You can access Iceberg tables but no other tables.
+ The catalog name cannot be **spark\_catalog**. This is the name of the initial catalog in Spark. It always connects to a Hive metastore. It is the default catalog in Spark, unless the user overwrites it using `spark.sql.defaultCatalog`.
+ You can set the `spark.sql.defaultCatalog` to your catalog name to make that the default catalog.

### Using Iceberg SparkSessionCatalog
<a name="emr-iceberg-spark-catalog-spark-session"></a>

The following shows the command for using **SparkSessionCatalog** as the Spark Iceberg catalog:

```
spark-shell \
    --conf spark.sql.catalog.spark_catalog=org.apache.iceberg.spark.SparkSessionCatalog \
    --conf spark.sql.catalog.spark_catalog.warehouse=s3://{{amzn-s3-demo-bucket1}}/{{prefix}} \
    --conf spark.sql.catalog.spark_catalog.type=glue
```

Considerations for this approach:
+ If a table is not found as an Iceberg table, Spark will try to see if it is a table in the Hive metastore. See [Using the AWS Glue Data Catalog as the catalog for Hive](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-hive-metastore-glue.html) for more information.
+ The catalog name must be **spark\_catalog**.

## Using Iceberg Spark extensions
<a name="emr-iceberg-spark-catalog-extensions"></a>

Iceberg offers Spark extension `org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions` that users can set through the Spark extensions config `spark.sql.extensions`. The extensions enable key Iceberg features such as row level DELETE, UPDATE and MERGE, Iceberg-specific Spark data-definition language statements and procedures, such as compaction, snapshot expiration, branching and tagging, and so on. See the following for more details:
+ Iceberg Spark write extensions: [Spark Writes](https://iceberg.apache.org/docs/nightly/spark-writes/)
+ Iceberg Spark DDL extensions: [ALTER TABLE SQL extensions](https://iceberg.apache.org/docs/nightly/spark-ddl/#alter-table-sql-extensions/)
+ Iceberg Spark procedure extensions: [Spark Procedures](https://iceberg.apache.org/docs/nightly/spark-ddl/#alter-table-sql-extensions/)

## Considerations for using Iceberg with Spark
<a name="spark-considerations-catalog"></a>
+ Amazon EMR 6.5.0 does not support Iceberg running on Amazon EMR on EKS by default. An Amazon EMR 6.5.0 custom image is available so that you can pass `--jars local:///usr/share/aws/iceberg/lib/iceberg-spark3-runtime.jar` as a `spark-submit` parameter to create Iceberg tables on Amazon EMR on EKS. For more information, see [Submit a Spark workload in Amazon EMR using a custom image](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/docker-custom-images-steps.html#docker-custom-images-submit) in the *Amazon EMR on EKS Development Guide*. You can also contact Support for assistance. Starting with Amazon EMR 6.6.0, Iceberg is supported on Amazon EMR on EKS.
+ When using AWS Glue as a catalog for Iceberg, make sure the database in which you are creating a table exists in AWS Glue. If you are using services such as AWS Lake Formation and you're unable to load the catalog, make sure you have proper access to the service to execute the command.
+ If you use Iceberg SparkSessionCatalog, as described in [Configuration differences when you use Iceberg SparkCatalog versus SparkSessionCatalog](#emr-iceberg-spark-catalog), you must follow the configuration steps described in [Configure AWS Glue Data Catalog as the Apache Hive metastore](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-hive-metastore-glue.html), in addition to configuring Spark Iceberg AWS Glue Data Catalog settings.