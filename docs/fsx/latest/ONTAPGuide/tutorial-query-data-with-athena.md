

# Query files with SQL using Amazon Athena
<a name="tutorial-query-data-with-athena"></a>

Enterprise systems frequently produce file-based output — log exports, transaction extracts, inventory snapshots, inter-system file drops — that lands on an NFS or SMB file share.

With an Amazon S3 access point attached to the FSx for ONTAP volume, Amazon Athena queries the files in place. Your applications and users continue to write to the volume over NFS or SMB the way they always have, and analysts run standard SQL against that data through the access point. Because an FSx for ONTAP volume is simultaneously accessible over NFS, SMB, and the Amazon S3 API, the same file can be produced by one protocol and consumed by another without a copy.

In this tutorial, you upload a sample dataset to your FSx for ONTAP volume through an Amazon S3 access point, register it in the AWS Glue Data Catalog, and query it with Amazon Athena.

**Note**  
This tutorial takes approximately **20 to 30 minutes** to complete. The AWS services used incur charges for the resources you create. If you complete all the steps, including the **Clean up** section promptly, the expected cost is less than **$1** in the US East (N. Virginia) AWS Region. This estimate does not include ongoing charges for the FSx for ONTAP volume itself.

## Prerequisites
<a name="tutorial-athena-prerequisites"></a>

