# Audit findings reports

If you set up CloudWatch Logs data protection audit policies to write audit reports to CloudWatch Logs, Amazon S3, or Firehose,
these findings reports are similar to the following example. CloudWatch Logs writes one findings report for each
log event that contains sensitive data.

```
{
    "auditTimestamp": "2023-01-23T21:11:20Z",
    "resourceArn": "arn:aws:logs:us-west-2:111122223333:log-group:/aws/lambda/MyLogGroup:*",
    "dataIdentifiers": [
        {
            "name": "EmailAddress",
            "count": 2,
            "detections": [
                {
                    "start": 13,
                    "end": 26
                },
{
                    "start": 30,
                    "end": 43
                }
            ]
        }
    ]
}
```

The fields in the report are as follows:

- The `resourceArn` field displays the log group where the sensitive data was found.
- The `dataIdentifiers` object displays information about the findings for one type
  of senssitive data that you are auditing.
- The `name` field identifies which type of sensitive data this section is reporting about.
- The `count` field displays the number of times this type of sensitive data
  appears in the log event.
- The `start` and `end` fields show where in the log event, by character count,
  each occurrence of the sensitive data appears.
  The previous example shows a report of finding two email addresses in one log event. The first email address
  starts at the 13th character of the log event and ends at the 26th character. The second email address
  runs from the 30th character to the 43rd character. Even though this log event has two email addresses,
  the value of the `LogEventsWithFindings` metric is incremented only by one, because that metric
  counts the number of log events that contain sensitive data, not the number of occurrences of sensitive data.

## Required key policy to send audit findings to an bucket protected by AWS KMS

You can protect the data in an Amazon S3 bucket by enabling either Server-Side Encryption with
Amazon S3-Managed Keys (SSE-S3) or Server-Side Encryption with KMS Keys (SSE-KMS). For more information,
see [Protecting data using server-side encryption](../../../AmazonS3/latest/userguide/serv-side-encryption.md "../../../AmazonS3/latest/userguide/serv-side-encryption.md")
in the Amazon S3 User Guide.

If you send audit findings to a bucket that is protected with SSE-S3, no additional configuration is required.
Amazon S3 handles the encryption key.

If you send audit findings to a bucket that is protected with SSE-KMS, you must update the key policy for
your KMS key so that the log delivery account can write to your S3 bucket. For more
information about the required key policy for use with SSE-KMS, see
[Amazon S3](AWS-logs-infrastructure-S3.md#AWS-logs-SSE-KMS-S3 "AWS-logs-infrastructure-S3.md#AWS-logs-SSE-KMS-S3")
in the Amazon CloudWatch Logs User Guide.
