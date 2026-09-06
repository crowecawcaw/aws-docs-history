

# Build ETL pipelines using AWS Glue
<a name="tutorial-transform-data-with-glue"></a>

Data engineering teams often have raw data landing on an FSx for ONTAP volume from applications, daily file drops, or partner integrations over NFS or SMB. Preparing that data for downstream analytics requires reading, transforming, enriching, or repartitioning it at scale, and making the curated output available to analysts and applications.

With an Amazon S3 access point attached to the FSx for ONTAP volume, AWS Glue reads the source data, transforms it with your choice of runtime (Apache Spark, Python shell, or Ray), and writes the curated output back to the same volume. Both the raw and curated datasets stay on FSx for ONTAP, so the volume's snapshot, backup, and retention policies apply uniformly across the pipeline. Because an FSx for ONTAP volume is simultaneously accessible over NFS, SMB, and the Amazon S3 API, the raw data can be produced by NFS or SMB clients and the curated output can be consumed by any of those protocols.

In this tutorial, you use the NYC Taxi trip dataset from the [Query files with SQL using Amazon Athena](tutorial-query-data-with-athena.md) tutorial. A AWS Glue ETL job reads the raw Parquet data, adds computed columns, filters invalid records, and writes the transformed output back to the volume partitioned by time of day.

**Note**  
This tutorial takes approximately **25 to 35 minutes** to complete. The AWS services used incur charges for the resources you create. If you complete all the steps, including the **Clean up** section promptly, the expected cost is less than **$1** in the US East (N. Virginia) AWS Region. This estimate does not include ongoing charges for the FSx for ONTAP volume itself.

## Prerequisites
<a name="tutorial-glue-prerequisites"></a>

Before you begin, make sure you have the following:
+ Complete Steps 1 through 3 of the [Query files with SQL using Amazon Athena](tutorial-query-data-with-athena.md) tutorial. That procedure uploads the NYC Taxi dataset to the access point, creates the `fsxn_taxi_demo` database in the AWS Glue Data Catalog, and registers the `taxi_data` table. This tutorial builds on those resources, so do not run the Athena tutorial's **Clean up** section until you have finished this tutorial.
+ An IAM role for AWS Glue with an inline policy that grants write access to CloudWatch Logs, read/write access to the access point, and access to the AWS Glue Data Catalog database used by this tutorial. The following steps create a role with the minimum permissions needed for this tutorial.

  1. Save the following trust policy as `glue-trust-policy.json`. It allows AWS Glue to assume the role.

     ```
     {
         "Version": "2012-10-17", 		 	 	 
         "Statement": [
             {
                 "Effect": "Allow",
                 "Principal": {"Service": "glue.amazonaws.com"},
                 "Action": "sts:AssumeRole"
             }
         ]
     }
     ```

  1. Save the following permissions policy as `glue-permissions.json`. Replace `{{region}}`, `{{account-id}}`, and `{{access-point-name}}` with your values.

     ```
     {
         "Version": "2012-10-17", 		 	 	 
         "Statement": [
             {
                 "Sid": "Logs",
                 "Effect": "Allow",
                 "Action": [
                     "logs:CreateLogGroup",
                     "logs:CreateLogStream",
                     "logs:PutLogEvents"
                 ],
                 "Resource": "arn:aws:logs:{{region}}:{{account-id}}:log-group:/aws-glue/*"
             },
             {
                 "Sid": "AccessPoint",
                 "Effect": "Allow",
                 "Action": [
                     "s3:GetObject",
                     "s3:PutObject",
                     "s3:ListBucket",
                     "s3:DeleteObject"
                 ],
                 "Resource": [
                     "arn:aws:s3:{{region}}:{{account-id}}:accesspoint/{{access-point-name}}",
                     "arn:aws:s3:{{region}}:{{account-id}}:accesspoint/{{access-point-name}}/object/*"
                 ]
             },
             {
                 "Sid": "DataCatalog",
                 "Effect": "Allow",
                 "Action": [
                     "glue:GetDatabase",
                     "glue:GetTable",
                     "glue:GetTables",
                     "glue:CreateTable",
                     "glue:UpdateTable",
                     "glue:DeleteTable",
                     "glue:BatchCreatePartition",
                     "glue:BatchDeletePartition",
                     "glue:CreatePartition",
                     "glue:UpdatePartition",
                     "glue:GetPartition",
                     "glue:GetPartitions"
                 ],
                 "Resource": [
                     "arn:aws:glue:{{region}}:{{account-id}}:catalog",
                     "arn:aws:glue:{{region}}:{{account-id}}:database/fsxn_taxi_demo",
                     "arn:aws:glue:{{region}}:{{account-id}}:table/fsxn_taxi_demo/*"
                 ]
             }
         ]
     }
     ```

  1. Create the role and attach the inline policy.

     ```
     $ aws iam create-role \
         --role-name {{fsxn-tutorial-glue-etl-role}} \
         --assume-role-policy-document file://glue-trust-policy.json
     
     aws iam put-role-policy \
         --role-name {{fsxn-tutorial-glue-etl-role}} \
         --policy-name glue-fsxn-access \
         --policy-document file://glue-permissions.json
     ```

  This tutorial stores the ETL script on the access point itself, so no separate Amazon S3 bucket is required. The `AccessPoint` statement covers both the script and the taxi data; the `DataCatalog` statement scopes AWS Glue catalog access to the `fsxn_taxi_demo` database that the crawler in Step 4 updates.

