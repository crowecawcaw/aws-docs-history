# Accessing Amazon S3 tables with Amazon EMR

Amazon EMR (previously called Amazon Elastic MapReduce) is a managed cluster platform that
simplifies running big data frameworks, such as Apache Hadoop and
Apache Spark, on AWS to process and analyze vast amounts of data. Using
these frameworks and related open-source projects, you can process data for analytics
purposes and business intelligence workloads. Amazon EMR also lets you transform and move
large amounts of data into and out of other AWS data stores and databases.

You can use Apache Iceberg clusters in Amazon EMR to work with S3 tables by
connecting to table buckets in a Spark session. To connect to
table buckets in Amazon EMR, you can use the AWS analytics services integration through
AWS Glue Data Catalog, or you can use the open source Amazon S3 Tables Catalog for Apache Iceberg client catalog.

###### Note

S3 Tables is supported on [Amazon EMR version 7.5](../../../emr/latest/ReleaseGuide/emr-release-components.md "../../../emr/latest/ReleaseGuide/emr-release-components.md")
or higher.

## Connecting to S3 table buckets with Spark on

an Amazon EMR Iceberg cluster

In this procedure, you set up an Amazon EMR cluster configured for Apache Iceberg and
then launch a Spark session that connects to your table buckets. You can set this up
using the AWS analytics services integration through AWS Glue, or you can use the open source
Amazon S3 Tables Catalog for Apache Iceberg client catalog. For information about the client catalog, see [Accessing tables using the Amazon S3 Tables Iceberg REST endpoint](s3-tables-integrating-open-source.md "s3-tables-integrating-open-source.md").

Choose your method of using tables with Amazon EMR from the following options.

Amazon S3 Tables Catalog for Apache Iceberg
The following prerequisites are required to query tables with Spark
on Amazon EMR using the Amazon S3 Tables Catalog for Apache Iceberg.

###### Prerequisites

- Attach the `AmazonS3TablesFullAccess` policy to the
  IAM role you use for Amazon EMR.

###### To set up an Amazon EMR cluster to query tables with Spark

1. Create a cluster with the following configuration. To use this example, replace the
   `user input placeholders` with your own
   information.

```
aws emr create-cluster --release-label emr-7.5.0 \
--applications Name=Spark \
--configurations file://configurations.json \
--region `us-east-1` \
--name My_Spark_Iceberg_Cluster \
--log-uri s3://``amzn-s3-demo-bucket``/ \
--instance-type m5.xlarge \
--instance-count 2 \
--service-role `EMR_DefaultRole` \
--ec2-attributes \

InstanceProfile=`EMR_EC2_DefaultRole`,SubnetId=`subnet-1234567890abcdef0`,KeyName=`my-key-pair`
```

`configurations.json`:

```
[{
"Classification":"iceberg-defaults",
"Properties":{"iceberg.enabled":"true"}
}]
```