Before you begin, make sure you have the following:
+ An FSx for ONTAP volume with an Amazon S3 access point attached. The access point must have an **internet** network origin. For instructions on creating an access point, see [Creating an access point](fsxn-creating-access-points.md).
+ An Athena workgroup configured with a query results location. Athena writes query results to an Amazon S3 bucket, not to the FSx for ONTAP volume. If you do not have a workgroup, you can use the `primary` workgroup and configure a results location in the Athena console under **Settings**. For more information, see [Managing workgroups](https://docs.aws.amazon.com/athena/latest/ug/workgroups-create-update-delete.html) in the *Amazon Athena User Guide*.
+ An IAM role for AWS Glue with the `AWSGlueServiceRole` managed policy attached and an inline policy that grants access to your Amazon S3 access point. If you do not have one, use the following steps.

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

  1. Save the following permissions policy as `glue-s3-policy.json`. It grants access to the access point. Replace `{{region}}`, `{{account-id}}`, and `{{access-point-name}}` with your values.

     ```
     {
         "Version": "2012-10-17", 		 	 	 
         "Statement": [
             {
                 "Effect": "Allow",
                 "Action": [
                     "s3:GetObject",
                     "s3:ListBucket"
                 ],
                 "Resource": [
                     "arn:aws:s3:{{region}}:{{account-id}}:accesspoint/{{access-point-name}}",
                     "arn:aws:s3:{{region}}:{{account-id}}:accesspoint/{{access-point-name}}/object/*"
                 ]
             }
         ]
     }
     ```

  1. Create the role and attach the policies.

     ```
     $ aws iam create-role \
         --role-name {{fsxn-tutorial-glue-role}} \
         --assume-role-policy-document file://glue-trust-policy.json
     
     aws iam attach-role-policy \
         --role-name {{fsxn-tutorial-glue-role}} \
         --policy-arn arn:aws:iam::aws:policy/service-role/AWSGlueServiceRole
     
     aws iam put-role-policy \
         --role-name {{fsxn-tutorial-glue-role}} \
         --policy-name s3-access-point-policy \
         --policy-document file://glue-s3-policy.json
     ```
+ IAM permissions to run Athena queries and access the AWS Glue Data Catalog.

**Important**  
The Amazon S3 access point must use an internet network origin. Athena accesses Amazon S3 from managed infrastructure, not from your VPC. access points with a VPC network origin deny requests from Athena.

## Step 1: Upload sample data to your FSx for ONTAP volume
<a name="tutorial-athena-upload-data"></a>

This tutorial uses the [NYC Taxi and Limousine Commission (TLC) Trip Record Data](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page), a publicly available dataset of taxi trips in New York City. The data is in Apache Parquet format, a columnar format that Athena can query efficiently.

Download one month of yellow taxi trip data and upload it to your FSx for ONTAP volume through the Amazon S3 access point.

```
$ curl -O https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2024-01.parquet
```

Upload the file to your FSx for ONTAP volume using the access point alias. Replace `{{my-ap-alias-ext-s3alias}}` with your access point alias.

```
$ aws s3 cp yellow_tripdata_2024-01.parquet \
    s3://{{my-ap-alias-ext-s3alias}}/taxi-data/yellow_tripdata_2024-01.parquet
```

Verify the file is accessible through the access point.

```
$ aws s3 ls s3://{{my-ap-alias-ext-s3alias}}/taxi-data/
2024-01-23 02:18:13   49961641 yellow_tripdata_2024-01.parquet
```

## Step 2: Create a database in the AWS Glue Data Catalog
<a name="tutorial-athena-create-database"></a>

Create a database in the AWS Glue Data Catalog to hold the table metadata. You can create the database using the AWS Glue console, the Athena query editor, or the AWS CLI.

**AWS Glue console**

1. Open the AWS Glue console at [https://console.aws.amazon.com/glue/](https://console.aws.amazon.com/glue/).

1. In the navigation pane, under **Data Catalog**, choose **Databases**.

1. Choose **Add database**.

1. For **Name**, enter `{{fsxn_taxi_demo}}`.

1. Choose **Create database**.

**Athena query editor or AWS CLI**

```
$ aws athena start-query-execution \
    --query-string "CREATE DATABASE IF NOT EXISTS {{fsxn_taxi_demo}}" \
    --work-group {{primary}}
```

## Step 3: Register the data in the AWS Glue Data Catalog
<a name="tutorial-athena-register-data"></a>

You can register your data using either a AWS Glue crawler (recommended) or a manual `CREATE EXTERNAL TABLE` statement in Athena.

### Option A: Use a AWS Glue crawler (recommended)
<a name="tutorial-athena-glue-crawler"></a>

A AWS Glue crawler automatically discovers the schema of your data and creates a table in the AWS Glue Data Catalog. This is the recommended approach because the crawler infers the correct column types from the Parquet file metadata.

1. Create a crawler that points to the access point alias. Replace `{{my-ap-alias-ext-s3alias}}` with your access point alias and `{{my-glue-role-arn}}` with the ARN of your AWS Glue IAM role.

   ```
   $ aws glue create-crawler \
       --name {{fsxn-taxi-crawler}} \
       --role {{my-glue-role-arn}} \
       --database-name {{fsxn_taxi_demo}} \
       --targets '{"S3Targets": [{"Path": "s3://{{my-ap-alias-ext-s3alias}}/taxi-data/"}]}'
   ```

1. Run the crawler.

   ```
   $ aws glue start-crawler --name {{fsxn-taxi-crawler}}
   ```

1. Check the crawler status. The crawler typically completes in one to two minutes.

   ```
   $ aws glue get-crawler --name {{fsxn-taxi-crawler}} \
       --query "Crawler.{State:State,Status:LastCrawl.Status}"
   ```

   When the crawler finishes, the state is `READY` and the status is `SUCCEEDED`. The crawler creates a table named `taxi_data` (derived from the folder name) in the `fsxn_taxi_demo` database.

### Option B: Create a table manually in Athena
<a name="tutorial-athena-manual-ddl"></a>

If you already know the schema of your data, you can create the table directly in Athena using a `CREATE EXTERNAL TABLE` statement. Use the access point alias in the `LOCATION` clause.

```
CREATE EXTERNAL TABLE fsxn_taxi_demo.yellow_taxi_trips (
    VendorID bigint,
    tpep_pickup_datetime timestamp,
    tpep_dropoff_datetime timestamp,
    passenger_count bigint,
    trip_distance double,
    RatecodeID bigint,
    store_and_fwd_flag string,
    PULocationID bigint,
    DOLocationID bigint,
    payment_type bigint,
    fare_amount double,
    extra double,
    mta_tax double,
    tip_amount double,
    tolls_amount double,
    improvement_surcharge double,
    total_amount double,
    congestion_surcharge double,
    Airport_fee double
)
STORED AS PARQUET
LOCATION 's3://{{my-ap-alias-ext-s3alias}}/taxi-data/'
```

**Note**  
The column types must match the types in the Parquet file. For this dataset, fields like `passenger_count` and `VendorID` are stored as `bigint` (INT64) in the Parquet file, not `double`. If the types do not match, Athena returns a `HIVE_BAD_DATA` error. Using a AWS Glue crawler (Option A) avoids this issue because the crawler infers the correct types automatically.

## Step 4: Query your data
<a name="tutorial-athena-query-data"></a>

Open the Athena query editor or use the AWS CLI to run SQL queries against your FSx for ONTAP data. The following examples use the table created by the AWS Glue crawler (`taxi_data`). If you created the table manually, replace `taxi_data` with `yellow_taxi_trips`.

**Count total trips and calculate averages**

```
SELECT
    COUNT(*) AS total_trips,
    ROUND(AVG(trip_distance), 2) AS avg_distance_miles,
    ROUND(AVG(total_amount), 2) AS avg_total_usd,
    ROUND(AVG(passenger_count), 1) AS avg_passengers
FROM fsxn_taxi_demo.taxi_data
```

Example output:


| total\_trips | avg\_distance\_miles | avg\_total\_usd | avg\_passengers | 
| --- | --- | --- | --- | 
| 2964624 | 3.65 | 26.80 | 1.3 | 

**Find the busiest pickup hours**

```
SELECT
    HOUR(tpep_pickup_datetime) AS pickup_hour,
    COUNT(*) AS trip_count,
    ROUND(AVG(total_amount), 2) AS avg_fare
FROM fsxn_taxi_demo.taxi_data
GROUP BY HOUR(tpep_pickup_datetime)
ORDER BY trip_count DESC
LIMIT 5
```

**Find the highest-revenue pickup locations**

```
SELECT
    PULocationID AS pickup_location,
    COUNT(*) AS trip_count,
    ROUND(SUM(total_amount), 2) AS total_revenue
FROM fsxn_taxi_demo.taxi_data
GROUP BY PULocationID
ORDER BY total_revenue DESC
LIMIT 10
```

## Considerations
<a name="tutorial-athena-considerations"></a>
+ **Read-only access.** Athena reads data from your FSx for ONTAP volume through the access point. Athena query results are written to the Amazon S3 results bucket, not back to the FSx for ONTAP volume.
+ **Internet origin required.** Athena accesses Amazon S3 from managed infrastructure outside your VPC. The `aws:SourceVpc` and `aws:SourceVpce` condition keys are not available for Athena requests. You must use an internet-origin access point.
+ **File format.** Athena supports Parquet, ORC, JSON, CSV, and other formats. Columnar formats like Parquet and ORC provide the best query performance because Athena reads only the columns referenced in your query.
+ **File system user permissions.** The file system user associated with the access point must have read permission on the files being queried.
+ **AWS Glue Data Catalog table is reusable.** Once you register a table in the AWS Glue Data Catalog, it is available to other AWS analytics services that integrate with the AWS Glue Data Catalog, such as Amazon Redshift Spectrum, Amazon EMR, and AWS Glue ETL jobs.

## Clean up
<a name="tutorial-athena-clean-up"></a>

To avoid ongoing charges, delete the resources you created in this tutorial.

1. Drop the Athena tables and database.

   ```
   DROP TABLE IF EXISTS fsxn_taxi_demo.taxi_data;
   DROP TABLE IF EXISTS fsxn_taxi_demo.yellow_taxi_trips;
   DROP DATABASE IF EXISTS fsxn_taxi_demo CASCADE;
   ```

1. Delete the AWS Glue crawler.

   ```
   $ aws glue delete-crawler --name {{fsxn-taxi-crawler}}
   ```

1. Delete the sample data from your FSx for ONTAP volume.

   ```
   $ aws s3 rm s3://{{my-ap-alias-ext-s3alias}}/taxi-data/yellow_tripdata_2024-01.parquet
   ```