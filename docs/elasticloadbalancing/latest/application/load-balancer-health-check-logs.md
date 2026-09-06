

# Health check logs
<a name="load-balancer-health-check-logs"></a>

Elastic Load Balancing provides health check logs that capture detailed information about the health check status of your registered targets, including failure reasons when health checks fail. Health check logs are supported for EC2 instances, IP address, and Lambda function targets. Each log entry contains information such as the health check request type or connection, timestamp, target address, target group ID, health status and reason code. You can use these health check logs to analyze target health patterns, monitor health transitions, and troubleshoot issues.

Health check logs are an optional feature that is disabled by default. After you enable health check logs for your load balancer, Elastic Load Balancing captures the logs and stores them as compressed files in the Amazon S3 bucket that you specify. You can disable health check logs at any time.

You are charged storage costs for Amazon S3, but not charged for the bandwidth used by Elastic Load Balancing to send log files to Amazon S3. For more information about storage costs, see [Amazon S3 pricing](https://aws.amazon.com/s3/pricing/).

**Important**  
While traditional "legacy" logs (described in this section) remain available, Application Load Balancer now offers enhanced logging options through CloudWatch Logs. CloudWatch Logs provide more flexible delivery options, including to Amazon CloudWatch Logs, Amazon Data Firehose, and Amazon Simple Storage Service. To configure these improved logging options, visit your load balancer's **Integrations** tab. For more information on CloudWatch Logs, see [CloudWatch Logs for your Application Load Balancer](load-balancer-cloudwatch-logs.md).

**Topics**
+ [Health check log files](#health-check-log-file-format)
+ [Health check log entries](#health-check-log-entry-format)
+ [Example log entries](#health-check-log-file-entries)
+ [Configure log delivery notifications](#health-check-log-event-notifications)
+ [Processing health check log files](#health-check-log-processing-tools)
+ [Enable health check logs for your Application Load Balancer](enable-health-check-logging.md)
+ [Disable health check logs for your Application Load Balancer](disable-health-check-logging.md)

## Health check log files
<a name="health-check-log-file-format"></a>

Elastic Load Balancing publishes a log file for each load balancer node every 5 minutes. The load balancer can deliver multiple logs for the same period when a large number of targets are attached to the load balancer or a small health check interval is configured (for example, every 5 seconds).

The file names of the health check logs use the following format:

```
{{bucket}}[/{{prefix}}]/AWSLogs/{{aws-account-id}}/elasticloadbalancing/{{region}}/{{yyyy}}/{{mm}}/{{dd}}/health_check_log_{{aws-account-id}}_elasticloadbalancing_{{region}}_app.{{load-balancer-id}}_{{end-time}}_{{ip-address}}_{{random-string}}.log.gz
```

*bucket*  
The name of the S3 bucket.

*prefix*  
(Optional) The prefix (logical hierarchy) for the bucket. The prefix that you specify must not include the string `AWSLogs`. For more information, see [Organizing objects using prefixes](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-prefixes.html).

`AWSLogs`  
We add the portion of the file name starting with `AWSLogs` after the bucket name and optional prefix that you specify.

*aws-account-id*  
The AWS account ID of the owner.

*region*  
The Region for your load balancer and S3 bucket.

*yyyy*/*mm*/*dd*  
The date that the log was delivered.

*load-balancer-id*  
The resource ID of the load balancer. If the resource ID contains any forward slashes (/), they are replaced with periods (.).

*end-time*  
The date and time that the logging interval ended. For example, an end time of 20140215T2340Z contains entries for requests made between 23:35 and 23:40 in UTC or Zulu time.

*ip-address*  
The IP address of the load balancer node that handled the request. For an internal load balancer, this is a private IP address.

*random-string*  
A system-generated random string.

The following is an example log file name with a prefix:

```
s3://amzn-s3-demo-logging-bucket/logging-prefix/AWSLogs/123456789012/elasticloadbalancing/us-east-2/2022/05/01/health_check_log_123456789012_elasticloadbalancing_us-east-2_app.my-loadbalancer.1234567890abcdef_20220215T2340Z_172.160.001.192_20sg8hgm.log.gz
```

The following is an example log file name without a prefix:

```
s3://amzn-s3-demo-logging-bucket/AWSLogs/123456789012/elasticloadbalancing/us-east-2/2022/05/01/health_check_log_123456789012_elasticloadbalancing_us-east-2_app.my-loadbalancer.1234567890abcdef_20220215T2340Z_172.160.001.192_20sg8hgm.log.gz
```

You can store log files in your bucket indefinitely. You can also define Amazon S3 lifecycle rules to archive or delete log files automatically. For more information, see [Object lifecycle management](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html) in the *Amazon S3 User Guide*.

## Health check log entries
<a name="health-check-log-entry-format"></a>

Elastic Load Balancing logs target health check results including the failure reasons for all registered targets of that load balancer. Each log entry contains the details of a single health check result made to the registered target.

**Topics**
+ [Syntax](#health-check-log-entry-syntax)
+ [Error reason codes](#health-check-error-reason-codes)

### Syntax
<a name="health-check-log-entry-syntax"></a>

The following table describes the fields of a health check log entry, in order. All fields are delimited by spaces. When we add a new field, we add it to the end of the log entry. As we prepare to release a new field, you might see an additional trailing "-" before the field is released. Ensure that you configure log parsing to stop after the last documented field, and update log parsing after we release a new field.


| Field (position) | Description | 
| --- | --- | 
| type (1) | The type of health check request or connection. The possible values are as follows (ignore any other values):+  `http` -- HTTP <br />+  `https` -- HTTP over TLS <br />+  `h2` -- HTTP/2 over TLS <br />+  `grpc` -- gRPC <br />+  `lambda` -- Lambda Function  | 
| time (2) | Timestamp of when health check is initiated on a target, in ISO 8601 format. | 
| latency (3) | Total time elapsed (in seconds) to complete the current health check. | 
| target\_addr (4) | IP address and port of the target in the format, IP:Port. Lambda’s ARN if the target is a Lambda function. | 
| target\_group\_id (5) | Name of the target group the target is associated with. | 
| status (6) | The status of the health check. This value is `PASS` if the health check succeeds. On an unsuccessful health check the value is `FAIL` | 
| status\_code (7) | The response code received from the target for the health check request. | 
| reason\_code (8) | The reason for failure if the health check fails. See [Error reason codes](#health-check-error-reason-codes) | 
| elb (9) | The resource ID of the load balancer. If you are parsing access log entries, note that resources IDs can contain forward slashes (/). | 
| ip\_address (10) | The IP address of the load balancer node that handled the request. For an internal load balancer, this is a private IP address. | 

### Error reason codes
<a name="health-check-error-reason-codes"></a>

If the target health check fails, the load balancer will log one of the following reason codes in the health check log. 


| Code | Description | 
| --- | --- | 
| `TimedOut` | Health check failed because the connection attempt to the target timed out or the target did not respond within the configured health check timeout period. This can occur when the target's security group blocks inbound traffic on the health check port, the target is slow to respond, or the TLS handshake did not complete in time | 
| `ConnectionReset` | Health check failed because the target reset or gracefully closed the connection before a valid response was returned | 
| `ResponseCodeMismatch` | HTTP status code of the target's response to the health check request did not match the configured status code | 
| `ResponseStringMismatch` | Response body returned by the target did not contain the string configured in the target group health check configuration | 
| `InternalError` | Internal load balancer error | 
| `TargetError` | Target returns 5xx error code in response to the health check request | 
| `GRPCStatusHeaderEmpty` | GRPC target response has a grpc-status header without value | 
| `GRPCUnexpectedStatus` | GRPC target responds with an unexpected grpc-status | 

**Note**  
The new `TimedOut` error reason code replaces the `RequestTimedOut` and `ConnectionTimedOut` reason codes.

## Example log entries
<a name="health-check-log-file-entries"></a>

The following are examples of health check log entries. Note that the example text appears on multiple lines only to make them easier to read.

The following is an example log entry for a successful health check.

```
http 2025-10-31T12:44:59.875678Z 0.019584011 172.31.20.97:80 HCLogsTestIPs PASS 200 -
```

The following is an example log entry for a failed health check.

```
http 2025-10-31T12:44:58.901409Z 1.121980746 172.31.31.9:80 HCLogsTestIPs FAIL 502 TargetError
```

## Configure log delivery notifications
<a name="health-check-log-event-notifications"></a>

To receive notifications when Elastic Load Balancing delivers logs to your S3 bucket, use Amazon S3 Event Notifications. Elastic Load Balancing uses [PutObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObject.html), [CreateMultipartUpload](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateMultipartUpload.html), and [POST Object](https://docs.aws.amazon.com/AmazonS3/latest/API/RESTObjectPOST.html) to deliver logs to Amazon S3. To ensure that you receive all log delivery notifications, include all of these object creation events in your configuration.

For more information, see [Amazon S3 Event Notifications](https://docs.aws.amazon.com/AmazonS3/latest/userguide/EventNotifications.html) in the *Amazon Simple Storage Service User Guide*.

## Processing health check log files
<a name="health-check-log-processing-tools"></a>

The health check log files are compressed. If you download the files, you must uncompress them to view the information.

If there is a lot of demand on your website, your load balancer can generate log files with gigabytes of data. You might not be able to process such a large amount of data using line-by-line processing. Therefore, you might have to use analytical tools that provide parallel processing solutions. For example, you can use the following analytical tools to analyze and process health-check logs:
+ Amazon Athena is an interactive query service that makes it easy to analyze data in Amazon S3 using standard SQL.
+ [Loggly](https://documentation.solarwinds.com/en/success_center/loggly/content/admin/s3-ingestion-auto.htm)
+ [Splunk](https://splunk.github.io/splunk-add-on-for-amazon-web-services/)
+ [Sumo logic](https://www.sumologic.com/application/elb/)