# Track object storage bucket requests with

access logs

Access logging provides detailed records for the requests that are made to a bucket in the
Amazon Lightsail object storage service. This information can include the request type, the
resources that are specified in the request, and the time and date that the request was
processed. Access logs are useful for many applications. For example, access log information can
be useful in security and access audits. It can also help you learn about your customer
base.

**Contents**

- [What do I need to enable log
  delivery](#access-log-delivery "#access-log-delivery")
- [Log object key format](#log-object-key-format "#log-object-key-format")
- [How are logs
  delivered?](#how-are-logs-delivered "#how-are-logs-delivered")
- [Best effort access log
  delivery](#best-effort-access-log-delivery "#best-effort-access-log-delivery")
- [Bucket logging status
  changes take effect over time](#bucket-logging-status-changes "#bucket-logging-status-changes")

## What do I need to enable log delivery?

Consider the following before enabling log delivery. For details, see [Enable bucket access
logging](amazon-lightsail-enabling-bucket-access-logs.md "amazon-lightsail-enabling-bucket-access-logs.md").

1. **Identify the target bucket for the logs.** This bucket
   is where you want Lightsail to save the access logs as objects. Both the source and
   target buckets must be in the same AWS Region and owned by the same account.

You can have logs delivered to any bucket that you own that is in the same Region as
the source bucket, including the source bucket itself. But for simpler log management, we
recommend that you save access logs in a different bucket.

When your source bucket and target bucket are the same bucket, additional logs are
created for the logs that are written to the bucket. This might not be ideal because it
could result in a small increase in your storage consumption. In addition, the extra logs
about logs might make it harder to find the log that you are looking for. If you choose to
save access logs in the source bucket, we recommend that you specify a prefix for the log
object keys so that the object names begin with a common string and the log objects are
easier to identify. Key prefixes are also useful to distinguish between source buckets
when multiple buckets log to the same target bucket. 2. **(Optional) Identify a prefix for the log object keys.**
The prefix makes it simpler for you to locate the log objects. For example, if you specify
the prefix value `logs/`, each log object that Lightsail creates begins with
the `logs/` prefix in its key. The trailing slash `/` is required to
denote the end of the prefix. Following is an example of a log object key with the
`logs/` prefix:

```
logs/2021-11-31-21-32-16-E568B2907131C0C0
```

## Log object key format

Lightsail uses the following object key format for the log objects it uploads in the
target bucket:

```
TargetPrefix/YYYY-mm-DD-HH-MM-SS-UniqueString
```

In the key, `YYYY`, `mm`, `DD`, `HH`,
`MM`, and `SS` are the digits of the year, month, day, hour, minute,
and seconds (respectively) when the log file was delivered. These dates and times are in
Coordinated Universal Time (UTC).

A log file delivered at a specific time can contain records written at any point before
that time. There is no way to know whether all log records for a certain time interval have
been delivered or not.

The `UniqueString` component of the key is there to prevent overwriting of
files. It has no meaning, and log processing software should ignore it.

## How are logs delivered?

Lightsail periodically collects access log records, consolidates the records in log
files, and then uploads log files to your target bucket as log objects. If you enable logging
on multiple source buckets that deliver to the same target bucket, the target bucket will have
access logs for all those source buckets. However, each log object reports access log records
for a specific source bucket.

## Best effort access log delivery

Access log records are delivered on a best effort basis. Most requests for a bucket that
is properly configured for logging result in a delivered log record. Most log records are
delivered within a few hours of the time that they are recorded, but they can be delivered
more frequently.

The completeness and timeliness of access logging is not guaranteed. The log record for a
particular request might be delivered long after the request was actually processed, or it
might not be delivered at all. The purpose of access logs is to give you an idea of the nature
of traffic against your bucket. It is rare to lose log records, but access logging is not
meant to be a complete accounting of all requests.

## Bucket logging status changes take effect over

time

Changes to the logging status of a bucket take time to actually affect the delivery of log
files. For example, if you enable logging for a bucket, some requests made in the following
hour might be logged, while others might not. If you change the target bucket for logging from
bucket A to bucket B, some logs for the next hour might continue to be delivered to bucket A,
while others might be delivered to the new target bucket B. In all cases, the new settings
eventually take effect without any further action on your part.

###### Topics

- [Access log format](amazon-lightsail-bucket-access-log-format.md "amazon-lightsail-bucket-access-log-format.md")
- [Manage access
  logs](amazon-lightsail-enabling-bucket-access-logs.md "amazon-lightsail-enabling-bucket-access-logs.md")
- [Use access
  logs](amazon-lightsail-using-bucket-access-logs.md "amazon-lightsail-using-bucket-access-logs.md")