2. [Connect
   to the Spark primary node using SSH](../../../emr/latest/ManagementGuide/emr-connect-master-node-ssh.md#emr-connect-cli "../../../emr/latest/ManagementGuide/emr-connect-master-node-ssh.md#emr-connect-cli").
3. To initialize a Spark session for Iceberg that
   connects to your table bucket, enter the following command. Replace the
   `user input placeholders` with your table bucket
   ARN.

```
spark-shell \
--packages software.amazon.s3tables:s3-tables-catalog-for-iceberg-runtime:0.1.3 \
--conf spark.sql.catalog.s3tablesbucket=org.apache.iceberg.spark.SparkCatalog \
--conf spark.sql.catalog.s3tablesbucket.catalog-impl=software.amazon.s3tables.iceberg.S3TablesCatalog \
--conf spark.sql.catalog.s3tablesbucket.warehouse=arn:aws:s3tables:`us-east-1`:`111122223333`:bucket/`amzn-s3-demo-bucket1` \
--conf spark.sql.defaultCatalog=s3tablesbucket \
--conf spark.sql.extensions=org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions
```

4. Query your tables with Spark SQL. For example
   queries, see [Querying S3 tables with Spark SQL](s3-tables-client-catalog.md#query-with-spark "s3-tables-client-catalog.md#query-with-spark").

AWS analytics services integration
The following prerequisites are required to query tables with Spark
on Amazon EMR using the AWS analytics services integration.

###### Prerequisites

- [Integrate your table
  buckets with AWS analytics services](s3-tables-integrating-aws.md "s3-tables-integrating-aws.md").
- Create the default service role for Amazon EMR (`EMR_DefaultRole_V2`). For details, see [Service role for Amazon EMR (EMR role)](../../../emr/latest/ManagementGuide/emr-iam-role.md "../../../emr/latest/ManagementGuide/emr-iam-role.md") .
- Create the Amazon EC2 instance profile for Amazon EMR (`EMR_EC2_DefaultRole`). For details, see [Service role
  for cluster EC2 instances (EC2 instance profile)](../../../emr/latest/ManagementGuide/emr-iam-role-ec2.md "../../../emr/latest/ManagementGuide/emr-iam-role-ec2.md").
  - Attach the `AmazonS3TablesFullAccess` policy to
    `EMR_EC2_DefaultRole`.

###### To set up an Amazon EMR cluster to query tables with Spark

1. Create a cluster with the following configuration. To use this example, replace the
   `user input placeholder` values with your own
   information.

```
aws emr create-cluster --release-label emr-7.5.0 \
--applications Name=Spark \
--configurations file://configurations.json \
--region `us-east-1` \
--name My_Spark_Iceberg_Cluster \
--log-uri s3://``amzn-s3-demo-bucket``/ \
--instance-type m5.xlarge \
--instance-count 2 \
--service-role `EMR_DefaultRole` \
--ec2-attributes \

InstanceProfile=`EMR_EC2_DefaultRole`,SubnetId=`subnet-1234567890abcdef0`,KeyName=`my-key-pair`
```

`configurations.json`:

```
[{
"Classification":"iceberg-defaults",
"Properties":{"iceberg.enabled":"true"}
}]
```

2. [Connect
   to the Spark primary node using SSH](../../../emr/latest/ManagementGuide/emr-connect-master-node-ssh.md#emr-connect-cli "../../../emr/latest/ManagementGuide/emr-connect-master-node-ssh.md#emr-connect-cli").
3. Enter the following command to initialize a Spark session for
   Iceberg that connects to your tables. Replace the `user
input placeholders` for Region, account ID and table bucket name with your own information.

```
spark-shell \
--conf spark.sql.extensions=org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions \
--conf spark.sql.defaultCatalog=s3tables \
--conf spark.sql.catalog.s3tables=org.apache.iceberg.spark.SparkCatalog \
--conf spark.sql.catalog.s3tables.catalog-impl=org.apache.iceberg.aws.glue.GlueCatalog \
--conf spark.sql.catalog.s3tables.client.region=`us-east-1` \
--conf spark.sql.catalog.s3tables.glue.id=`111122223333`:s3tablescatalog/`amzn-s3-demo-table-bucket`
```

4. Query your tables with Spark SQL. For example queries, see [Querying S3 tables with Spark SQL](s3-tables-client-catalog.md#query-with-spark "s3-tables-client-catalog.md#query-with-spark")

###### Note

If you are using the `DROP TABLE PURGE` command with Amazon EMR:

- Amazon EMR version 7.5

Set the Spark config
`spark.sql.catalog.`your-catalog-name`.cache-enabled` to
`false`. If this config is set to `true`, run the command in a new session
or application so the table cache is not activated.

- Amazon EMR versions higher than 7.5

`DROP TABLE` is not supported. You can use the S3 Tables
`DeleteTable` REST API to delete a table.
