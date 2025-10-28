# CloudFront and edge function logging

Amazon CloudFront provides different kinds of logging. You can log the viewer requests that come to
your CloudFront distributions, or you can log the CloudFront service activity (API activity) in your
AWS account. You can also get logs from your CloudFront Functions and Lambda@Edge
functions.

## Logging requests

CloudFront provides the following ways to log the requests that come to your
distributions.

**Standard logs (access logs)**

CloudFront standard logs provide detailed records about every request that's
made to a distribution.
You
can use the logs for scenarios,
such
as security and access audits.

CloudFront standard logs are delivered to
the
delivery destination that you specify.

For more information, see
[Standard logging (access logs)](AccessLogs.md "AccessLogs.md").

**Real-time logs**

CloudFront real-time logs provide information about requests made to a
distribution, in real time (log records are delivered within seconds of
receiving the requests). You can choose the _sampling
rate_ for your real-time logs—that is, the percentage
of requests for which you want to receive real-time log records. You can
also choose the specific fields that you want to receive in the log
records.

CloudFront real-time logs are delivered to the data stream of your choice in
Amazon Kinesis Data Streams. CloudFront charges for real-time logs, in addition to the charges you
incur for using Kinesis Data Streams.

For more information, see [Use real-time logs](real-time-logs.md "real-time-logs.md").

## Logging edge functions

You can use Amazon CloudWatch Logs to get logs for your edge functions, both Lambda@Edge and
CloudFront Functions. You can access the logs using the CloudWatch console or the CloudWatch Logs API. For
more information, see [Edge function logs](edge-functions-logs.md "edge-functions-logs.md").

## Logging service activity

You can use AWS CloudTrail to log the CloudFront service activity (API activity) in your AWS
account. CloudTrail provides a record of API actions taken by a user, role, or AWS service
in CloudFront. Using the information collected by CloudTrail, you can determine the API request that
was made to CloudFront, the IP address from which the request was made, who made the request,
when it was made, and additional details.

For more information, see [Logging Amazon CloudFront API calls using AWS CloudTrail](logging_using_cloudtrail.md "logging_using_cloudtrail.md").

For more information about logging, see the following topics:

###### Topics

- [Standard logging (access logs)](AccessLogs.md "AccessLogs.md")
- [Use real-time logs](real-time-logs.md "real-time-logs.md")
- [Edge function logs](edge-functions-logs.md "edge-functions-logs.md")
- [Logging Amazon CloudFront API calls using AWS CloudTrail](logging_using_cloudtrail.md "logging_using_cloudtrail.md")