**Important**  
The Amazon S3 access point must use an internet network origin. AWS Glue jobs access Amazon S3 from managed infrastructure, not from your VPC.

## Step 1: Create the ETL script
<a name="tutorial-glue-create-script"></a>

The following PySpark script reads the raw taxi trip data from your FSx for ONTAP volume, applies transformations, and writes the results back to the volume. Save this script as `taxi_transform.py`.

```
import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import col, hour, dayofweek, when, round as spark_round

args = getResolvedOptions(sys.argv, ['JOB_NAME', 'AP_ALIAS'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

ap_alias = args['AP_ALIAS']

# Read raw taxi data from FSx through the access point
df = spark.read.parquet(f"s3://{ap_alias}/taxi-data/")

# Transform: filter invalid records, add computed columns
transformed = df \
    .filter(col("trip_distance") > 0) \
    .filter(col("total_amount") > 0) \
    .filter(col("passenger_count") > 0) \
    .withColumn("pickup_hour", hour(col("tpep_pickup_datetime"))) \
    .withColumn("pickup_day_of_week", dayofweek(col("tpep_pickup_datetime"))) \
    .withColumn("cost_per_mile",
        spark_round(col("total_amount") / col("trip_distance"), 2)) \
    .withColumn("time_of_day",
        when(hour(col("tpep_pickup_datetime")).between(6, 11), "morning")
        .when(hour(col("tpep_pickup_datetime")).between(12, 16), "afternoon")
        .when(hour(col("tpep_pickup_datetime")).between(17, 21), "evening")
        .otherwise("night")
    ) \
    .select(
        "tpep_pickup_datetime", "tpep_dropoff_datetime",
        "passenger_count", "trip_distance",
        "PULocationID", "DOLocationID",
        "fare_amount", "tip_amount", "total_amount",
        "pickup_hour", "pickup_day_of_week",
        "cost_per_mile", "time_of_day"
    )

# Write transformed data back to FSx, partitioned by time of day
transformed.write \
    .mode("overwrite") \
    .partitionBy("time_of_day") \
    .parquet(f"s3://{ap_alias}/taxi-data-transformed/")

job.commit()
```

The script performs the following transformations:
+ **Filters** records with zero or negative trip distance, fare, or passenger count.
+ **Adds computed columns:** `pickup_hour`, `pickup_day_of_week`, `cost_per_mile`, and `time_of_day` (morning, afternoon, evening, or night).
+ **Selects** a subset of columns relevant for analysis.
+ **Partitions** the output by `time_of_day`, which improves query performance when filtering by time period.

## Step 2: Upload the script and create the job
<a name="tutorial-glue-create-job"></a>

Upload the ETL script to your FSx for ONTAP volume through the access point, and create a AWS Glue job that references it. AWS Glue loads the script from the access point at job startup, the same way it loads scripts from a standard Amazon S3 bucket.

```
$ # Upload the script to the access point
aws s3 cp taxi_transform.py \
    s3://{{my-ap-alias-ext-s3alias}}/glue-scripts/taxi_transform.py

# Create the Glue job
aws glue create-job \
    --name {{fsxn-taxi-transform}} \
    --role {{my-glue-role-arn}} \
    --command '{
        "Name": "glueetl",
        "ScriptLocation": "s3://{{my-ap-alias-ext-s3alias}}/glue-scripts/taxi_transform.py",
        "PythonVersion": "3"
    }' \
    --default-arguments '{
        "--AP_ALIAS": "{{my-ap-alias-ext-s3alias}}",
        "--job-language": "python"
    }' \
    --glue-version "4.0" \
    --number-of-workers 2 \
    --worker-type "G.1X"
```

## Step 3: Run the job
<a name="tutorial-glue-run-job"></a>

