

# Logging requests for S3 Tables using server access logging

Server access logging for S3 Tables provides detailed records for the requests that are made to a table bucket. When you enable server access logging on a table bucket, Amazon S3 generates a log record for every request that is made to that table bucket, and delivers the log files to a general purpose bucket that you specify. These logs can help you with security and access auditing, access analysis, and cost attribution.

Server access logging is configured at the table bucket level. By default, Amazon S3 doesn't collect server access logs for table buckets. When you enable logging on a table bucket, Amazon S3 logs requests for all namespaces and tables in that table bucket.

This topic describes server access logging for S3 Tables. If you want to enable server access logging for general purpose buckets instead, see [Logging requests with server access logging](ServerLogs.md).

## How server access logging works for S3 Tables
<a name="s3-tables-server-logs-how-it-works"></a>

You turn server access logging on or off at the table bucket level. To enable or update logging, you use the `PutTableBucketLogging` operation with a `tableBucketLoggingStatus` that contains a `loggingEnabled` element. The `loggingEnabled` element specifies the following values:
+ `targetBucket` – Required. The name of the destination general purpose bucket where Amazon S3 delivers the log files.
+ `targetPrefix` – Required. The key prefix that Amazon S3 uses for the delivered log objects, for example `logs/`. You can specify an empty prefix. Amazon S3 doesn't add a slash (`/`) after the prefix. For more information, see [Log delivery location and key format](#s3-tables-server-logs-key-format).
+ `targetObjectKeyFormat` – Required. Contains a `partitionedPrefix` element with a `partitionDateSource` value that controls the date that Amazon S3 uses to partition the delivered log objects. The value is either `EventTime` or `DeliveryTime`.

To view the current logging configuration for a table bucket, use the `GetTableBucketLogging` operation. After you enable logging, it might take a few hours before Amazon S3 begins delivering log files to the destination general purpose bucket.

**Note**  
The following limitations apply to server access logging for S3 Tables:  
Server access logging for S3 Tables is available in all AWS Regions.
Logging is configured at the table bucket level only. When you enable logging, all namespaces and tables in the table bucket are logged. There is no per-namespace or per-table setting.
Delivery to Amazon CloudWatch Logs is not supported. Amazon S3 delivers S3 Tables server access logs only to a general purpose bucket.
You can't enable server access logging on AWS managed tables.
Server access logging for S3 Tables doesn't support the `SimplePrefix` log object key format. For more information, see [SimplePrefix](https://docs.aws.amazon.com/AmazonS3/latest/API/API_SimplePrefix.html).
Server access logging for S3 Tables doesn't support ACLs.
Server access logging for S3 Tables doesn't log requests for table buckets that are made to the wrong Regional endpoint. S3 Tables only supports requests that are made to the correct Regional endpoint.

## Best-effort log delivery
<a name="s3-tables-server-logs-best-effort"></a>

S3 Tables server access log records are delivered on a best-effort basis. Most requests for a table bucket that is properly configured for logging result in a delivered log record. Most log records are delivered within a few hours of the time that they are recorded, but they can be delivered more frequently.

The completeness and timeliness of server logging is not guaranteed. The log record for a particular request might be delivered long after the request was actually processed, or *it might not be delivered at all*. You might even see a duplicate log record. The purpose of server logs is to give you an idea of the nature of traffic against your table bucket. Although log records are rarely lost or duplicated, be aware that server logging is not meant to be a complete accounting of all requests.

For guaranteed and more complete audit logging, use AWS CloudTrail. CloudTrail captures all API calls for S3 Tables as events. For more information, see [Logging with AWS CloudTrail for S3 Tables](s3-tables-logging.md).

## Logging status changes take effect over time
<a name="s3-tables-server-logs-consistency"></a>

Changes to the logging status of a table bucket take time to actually affect the delivery of log files. For example, if you enable logging for a table bucket, some requests made in the following hour might be logged, and others might not. Suppose that you change the destination bucket for logging from bucket A to bucket B. For the next hour, some logs might continue to be delivered to bucket A, whereas others might be delivered to the new destination bucket B. In all cases, the new settings eventually take effect without any further action on your part.

