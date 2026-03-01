# Logging requests with server access logging

Server access logging provides detailed records for the requests that are made to a bucket.
Server access logs are useful for many applications. For example, access log information can be
useful in security and access audits. This information can also help you learn about your
customer base and understand your Amazon S3 bill.

###### Note

Server access logs don't record information about wrong-Region redirect errors for Regions
that launched after March 20, 2019. Wrong-Region redirect errors occur when a request for an
object or bucket is made outside the Region in which the bucket exists.

## How do I enable log delivery?

To enable log delivery, perform the following basic steps. For details, see [Enabling Amazon S3 server access logging](enable-server-access-logging.md "enable-server-access-logging.md").

1. **Provide the name of the destination bucket** (also
   known as a _target bucket_). This bucket is where you
   want Amazon S3 to save the access logs as objects. Both the source and destination buckets must
   be in the same
   AWS Region
   and owned by the same account. The destination bucket must not have an
   S3 Object Lock default retention period configuration. The destination bucket must also
   not have Requester Pays enabled.

You can have logs delivered to any bucket
that
you own that is in the same Region as the source bucket, including the
source bucket itself. But for simpler log management, we recommend that you save access
logs in a different bucket.

When your source bucket and destination bucket are the same bucket, additional logs
are created for the logs that are written to the bucket, which creates an infinite loop of
logs. We do not recommend doing this because it could result in a small increase in your
storage billing. In addition, the extra logs about logs might make it harder to find the
log that you are looking for.

If you choose to save access logs in the source bucket, we recommend that you specify
a destination prefix (also known as a _target prefix_)
for all log object keys. When you specify a prefix, all the log object names begin with a
common string, which makes the log objects easier to identify. 2. **(Optional) Assign a destination prefix to all Amazon S3 log object
keys.** The destination prefix (also known as a _target
prefix_) makes it simpler for you to locate the log objects. For example, if
you specify the prefix value `logs/`, each log object that Amazon S3 creates begins
with the `logs/` prefix in its key, for example:

```
logs/2013-11-01-21-32-16-E568B2907131C0C0
```

If you specify the prefix value `logs`, the log object appears as
follows:

```
logs2013-11-01-21-32-16-E568B2907131C0C0
```

