# CloudFront and edge function logging

Amazon CloudFront provides different kinds of logging. You can log the viewer requests that come to
your CloudFront distributions, or you can log the CloudFront service activity (API activity) in your
AWS account. You can also get logs from your CloudFront Functions and Lambda@Edge
functions.

## Logging requests

CloudFront provides the following ways to log the requests that come to your
distributions.

**Access logs (standard logs)**

CloudFront
access
logs provide detailed records about every request that's
made to a distribution. You can use the logs for scenarios, such as security
and access audits.

CloudFront
access
logs are delivered to the delivery destination that you specify.

Use access logs when you need:

- Historical analysis and reporting
- Security audits and compliance requirements
- Cost-effective long-term log retention

For more information, see [Access logs (standard logs)](AccessLogs.md "AccessLogs.md").

**Real-time access logs**

CloudFront
real-time access logs
are delivered within seconds of receiving the requests and
provide information about requests made to a
distribution
in real time.

You
can choose the _sampling rate_ for your
real-time access logs—that is, the percentage of requests for which you
want to receive real-time access log records. You can also choose the specific
fields that you want to receive in the log
records.
Real-time access logs are ideal for live monitoring for content delivery
performance.

CloudFront real-time access logs are delivered to the data stream of your choice in
Amazon Kinesis Data Streams. CloudFront charges for real-time access logs, in addition to the charges you
incur for using Kinesis Data Streams.

Use real-time access logs when you need:

- Real-time monitoring and alerts
- Live dashboards and operational insights

For more information, see [Use real-time access logs](real-time-logs.md "real-time-logs.md").

**Connection logs**

Connection logs provide detailed information about the connection
between the server and the client for mTLS enabled distributions.
Connection logs provide visibility into client certificate information,
reasons for mTLS authentication failures and whether a connection was
permitted or refused.

Like access logs (standard logs), connection logs are delivered to the delivery
destination that you specify.

###### Note

To enable connection logs, you must first [enable mTLS](mtls-authentication.md "mtls-authentication.md") for your
distribution.

Use connection logs when you need:

- Reasons for successful or unsuccessful connections during the TLS
  handshake
- Visibility into the client certificate information

For more information, see [Observability using connection logs](connection-logs.md "connection-logs.md").

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

- [Access logs (standard logs)](AccessLogs.md "AccessLogs.md")
- [Use real-time access logs](real-time-logs.md "real-time-logs.md")
- [Edge function logs](edge-functions-logs.md "edge-functions-logs.md")
- [Logging Amazon CloudFront API calls using AWS CloudTrail](logging_using_cloudtrail.md "logging_using_cloudtrail.md")
