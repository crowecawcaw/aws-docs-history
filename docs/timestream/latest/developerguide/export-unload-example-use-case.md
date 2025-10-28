For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Example use case for UNLOAD from

Timestream for LiveAnalytics

Assume you are monitoring user session metrics, traffic sources, and product purchases
of your e-commerce website. You are using Timestream for LiveAnalytics to derive real-time insights into user
behavior, product sales, and perform marketing analytics on traffic channels (organic
search, social media, direct traffic, paid campaigns and others) that drive customers to
the website.

###### Topics

- [Exporting the data without any
  partitions](#export-unload-example-sample-1 "#export-unload-example-sample-1")
- [Partitioning data by
  channel](#export-unload-example-sample-2 "#export-unload-example-sample-2")
- [Partitioning data by event](#export-unload-example-sample-3 "#export-unload-example-sample-3")
- [Partitioning data by both channel
  and event](#export-unload-example-sample-4 "#export-unload-example-sample-4")
- [Manifest and metadata
  files](#export-unload-example-manifest-metadata "#export-unload-example-manifest-metadata")
- [Using Glue crawlers to
  build Glue Data Catalog](#export-unload-example-using-glue-crawlers "#export-unload-example-using-glue-crawlers")

## Exporting the data without any

partitions

You want to export the last two days of your data in CSV format.

```
UNLOAD(SELECT user_id, ip_address, event, session_id, measure_name, time,
query, quantity, product_id, channel
FROM sample_clickstream.sample_shopping
WHERE time BETWEEN ago(2d) AND now())
TO 's3://`<bucket_name>/withoutpartition`'
WITH (  format='CSV',
compression='GZIP')
```

## Partitioning data by

channel

You want to export the last two days of data in CSV format but would like to have
the data from each traffic channel in a separate folder. To do this, you need to
partition the data using the `channel` column as shown in the
following.

```
UNLOAD(SELECT user_id, ip_address, event, session_id, measure_name, time,
query, quantity, product_id, channel
FROM sample_clickstream.sample_shopping
WHERE time BETWEEN ago(2d) AND now())
TO 's3://`<bucket_name>/partitionbychannel`/'
WITH (
partitioned_by = ARRAY ['channel'],
format='CSV',
compression='GZIP')
```

## Partitioning data by event

You want to export the last two days of data in CSV format but would like to have
the data for each event in a separate folder. To do this, you need to partition the
data using the `event` column as shown in the following.

```
UNLOAD(SELECT user_id, ip_address, channel, session_id, measure_name, time,
query, quantity, product_id, event
FROM sample_clickstream.sample_shopping
WHERE time BETWEEN ago(2d) AND now())
TO 's3://`<bucket_name>/partitionbyevent`/'
WITH (
partitioned_by = ARRAY ['event'],
format='CSV',
compression='GZIP')
```

## Partitioning data by both channel

and event

You want to export the last two days of data in CSV format but would like to have
the data for each channel and within channel store each event in a separate folder.
To do this, you need to partition the data using both `channel` and
`event` column as shown in the following.

```
UNLOAD(SELECT user_id, ip_address, session_id, measure_name, time,
query, quantity, product_id, channel,event
FROM sample_clickstream.sample_shopping
WHERE time BETWEEN ago(2d) AND now())
TO 's3://`<bucket_name>/partitionbychannelevent`/'
WITH (
partitioned_by = ARRAY ['channel','event'],
format='CSV',
compression='GZIP')
```

## Manifest and metadata

files

### Manifest file

The manifest file provides information on the list of files that are exported
with the UNLOAD execution. The manifest file is available in the provided S3
bucket with a file name:
`S3://bucket_name/<queryid>_<UUID>_manifest.json`.
The manifest file will contain the url of the files in the results folder, the
number of records and size of the respective files, and the query metadata
(which is total bytes and total rows exported to S3 for the query).

```
{
  "result_files": [
    {
        "url":"s3://my_timestream_unloads/ec2_metrics/AEDAGANLHLBH4OLISD3CVOZZRWPX5GV2XCXRBKCVD554N6GWPWWXBP7LSG74V2Q_1448466917_szCL4YgVYzGXj2lS.gz",
        "file_metadata":
            {
                "content_length_in_bytes": 32295,
                "row_count": 10
            }
    },
    {
        "url":"s3://my_timestream_unloads/ec2_metrics/AEDAGANLHLBH4OLISD3CVOZZRWPX5GV2XCXRBKCVD554N6GWPWWXBP7LSG74V2Q_1448466917_szCL4YgVYzGXj2lS.gz",
        "file_metadata":
            {
                "content_length_in_bytes": 62295,
                "row_count": 20
            }
    },
  ],
  "query_metadata":
    {
      "content_length_in_bytes": 94590,
      "total_row_count": 30,
      "result_format": "CSV",
      "result_version": "Amazon Timestream version 1.0.0"
    },
  "author": {
        "name": "Amazon Timestream",
        "manifest_file_version": "1.0"
  }
}
```

### Metadata

The metadata file provides additional information about the data set such as
column name, column type, and schema. The metadata file is available in the
provided S3 bucket with a file name:
S3://bucket_name/<queryid>\_<UUID>\_metadata.json

Following is an example of a metadata file.

```
{
    "ColumnInfo": [
        {
            "Name": "hostname",
            "Type": {
                "ScalarType": "VARCHAR"
            }
        },
        {
            "Name": "region",
            "Type": {
                "ScalarType": "VARCHAR"
            }
        },
        {
            "Name": "measure_name",
            "Type": {
                "ScalarType": "VARCHAR"
            }
        },
        {
            "Name": "cpu_utilization",
            "Type": {
                "TimeSeriesMeasureValueColumnInfo": {
                    "Type": {
                        "ScalarType": "DOUBLE"
                    }
                }
            }
        }
  ],
  "Author": {
        "Name": "Amazon Timestream",
        "MetadataFileVersion": "1.0"
  }
}
```

The column information shared in the metadata file has same structure as
`ColumnInfo` sent in Query API response for `SELECT`
queries.

## Using Glue crawlers to

build Glue Data Catalog

1. Login to your account with Admin credentials for the following
   validation.
2. Create a Crawler for Glue Database using the guidelines provided [here](../../../glue/latest/ug/tutorial-add-crawler.md "../../../glue/latest/ug/tutorial-add-crawler.md"). Please note that the S3 folder to be provided in the
   datasource should be the `UNLOAD` result folder such as
   `s3://my_timestream_unloads/results`.
3. Run the crawler following the guidelines [here](../../../glue/latest/ug/tutorial-add-crawler.md#tutorial-add-crawler-step2 "../../../glue/latest/ug/tutorial-add-crawler.md#tutorial-add-crawler-step2").
4. View the Glue table.
   - Go to **AWS Glue** →
     **Tables**.
   - You will see a new table created with table prefix provided while
     creating the crawler.
   - You can see the schema and partition information by clicking the
     table details view.

The following are other AWS services and open-source projects that use the AWS
Glue Data Catalog.

- **Amazon Athena** – For more
  information, see [Understanding tables, databases, and data catalogs](../../../athena/latest/ug/understanding-tables-databases-and-the-data-catalog.md "../../../athena/latest/ug/understanding-tables-databases-and-the-data-catalog.md") in the
  Amazon Athena User Guide.
- **Amazon Redshift Spectrum** – For
  more information, see [Querying external data
  using Amazon Redshift Spectrum](../../../redshift/latest/dg/c-using-spectrum.md "../../../redshift/latest/dg/c-using-spectrum.md") in the Amazon Redshift Database
  Developer Guide.
- **Amazon EMR** – For more information,
  see [Use
  resource-based policies for Amazon EMR access to AWS Glue Data
  Catalog](../../../emr/latest/ManagementGuide/emr-iam-roles-glue.md "../../../emr/latest/ManagementGuide/emr-iam-roles-glue.md") in the Amazon EMR Management Guide.
- **AWS Glue Data Catalog client for Apache Hive
  metastore** – For more information about this GitHub
  project, see [AWS Glue Data Catalog Client for Apache Hive Metastore](https://github.com/awslabs/aws-glue-data-catalog-client-for-apache-hive-metastore "https://github.com/awslabs/aws-glue-data-catalog-client-for-apache-hive-metastore").