## Destination general purpose bucket requirements
<a name="s3-tables-server-logs-destination"></a>

Before you enable server access logging, confirm that the destination general purpose bucket meets the following requirements:
+ The destination general purpose bucket must be in the same AWS account and the same AWS Region as the source table bucket. Cross-account and cross-Region delivery are not supported.
+ The destination general purpose bucket must use Amazon S3 managed keys (SSE-S3) for default encryption. You can't use server-side encryption with AWS KMS keys (SSE-KMS) or dual-layer server-side encryption with AWS KMS keys (DSSE-KMS). If the destination general purpose bucket uses SSE-KMS or DSSE-KMS, Amazon S3 might deliver log objects that are encrypted with a key that you can't access.
+ The destination general purpose bucket must not have S3 Object Lock enabled.
+ The destination general purpose bucket must not have Requester Pays enabled.

For simpler log management, we recommend that you deliver logs to a general purpose bucket that you use only for server access logs.

## Permissions for server access logging
<a name="s3-tables-server-logs-permissions"></a>

Server access logging for S3 Tables requires two kinds of permissions: a bucket policy on the destination general purpose bucket that lets Amazon S3 deliver log files, and AWS Identity and Access Management permissions for the user or role that configures logging.

### Destination bucket policy
<a name="s3-tables-server-logs-destination-policy"></a>

Amazon S3 delivers log files by using the logging service principal (`logging.s3.amazonaws.com`). You must grant this service principal the `s3:PutObject` permission on the destination general purpose bucket. This uses the service principal model rather than the legacy log delivery access control list (ACL) group.

If you use the Amazon S3 console to enable server access logging, the console automatically updates the bucket policy on the destination general purpose bucket to grant this permission. If you enable logging with the AWS SDKs, the AWS Command Line Interface (AWS CLI), or the Amazon S3 REST API, you must add the bucket policy to the destination general purpose bucket yourself.

The following example bucket policy grants the `s3:PutObject` permission to the logging service principal. To use this bucket policy, replace the `{{user input placeholders}}` with your own information.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "S3TablesServerAccessLogsPolicy",
            "Effect": "Allow",
            "Principal": {
                "Service": "logging.s3.amazonaws.com"
            },
            "Action": "s3:PutObject",
            "Resource": "arn:aws:s3:::{{amzn-s3-demo-logging-bucket}}/{{logs}}/*",
            "Condition": {
                "ArnLike": {
                    "aws:SourceArn": "arn:aws:s3tables:{{us-east-1}}:{{111122223333}}:bucket/{{amzn-s3-demo-table-bucket}}"
                },
                "StringEquals": {
                    "aws:SourceAccount": "{{111122223333}}"
                }
            }
        }
    ]
}
```

**Note**  
If there are `Deny` statements in your bucket policy, make sure that they don't prevent Amazon S3 from delivering access logs.

### Permissions to configure logging
<a name="s3-tables-server-logs-iam"></a>

To configure server access logging, the user or role that makes the request must have permission to call the `s3tables:PutTableBucketLogging` and `s3tables:GetTableBucketLogging` actions on the table bucket. The following example AWS Identity and Access Management policy grants these permissions. To use this policy, replace the `{{user input placeholders}}` with your own information.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "ConfigureS3TablesServerAccessLogging",
            "Effect": "Allow",
            "Action": [
                "s3tables:PutTableBucketLogging",
                "s3tables:GetTableBucketLogging"
            ],
            "Resource": "arn:aws:s3tables:{{us-east-1}}:{{111122223333}}:bucket/{{amzn-s3-demo-table-bucket}}"
        }
    ]
}
```

## Enabling or updating server access logging
<a name="s3-tables-server-logs-enable"></a>

You can enable or update server access logging for a table bucket by using the Amazon S3 console, the AWS Command Line Interface (AWS CLI), the AWS SDKs, or the Amazon S3 REST API.

