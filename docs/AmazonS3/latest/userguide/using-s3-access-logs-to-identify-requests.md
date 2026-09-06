

# Using Amazon S3 server access logs to identify requests
<a name="using-s3-access-logs-to-identify-requests"></a>

You can identify Amazon S3 requests by using Amazon S3 server access logs.

**Note**  
To identify Amazon S3 requests, we recommend that you use AWS CloudTrail data events instead of Amazon S3 server access logs. CloudTrail data events are easier to set up and contain more information. For more information, see [Identifying Amazon S3 requests using CloudTrail](cloudtrail-request-identification.md).
Depending on how many access requests you get, analyzing your logs might require more resources or time than using CloudTrail data events.

**Topics**
+ [Querying access logs for requests by using Amazon Athena](#querying-s3-access-logs-for-requests)
+ [Identifying Signature Version 2 requests](#using-s3-access-logs-to-identify-sigv2-requests)
+ [Identifying object access requests](#using-s3-access-logs-to-identify-objects-access)

## Querying access logs for requests by using Amazon Athena
<a name="querying-s3-access-logs-for-requests"></a>

You can identify Amazon S3 requests with Amazon S3 access logs by using Amazon Athena. 

Amazon S3 stores server access logs as objects in an S3 bucket. It is often easier to use a tool that can analyze the logs in Amazon S3. Athena supports analysis of S3 objects and can be used to query Amazon S3 access logs.

**Example**  
The following example shows how you can query Amazon S3 server access logs in Amazon Athena. Replace the `{{user input placeholders}}` used in the following examples with your own information.  
To specify an Amazon S3 location in an Athena query, you must provide an S3 URI for the bucket where your logs are delivered to. This URI must include the bucket name and prefix in the following format: `s3://{{{{amzn-s3-demo-bucket1}}-logs/prefix}}/` 

1. Open the Athena console at [https://console.aws.amazon.com/athena/](https://console.aws.amazon.com/athena/home).

1. In the Query Editor, run a command similar to the following. Replace `{{s3_access_logs_db}}` with the name that you want to give to your database. 

   ```
   CREATE DATABASE {{s3_access_logs_db}}
   ```
**Note**  
It's a best practice to create the database in the same AWS Region as your S3 bucket. 

1. In the Query Editor, run a command similar to the following to create a table schema in the database that you created in step 2. Replace `{{s3_access_logs_db.mybucket_logs}}` with the name that you want to give to your table. The `STRING` and `BIGINT` data type values are the access log properties. You can query these properties in Athena. For `LOCATION`, enter the S3 bucket and prefix path as noted earlier.

------
#### [ Date-based partitioning ]

   ```
   CREATE EXTERNAL TABLE {{s3_access_logs_db.mybucket_logs}}( 
    `bucketowner` STRING, 
    `bucket_name` STRING, 
    `requestdatetime` STRING, 
    `remoteip` STRING, 
    `requester` STRING, 
    `requestid` STRING, 
    `operation` STRING, 
    `key` STRING, 
    `request_uri` STRING, 
    `httpstatus` STRING, 
    `errorcode` STRING, 
    `bytessent` BIGINT, 
    `objectsize` BIGINT, 
    `totaltime` STRING, 
    `turnaroundtime` STRING, 
    `referrer` STRING, 
    `useragent` STRING, 
    `versionid` STRING, 
    `hostid` STRING, 
    `sigv` STRING, 
    `ciphersuite` STRING, 
    `authtype` STRING, 
    `endpoint` STRING, 
    `tlsversion` STRING,
    `accesspointarn` STRING,
    `aclrequired` STRING,
    `sourceregion` STRING)
    PARTITIONED BY (
      `timestamp` string)
   ROW FORMAT SERDE 
    'org.apache.hadoop.hive.serde2.RegexSerDe' 
   WITH SERDEPROPERTIES ( 
    'input.regex'='([^ ]*) ([^ ]*) \\[(.*?)\\] ([^ ]*) ([^ ]*) ([^ ]*) ([^ ]*) ([^ ]*) (\"[^\"]*\"|-) (-|[0-9]*) ([^ ]*) ([^ ]*) ([^ ]*) ([^ ]*) ([^ ]*) ([^ ]*) (\"[^\"]*\"|-) ([^ ]*)(?: ([^ ]*) ([^ ]*) ([^ ]*) ([^ ]*) ([^ ]*) ([^ ]*) ([^ ]*) ([^ ]*) ([^ ]*))?.*$') 
   STORED AS INPUTFORMAT 
    'org.apache.hadoop.mapred.TextInputFormat' 
   OUTPUTFORMAT 
    'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
   LOCATION
    's3://{{bucket-name/prefix-name/account-id/region/source-bucket-name/}}'
    TBLPROPERTIES (
     'projection.enabled'='true', 
     'projection.timestamp.format'='yyyy/MM/dd', 
     'projection.timestamp.interval'='1', 
     'projection.timestamp.interval.unit'='DAYS', 
     'projection.timestamp.range'='2024/01/01,NOW', 
     'projection.timestamp.type'='date', 
     'storage.location.template'='s3://{{bucket-name/prefix-name/account-id/region/source-bucket-name/}}${timestamp}')
   ```

------
#### [ Non-date-based partitioning ]

   ```
   CREATE EXTERNAL TABLE `{{s3_access_logs_db.mybucket_logs}}`(
     `bucketowner` STRING, 
     `bucket_name` STRING, 
     `requestdatetime` STRING, 
     `remoteip` STRING, 
     `requester` STRING, 
     `requestid` STRING, 
     `operation` STRING, 
     `key` STRING, 
     `request_uri` STRING, 
     `httpstatus` STRING, 
     `errorcode` STRING, 
     `bytessent` BIGINT, 
     `objectsize` BIGINT, 
     `totaltime` STRING, 
     `turnaroundtime` STRING, 
     `referrer` STRING, 
     `useragent` STRING, 
     `versionid` STRING, 
     `hostid` STRING, 
     `sigv` STRING, 
     `ciphersuite` STRING, 
     `authtype` STRING, 
     `endpoint` STRING, 
     `tlsversion` STRING,
     `accesspointarn` STRING,
     `aclrequired` STRING,
     `sourceregion` STRING)
   ROW FORMAT SERDE 
     'org.apache.hadoop.hive.serde2.RegexSerDe' 
   WITH SERDEPROPERTIES ( 
     'input.regex'='([^ ]*) ([^ ]*) \\[(.*?)\\] ([^ ]*) ([^ ]*) ([^ ]*) ([^ ]*) ([^ ]*) (\"[^\"]*\"|-) (-|[0-9]*) ([^ ]*) ([^ ]*) ([^ ]*) ([^ ]*) ([^ ]*) ([^ ]*) (\"[^\"]*\"|-) ([^ ]*)(?: ([^ ]*) ([^ ]*) ([^ ]*) ([^ ]*) ([^ ]*) ([^ ]*) ([^ ]*) ([^ ]*) ([^ ]*))?.*$') 
   STORED AS INPUTFORMAT 
     'org.apache.hadoop.mapred.TextInputFormat' 
   OUTPUTFORMAT 
     'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
   LOCATION
     's3://{{amzn-s3-demo-bucket1-logs/prefix/}}'
   ```

------

1. In the navigation pane, under **Database**, choose your database.

1. Under **Tables**, choose **Preview table** next to your table name.

   In the **Results** pane, you should see data from the server access logs, such as `bucketowner`, `bucket`, `requestdatetime`, and so on. This means that you successfully created the Athena table. You can now query the Amazon S3 server access logs.

**Example — Show who deleted an object and when (timestamp, IP address, and IAM user)**  

```
SELECT requestdatetime, remoteip, requester, key 
FROM {{s3_access_logs_db.mybucket_logs}} 
WHERE key = '{{images/picture.jpg}}' AND operation like '%DELETE%';
```

**Example — Show all operations that were performed by an IAM user**  

```
SELECT * 
FROM {{s3_access_logs_db.mybucket_logs}} 
WHERE requester='arn:aws:iam::{{123456789123}}:user/{{user_name}}';
```

**Example — Show all operations that were performed on an object in a specific time period**  

```
SELECT *
FROM {{s3_access_logs_db.mybucket_logs}}
WHERE Key='{{prefix/images/picture.jpg}}' 
AND parse_datetime(requestdatetime,'{{dd/MMM/yyyy:HH:mm:ss Z}}')
BETWEEN parse_datetime('{{2017-02-18:07:00:00}}','yyyy-MM-dd:HH:mm:ss')
AND parse_datetime('{{2017-02-18:08:00:00}}','yyyy-MM-dd:HH:mm:ss');
```

**Example — Show how much data was transferred to a specific IP address in a specific time period**  

```
SELECT coalesce(SUM(bytessent), 0) AS bytessenttotal
FROM {{s3_access_logs_db.mybucket_logs}}
WHERE remoteip='192.0.2.1'
AND parse_datetime(requestdatetime,'dd/MMM/yyyy:HH:mm:ss Z')
BETWEEN parse_datetime('{{2022-06-01}}','yyyy-MM-dd')
AND parse_datetime('{{2022-07-01}}','yyyy-MM-dd');
```

**Example — Find request IDs for HTTP 5xx errors in a specific time period**  

```
SELECT requestdatetime, key, httpstatus, errorcode, requestid, hostid 
FROM {{s3_access_logs_db.mybucket_logs}}
WHERE httpstatus like '5%' AND timestamp
BETWEEN '2024/01/29'
AND '2024/01/30'
```

## Identifying Signature Version 2 requests
<a name="using-s3-access-logs-to-identify-sigv2-requests"></a>

You can use server access logs to identify Signature Version 2 requests. For details on querying logs with Amazon Athena, see the Athena querying section under [Delivering logs to an Amazon S3 general purpose bucket](sal-gp-section.md).

## Identifying object access requests
<a name="using-s3-access-logs-to-identify-objects-access"></a>

You can use server access logs to identify object access patterns. For details on querying logs with Amazon Athena, see the Athena querying section under [Delivering logs to an Amazon S3 general purpose bucket](sal-gp-section.md).