[Prefixes](../../../general/latest/gr/glos-chap.md#keyprefix "../../../general/latest/gr/glos-chap.md#keyprefix") are also useful to distinguish between source buckets when multiple
buckets log to the same destination bucket.

This prefix can also help when you delete the logs. For example, you can set a
lifecycle configuration rule for Amazon S3 to delete objects with a specific prefix. For more
information, see [Deleting Amazon S3 log files](deleting-log-files-lifecycle.md "deleting-log-files-lifecycle.md"). 3. **(Optional) Set permissions so that
others can access the generated logs.** By default, only the bucket owner
always has full access to the log objects. If your destination bucket uses the Bucket
owner enforced setting for S3 Object Ownership to disable access control lists (ACLs),
you can't grant permissions in destination grants (also known as _target grants_) that use ACLs. However, you can update your bucket policy for
the destination bucket to grant access to others. For more information, see [Identity and Access Management for Amazon S3](security-iam.md "security-iam.md") and [Permissions for log delivery](enable-server-access-logging.md#grant-log-delivery-permissions-general "enable-server-access-logging.md#grant-log-delivery-permissions-general"). 4. **(Optional) Set a log object key format for the log
files.** You have two options for the log object key format (also known as the
_target object key format_):

    * **Non-date-based partitioning** – This is the
     original log object key format. If you choose this format, the log file key format
     appears as follows:



    ```
    [DestinationPrefix][YYYY]-[MM]-[DD]-[hh]-[mm]-[ss]-[UniqueString]
    ```

    For example, if you specify `logs/` as the prefix, your log objects are
     named like this:



    ```
    logs/2013-11-01-21-32-16-E568B2907131C0C0
    ```
    * **Date-based partitioning** – If you choose
     date-based partitioning, you can choose the event time or delivery time for the log
     file as the date source used in the log format. This format makes it easier to query the logs.


    If you choose date-based partitioning, the log file key format appears as follows:



    ```
    [DestinationPrefix][SourceAccountId]/[SourceRegion]/[SourceBucket]/[YYYY]/[MM]/[DD]/[YYYY]-[MM]-[DD]-[hh]-[mm]-[ss]-[UniqueString]
    ```

    For example, if you specify `logs/` as the target prefix, your log
     objects are named like this:



    ```
    logs/123456789012/us-west-2/`amzn-s3-demo-source-bucket`/2023/03/01/2023-03-01-21-32-16-E568B2907131C0C0
    ```

    For delivery time delivery, the time in the log file names corresponds to the
     delivery time for the log files.


    For event time delivery, the year, month, and day correspond to the day on which
     the event occurred, and the hour, minutes and seconds are set to `00` in
     the key. The logs delivered in these log files are for a specific day only.

If you're configuring your logs through the AWS Command Line Interface (AWS CLI), AWS SDKs, or Amazon S3
REST API, use `TargetObjectKeyFormat` to specify the log object key format. To
specify non-date-based partitioning, use `SimplePrefix`. To specify data-based
partitioning, use `PartitionedPrefix`. If you use
`PartitionedPrefix`, use `PartitionDateSource` to specify either
`EventTime` or `DeliveryTime`.

For `SimplePrefix`, the log file key format appears as follows:

```
[TargetPrefix][YYYY]-[MM]-[DD]-[hh]-[mm]-[ss]-[UniqueString]
```

For `PartitionedPrefix` with event time or delivery time, the log file key
format appears as follows:

```
[TargetPrefix][SourceAccountId]/[SourceRegion]/[SourceBucket]/[YYYY]/[MM]/[DD]/[YYYY]-[MM]-[DD]-[hh]-[mm]-[ss]-[UniqueString]
```

## Log object key format

Amazon S3 uses the following object key formats for the log objects that it uploads in the
destination bucket:

- **Non-date-based partitioning** – This is the
  original log object key format. If you choose this format, the log file key format appears
  as follows:

```
[DestinationPrefix][YYYY]-[MM]-[DD]-[hh]-[mm]-[ss]-[UniqueString]
```

- **Date-based partitioning** – If you choose
  date-based partitioning, you can choose the event time or delivery time for the log file
  as the date source used in the log format. This format makes it easier to query the
  logs.

If you choose date-based partitioning, the log file key format appears as follows:

```
[DestinationPrefix][SourceAccountId]/[SourceRegion]/[SourceBucket]/[YYYY]/[MM]/[DD]/[YYYY]-[MM]-[DD]-[hh]-[mm]-[ss]-[UniqueString]
```

In the log object key, `YYYY`, `MM`, `DD`,
`hh`, `mm`, and `ss` are the digits of the year, month,
day, hour, minute, and seconds (respectively). These dates and times are in Coordinated
Universal Time (UTC).

A log file delivered at a specific time can contain records written at any point before
that time. There is no way to know whether all log records for a certain time interval have
been delivered or not.

The `UniqueString` component of the key is there to prevent overwriting of
files. It has no meaning, and log processing software should ignore it.

## How are logs delivered?

Amazon S3 periodically collects access log records, consolidates the records in log files, and
then uploads log files to your destination bucket as log objects. If you enable logging on
multiple source buckets that identify the same destination bucket, the destination bucket will
have access logs for all those source buckets. However, each log object reports access log
records for a specific source bucket.

Amazon S3 uses a special log delivery account to write server access logs. These writes are
subject to the usual access control restrictions. We recommend that you update the bucket
policy on the destination bucket to grant access to the logging service principal
(`logging.s3.amazonaws.com`) for access log delivery. You can also grant access
for access log delivery to the S3 log delivery group through your bucket access control list
(ACL). However, granting access to the S3 log delivery group by using your bucket ACL is not
recommended.

When you enable server access logging and grant access for access log delivery through
your destination bucket policy, you must update the policy to allow `s3:PutObject`
access for the logging service principal. If you use the Amazon S3 console to enable server access
logging, the console automatically updates the destination bucket policy to grant these
permissions to the logging service principal. For more information about granting permissions
for server access log delivery, see [Permissions for log delivery](enable-server-access-logging.md#grant-log-delivery-permissions-general "enable-server-access-logging.md#grant-log-delivery-permissions-general").

###### Note

S3 does not support delivery of CloudTrail logs or server access logs to the requester or the
bucket owner for VPC endpoint requests when the VPC endpoint policy denies them or for
requests that fail before the VPC policy is evaluated.

###### Bucket owner enforced setting for S3 Object Ownership

If the destination bucket uses the Bucket owner enforced setting for Object Ownership,
ACLs are disabled and no longer affect permissions. You must update the bucket policy on the
destination bucket to grant access to the logging service principal. For more information
about Object Ownership, see [Grant access to the S3 log delivery group for server access logging](object-ownership-migrating-acls-prerequisites.md#object-ownership-server-access-logs "object-ownership-migrating-acls-prerequisites.md#object-ownership-server-access-logs").

## Best-effort server log delivery

Server access log records are delivered on a best-effort basis. Most requests for a bucket
that is properly configured for logging result in a delivered log record. Most log records are
delivered within a few hours of the time that they are recorded, but they can be delivered
more frequently.

The completeness and timeliness of server logging is not guaranteed. The log record for a
particular request might be delivered long after the request was actually processed, or
_it might not be delivered at all_. It is possible that you might even
see a duplication of a log record. The purpose of server logs is to give you an idea of the
nature of traffic against your bucket. Although log records are rarely lost or duplicated, be
aware that server logging is not meant to be a complete accounting of all requests.

Because of the best-effort nature of server logging, your usage reports might include one
or more access requests that do not appear in a delivered server log. You can find these usage
reports under **Cost & usage reports** in the
AWS Billing and Cost Management console.

## Bucket logging status changes take effect over time

Changes to the logging status of a bucket take time to actually affect the delivery of log
files. For example, if you enable logging for a bucket, some requests made in the following
hour might be logged, and others might not. Suppose that you change the destination bucket for
logging from bucket A to bucket B. For the next hour, some logs might continue to be delivered
to bucket A, whereas others might be delivered to the new destination bucket B. In all cases,
the new settings eventually take effect without any further action on your part.

For more information about logging and log files, see the following sections:

###### Topics

- [Enabling Amazon S3 server access logging](enable-server-access-logging.md "enable-server-access-logging.md")
- [Amazon S3 server access log format](LogFormat.md "LogFormat.md")
- [Deleting Amazon S3 log files](deleting-log-files-lifecycle.md "deleting-log-files-lifecycle.md")
- [Using Amazon S3 server access logs to identify requests](using-s3-access-logs-to-identify-requests.md "using-s3-access-logs-to-identify-requests.md")
- [Troubleshoot server access logging](troubleshooting-server-access-logging.md "troubleshooting-server-access-logging.md")