```
$ aws glue start-job-run --job-name {{fsxn-taxi-transform}}
```

Monitor the job status. The job typically completes in one to two minutes with two G.1X workers.

```
$ aws glue get-job-runs --job-name {{fsxn-taxi-transform}} \
    --query "JobRuns[0].{State:JobRunState,Duration:ExecutionTime,Error:ErrorMessage}"
```

When the job completes, verify the transformed output on your FSx for ONTAP volume.

```
$ aws s3 ls s3://{{my-ap-alias-ext-s3alias}}/taxi-data-transformed/
                           PRE time_of_day=afternoon/
                           PRE time_of_day=evening/
                           PRE time_of_day=morning/
                           PRE time_of_day=night/
```

The output is partitioned into four directories by time of day. Each partition contains Parquet files with the transformed data.

## Step 4: Query the transformed data
<a name="tutorial-glue-query-transformed"></a>

Run a AWS Glue crawler on the transformed output to register it in the AWS Glue Data Catalog, then query it with Athena.

```
$ # Create a crawler for the transformed data
aws glue create-crawler \
    --name {{fsxn-taxi-transformed-crawler}} \
    --role {{my-glue-role-arn}} \
    --database-name {{fsxn_taxi_demo}} \
    --targets '{"S3Targets": [{"Path": "s3://{{my-ap-alias-ext-s3alias}}/taxi-data-transformed/"}]}'

# Run the crawler
aws glue start-crawler --name {{fsxn-taxi-transformed-crawler}}
```

After the crawler completes, query the transformed data in Athena. The partitioned structure allows Athena to scan only the relevant partitions.

```
-- Average cost per mile by time of day
SELECT
    time_of_day,
    COUNT(*) AS trip_count,
    ROUND(AVG(cost_per_mile), 2) AS avg_cost_per_mile,
    ROUND(AVG(tip_amount), 2) AS avg_tip
FROM fsxn_taxi_demo.taxi_data_transformed
GROUP BY time_of_day
ORDER BY trip_count DESC
```

```
-- Busiest pickup locations during morning rush
SELECT
    PULocationID AS pickup_location,
    COUNT(*) AS trip_count,
    ROUND(AVG(trip_distance), 2) AS avg_distance
FROM fsxn_taxi_demo.taxi_data_transformed
WHERE time_of_day = 'morning'
GROUP BY PULocationID
ORDER BY trip_count DESC
LIMIT 10
```

Because the data is partitioned by `time_of_day`, the second query scans only the `morning` partition, reducing the amount of data read and improving query performance.

## Considerations
<a name="tutorial-glue-considerations"></a>
+ **Internet origin required.** AWS Glue jobs access Amazon S3 from managed infrastructure outside your VPC. You must use an internet-origin access point.
+ **Read and write.** AWS Glue ETL jobs can both read from and write to your FSx for ONTAP volume through the access point. The access point policy and file system user must allow both `s3:GetObject` and `s3:PutObject`.
+ **Worker sizing.** The number and type of AWS Glue workers affects job performance and cost. For the 48 MB sample dataset, two G.1X workers are sufficient. For larger datasets, increase the worker count or use G.2X workers.
+ **Partitioning.** Writing partitioned output improves downstream query performance in Athena and other analytics services. Choose partition keys based on how the data is typically queried.
+ **Script storage.** AWS Glue loads ETL scripts from Amazon S3 at job startup. This tutorial stores the script on the access point so that the script lives alongside the data, but you can also host it in a standard Amazon S3 bucket. If you use a standalone bucket, extend the role's inline policy with `s3:GetObject` on the script bucket ARN.

## Clean up
<a name="tutorial-glue-clean-up"></a>

To avoid ongoing charges, delete the resources you created in this tutorial.

In the Athena query editor, drop the table created by the crawler:

```
DROP TABLE IF EXISTS fsxn_taxi_demo.taxi_data_transformed;
```

```
$ # Delete the Glue job and crawler
aws glue delete-job --name {{fsxn-taxi-transform}}
aws glue delete-crawler --name {{fsxn-taxi-transformed-crawler}}

# Delete the ETL script and transformed data from the access point
aws s3 rm s3://{{my-ap-alias-ext-s3alias}}/glue-scripts/taxi_transform.py
aws s3 rm s3://{{my-ap-alias-ext-s3alias}}/taxi-data-transformed/ --recursive

# Delete the IAM role
aws iam delete-role-policy \
    --role-name {{fsxn-tutorial-glue-etl-role}} \
    --policy-name glue-fsxn-access
aws iam delete-role --role-name {{fsxn-tutorial-glue-etl-role}}
```