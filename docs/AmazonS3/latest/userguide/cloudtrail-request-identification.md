# Identifying Amazon S3 requests using CloudTrail

In Amazon S3, you can identify requests using an AWS CloudTrail event log. AWS CloudTrail is the
preferred way of identifying Amazon S3 requests, but if you are using Amazon S3 server access
logs, see [Using Amazon S3 server access logs to identify requests](using-s3-access-logs-to-identify-requests.md "using-s3-access-logs-to-identify-requests.md").

###### Topics

- [Identifying requests made to Amazon S3 in a CloudTrail log](#identify-S3-requests-using-in-CTlog "#identify-S3-requests-using-in-CTlog")
- [Identifying Amazon S3 Signature Version 2 requests by using CloudTrail](#cloudtrail-identification-sigv2-requests "#cloudtrail-identification-sigv2-requests")
- [Identifying access to S3 objects by using CloudTrail](#cloudtrail-identification-object-access "#cloudtrail-identification-object-access")

## Identifying requests made to Amazon S3 in a CloudTrail log

After you set up CloudTrail to deliver events to a bucket, you should start to see
objects go to your destination bucket on the Amazon S3 console. These are formatted
as follows:

`s3://`amzn-s3-demo-bucket1`/AWSLogs/`111122223333`/CloudTrail/`Region`/`yyyy`/`mm`/`dd``

Events logged by CloudTrail are stored as compressed, gzipped JSON
objects in your S3 bucket. To efficiently find requests, you should use a
service like Amazon Athena to index and query the CloudTrail logs.

For more information about CloudTrail and Athena, see [Creating the table for AWS CloudTrail logs in Athena using partition
projection](../../../athena/latest/ug/cloudtrail-logs.md#create-cloudtrail-table-partition-projection "../../../athena/latest/ug/cloudtrail-logs.md#create-cloudtrail-table-partition-projection") in the _Amazon Athena User
Guide_.

## Identifying Amazon S3 Signature Version 2 requests by using CloudTrail

You can use a CloudTrail event log to identify which API signature version was used
to sign a request in Amazon S3. This capability is important because support for
Signature Version 2 will be turned off (deprecated). After that, Amazon S3 will no
longer accept requests that use Signature Version 2, and all requests must use
_Signature Version 4_ signing.

We _strongly_ recommend that you use CloudTrail to help determine
whether any of your workflows are using Signature Version 2 signing. Remediate
them by upgrading your libraries and code to use Signature Version 4 instead to
prevent any impact to your business.

For more information, see [Announcement: AWS CloudTrail for Amazon S3 adds new fields for enhanced security
auditing](https://forums.aws.amazon.com/ann.jspa?annID=6551 "https://forums.aws.amazon.com/ann.jspa?annID=6551") in AWS re:Post.

###### Note

CloudTrail events for Amazon S3 include the signature version in the request details
under the key name of '`additionalEventData`. To find the
signature version on requests made for objects in Amazon S3 such as
`GET`, `PUT`, and `DELETE` requests,
you must enable CloudTrail data events. (This feature is turned off by
default.)

AWS CloudTrail is the preferred method for identifying Signature Version 2 requests.
If you're using Amazon S3 server-access logs, see [Identifying Signature Version 2 requests by using Amazon S3 access logs](using-s3-access-logs-to-identify-requests.md#using-s3-access-logs-to-identify-sigv2-requests "using-s3-access-logs-to-identify-requests.md#using-s3-access-logs-to-identify-sigv2-requests").

###### Topics

- [Athena query examples for identifying Amazon S3 Signature Version 2 requests](#ct-examples-identify-sigv2-requests "#ct-examples-identify-sigv2-requests")
- [Partitioning Signature Version 2 data](#partitioning-sigv2-data "#partitioning-sigv2-data")

### Athena query examples for identifying Amazon S3 Signature Version 2 requests

###### Example— Select all Signature Version 2 events, and print only `EventTime`, `S3_Action`, `Request_Parameters`, `Region`, `SourceIP`, and `UserAgent`

In the following Athena query, replace
`s3_cloudtrail_events_db.cloudtrail_table`
with your Athena details, and increase or remove the limit as needed.

```

SELECT EventTime, EventName as S3_Action, requestParameters as Request_Parameters, awsregion as AWS_Region, sourceipaddress as Source_IP, useragent as User_Agent
FROM `s3_cloudtrail_events_db.cloudtrail_table`
WHERE eventsource='s3.amazonaws.com'
AND json_extract_scalar(additionalEventData, '$.SignatureVersion')='SigV2'
LIMIT 10;

```

###### Example— Select all requesters that are sending Signature Version 2 traffic

```

SELECT useridentity.arn, Count(requestid) as RequestCount
FROM `s3_cloudtrail_events_db.cloudtrail_table`
WHERE eventsource='s3.amazonaws.com'
    and json_extract_scalar(additionalEventData, '$.SignatureVersion')='SigV2'
Group by useridentity.arn

```

### Partitioning Signature Version 2 data

If you have a large amount of data to query, you can reduce the costs and
running time of Athena by creating a partitioned table.

To do this, create a new table with partitions as follows.

```

   CREATE EXTERNAL TABLE `s3_cloudtrail_events_db.cloudtrail_table`_partitioned(
        eventversion STRING,
        userIdentity STRUCT<
            type:STRING,
            principalid:STRING,
            arn:STRING,
            accountid:STRING,
            invokedby:STRING,
            accesskeyid:STRING,
            userName:STRING,
         sessioncontext:STRUCT<
                    attributes:STRUCT<
                    mfaauthenticated:STRING,
                    creationdate:STRING>,
                    sessionIssuer:STRUCT<
                    type:STRING,
                    principalId:STRING,
                    arn:STRING,
                    accountId:STRING,
                    userName:STRING>
                >
             >,
        eventTime STRING,
        eventSource STRING,
        eventName STRING,
        awsRegion STRING,
        sourceIpAddress STRING,
        userAgent STRING,
        errorCode STRING,
        errorMessage STRING,
        requestParameters STRING,
        responseElements STRING,
        additionalEventData STRING,
        requestId STRING,
        eventId STRING,
        resources ARRAY<STRUCT<ARN:STRING,accountId: STRING,type:STRING>>,
        eventType STRING,
        apiVersion STRING,
        readOnly STRING,
        recipientAccountId STRING,
        serviceEventDetails STRING,
        sharedEventID STRING,
        vpcEndpointId STRING
    )
    PARTITIONED BY (region string, year string, month string, day string)
    ROW FORMAT SERDE 'org.apache.hadoop.hive.ql.io.orc.OrcSerde'
    STORED AS INPUTFORMAT 'org.apache.hadoop.hive.ql.io.SymlinkTextInputFormat'
    OUTPUTFORMAT 'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
    LOCATION 's3://`amzn-s3-demo-bucket1`/AWSLogs/`111122223333`/';

```

Then, create the partitions individually. You can't get results from dates
that you haven't created.

```

ALTER TABLE `s3_cloudtrail_events_db.cloudtrail_table`_partitioned ADD
    PARTITION (region= 'us-east-1', year= '2019', month= '02', day= '19') LOCATION 's3://`amzn-s3-demo-bucket1`/AWSLogs/`111122223333`/CloudTrail/us-east-1/2019/02/19/'
    PARTITION (region= 'us-west-1', year= '2019', month= '02', day= '19') LOCATION 's3://`amzn-s3-demo-bucket1`/AWSLogs/`111122223333`/CloudTrail/us-west-1/2019/02/19/'
    PARTITION (region= 'us-west-2', year= '2019', month= '02', day= '19') LOCATION 's3://`amzn-s3-demo-bucket1`/AWSLogs/`111122223333`/CloudTrail/us-west-2/2019/02/19/'
    PARTITION (region= 'ap-southeast-1', year= '2019', month= '02', day= '19') LOCATION 's3://`amzn-s3-demo-bucket1`/AWSLogs/`111122223333`/CloudTrail/ap-southeast-1/2019/02/19/'
    PARTITION (region= 'ap-southeast-2', year= '2019', month= '02', day= '19') LOCATION 's3://`amzn-s3-demo-bucket1`/AWSLogs/`111122223333`/CloudTrail/ap-southeast-2/2019/02/19/'
    PARTITION (region= 'ap-northeast-1', year= '2019', month= '02', day= '19') LOCATION 's3://`amzn-s3-demo-bucket1`/AWSLogs/`111122223333`/CloudTrail/ap-northeast-1/2019/02/19/'
    PARTITION (region= 'eu-west-1', year= '2019', month= '02', day= '19') LOCATION 's3://`amzn-s3-demo-bucket1`/AWSLogs/`111122223333`/CloudTrail/eu-west-1/2019/02/19/'
    PARTITION (region= 'sa-east-1', year= '2019', month= '02', day= '19') LOCATION 's3://`amzn-s3-demo-bucket1`/AWSLogs/`111122223333`/CloudTrail/sa-east-1/2019/02/19/';

```

You can then make the request based on these partitions, and you don't
need to load the full bucket.

```

SELECT useridentity.arn,
Count(requestid) AS RequestCount
FROM `s3_cloudtrail_events_db.cloudtrail_table`_partitioned
WHERE eventsource='s3.amazonaws.com'
AND json_extract_scalar(additionalEventData, '$.SignatureVersion')='SigV2'
AND region='`us-east-1`'
AND year='2019'
AND month='02'
AND day='19'
Group by useridentity.arn

```

## Identifying access to S3 objects by using CloudTrail

You can use your AWS CloudTrail event logs to identify Amazon S3 object access requests
for data events such as `GetObject`, `DeleteObject`, and
`PutObject`, and discover additional information about those
requests.

###### Note

If you are logging data activity with AWS CloudTrail, the event record for an Amazon S3 `DeleteObjects` data event includes both the `DeleteObjects` event and a `DeleteObject` event for each object deleted as part of that operation. You can exclude the additional visibility about deleted objects from the event record. For more information, see [AWS CLI examples for filtering data events](../../../awscloudtrail/latest/userguide/filtering-data-events.md#filtering-data-events-deleteobjects "../../../awscloudtrail/latest/userguide/filtering-data-events.md#filtering-data-events-deleteobjects") in the _AWS CloudTrail User Guide._

The following example shows how to get all `PUT` object requests
for Amazon S3 from an AWS CloudTrail event log.

###### Topics

- [Athena query examples for identifying Amazon S3 object access requests](#ct-examples-identify-object-access-requests "#ct-examples-identify-object-access-requests")

### Athena query examples for identifying Amazon S3 object access requests

In the following Athena query examples, replace
`s3_cloudtrail_events_db.cloudtrail_table`
with your Athena details, and modify the date range as needed.

###### Example— Select all events that have `PUT` object access requests, and print only `EventTime`, `EventSource`, `SourceIP`, `UserAgent`, `BucketName`, `object`, and `UserARN`

```
SELECT
  eventTime,
  eventName,
  eventSource,
  sourceIpAddress,
  userAgent,
  json_extract_scalar(requestParameters, '$.bucketName') as bucketName,
  json_extract_scalar(requestParameters, '$.key') as object,
  userIdentity.arn as userArn
FROM
  `s3_cloudtrail_events_db.cloudtrail_table`
WHERE
  eventName = 'PutObject'
  AND eventTime BETWEEN '`2019-07-05T00:00:00Z`' and '`2019-07-06T00:00:00Z`'

```

###### Example— Select all events that have `GET` object access requests, and print only `EventTime`, `EventSource`, `SourceIP`, `UserAgent`, `BucketName`, `object`, and `UserARN`

```
SELECT
  eventTime,
  eventName,
  eventSource,
  sourceIpAddress,
  userAgent,
  json_extract_scalar(requestParameters, '$.bucketName') as bucketName,
  json_extract_scalar(requestParameters, '$.key') as object,
  userIdentity.arn as userArn
FROM
  `s3_cloudtrail_events_db.cloudtrail_table`
WHERE
  eventName = 'GetObject'
  AND eventTime BETWEEN '`2019-07-05T00:00:00Z`' and '`2019-07-06T00:00:00Z`'
```

###### Example— Select all anonymous requester events to a bucket in a certain period and print only `EventTime`, `EventName`, `EventSource`, `SourceIP`, `UserAgent`, `BucketName`, `UserARN`, and `AccountID`

```
SELECT
  eventTime,
  eventName,
  eventSource,
  sourceIpAddress,
  userAgent,
  json_extract_scalar(requestParameters, '$.bucketName') as bucketName,
  userIdentity.arn as userArn,
  userIdentity.accountId
FROM
  `s3_cloudtrail_events_db.cloudtrail_table`
WHERE
  userIdentity.accountId = 'anonymous'
  AND eventTime BETWEEN '`2019-07-05T00:00:00Z`' and '`2019-07-06T00:00:00Z`'
```

###### Example— Identify all requests that required an ACL for authorization

The following Amazon Athena query example shows how to identify all
requests to your S3 buckets that required an access control list (ACL)
for authorization. If the request required an ACL for authorization, the
`aclRequired` value in `additionalEventData`
is `Yes`. If no ACLs were required, `aclRequired`
is not present. You can use this information to migrate those ACL
permissions to the appropriate bucket policies. After you've created
these bucket policies, you can disable ACLs for these buckets. For more
information about disabling ACLs, see [Prerequisites for disabling ACLs](object-ownership-migrating-acls-prerequisites.md "object-ownership-migrating-acls-prerequisites.md").

```
SELECT
  eventTime,
  eventName,
  eventSource,
  sourceIpAddress,
  userAgent,
  userIdentity.arn as userArn,
  json_extract_scalar(requestParameters, '$.bucketName') as bucketName,
  json_extract_scalar(requestParameters, '$.key') as object,
  json_extract_scalar(additionalEventData, '$.aclRequired') as aclRequired
FROM
  `s3_cloudtrail_events_db.cloudtrail_table`
WHERE
  json_extract_scalar(additionalEventData, '$.aclRequired') = 'Yes'
  AND eventTime BETWEEN '2022-05-10T00:00:00Z' and '2022-08-10T00:00:00Z'
```

###### Note

- These query examples can also be useful for security
  monitoring. You can review the results for
  `PutObject` or `GetObject` calls from
  unexpected or unauthorized IP addresses or requesters and for
  identifying any anonymous requests to your buckets.
- This query only retrieves information from the time at which
  logging was enabled.

If you are using Amazon S3 server access logs, see [Identifying object access requests by using Amazon S3 access logs](using-s3-access-logs-to-identify-requests.md#using-s3-access-logs-to-identify-objects-access "using-s3-access-logs-to-identify-requests.md#using-s3-access-logs-to-identify-objects-access").
