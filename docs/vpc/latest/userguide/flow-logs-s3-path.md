# Flow log files

VPC Flow Logs collects data about the IP traffic going to and from your VPC into log records, aggregates those records into log files, and then publishes the log files to the Amazon S3 bucket at 5-minute intervals. Multiple files may be published and each log file may contain some or all of the flow log records for the IP traffic recorded in the previous 5 minutes.

In Amazon S3, the **Last modified** field for the flow log file
indicates the date and time at which the file was uploaded to the Amazon S3 bucket. This
is later than the timestamp in the file name, and differs by the amount of time
taken to upload the file to the Amazon S3 bucket.

###### Log file format

You can specify one of the following formats for the log files. Each file is
compressed into a single Gzip file.

- **Text** – Plain text. This is
  the default format.
- **Parquet** – Apache Parquet is a
  columnar data format. Queries on data in Parquet format are 10 to 100
  times faster compared to queries on data in plain text. Data in Parquet
  format with Gzip compression takes 20 percent less storage space than
  plain text with Gzip compression.

###### Note

If data in Parquet format with Gzip compression is less than 100 KB per aggregation period, storing data in Parquet format may take up more space than plain text with Gzip compression due to Parquet file memory requirements.

###### Log file options

You can optionally specify the following options.

- **Hive-compatible S3 prefixes** –
  Enable Hive-compatible prefixes instead of importing partitions into your
  Hive-compatible tools. Before you run queries, use the **MSCK REPAIR TABLE**
  command.
- **Hourly partitions** – If you have a
  large volume of logs and typically target queries to a specific hour, you
  can get faster results and save on query costs by partitioning logs on an
  hourly basis.

###### Log file S3 bucket structure

Log files are saved to the specified Amazon S3 bucket using a folder structure that is
based on the flow log's ID, Region, creation date, and destination options.

By default, the files are delivered to the following location.

```
`bucket-and-optional-prefix`/AWSLogs/`account_id`/vpcflowlogs/`region`/`year`/`month`/`day`/
```

If you enable Hive-compatible S3 prefixes, the files are delivered to the following location.

```
`bucket-and-optional-prefix`/AWSLogs/aws-account-id=`account_id`/aws-service=vpcflowlogs/aws-region=`region`/year=`year`/month=`month`/day=`day`/
```

If you enable hourly partitions, the files are delivered to the following location.

```
`bucket-and-optional-prefix`/AWSLogs/`account_id`/vpcflowlogs/`region`/`year`/`month`/`day`/`hour`/
```

If you enable Hive-compatible partitions and partition the flow log per hour,
the files are delivered to the following location.

```
`bucket-and-optional-prefix`/AWSLogs/aws-account-id=`account_id`/aws-service=vpcflowlogs/aws-region=`region`/year=`year`/month=`month`/day=`day`/hour=`hour`/
```

###### Log file names

The file name of a log file is based on the flow log ID, Region, and creation
date and time. File names use the following format.

```
`aws_account_id`_vpcflowlogs_`region`_`flow_log_id`_`YYYYMMDD`T`HHmm`Z_`hash`.log.gz
```

The following is an example of a log file for a flow log created by AWS
account 123456789012, for a resource in the us-east-1
Region, on June 20, 2018 at 16:20 UTC. The file
contains the flow log records with an end time between 16:20:00
and 16:24:59.

```
123456789012_vpcflowlogs_us-east-1_fl-1234abcd_20180620T1620Z_fe123456.log.gz
```