### Using the S3 console
<a name="s3-tables-server-logs-enable-console"></a>

1. Sign in to the AWS Management Console and open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/).

1. In the left navigation pane, choose **Table buckets**.

1. In the **Table buckets** list, choose the name of the table bucket that you want to enable server access logging for.

1. Choose **Properties**.

1. In the **Server access logging** section, choose **Edit**.

1. Under **Server access logging**, choose **Enable**.

1. Under **Destination bucket**, specify a general purpose bucket and an optional prefix. If you specify a prefix, we recommend including a forward slash (`/`) after the prefix to make it easier to find your logs.
**Note**  
Specifying a prefix with a slash (`/`) makes it simpler for you to locate the log objects. For example, if you specify the prefix value `logs/`, each log object that Amazon S3 creates begins with the `logs/` prefix in its key, as follows:  

   ```
   logs/2013-11-01-21-32-16-E568B2907131C0C0
   ```
If you specify the prefix value `logs` without a slash, the log object appears as follows:  

   ```
   logs2013-11-01-21-32-16-E568B2907131C0C0
   ```

1. Under **Source of date used in log object key format**, do one of the following:
   + Choose **S3 event time** so that the year, month, and day in the log object key are based on the time of the S3 event in the delivered file. This option corresponds to the `EventTime` value for `partitionDateSource` in the `partitionedPrefix` element of `targetObjectKeyFormat`, and is the default.
   + Choose **Log file delivery time** so that the year, month, and day in the log object key are based on when the log file was delivered to Amazon S3. This option corresponds to the `DeliveryTime` value for `partitionDateSource` in the `partitionedPrefix` element of `targetObjectKeyFormat`.

