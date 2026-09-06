

# Run Spark jobs using Amazon EMR Serverless
<a name="tutorial-run-spark-with-emr-serverless"></a>

Data engineering teams that run Spark workloads — for log processing, feature engineering, complex ETL, or scientific analysis — often have source data on an FSx for ONTAP volume written by on-premises ingestion pipelines, NFS or SMB data movers, or applications that mount the volume directly.

With an Amazon S3 access point attached to the volume, Amazon EMR Serverless reads the data through the access point, runs the Spark job against it, and writes the results back to the same volume. Amazon EMR Serverless handles cluster lifecycle automatically — you submit a job and pay for the seconds it runs.

This pattern suits workloads that need a full Spark runtime (custom libraries, iterative algorithms, long-running transformations, or interactive notebooks via Amazon EMR Studio) where the lighter-weight options — Amazon Athena for SQL and AWS Glue for managed ETL — are not the right fit. For information on those alternatives, see [Query files with SQL using Amazon Athena](tutorial-query-data-with-athena.md) and [Build ETL pipelines using AWS Glue](tutorial-transform-data-with-glue.md).

In this tutorial, you simulate a meteorology team aggregating a year of NOAA Global Surface Summary of the Day (GSOD) observations staged on an FSx for ONTAP volume. You submit a PySpark job that reads the raw CSV files, computes monthly per-station aggregates (average temperature, total precipitation, and a count of days with precipitation events), and writes the results as Parquet partitioned by month — all through the access point.

**Note**  
This tutorial takes approximately **30 to 40 minutes** to complete. The AWS services used incur charges for the resources you create. If you complete all the steps, including the **Clean up** section promptly, the expected cost is less than **$1** in the US East (N. Virginia) AWS Region. This estimate does not include ongoing charges for the FSx for ONTAP volume itself.

## Prerequisites
<a name="tutorial-emr-prerequisites"></a>
+ An FSx for ONTAP volume with an Amazon S3 access point attached. The access point must have an **internet** network origin so that the Amazon EMR Serverless service can reach it. For instructions, see [Creating an access point](fsxn-creating-access-points.md).
+ AWS CLI version 2 installed and configured with credentials that can create IAM roles and Amazon EMR Serverless resources.

## Step 1: Upload the sample dataset to the access point
<a name="tutorial-emr-upload-data"></a>

The NOAA GSOD dataset is a public dataset of daily weather observations, one CSV file per station per year. For this tutorial, you download a 100-station subset from the public `noaa-gsod-pds` Amazon S3 bucket and upload it to your access point.

1. Download the first 100 station files for 2024.

   ```
   $ mkdir -p ~/gsod && cd ~/gsod
   aws s3 ls s3://noaa-gsod-pds/2024/ --no-sign-request | head -100 | awk '{print $NF}' > files.txt
   while read f; do
       aws s3 cp "s3://noaa-gsod-pds/2024/$f" "$f" --no-sign-request --only-show-errors
   done < files.txt
   ls | wc -l
   ```

   The command downloads approximately 100 CSV files totaling about 7–8 MB.

1. Upload the files to the access point under the `gsod/2024/` prefix. Replace {{access-point-alias}} with your access point alias.

   ```
   $ aws s3 cp ~/gsod/ "s3://{{access-point-alias}}/gsod/2024/" --recursive --exclude "files.txt" --only-show-errors
   ```

## Step 2: Write the PySpark job
<a name="tutorial-emr-write-script"></a>

The job reads all CSV files under the input prefix, filters sentinel values that represent missing data, parses the `FRSHTT` bitfield (Fog, Rain, Snow, Hail, Thunder, Tornado) to count precipitation-event days, aggregates per `(station, month)`, and writes partitioned Parquet back to the access point.

1. Save the following script to a file named `gsod_monthly.py`.

   ```
   # gsod_monthly.py
   import sys
   from pyspark.sql import SparkSession
   from pyspark.sql import functions as F
   
   INPUT_PATH, OUTPUT_PATH = sys.argv[1], sys.argv[2]
   
   # GSOD sentinels for missing data
   TEMP_SENTINEL = 9999.9
   PRCP_SENTINEL = 99.99
   
   spark = SparkSession.builder.appName("gsod-monthly-summary").getOrCreate()
   
   raw = spark.read.option("header", True).csv(INPUT_PATH)
   
   cleaned = (raw
       .select(
           F.col("STATION").alias("station"),
           F.col("NAME").alias("station_name"),
           F.col("LATITUDE").cast("double").alias("lat"),
           F.col("LONGITUDE").cast("double").alias("lon"),
           F.to_date("DATE", "yyyy-MM-dd").alias("date"),
           F.col("TEMP").cast("double").alias("temp_f"),
           F.col("PRCP").cast("double").alias("prcp_in"),
           F.col("FRSHTT").alias("frshtt"),
       )
       .filter(F.col("temp_f") != TEMP_SENTINEL)
       .withColumn("month", F.date_format("date", "yyyy-MM"))
       .withColumn(
           "prcp_in",
           F.when(F.col("prcp_in") == PRCP_SENTINEL, None).otherwise(F.col("prcp_in")),
       )
       # FRSHTT is a 6-char bitfield: Fog, Rain, Snow, Hail, Thunder, Tornado.
       # Check only positions 2-4 (Rain, Snow, Hail) for precipitation events.
       .withColumn(
           "had_precip_event",
           F.when(F.col("frshtt").substr(2, 3).rlike("1"), 1).otherwise(0),
       )
   )
   
   monthly = (cleaned
       .groupBy("station", "station_name", "lat", "lon", "month")
       .agg(
           F.avg("temp_f").alias("avg_temp_f"),
           F.min("temp_f").alias("min_temp_f"),
           F.max("temp_f").alias("max_temp_f"),
           F.sum("prcp_in").alias("total_prcp_in"),
           F.sum("had_precip_event").alias("precip_event_days"),
           F.count("*").alias("observation_days"),
       )
   )
   
   (monthly.write
       .mode("overwrite")
       .partitionBy("month")
       .parquet(OUTPUT_PATH))
   
   spark.stop()
   ```

