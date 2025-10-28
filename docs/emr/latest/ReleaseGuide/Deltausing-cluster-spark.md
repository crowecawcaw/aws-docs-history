# Use a Delta Lake cluster with

Spark

Starting with Amazon EMR version 6.9.0, you can use Delta Lake with your Spark cluster
without the need for bootstrap actions. For Amazon EMR releases 6.8.0 and lower, you can
use bootstrap actions to pre-install the necessary dependencies.

The following examples use the AWS CLI to work with Delta Lake on an Amazon EMR Spark
cluster.

To use Delta Lake on Amazon EMR with the AWS Command Line Interface, first create a cluster. For
information on how to specify the Delta Lake classification with AWS Command Line Interface, see [Supply a configuration using the AWS Command Line Interface when you create a cluster](emr-configure-apps-create-cluster.md#emr-configure-apps-create-cluster-cli "emr-configure-apps-create-cluster.md#emr-configure-apps-create-cluster-cli") or
[Supply a configuration with the Java SDK when you create a
cluster](emr-configure-apps-create-cluster.md#emr-configure-apps-create-cluster-sdk "emr-configure-apps-create-cluster.md#emr-configure-apps-create-cluster-sdk").

1. Create a file, `configurations.json`, with the
   following content:

```
[{"Classification":"delta-defaults",  "Properties":{"delta.enabled":"true"} }]
```

2. Create a cluster with the following configuration, replacing the example
   Amazon S3 `bucket path` and the `subnet
ID` with your own.

```
aws emr create-cluster
     --release-label  emr-6.9.0
     --applications Name=Spark
     --configurations file://delta_configurations.json
     --region us-east-1
     --name My_Spark_Delta_Cluster
     --log-uri  s3://`amzn-s3-demo-bucket/`
     --instance-type m5.xlarge
     --instance-count 2
     --service-role EMR_DefaultRole_V2
     --ec2-attributes  InstanceProfile=EMR_EC2_DefaultRole,SubnetId=`subnet-1234567890abcdef0`
```

Alternatively, you can create an Amazon EMR cluster and Spark application with
the following files as JAR dependencies in a Spark job:

```
/usr/share/aws/delta/lib/delta-core.jar,
/usr/share/aws/delta/lib/delta-storage.jar,
/usr/share/aws/delta/lib/delta-storage-s3-dynamodb.jar
```

###### Note

If you use Amazon EMR releases 7.0.0 or higher, use `/usr/share/aws/delta/lib/delta-spark.jar`
instead of `/usr/share/aws/delta/lib/delta-core.jar`.

For more information, see [Submitting Applications](https://spark.apache.org/docs/latest/submitting-applications.html#submitting-applications "https://spark.apache.org/docs/latest/submitting-applications.html#submitting-applications").

To include a jar dependency in the Spark job, you can add the following
configuration properties to the Spark application:

```
--conf “spark.jars=/usr/share/aws/delta/lib/delta-core.jar,
     /usr/share/aws/delta/lib/delta-storage.jar,
     /usr/share/aws/delta/lib/delta-storage-s3-dynamodb.jar"
```

For more information about Spark job dependencies, see [Dependency Management](https://spark.apache.org/docs/latest/running-on-kubernetes.html#dependency-management "https://spark.apache.org/docs/latest/running-on-kubernetes.html#dependency-management").

If you use Amazon EMR releases 7.0.0 or higher, add the `/usr/share/aws/delta/lib/delta-spark.jar` configuration instead.

```
--conf “spark.jars=/usr/share/aws/delta/lib/delta-spark.jar,
     /usr/share/aws/delta/lib/delta-storage.jar,
     /usr/share/aws/delta/lib/delta-storage-s3-dynamodb.jar"
```

## Initialize a Spark session

for Delta Lake

The following examples show how to launch the interactive Spark shell, use
Spark submit, or use Amazon EMR Notebooks to work with Delta Lake on Amazon EMR.

spark-shell

1. Connect to the primary node using SSH. For more
   information, see [Connect to the primary node using SSH](../ManagementGuide/emr-connect-master-node-ssh.md "../ManagementGuide/emr-connect-master-node-ssh.md") in the
   _Amazon EMR Management Guide_.
2. Enter the following command to launch the Spark shell. To
   use the PySpark shell, replace `spark-shell` with
   `pyspark`.

```
spark-shell \
   --conf "spark.sql.extensions=io.delta.sql.DeltaSparkSessionExtension" \
   --conf "spark.sql.catalog.spark_catalog=org.apache.spark.sql.delta.catalog.DeltaCatalog"
```

If you run Amazon EMR releases 6.15.0 or higher, you must also
use the following configurations to use fine-grained access control
based on Lake Formation with Delta Lake.

```
spark-shell \
  --conf spark.sql.extensions=io.delta.sql.DeltaSparkSessionExtension,com.amazonaws.emr.recordserver.connector.spark.sql.RecordServerSQLExtension \
  --conf spark.sql.catalog.spark_catalog=org.apache.spark.sql.delta.catalog.DeltaCatalog \
  --conf spark.sql.catalog.spark_catalog.lf.managed=true
```

spark-submit

1. Connect to the primary node using SSH. For more
   information, see [Connect to the primary node using SSH](../ManagementGuide/emr-connect-master-node-ssh.md "../ManagementGuide/emr-connect-master-node-ssh.md") in the
   _Amazon EMR Management Guide_.
2. Enter the following command to launch the Spark session
   for Delta Lake.

```
spark-submit
—conf "spark.sql.extensions=io.delta.sql.DeltaSparkSessionExtension"
—conf "spark.sql.catalog.spark_catalog=org.apache.spark.sql.delta.catalog.DeltaCatalog"
```

If you run Amazon EMR releases 6.15.0 or higher, you must also
use the following configurations to use fine-grained access control
based on Lake Formation with Delta Lake.

```
spark-submit \  `
--conf spark.sql.extensions=io.delta.sql.DeltaSparkSessionExtension,com.amazonaws.emr.recordserver.connector.spark.sql.RecordServerSQLExtension
--conf spark.sql.catalog.spark_catalog=org.apache.spark.sql.delta.catalog.DeltaCatalog \
--conf spark.sql.catalog.spark_catalog.lf.managed=true
```

EMR Studio notebooks
To initialize a Spark session using Amazon EMR Studio notebooks,
configure your Spark session using **%%configure**
magic command in your Amazon EMR notebook, as in the following example.
For more information, see [Use EMR Notebooks magics](../ManagementGuide/emr-studio-magics.md#emr-magics "../ManagementGuide/emr-studio-magics.md#emr-magics") in the _Amazon EMR
Management Guide_.

```
%%configure -f
{
  "conf": {
    "spark.sql.extensions":  "io.delta.sql.DeltaSparkSessionExtension",
     "spark.sql.catalog.spark_catalog":  "org.apache.spark.sql.delta.catalog.DeltaCatalog"
  }
}
```

If you run Amazon EMR releases 6.15.0 or higher, you must also
use the following configurations to use fine-grained access control
based on Lake Formation with Delta Lake.

```
%%configure -f
{
  "conf": {
    "spark.sql.extensions": "io.delta.sql.DeltaSparkSessionExtension,com.amazonaws.emr.recordserver.connector.spark.sql.RecordServerSQLExtension",
    "spark.sql.catalog.spark_catalog": "org.apache.spark.sql.delta.catalog.DeltaCatalog",
    "spark.sql.catalog.spark_catalog.lf.managed": "true"
  }
}
```

## Write to a Delta Lake table

The following example shows how to create a DataFrame and write it as a
Delta Lake dataset. The example shows how to work with datasets with the Spark
shell while connected to the primary node using SSH as the default hadoop user.

###### Note

To paste code samples into the Spark shell, type **:paste**
at the prompt, paste the example, and then press **CTRL +
D**.

PySpark
Spark includes a Python based shell, `pyspark`, that
you can use to prototype Spark programs written in Python. Just as
with `spark-shell`, invoke `pyspark` on the
primary node.

```
## Create a DataFrame
data =  spark.createDataFrame([("100", "2015-01-01", "2015-01-01T13:51:39.340396Z"),
("101",  "2015-01-01", "2015-01-01T12:14:58.597216Z"),
("102", "2015-01-01", "2015-01-01T13:51:40.417052Z"),
("103",  "2015-01-01",  "2015-01-01T13:51:40.519832Z")],
["id", "creation_date",  "last_update_time"])

## Write a DataFrame as a Delta Lake dataset to the S3  location
spark.sql("""CREATE  TABLE IF NOT EXISTS delta_table (id string, creation_date string,
last_update_time string)
USING delta location
's3://`amzn-s3-demo-bucket`/example-prefix/db/delta_table'""");

data.writeTo("delta_table").append()
```

Scala

```
import org.apache.spark.sql.SaveMode
import org.apache.spark.sql.functions._

// Create a DataFrame
val data = Seq(("100",  "2015-01-01",  "2015-01-01T13:51:39.340396Z"),
("101",  "2015-01-01",  "2015-01-01T12:14:58.597216Z"),
("102",  "2015-01-01", "2015-01-01T13:51:40.417052Z"),
("103",  "2015-01-01",  "2015-01-01T13:51:40.519832Z")).toDF("id", "creation_date",  "last_update_time")

// Write a DataFrame as a Delta Lake dataset to the S3  location
spark.sql("""CREATE  TABLE IF NOT EXISTS delta_table (id string,
creation_date string,
last_update_time string)
USING delta location
's3://`amzn-s3-demo-bucket`/example-prefix/db/delta_table'""");

data.write.format("delta").mode("append").saveAsTable("delta_table")
```

SQL

```
-- Create a Delta  Lake table with the S3 location
CREATE TABLE delta_table(id string,
creation_date string,
last_update_time string)
USING delta `LOCATION`
's3://`amzn-s3-demo-bucket`/example-prefix/db/delta_table';

-- insert data into the table
INSERT INTO delta_table VALUES  ("100", "2015-01-01",  "2015-01-01T13:51:39.340396Z"),
("101",  "2015-01-01",  "2015-01-01T12:14:58.597216Z"),
("102",  "2015-01-01", "2015-01-01T13:51:40.417052Z"),
("103",  "2015-01-01", "2015-01-01T13:51:40.519832Z");
```

## Read from a Delta Lake table

PySpark

```
ddf = spark.table("delta_table")
ddf.show()
```

Scala

```
val ddf =  spark.table("delta_table")
ddf.show()
```

SQL

```
SELECT * FROM delta_table;
```
