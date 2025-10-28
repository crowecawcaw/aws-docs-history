# Metastore configuration for EMR Serverless

A _Hive metastore_ is a centralized location that stores structural
information about your tables, including schemas, partition names, and data types. With
EMR Serverless, persist this table metadata in a metastore that has access to your
jobs.

You have two options for a Hive metastore:

- The AWS Glue Data Catalog
- An external Apache Hive metastore

## Using the AWS Glue Data Catalog as a metastore

You can configure your Spark and Hive jobs to use the AWS Glue Data Catalog as its metastore. We
recommend this configuration when you require a persistent metastore or a metastore shared
by different applications, services, or AWS accounts. For more information about the
Data Catalog, refer to [Populating the AWS Glue Data Catalog](../../../glue/latest/dg/populate-data-catalog.md "../../../glue/latest/dg/populate-data-catalog.md"). For information about AWS Glue pricing, refer to [AWS Glue pricing](https://aws.amazon.com/glue/pricing "https://aws.amazon.com/glue/pricing").

You can configure your EMR Serverless job to use the AWS Glue Data Catalog either in the same
AWS account as your application, or in a different AWS account.

### Configure the AWS Glue Data Catalog

To configure the Data Catalog, choose which type of EMR Serverless application that you
want to use.

Spark
When you use EMR Studio to run your jobs with EMR Serverless Spark
applications, the AWS Glue Data Catalog is the default metastore.

When you use SDKs or AWS CLI, set the
`spark.hadoop.hive.metastore.client.factory.class` configuration to
`com.amazonaws.glue.catalog.metastore.AWSGlueDataCatalogHiveClientFactory`
in the `sparkSubmit` parameters of your job run. The following example
shows how to configure the Data Catalog with the AWS CLI.

```
aws emr-serverless start-job-run \
    --application-id `application-id` \
    --execution-role-arn `job-role-arn` \
    --job-driver '{
        "sparkSubmit": {
            "entryPoint": "s3://`amzn-s3-demo-bucket`/code/pyspark/extreme_weather.py",
            "sparkSubmitParameters": "--conf spark.hadoop.hive.metastore.client.factory.class=com.amazonaws.glue.catalog.metastore.AWSGlueDataCatalogHiveClientFactory --conf spark.driver.cores=1 --conf spark.driver.memory=3g --conf spark.executor.cores=4 --conf spark.executor.memory=3g"
        }
    }'
```

Alternatively, you can set this configuration when you create a new
`SparkSession` in your Spark code.

```
from pyspark.sql import SparkSession

spark = (
    SparkSession.builder.appName("SparkSQL")
    .config(
        "spark.hadoop.hive.metastore.client.factory.class",
        "com.amazonaws.glue.catalog.metastore.AWSGlueDataCatalogHiveClientFactory",
    )
    .enableHiveSupport()
    .getOrCreate()
)

# we can query tables with SparkSQL
spark.sql("SHOW TABLES").show()

# we can also them with native Spark
print(spark.catalog.listTables())
```

Hive
For EMR Serverless Hive applications, the Data Catalog is the default metastore.
That is, when you run jobs on a EMR Serverless Hive application, Hive records
metastore information in the Data Catalog in the same AWS account as your application.
You don't need a virtual private cloud (VPC) to use the Data Catalog as your
metastore.

To access the Hive metastore tables, add the required AWS Glue policies outlined in
[Setting up IAM Permissions for AWS Glue](../../../glue/latest/dg/getting-started-access.md "../../../glue/latest/dg/getting-started-access.md").

### Configure cross-account access for

EMR Serverless and AWS Glue Data Catalog

To set up cross-account access for EMR Serverless, first sign in to the
following AWS accounts:

- `AccountA` – An AWS account where you have created an
  EMR Serverless application.
- `AccountB` – An AWS account that contains a AWS Glue Data Catalog that
  you want your EMR Serverless job runs to access.

1. Make sure an administrator or other authorized identity in `AccountB`
   attaches a resource policy to the Data Catalog in `AccountB`. This policy grants
   `AccountA` specific cross-account permissions to perform operations on
   resources in the `AccountB` catalog.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "glue:GetDatabase",
 "glue:CreateDatabase",
 "glue:GetDataBases",
 "glue:CreateTable",
 "glue:GetTable",
 "glue:UpdateTable",
 "glue:DeleteTable",
 "glue:GetTables",
 "glue:GetPartition",
 "glue:GetPartitions",
 "glue:CreatePartition",
 "glue:BatchCreatePartition",
 "glue:GetUserDefinedFunctions"
 ],
 "Resource": [
 "arn:aws:glue:*:123456789012:catalog"
 ],
 "Sid": "AllowGLUEGetdatabase"
 }
 ]
}`

```

