

# Setting up Apache Spark on Amazon EMR

Spark jobs on Amazon EMR Serverless read HealthLake tables in place, with no export or staging copy. The job's runtime role has no Amazon S3 permissions on the HealthLake data. Spark reads the data files only with temporary credentials that Lake Formation issues after it checks your grants.

![A Spark job runs on Amazon EMR Serverless with a runtime role. Its Iceberg catalog is configured with Lake Formation enabled and points at the HealthLake catalog ID. The job gets table metadata from the AWS Glue Data Catalog and temporary credentials from AWS Lake Formation, then reads the HealthLake data files in Amazon S3 with those credentials. The runtime role has no Amazon S3 permissions on the HealthLake data, so a direct read is denied.](https://docs.aws.amazon.com/healthlake/latest/devguide/images/healthlake-emr-access-path.png)


Before you begin, complete Steps 1 and 3 in [Getting started with HealthLake analytics](integrating-analytics-getting-started.md): find the resource link and turn on full table access. You grant Lake Formation permissions in Step 3 of this topic, after you create the runtime role.

## Prerequisites
<a name="integrating-spark-prerequisites"></a>

Before you query HealthLake data with Spark, make sure that you have the following:
+ Amazon EMR Serverless release 7.8.0 or later, which provides Lake Formation full table access for Iceberg tables.
+ The same AWS Region for the data store, the Amazon EMR Serverless application, and any output. Lake Formation doesn't vend credentials across Regions.
+ A data lake administrator to make the grants.
+ The AWS CLI.
+ An Amazon S3 location in your account for the job script and logs.

In the commands in this topic, replace {{us-east-1}} with the AWS Region of your data store.

This topic covers Amazon EMR Serverless only.

## Step 1: Find the HealthLake catalog ID and location
<a name="integrating-spark-step1"></a>

The catalog ID differs for each data store and Region, so look it up instead of hardcoding it.

**To find the HealthLake catalog ID and location**
+ Run the following command.

  ```bash
  aws glue get-database --name {{resource-link-name}} --region {{us-east-1}} --query "Database.[TargetDatabase.CatalogId, LocationUri]" --output text
  ```

Replace {{resource-link-name}} with the resource link to the HealthLake database in your account. You find it in Step 1 of [Getting started with HealthLake analytics](integrating-analytics-getting-started.md).

The command returns two values. The first is the HealthLake catalog ID, which you use for {{444455556666}}. The second is the Amazon S3 location URI, which you use for {{location-uri}} as the Spark catalog warehouse.

**Result:** Record the HealthLake catalog ID and the Amazon S3 location URI. You use the catalog ID in Step 2, Step 4, and Step 5. You use the location URI in Step 4.

## Step 2: Create the runtime role
<a name="integrating-spark-step2"></a>

Create an IAM role named `healthlake-emr-runtime` for the job to assume.

**To create the runtime role**

1. Save the following trust policy as `emr-trust-policy.json`. It allows only Amazon EMR Serverless applications in your account to assume the role.

   ```json
   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Effect": "Allow",
         "Principal": {
           "Service": "emr-serverless.amazonaws.com"
         },
         "Action": "sts:AssumeRole",
         "Condition": {
           "StringEquals": {
             "aws:SourceAccount": "{{111122223333}}"
           },
           "ArnLike": {
             "aws:SourceArn": "arn:aws:emr-serverless:{{us-east-1}}:{{111122223333}}:/applications/*"
           }
         }
       }
     ]
   }
   ```

   Replace {{111122223333}} with your AWS account ID, where you create the runtime role. Replace {{us-east-1}} with the AWS Region of your data store.

1. Save the following permissions policy as `emr-runtime-permissions.json`. It grants AWS Glue Data Catalog reads on the resource link in your catalog and on the target database in the HealthLake catalog. It also grants `lakeformation:GetDataAccess`, which requires `*` as the resource.

   ```json
   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Sid": "ReadResourceLink",
         "Effect": "Allow",
         "Action": [
           "glue:GetCatalog",
           "glue:GetDatabase",
           "glue:GetDatabases",
           "glue:GetTable",
           "glue:GetTables"
         ],
         "Resource": [
           "arn:aws:glue:{{us-east-1}}:{{111122223333}}:catalog",
           "arn:aws:glue:{{us-east-1}}:{{111122223333}}:database/{{resource-link-name}}",
           "arn:aws:glue:{{us-east-1}}:{{111122223333}}:table/{{resource-link-name}}/*"
         ]
       },
       {
         "Sid": "ReadHealthLakeCatalog",
         "Effect": "Allow",
         "Action": [
           "glue:GetCatalog",
           "glue:GetDatabase",
           "glue:GetDatabases",
           "glue:GetTable",
           "glue:GetTables"
         ],
         "Resource": [
           "arn:aws:glue:{{us-east-1}}:{{444455556666}}:catalog",
           "arn:aws:glue:{{us-east-1}}:{{444455556666}}:database/{{target-database-name}}",
           "arn:aws:glue:{{us-east-1}}:{{444455556666}}:table/{{target-database-name}}/*"
         ]
       },
       {
         "Sid": "RequestLakeFormationCredentials",
         "Effect": "Allow",
         "Action": "lakeformation:GetDataAccess",
         "Resource": "*"
       }
     ]
   }
   ```

   Replace {{target-database-name}} with the database in the HealthLake catalog that the resource link points to. You find it in Step 1 of [Getting started with HealthLake analytics](integrating-analytics-getting-started.md).

1. Create the role and attach the permissions policy.

   ```bash
   aws iam create-role --role-name healthlake-emr-runtime --assume-role-policy-document file://emr-trust-policy.json
   aws iam put-role-policy --role-name healthlake-emr-runtime --policy-name healthlake-emr-read --policy-document file://emr-runtime-permissions.json
   ```

**Important**  
Don't add Amazon S3 permissions on the HealthLake data to this role. That way, a successful read proves the credentials came from Lake Formation.

**Note**  
The job also needs `s3:GetObject` on the job script and `s3:PutObject` on the log location in your bucket. Add those to the role, or use a role that already has them.

**Result:** The role `healthlake-emr-runtime` exists. Record its ARN, `arn:aws:iam::{{111122223333}}:role/healthlake-emr-runtime`. You use it in Step 3 and Step 4.

## Step 3: Grant Lake Formation permissions to the runtime role
<a name="integrating-spark-step3"></a>

To grant the runtime role access to the tables, follow Step 2 in [Getting started with HealthLake analytics](integrating-analytics-getting-started.md). Choose All tables or named tables, and use the role ARN as the principal.

Verify the grant. The `list-permissions` command requires `--resource`, so check the resource link, then the tables.

```bash
aws lakeformation list-permissions --region {{us-east-1}} \
    --principal DataLakePrincipalIdentifier=arn:aws:iam::{{111122223333}}:role/healthlake-emr-runtime \
    --resource '{"Database":{"Name":"{{resource-link-name}}"}}'

aws lakeformation list-permissions --region {{us-east-1}} \
    --principal DataLakePrincipalIdentifier=arn:aws:iam::{{111122223333}}:role/healthlake-emr-runtime \
    --resource '{"Table":{"CatalogId":"{{444455556666}}","DatabaseName":"{{target-database-name}}","TableWildcard":{}}}'
```

For named tables, replace `"TableWildcard":{}` with `"Name":"{{table-name}}"`.

The resource link check can also list `ALL` when the `IAMAllowedPrincipals` group holds it on the link.

**Result:** Lake Formation grants the runtime role access to the HealthLake tables, and the command lists the grant.

## Step 4: Run a query
<a name="integrating-spark-step4"></a>

**To run a query**

1. If you don't already have an Amazon EMR Serverless application, create one.

   ```bash
   aws emr-serverless create-application --name healthlake-spark --type SPARK --release-label emr-7.9.0 --region {{us-east-1}}
   ```

   Record the `applicationId` from the output. You use it as {{application-id}}.

1. Save the following job script as `healthlake_query.py`, then upload it to your bucket.

   ```python
   from pyspark.sql import SparkSession
   
   spark = SparkSession.builder.appName("healthlake-query").getOrCreate()
   spark.sql("SELECT COUNT(*) FROM healthlake.`{{target-database-name}}`.patient").show()
   ```

   The resource links that HealthLake creates usually have the same name as their target database, but a resource link that you create can have a different name.

   ```bash
   aws s3 cp healthlake_query.py s3://amzn-s3-demo-bucket/scripts/
   ```

1. Start the job run with the catalog settings. The job uses the following Spark catalog settings.

   ```properties
   spark.jars=/usr/share/aws/iceberg/lib/iceberg-spark3-runtime.jar
   spark.sql.extensions=org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions
   spark.sql.catalog.healthlake=org.apache.iceberg.spark.SparkCatalog
   spark.sql.catalog.healthlake.type=glue
   spark.sql.catalog.healthlake.warehouse={{location-uri}}
   spark.sql.catalog.healthlake.client.region={{us-east-1}}
   spark.sql.catalog.healthlake.glue.lakeformation-enabled=true
   spark.sql.catalog.healthlake.glue.id={{444455556666}}
   spark.sql.catalog.healthlake.glue.account-id={{444455556666}}
   spark.sql.catalog.healthlake.io-impl=org.apache.iceberg.aws.s3.S3FileIO
   ```

   Pass the settings as `--conf` values in `sparkSubmitParameters`.

   ```bash
   aws emr-serverless start-job-run \
       --region {{us-east-1}} \
       --application-id {{application-id}} \
       --execution-role-arn arn:aws:iam::{{111122223333}}:role/healthlake-emr-runtime \
       --job-driver '{"sparkSubmit": {"entryPoint": "s3://amzn-s3-demo-bucket/scripts/healthlake_query.py", "sparkSubmitParameters": "--conf spark.jars=/usr/share/aws/iceberg/lib/iceberg-spark3-runtime.jar --conf spark.sql.extensions=org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions --conf spark.sql.catalog.healthlake=org.apache.iceberg.spark.SparkCatalog --conf spark.sql.catalog.healthlake.type=glue --conf spark.sql.catalog.healthlake.warehouse={{location-uri}} --conf spark.sql.catalog.healthlake.client.region={{us-east-1}} --conf spark.sql.catalog.healthlake.glue.lakeformation-enabled=true --conf spark.sql.catalog.healthlake.glue.id={{444455556666}} --conf spark.sql.catalog.healthlake.glue.account-id={{444455556666}} --conf spark.sql.catalog.healthlake.io-impl=org.apache.iceberg.aws.s3.S3FileIO"}}' \
       --configuration-overrides '{"monitoringConfiguration": {"s3MonitoringConfiguration": {"logUri": "s3://amzn-s3-demo-bucket/logs/"}}}'
   ```

   The following settings control how the job reads data through Lake Formation:  
`glue.lakeformation-enabled`  
Routes data-file reads through Lake Formation credential vending. Without it, every read fails with a 403 error.  
`glue.id`  
The catalog that Spark reads table metadata from. Set it to the HealthLake catalog ID to read the HealthLake catalog directly. Without it, Spark reads the tables through the resource link in your catalog. If you omit it, use the resource link name instead of the target database name in your queries.  
`glue.account-id`  
The account in the table ARNs that Lake Formation authorizes. Set it to the HealthLake catalog ID.

   Pass these settings when you start the job run. Spark caches a catalog the first time that code uses it, so a catalog used before its settings are complete stays misconfigured for the rest of the session.

1. Check the job run state. The `start-job-run` command returns a job run ID, which you use as {{job-run-id}}.

   ```bash
   aws emr-serverless get-job-run --region {{us-east-1}} --application-id {{application-id}} --job-run-id {{job-run-id}} --query jobRun.state
   ```

   The state is `SUCCESS` when the job finishes. The driver output is in `s3://amzn-s3-demo-bucket/logs/applications/{{application-id}}/jobs/{{job-run-id}}/SPARK_DRIVER/stdout.gz`. If you turn on job retries, the path has `attempts/{{attempt-number}}/` after the job run ID.

**Result:** The driver output shows the row count for the `patient` table.

For the table structure, nested data, resource versions, and data freshness, see [Understanding the analytics tables](integrating-analytics.md#integrating-analytics-tables).

## Step 5: Verify the access path
<a name="integrating-spark-step5"></a>

Confirm that the job reads through Lake Formation, not through the runtime role's own Amazon S3 permissions.

**To verify the access path**

1. In the driver log, confirm the credential vendor.

   ```
   TableStorageCredentialsCache: Using credential vendor class com.amazonaws.glue.accesscontrol.AWSLakeFormationCredentialVendor
   ```

1. Confirm that a direct read fails. First, get the table's metadata location.

   ```bash
   aws glue get-table --catalog-id {{444455556666}} --database-name {{target-database-name}} --name patient --region {{us-east-1}} --query "Table.Parameters.metadata_location" --output text
   ```

   Save the following script as `healthlake_direct_read.py`, then upload it to your bucket.

   ```python
   from pyspark.sql import SparkSession
   
   spark = SparkSession.builder.appName("healthlake-direct-read").getOrCreate()
   spark.read.text("{{metadata-location}}").show()
   ```

   Replace {{metadata-location}} with the metadata location from the `get-table` output.

   ```bash
   aws s3 cp healthlake_direct_read.py s3://amzn-s3-demo-bucket/scripts/
   ```

   Run the script with the same runtime role as in Step 4, but without the `healthlake` catalog `--conf` settings.

   ```bash
   aws emr-serverless start-job-run \
       --region {{us-east-1}} \
       --application-id {{application-id}} \
       --execution-role-arn arn:aws:iam::{{111122223333}}:role/healthlake-emr-runtime \
       --job-driver '{"sparkSubmit": {"entryPoint": "s3://amzn-s3-demo-bucket/scripts/healthlake_direct_read.py"}}' \
       --configuration-overrides '{"monitoringConfiguration": {"s3MonitoringConfiguration": {"logUri": "s3://amzn-s3-demo-bucket/logs/"}}}'
   ```

   The read must fail with `403 AccessDenied`. If it succeeds, the role has Amazon S3 permissions that it shouldn't have.

**Result:** Lake Formation vended the credentials, and the direct read is denied, which proves the data path runs through Lake Formation.

## Lake Formation access mode
<a name="integrating-spark-access-modes"></a>

This topic uses Lake Formation full table access. A job can't use full table access and fine-grained access control on the same Amazon EMR Serverless application. This topic doesn't cover fine-grained access control. For more information, see [Using Lake Formation with Amazon EMR Serverless](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/lake-formation-section.html) in the *Amazon EMR Serverless User Guide*.

## Reading only changed rows
<a name="integrating-spark-incremental"></a>

To read only rows that changed since a watermark, filter on `meta.lastUpdated`, for example `WHERE meta.lastUpdated > TIMESTAMP '{{watermark}}'`. Replace {{watermark}} with the timestamp of the data that you last read. Iceberg pushes the filter down to file pruning.

Follow these practices when you read changed rows:
+ Keep the watermark a literal, not a subquery, so the filter reaches the scan.
+ Confirm the pushdown with `EXPLAIN FORMATTED`.
+ Pin `spark.sql.session.timeZone=UTC`.
+ Deduplicate on `id` before a `MERGE`.

## Troubleshooting
<a name="integrating-spark-troubleshooting"></a>

The following table lists common issues and how to resolve them.


| Symptom | Cause and resolution | 
| --- | --- | 
| Every read fails with a 403 error. | `glue.lakeformation-enabled` is missing from the job run (Step 4), or full table access is off. To turn on full table access, complete Step 3 in [Getting started with HealthLake analytics](integrating-analytics-getting-started.md). | 
| AccessDenied after switching data store or Region. | The catalog ID is hardcoded or stale. Repeat [Step 1: Find the HealthLake catalog ID and location](#integrating-spark-step1). | 
| The job fails with glue.account-id can not be empty. | `glue.account-id` is missing. Set it to the HealthLake catalog ID, as in [Step 4: Run a query](#integrating-spark-step4). | 
| Table not found, or access denied, for a table that exists. | `glue.id` is set, but the query uses the resource link name. Query the target database name instead, as in [Step 4: Run a query](#integrating-spark-step4). | 
| Grant fails with an access error. | You aren't a data lake administrator. Make the grants in Step 3 of this topic as a data lake administrator. | 
| Repeated warning Cross account catalog references are not allowed. | Benign. An Amazon EMR catalog extension probes a catalog path, and the Iceberg catalog still reads the table. | 
| get-tables reports IsRegisteredWithLakeFormation: false. | Use `get-table`, singular, which reports it correctly. | 