1. Upload the script to the access point under the `scripts/` prefix.

   ```
   $ aws s3 cp gsod_monthly.py "s3://{{access-point-alias}}/scripts/gsod_monthly.py"
   ```

## Step 3: Create the Amazon EMR Serverless job role
<a name="tutorial-emr-iam-role"></a>

Amazon EMR Serverless assumes an IAM execution role when it runs your job. The role needs permissions to read and write the access point and to write logs to CloudWatch Logs. Expand the following section for setup steps.

### To create the Amazon EMR Serverless job role
<a name="tutorial-emr-iam-role-steps"></a>

1. Save the following trust policy as `emr-trust-policy.json`. It allows Amazon EMR Serverless to assume the role.

   ```
   {
       "Version": "2012-10-17", 		 	 	 
       "Statement": [{
           "Effect": "Allow",
           "Principal": {"Service": "emr-serverless.amazonaws.com"},
           "Action": "sts:AssumeRole"
       }]
   }
   ```

1. Save the following permissions policy as `emr-permissions.json`. Replace {{region}}, {{account-id}}, and {{access-point-name}} with your values.

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
                   "logs:PutLogEvents",
                   "logs:DescribeLogGroups",
                   "logs:DescribeLogStreams"
               ],
               "Resource": "*"
           },
           {
               "Sid": "APRead",
               "Effect": "Allow",
               "Action": ["s3:GetObject", "s3:ListBucket"],
               "Resource": [
                   "arn:aws:s3:{{region}}:{{account-id}}:accesspoint/{{access-point-name}}",
                   "arn:aws:s3:{{region}}:{{account-id}}:accesspoint/{{access-point-name}}/object/*"
               ]
           },
           {
               "Sid": "APWrite",
               "Effect": "Allow",
               "Action": [
                   "s3:PutObject", "s3:DeleteObject",
                   "s3:AbortMultipartUpload", "s3:ListMultipartUploadParts"
               ],
               "Resource": "arn:aws:s3:{{region}}:{{account-id}}:accesspoint/{{access-point-name}}/object/*"
           }
       ]
   }
   ```

1. Create the role and attach the policy.

   ```
   $ aws iam create-role --role-name fsxn-emr-job-role \
       --assume-role-policy-document file://emr-trust-policy.json
   aws iam put-role-policy --role-name fsxn-emr-job-role \
       --policy-name emr-access --policy-document file://emr-permissions.json
   ```

## Step 4: Create and start the Amazon EMR Serverless application
<a name="tutorial-emr-create-app"></a>

An Amazon EMR Serverless application is a long-lived compute environment for a specific release label and engine (Spark or Hive). You submit one or more jobs to it. Applications scale compute up and down automatically based on job demand and idle out when no jobs are running.

1. Create a Spark application using a recent Amazon EMR release.

   ```
   $ aws emr-serverless create-application \
       --name fsxn-emr-app --type SPARK --release-label emr-7.0.0
   ```

   Note the `applicationId` in the response.

1. Start the application. Starting pre-warms a small pool of workers so the first job runs without a cold-start delay.

   ```
   $ aws emr-serverless start-application --application-id {{application-id}}
   ```

   Wait for the state to become `STARTED`.

   ```
   $ aws emr-serverless get-application --application-id {{application-id}} \
       --query 'application.state'
   ```

## Step 5: Submit the Spark job
<a name="tutorial-emr-submit-job"></a>

Submit the job using the application ID and the execution role. The job reads the raw CSVs from `gsod/2024/` and writes partitioned Parquet to `gsod-monthly/`, both through the access point.

1. Save the job driver configuration as `job-driver.json`. Replace the placeholders.

   ```
   {
       "sparkSubmit": {
           "entryPoint": "s3://{{access-point-alias}}/scripts/gsod_monthly.py",
           "entryPointArguments": [
               "s3://{{access-point-alias}}/gsod/2024/",
               "s3://{{access-point-alias}}/gsod-monthly/"
           ],
           "sparkSubmitParameters": "--conf spark.executor.cores=2 --conf spark.executor.memory=4g --conf spark.driver.cores=2 --conf spark.driver.memory=4g --conf spark.executor.instances=2"
       }
   }
   ```

1. Save the following monitoring configuration as `job-config.json`. It sends driver and executor logs to CloudWatch Logs.

   ```
   {
       "monitoringConfiguration": {
           "cloudWatchLoggingConfiguration": {
               "enabled": true,
               "logGroupName": "/aws/emr-serverless/fsxn-emr-app"
           }
       }
   }
   ```

1. Submit the job.

   ```
   $ aws emr-serverless start-job-run \
       --application-id {{application-id}} \
       --execution-role-arn arn:aws:iam::{{account-id}}:role/fsxn-emr-job-role \
       --name gsod-monthly \
       --job-driver file://job-driver.json \
       --configuration-overrides file://job-config.json
   ```

   Note the `jobRunId` in the response.

1. Poll the job status. The job transitions from `SCHEDULED` to `RUNNING` to `SUCCESS`.

   ```
   $ aws emr-serverless get-job-run \
       --application-id {{application-id}} \
       --job-run-id {{job-run-id}} \
       --query 'jobRun.state'
   ```

**Note**  
If the job fails, check the driver logs in CloudWatch Logs under the log group `/aws/emr-serverless/fsxn-emr-app`. Amazon EMR Serverless writes one log stream per job run.

## Step 6: Inspect the output
<a name="tutorial-emr-inspect-output"></a>

Verify that the job wrote one Parquet partition per month and that the output is readable.

1. List the output partitions.

   ```
   $ aws s3 ls "s3://{{access-point-alias}}/gsod-monthly/" --recursive
   ```

   You should see one Parquet file per `month=YYYY-MM/` partition plus a `_SUCCESS` marker at the root.

1. Read a partition locally to verify the content.

   ```
   $ aws s3 cp "s3://{{access-point-alias}}/gsod-monthly/month=2024-06/" . \
       --recursive --exclude "_SUCCESS"
   python3 -c "import pyarrow.parquet as pq; \
       t = pq.read_table(next(__import__('glob').iglob('*.parquet'))); \
       print(t.schema); print(t.to_pandas().head())"
   ```

   The output schema includes `station`, `station_name`, `lat`, `lon`, `avg_temp_f`, `min_temp_f`, `max_temp_f`, `total_prcp_in`, `precip_event_days`, and `observation_days`.

## Extending the pattern
<a name="tutorial-emr-extending"></a>
+ **Query the output with Spark SQL.** Register the partitioned output as a table with the AWS Glue Data Catalog and query it with Spark SQL, Athena, or any other tool that reads AWS Glue catalog tables. For instructions on registering an access point-backed dataset, see [Query files with SQL using Amazon Athena](tutorial-query-data-with-athena.md).
+ **Use Iceberg for ACID writes.** For workloads that update or merge data, configure the job to write to an Iceberg table on the access point instead of plain Parquet. Amazon EMR Serverless includes the Iceberg runtime by default on recent release labels.
+ **Run interactively with Amazon EMR Studio.** Attach a Jupyter notebook to the Amazon EMR Serverless application to explore the data interactively. See [Interactive workloads with Amazon EMR Serverless](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/interactive-workloads.html) in the *Amazon EMR Serverless User Guide*.
+ **Schedule the job.** Use Amazon EventBridge Scheduler or AWS Step Functions to run the job on a recurring schedule (for example, when a new day of data lands on the volume).

## Troubleshooting
<a name="tutorial-emr-troubleshooting"></a>

Job fails with `AccessDenied` on the access point  
Verify that the job role policy grants `s3:GetObject` and `s3:ListBucket` on the access point ARN (not on a bucket), and that the access point has an internet network origin so the Amazon EMR Serverless service can reach it.

Job succeeds but the output is empty  
Check the input path. Amazon S3 `ListObjectsV2` treats prefixes literally, so `s3://alias/gsod/2024` (no trailing slash) and `s3://alias/gsod/2024/` (trailing slash) can behave differently. Include the trailing slash when pointing at a directory of files.

Driver logs are not in CloudWatch Logs  
The monitoring configuration must be passed through `--configuration-overrides` on `start-job-run`, not on the application. Each job run writes to its own log stream under the configured log group.

## Clean up
<a name="tutorial-emr-clean-up"></a>

Stop and delete the application, remove the IAM role, and delete any uploaded data you no longer need.

```
$ aws emr-serverless stop-application --application-id {{application-id}}
aws emr-serverless delete-application --application-id {{application-id}}
aws iam delete-role-policy --role-name fsxn-emr-job-role --policy-name emr-access
aws iam delete-role --role-name fsxn-emr-job-role
aws s3 rm "s3://{{access-point-alias}}/scripts/gsod_monthly.py"
aws s3 rm "s3://{{access-point-alias}}/gsod/" --recursive
aws s3 rm "s3://{{access-point-alias}}/gsod-monthly/" --recursive
```