1. Choose **Save changes**.

   When you enable server access logging on a table bucket, the console enables logging on the source table bucket. The console also updates the bucket policy for the destination general purpose bucket to grant the `s3:PutObject` permission to the logging service principal (`logging.s3.amazonaws.com`). For more information about this bucket policy, see [Destination bucket policy](#s3-tables-server-logs-destination-policy).

   You can view the logs in the destination general purpose bucket. After you enable server access logging, it might take a few hours before the logs are delivered.

### Using the AWS CLI
<a name="s3-tables-server-logs-enable-cli"></a>

**Enable or update logging**

To enable or update server access logging, use the `put-table-bucket-logging` command. The following example enables logging on the table bucket `amzn-s3-demo-table-bucket`. It delivers logs to the general purpose bucket `amzn-s3-demo-logging-bucket` under the `logs/` prefix and partitions the log object keys by event time. To use this example, replace the `{{user input placeholders}}` with your own information.

```
aws s3tables put-table-bucket-logging \
    --table-bucket-arn arn:aws:s3tables:{{us-east-1}}:{{111122223333}}:bucket/{{amzn-s3-demo-table-bucket}} \
    --table-bucket-logging-status '{
        "loggingEnabled": {
            "targetBucket": "{{amzn-s3-demo-logging-bucket}}",
            "targetPrefix": "{{logs/}}",
            "targetObjectKeyFormat": {
                "partitionedPrefix": {
                    "partitionDateSource": "EventTime"
                }
            }
        }
    }'
```

To partition log object keys by the time that the log file was delivered, specify `DeliveryTime` for `partitionDateSource`. The `targetObjectKeyFormat` value is required.

**View the logging configuration**

To view the current logging configuration for a table bucket, use the `get-table-bucket-logging` command.

```
aws s3tables get-table-bucket-logging \
    --table-bucket-arn arn:aws:s3tables:{{us-east-1}}:{{111122223333}}:bucket/{{amzn-s3-demo-table-bucket}}
```

When logging is enabled, the output looks like the following:

```
{
    "tableBucketLoggingStatus": {
        "loggingEnabled": {
            "targetBucket": "amzn-s3-demo-logging-bucket",
            "targetPrefix": "logs/",
            "targetObjectKeyFormat": {
                "partitionedPrefix": {
                    "partitionDateSource": "EventTime"
                }
            }
        }
    }
}
```

When logging is disabled, the output contains an empty logging status:

```
{
    "tableBucketLoggingStatus": {}
}
```

**Disable logging**

To disable server access logging, use the `put-table-bucket-logging` command with an empty logging status.

```
aws s3tables put-table-bucket-logging \
    --table-bucket-arn arn:aws:s3tables:{{us-east-1}}:{{111122223333}}:bucket/{{amzn-s3-demo-table-bucket}} \
    --table-bucket-logging-status '{}'
```

### Using the AWS SDKs
<a name="s3-tables-server-logs-enable-sdk"></a>

The following example uses the AWS SDK for Python (Boto3) to enable server access logging on a table bucket, view the configuration, and then disable logging. Replace the `{{user input placeholders}}` with your own information.

```python
import boto3

client = boto3.client('s3tables')

table_bucket_arn = 'arn:aws:s3tables:us-east-1:111122223333:bucket/amzn-s3-demo-table-bucket'

# Enable or update server access logging.
client.put_table_bucket_logging(
    tableBucketARN=table_bucket_arn,
    tableBucketLoggingStatus={
        'loggingEnabled': {
            'targetBucket': 'amzn-s3-demo-logging-bucket',
            'targetPrefix': 'logs/',
            'targetObjectKeyFormat': {
                'partitionedPrefix': {
                    'partitionDateSource': 'EventTime'
                }
            }
        }
    }
)

# View the current logging configuration.
response = client.get_table_bucket_logging(tableBucketARN=table_bucket_arn)
print(response['tableBucketLoggingStatus'])

# Disable server access logging.
client.put_table_bucket_logging(
    tableBucketARN=table_bucket_arn,
    tableBucketLoggingStatus={}
)
```

### Using the REST API
<a name="s3-tables-server-logs-enable-rest"></a>

**Enable or update logging**

To enable or update logging, submit a `PutTableBucketLogging` request. The table bucket ARN is URL-encoded in the request path, and the request body contains the logging status. A successful request returns `204 No Content`.

```
PUT /buckets/arn%3Aaws%3As3tables%3Aus-east-1%3A111122223333%3Abucket%2F{{amzn-s3-demo-table-bucket}}/logging HTTP/1.1
Host: s3tables.us-east-1.amazonaws.com
Content-Type: application/json

{
    "tableBucketLoggingStatus": {
        "loggingEnabled": {
            "targetBucket": "amzn-s3-demo-logging-bucket",
            "targetPrefix": "logs/",
            "targetObjectKeyFormat": {
                "partitionedPrefix": {
                    "partitionDateSource": "EventTime"
                }
            }
        }
    }
}
```

**View the logging configuration**

To retrieve the current logging configuration, submit a `GetTableBucketLogging` request.

```
GET /buckets/arn%3Aaws%3As3tables%3Aus-east-1%3A111122223333%3Abucket%2F{{amzn-s3-demo-table-bucket}}/logging HTTP/1.1
Host: s3tables.us-east-1.amazonaws.com
```

**Disable logging**

To disable logging, submit a `PutTableBucketLogging` request with an empty logging status.

```
PUT /buckets/arn%3Aaws%3As3tables%3Aus-east-1%3A111122223333%3Abucket%2F{{amzn-s3-demo-table-bucket}}/logging HTTP/1.1
Host: s3tables.us-east-1.amazonaws.com
Content-Type: application/json

{
    "tableBucketLoggingStatus": {}
}
```

## Disabling server access logging
<a name="s3-tables-server-logs-disable"></a>

To disable server access logging, send a `PutTableBucketLogging` request with an empty logging status. There is no separate operation to delete the logging configuration. With the AWS CLI, run the `put-table-bucket-logging` command with `--table-bucket-logging-status '{}'`. With Boto3, call `put_table_bucket_logging` with `tableBucketLoggingStatus={}`.

```
aws s3tables put-table-bucket-logging \
    --table-bucket-arn arn:aws:s3tables:{{us-east-1}}:{{111122223333}}:bucket/{{amzn-s3-demo-table-bucket}} \
    --table-bucket-logging-status '{}'
```

To disable logging by using the Amazon S3 console, choose the table bucket, choose **Properties**, and in the **Server access logging** section choose **Edit**. Then choose **Disable**, and choose **Save changes**.

When you disable logging, Amazon S3 stops generating log records for the table bucket. Log files that were already delivered to the destination general purpose bucket are not affected.

## Log delivery location and key format
<a name="s3-tables-server-logs-key-format"></a>

Amazon S3 delivers log files to the destination general purpose bucket by using a key that identifies the source table bucket. Log objects use the following key format:

```
s3://{{targetBucket}}/{{targetPrefix}}{{accountId}}/{{region}}/{{tableBucketName}}/{{YYYY}}/{{MM}}/{{DD}}/{{YYYY}}-{{MM}}-{{DD}}-{{hh}}-{{mm}}-{{ss}}-{{UniqueString}}
```

The following example shows a delivered log object key:

```
s3://amzn-s3-demo-logging-bucket/logs/111122223333/us-east-1/amzn-s3-demo-table-bucket/2026/10/28/2026-10-28-00-00-00-4520D3E0684DC910
```

The key format uses the following parts:
+ `{{targetPrefix}}` – Amazon S3 appends the prefix exactly as you provide it and doesn't insert a slash (`/`) after it. A prefix of `logs` without a trailing slash produces a key that begins `logs111122223333/`. To keep log objects organized, end the prefix with a slash (`/`). If you leave the prefix empty, the key begins with the account ID.
+ `{{accountId}}` – The AWS account that owns the source table bucket.
+ `{{region}}` – The AWS Region of the source table bucket.
+ `{{tableBucketName}}` – The name of the source table bucket. All records for the table bucket, its namespaces, its tables, and data requests are delivered under this single folder. There are no per-table or per-namespace folders.
+ `{{YYYY}}/{{MM}}/{{DD}}/` – The date folders. S3 Tables server access logs are always date-partitioned.

The `partitionDateSource` value in the `partitionedPrefix` element of `targetObjectKeyFormat` controls how Amazon S3 chooses the date:
+ `EventTime` (default) – The date folders are based on the date of the request. The time in the file name is always `00-00-00`.
+ `DeliveryTime` – The date folders are based on the date that the log file was delivered. The time in the file name is the actual delivery time.

## Server access log format for S3 Tables
<a name="s3-tables-server-logs-format"></a>

Server access logs for S3 Tables are delivered in space-delimited text format. Each log record represents one request and contains 25 fields in the following order:

```
table_bucket_arn [request_time] table_arn namespace_name table_name key object_size remote_ip requester request_id operation http_status error_code bytes_sent total_time turnaround_time "referer" "user_agent" signature_version cipher_suite authentication_type host_header tls_version request_time_iso source_region
```

In a log record, the `request_time` field is enclosed in square brackets, and the `referer` and `user_agent` fields are enclosed in double quotation marks. A hyphen (`-`) indicates a field that doesn't apply to the request.

The following table describes each field.


| Field | Description | Example | 
| --- | --- | --- | 
| table\_bucket\_arn | The ARN of the table bucket that received the request. | arn:aws:s3tables:us-east-2:111122223333:bucket/amzn-s3-demo-table-bucket | 
| request\_time | The time that the request was received, enclosed in square brackets. | [28/Oct/2026:13:46:39 \+0000] | 
| table\_arn | The ARN of the table, or - for table bucket and namespace requests. | arn:aws:s3tables:us-east-2:111122223333:bucket/amzn-s3-demo-table-bucket/table/cdae79fb-03e3-49dc-92c7-10e279e37e8f | 
| namespace\_name | The namespace in the request, or -. | sal\_ns | 
| table\_name | The table name in the request, or -. | events | 
| key | The object key for data requests, or -. | metadata/00000-a3001105-metadata.json | 
| object\_size | The object size in bytes for data requests, or -. | 756 | 
| remote\_ip | The IP address of the requester. | 15.248.6.220 | 
| requester | The IAM identity of the requester. | arn:aws:sts::111122223333:assumed-role/Admin/example-session | 
| request\_id | The request ID. | 6TBZ2YZN2PGW74S8 | 
| operation | The operation that was performed. | S3Tables.GetTable | 
| http\_status | The HTTP status code of the response. | 200 | 
| error\_code | The error code, or - if there was no error. | NotFoundException | 
| bytes\_sent | The number of response bytes sent, or -. | 735 | 
| total\_time | The total time to serve the request, in milliseconds. | 49 | 
| turnaround\_time | The time that Amazon S3 spent processing the request, in milliseconds. | 49 | 
| referer | The value of the HTTP Referer header, enclosed in double quotation marks. | "https://analytics.example.com/" | 
| user\_agent | The value of the HTTP User-Agent header, enclosed in double quotation marks. | "aws-cli/2.34.34" | 
| signature\_version | The signature version that was used to authenticate the request. | SigV4 | 
| cipher\_suite | The TLS cipher suite that was used for the request. | TLS\_AES\_128\_GCM\_SHA256 | 
| authentication\_type | The authentication type: AuthHeader for an authorization header, or QueryString for a presigned URL. | AuthHeader | 
| host\_header | The endpoint that was used for the request. | s3tables.us-east-2.amazonaws.com | 
| tls\_version | The TLS version that was used for the request. | TLSv1.3 | 
| request\_time\_iso | The time that the request was received, in ISO 8601 format with milliseconds. | 2026-10-28T13:46:39.000Z | 
| source\_region | The AWS Region that the request came from, or -. | us-west-2 | 

**Note**  
The `operation` field is declared as `S3Tables.{{ActionName}}` for S3 Tables API requests and Iceberg REST catalog endpoint requests, or `REST.{{HTTP_method}}.{{resource_type}}` for requests to table storage. For Iceberg REST catalog endpoint requests, {{ActionName}} is the IAM action that the request is authorized as. For example, a `loadTable` request is logged as `S3Tables.GetTableMetadataLocation`.

The following example shows a log record for a `GetTable` request.

```
arn:aws:s3tables:us-east-2:111122223333:bucket/amzn-s3-demo-table-bucket [28/Oct/2026:13:46:35 +0000] arn:aws:s3tables:us-east-2:111122223333:bucket/amzn-s3-demo-table-bucket/table/cdae79fb-03e3-49dc-92c7-10e279e37e8f sal_ns events - - 15.248.6.88 arn:aws:sts::111122223333:assumed-role/Admin/example-session c4e215be-ad2b-4b55-a190-4225aada1885 S3Tables.GetTable 200 - 735 49 49 "-" "aws-cli/2.34.34" SigV4 TLS_AES_128_GCM_SHA256 AuthHeader s3tables.us-east-2.amazonaws.com TLSv1.3 2026-10-28T13:46:35.634Z us-west-2
```

## Managing log retention
<a name="s3-tables-server-logs-lifecycle"></a>

A destination general purpose bucket that receives server access logs can accumulate many log objects over time. You can use Amazon S3 Lifecycle configuration to set rules so that Amazon S3 automatically deletes log objects after a specified period. If you specified a prefix in your logging configuration, you can scope the lifecycle rule to that prefix. For example, if your log objects have the prefix `logs/`, you can create a lifecycle rule to delete all objects with that prefix after a specified number of days. For more information, see [Managing the lifecycle of objects](object-lifecycle-mgmt.md).

Keep the following behavior in mind when you manage log retention:
+ If you delete a table or a table bucket, the log files that were already delivered to the destination general purpose bucket persist. They are managed independently of the source table bucket.
+ If you delete the destination general purpose bucket, the logging configuration remains on the table bucket, but Amazon S3 silently drops log records until you recreate the destination general purpose bucket or update the logging configuration.

## Charges for server access logging
<a name="s3-tables-server-logs-billing"></a>

There is no additional S3 Tables charge for generating and delivering server access logs. You pay the standard Amazon S3 charges for the destination general purpose bucket, including storage of the delivered log files, requests, and data transfer for accessing the log files. You can delete the log files at any time. For current rates, see [Amazon S3 pricing](https://aws.amazon.com/s3/pricing/).

## Querying server access logs by using Amazon Athena
<a name="s3-tables-server-logs-athena"></a>

You can analyze S3 Tables server access logs by using Amazon Athena. The following example shows how to create a database and table in Athena, and then query the delivered log files. Replace the `{{user input placeholders}}` with your own information. For more information about using Athena with S3 Tables, see [Querying Amazon S3 tables with Athena](s3-tables-integrating-athena.md).

1. Open the Athena console at [https://console.aws.amazon.com/athena/](https://console.aws.amazon.com/athena/home).

1. In the query editor, run the following command to create a database. Replace `{{s3_tables_access_logs_db}}` with the name that you want to give to your database.

   ```sql
   CREATE DATABASE {{s3_tables_access_logs_db}}
   ```

1. Run the following command to create a table schema in the database. For `LOCATION`, enter the destination general purpose bucket, prefix, account ID, Region, and source table bucket name. Amazon S3 appends the prefix without inserting a slash, so there is no slash between `{{targetPrefix}}` and the account ID.

   ```sql
   CREATE EXTERNAL TABLE {{s3_tables_access_logs_db.s3_tables_logs}}(
     `table_bucket_arn` STRING,
     `request_time` STRING,
     `table_arn` STRING,
     `namespace_name` STRING,
     `table_name` STRING,
     `key` STRING,
     `object_size` BIGINT,
     `remote_ip` STRING,
     `requester` STRING,
     `request_id` STRING,
     `operation` STRING,
     `http_status` STRING,
     `error_code` STRING,
     `bytes_sent` BIGINT,
     `total_time` STRING,
     `turnaround_time` STRING,
     `referer` STRING,
     `user_agent` STRING,
     `signature_version` STRING,
     `cipher_suite` STRING,
     `authentication_type` STRING,
     `host_header` STRING,
     `tls_version` STRING,
     `request_time_iso` STRING,
     `source_region` STRING)
   PARTITIONED BY (
     `timestamp` string)
   ROW FORMAT SERDE
     'org.apache.hadoop.hive.serde2.RegexSerDe'
   WITH SERDEPROPERTIES (
     'input.regex'='([^ ]*) \\[(.*?)\\] ([^ ]*) ([^ ]*) ([^ ]*) ([^ ]*) ([^ ]*) ([^ ]*) ([^ ]*) ([^ ]*) ([^ ]*) ([^ ]*) ([^ ]*) ([^ ]*) ([^ ]*) ([^ ]*) (\"[^\"]*\"|-) (\"[^\"]*\"|-) ([^ ]*) ([^ ]*) ([^ ]*) ([^ ]*) ([^ ]*) ([^ ]*) ([^ ]*).*$')
   STORED AS INPUTFORMAT
     'org.apache.hadoop.mapred.TextInputFormat'
   OUTPUTFORMAT
     'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
   LOCATION
     's3://{{amzn-s3-demo-logging-bucket}}/{{logs/}}{{111122223333}}/{{us-east-1}}/{{amzn-s3-demo-table-bucket}}/'
   TBLPROPERTIES (
     'projection.enabled'='true',
     'projection.timestamp.format'='yyyy/MM/dd',
     'projection.timestamp.interval'='1',
     'projection.timestamp.interval.unit'='DAYS',
     'projection.timestamp.range'='{{2026/01/01}},NOW',
     'projection.timestamp.type'='date',
     'storage.location.template'='s3://{{amzn-s3-demo-logging-bucket}}/{{logs/}}{{111122223333}}/{{us-east-1}}/{{amzn-s3-demo-table-bucket}}/${timestamp}')
   ```

1. In the navigation pane, under **Database**, choose your database.

1. Under **Tables**, choose **Preview table** next to your table name. In the **Results** pane, you see data from the server access logs. You can now query the S3 Tables server access logs.