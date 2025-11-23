# Health check logs

ELB provides health check logs that capture detailed information
about the health check status of your registered targets, including failure reasons when
health checks fail. Health check logs are supported for EC2 instances, IP address, and
Lambda function targets. Each log entry contains information such as the health check request
type or connection, timestamp, target address, target group ID, health status and reason code.
You can use these health check logs to analyze target health patterns, monitor health transitions,
and troubleshoot issues.

Health check logs are an optional feature that is disabled by default. After you enable health check logs
for your load balancer, ELB captures the logs and stores them as compressed files in the
Amazon S3 bucket that you specify. You can disable health check logs at any time.

You are charged storage costs for Amazon S3, but not charged for the bandwidth used by ELB
to send log files to Amazon S3. For more information about storage costs, see [Amazon S3 pricing](https://aws.amazon.com/s3/pricing/ "https://aws.amazon.com/s3/pricing/").

###### Contents

- [Health check log files](#health-check-log-file-format "#health-check-log-file-format")
- [Health check log entries](#health-check-log-entry-format "#health-check-log-entry-format")
- [Example log entries](#health-check-log-file-entries "#health-check-log-file-entries")
- [Configure log delivery notifications](#health-check-log-event-notifications "#health-check-log-event-notifications")
- [Processing health check log files](#health-check-log-processing-tools "#health-check-log-processing-tools")
- [Enable health check logs for your Application Load Balancer](enable-health-check-logging.md "enable-health-check-logging.md")
- [Disable health check logs for your Application Load Balancer](disable-health-check-logging.md "disable-health-check-logging.md")

## Health check log files

ELB publishes a log file for each load balancer node every 5 minutes.
The load balancer can deliver multiple logs for the same period when a large number
of targets are attached to the load balancer or a small health check interval is
configured (for example, every 5 seconds).

The file names of the health check logs use the following format:

```
`bucket`[/`prefix`]/AWSLogs/`aws-account-id`/elasticloadbalancing/`region`/`yyyy`/`mm`/`dd`/health_check_log_`aws-account-id`_elasticloadbalancing_`region`_app.`load-balancer-id`_`end-time`_`ip-address`_`random-string`.log.gz
```

_bucket_

The name of the S3 bucket.

_prefix_

(Optional) The prefix (logical hierarchy) for the bucket. The prefix
that you specify must not include the string `AWSLogs`. For
more information, see [Organizing
objects using prefixes](../../../AmazonS3/latest/userguide/using-prefixes.md "../../../AmazonS3/latest/userguide/using-prefixes.md").

`AWSLogs`

We add the portion of the file name starting with `AWSLogs` after the
bucket name and optional prefix that you specify.

_aws-account-id_

The AWS account ID of the owner.

_region_

The Region for your load balancer and S3 bucket.

_yyyy_/_mm_/_dd_

The date that the log was delivered.

_load-balancer-id_

The resource ID of the load balancer. If the resource ID contains any
forward slashes (/), they are replaced with periods (.).

_end-time_

The date and time that the logging interval ended. For example, an end
time of 20140215T2340Z contains entries for requests made between 23:35
and 23:40 in UTC or Zulu time.

_ip-address_

The IP address of the load balancer node that handled the request. For
an internal load balancer, this is a private IP address.

_random-string_

A system-generated random string.

The following is an example log file name with a prefix:

```
s3://amzn-s3-demo-logging-bucket/logging-prefix/AWSLogs/123456789012/elasticloadbalancing/us-east-2/2022/05/01/health_check_log_123456789012_elasticloadbalancing_us-east-2_app.my-loadbalancer.1234567890abcdef_20220215T2340Z_172.160.001.192_20sg8hgm.log.gz
```

The following is an example log file name without a prefix:

```
s3://amzn-s3-demo-logging-bucket/AWSLogs/123456789012/elasticloadbalancing/us-east-2/2022/05/01/health_check_log_123456789012_elasticloadbalancing_us-east-2_app.my-loadbalancer.1234567890abcdef_20220215T2340Z_172.160.001.192_20sg8hgm.log.gz
```

You can store your log files in your bucket for as long as you want, but you can
also define Amazon S3 lifecycle rules to archive or delete log files automatically. For
more information, see [Object
lifecycle management](../../../AmazonS3/latest/userguide/object-lifecycle-mgmt.md "../../../AmazonS3/latest/userguide/object-lifecycle-mgmt.md") in the _Amazon S3 User Guide_.

## Health check log entries

ELB logs target health check results including the failure reasons
for all registered targets of that load balancer. Each log entry contains the details of a
single health check result made to the registered target.

###### Contents

- [Syntax](#health-check-log-entry-syntax "#health-check-log-entry-syntax")
- [Error reason codes](#health-check-error-reason-codes "#health-check-error-reason-codes")

### Syntax

The following table describes the fields of a health check log entry, in order.
All fields are delimited by spaces. When we add a new field, we add it to the end
of the log entry. As we prepare to release a new field, you might see an additional
trailing "-" before the field is released. Ensure that you configure log parsing to
stop after the last documented field, and update log parsing after we release a new field.

| Field (position)    | Description                                                                                                                                                                                                                                       |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| type (1)            | The type of health check request or connection. The possible values are as follows (ignore any other values):<br>• `http` -- HTTP<br>• `https` -- HTTP over TLS<br>• `h2` -- HTTP/2 over TLS<br>• `grpc` -- gRPC<br>• `lambda` -- Lambda Function |
| time (2)            | Timestamp of when health check is initiated on a target, in ISO 8601 format.                                                                                                                                                                      |
| latency (3)         | Total time elapsed (in seconds) to complete the current health check.                                                                                                                                                                             |
| target_addr (4)     | IP address and port of the target in the format, IP:Port. Lambda’s ARN if the target is a Lambda function.                                                                                                                                        |
| target_group_id (5) | Name of the target group the target is associated with.                                                                                                                                                                                           |
| status (6)          | The status of the health check. This value is `PASS` if the health check succeeds. On an unsuccessful health check the value is `FAIL`                                                                                                            |
| status_code (7)     | The response code received from the target for the health check request.                                                                                                                                                                          |
| reason_code (8)     | The reason for failure if the health check fails. See [Error reason codes](#health-check-error-reason-codes "#health-check-error-reason-codes")                                                                                                   |

### Error reason codes

If the target health check fails, the load balancer will log one of the following
reason codes in the health check log.

| Code                        | Description                                                                                                                  |
| --------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `RequestTimedOut`           | Health check request timed out while waiting for response                                                                    |
| `ConnectionTimedOut`        | Health check failed because TCP connection attempt timed out                                                                 |
| `ConnectionReset`           | Health check failed due to connection reset                                                                                  |
| `ResponseCodeMismatch`      | HTTP status code of the target’s response to the health check<br>request did not match the configured status code            |
| `ResponseStringMismatch`    | Response body returned by the target did not contain<br>the string configured in the target group health check configuration |
| `InternalError`             | Internal load balancer error                                                                                                 |
| `TargetError`               | Target returns 5xx error code in response to the health check request                                                        |
| `ClientCertTypeUnsupported` | Client certificate type is unsupported                                                                                       |
| `GRPCStatusHeaderEmpty`     | GRPC target response has a grpc-status header without value                                                                  |
| `GRPCUnexpectedStatus`      | GRPC target responds with an unexpected grpc-status                                                                          |

## Example log entries

The following are examples of health check log entries.
Note that the example text appears on multiple lines only to make them easier to read.

The following is an example log entry for a successful health check.

```
http 2025-10-31T12:44:59.875678Z 0.019584011 172.31.20.97:80 HCLogsTestIPs PASS 200 -
```

The following is an example log entry for a failed health check.

```
http 2025-10-31T12:44:58.901409Z 1.121980746 172.31.31.9:80 HCLogsTestIPs FAIL 502 TargetError
```

## Configure log delivery notifications

To receive notifications when ELB delivers logs to your S3 bucket, use Amazon S3 Event
Notifications. ELB uses [PutObject](../../../AmazonS3/latest/API/API_PutObject.md "../../../AmazonS3/latest/API/API_PutObject.md"),
[CreateMultipartUpload](../../../AmazonS3/latest/API/API_CreateMultipartUpload.md "../../../AmazonS3/latest/API/API_CreateMultipartUpload.md"),
and [POST Object](../../../AmazonS3/latest/API/RESTObjectPOST.md "../../../AmazonS3/latest/API/RESTObjectPOST.md")
to deliver logs to Amazon S3. To ensure that you receive all log delivery notifications,
include all of these object creation events in your configuration.

For more information, see [Amazon S3 Event Notifications](../../../AmazonS3/latest/userguide/EventNotifications.md "../../../AmazonS3/latest/userguide/EventNotifications.md") in the _Amazon Simple Storage Service User Guide_.

## Processing health check log files

The health check log files are compressed. If you download the files,
you must uncompress them to view the information.

If there is a lot of demand on your website, your load balancer can generate log
files with gigabytes of data. You might not be able to process such a large amount
of data using line-by-line processing. Therefore, you might have to use analytical
tools that provide parallel processing solutions. For example, you can use the
following analytical tools to analyze and process health-check logs:

- Amazon Athena is an interactive query service that makes it easy to analyze
  data in Amazon S3 using standard SQL.
- [Loggly](https://documentation.solarwinds.com/en/success_center/loggly/content/admin/s3-ingestion-auto.htm "https://documentation.solarwinds.com/en/success_center/loggly/content/admin/s3-ingestion-auto.htm")
- [Splunk](https://splunk.github.io/splunk-add-on-for-amazon-web-services/ "https://splunk.github.io/splunk-add-on-for-amazon-web-services/")
- [Sumo
  logic](https://www.sumologic.com/application/elb/ "https://www.sumologic.com/application/elb/")