2. Add an IAM policy to the EMR Serverless job runtime role in
   `AccountA` so that role can access Data Catalog resources in
   `AccountB`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "glue:GetDatabase",
 "glue:CreateDatabase",
 "glue:GetDataBases",
 "glue:CreateTable",
 "glue:GetTable",
 "glue:UpdateTable",
 "glue:DeleteTable",
 "glue:GetTables",
 "glue:GetPartition",
 "glue:GetPartitions",
 "glue:CreatePartition",
 "glue:BatchCreatePartition",
 "glue:GetUserDefinedFunctions"
 ],
 "Resource": [
 "arn:aws:glue:*:123456789012:catalog"
 ],
 "Sid": "AllowGLUEGetdatabase"
 }
 ]
}`

```

3. Start your job run. This step is slightly different depending on
   `AccountA`'s EMR Serverless application type.

Spark
Pass the `spark.hadoop.hive.metastore.glue.catalogid` property in
the `sparkSubmitParameters` as shown in the following example.
Replace `AccountB-catalog-id` with the ID
of the Data Catalog in `AccountB`.

```
aws emr-serverless start-job-run \
--application-id "`application-id`" \
--execution-role-arn "`job-role-arn`" \
--job-driver '{
    "sparkSubmit": {
        "entryPoint": "s3://`amzn-s3-demo-bucket`/scripts/test.py",
         "sparkSubmitParameters": "--conf spark.hadoop.hive.metastore.client.factory.class=com.amazonaws.glue.catalog.metastore.AWSGlueDataCatalogHiveClientFactory --conf spark.hadoop.hive.metastore.glue.catalogid=`AccountB-catalog-id` --conf spark.executor.cores=1 --conf spark.executor.memory=1g --conf spark.driver.cores=1 --conf spark.driver.memory=1g --conf spark.executor.instances=1"
    }
  }' \
--configuration-overrides '{
    "monitoringConfiguration": {
    "s3MonitoringConfiguration": {
    "logUri": "s3://`amzn-s3-demo-bucket`/logs/"
    }
  }
}'
```

Hive
Set the `hive.metastore.glue.catalogid` property in the
`hive-site` classification as shown in the following example.
Replace `AccountB-catalog-id` with the ID
of the Data Catalog in `AccountB`.

```
aws emr-serverless start-job-run \
--application-id "`application-id`" \
--execution-role-arn "`job-role-arn`" \
--job-driver '{
    "hive": {
    "query": "s3://`amzn-s3-demo-bucket`/hive/scripts/create_table.sql",
    "parameters": "--hiveconf hive.exec.scratchdir=s3://`amzn-s3-demo-bucket`/hive/scratch --hiveconf hive.metastore.warehouse.dir=s3://`amzn-s3-demo-bucket`/hive/warehouse"
    }
}' \
--configuration-overrides '{
    "applicationConfiguration": [{
        "classification": "hive-site",
        "properties": {
            "hive.metastore.glue.catalogid": "`AccountB-catalog-id`"
        }
    }]
}'
```

### Considerations when using the

AWS Glue Data Catalog

You can add auxiliary JARs with `ADD JAR` in your Hive scripts. For
additional considerations, refer to [Considerations when using AWS Glue Data Catalog](../ReleaseGuide/emr-hive-metastore-glue.md#emr-hive-glue-considerations-hive "../ReleaseGuide/emr-hive-metastore-glue.md#emr-hive-glue-considerations-hive").
