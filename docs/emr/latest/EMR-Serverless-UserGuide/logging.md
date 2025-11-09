# Storing logs

To monitor your job progress on EMR Serverless and troubleshoot job failures, choose how EMR Serverless stores and serves application logs. When you submit a job
run, specify managed storage, Amazon S3, and Amazon CloudWatch as your logging options.

With CloudWatch, specify the log types and log locations that you want to use, or
accept the default types and locations. For more information on CloudWatch logs, refer to [Logging for EMR Serverless with
Amazon CloudWatch](#jobs-log-storage-cw "#jobs-log-storage-cw"). With managed storage and S3 logging, the following
table lists the log locations and UI availability that you can expect if you choose
[managed storage](#jobs-log-storage-managed-storage "#jobs-log-storage-managed-storage"), [Amazon S3 buckets](#jobs-log-storage-s3-buckets "#jobs-log-storage-s3-buckets"), or both.

| Option                             | Event logs                | Container logs            | Application UI |
| ---------------------------------- | ------------------------- | ------------------------- | -------------- |
| Managed storage                    | Stored in managed storage | Stored in managed storage | Supported      |
| Both managed storage and S3 bucket | Stored in both places     | Stored in S3 bucket       | Supported      |
| Amazon S3 bucket                   | Stored in S3 bucket       | Stored in S3 bucket       | Not supported1 |

1 We suggest that you keep the **Managed
storage** option selected. Otherwise, you can't use the built-in
application UIs.

## Logging for EMR Serverless with

managed storage

By default, EMR Serverless stores application logs securely in Amazon EMR managed
storage for a maximum of 30 days.

###### Note

If you turn off the default option, Amazon EMR can't troubleshoot your jobs on your
behalf. Example: You cannot access Spark-UI from the EMR Serverless Console.

To turn off this option from EMR Studio, deselect the **Allow AWS to
retain logs for 30 days** check box in the **Additional
settings** section of the **Submit job** page.

To turn off this option from the AWS CLI, use the
`managedPersistenceMonitoringConfiguration` configuration when you
submit a job run.

```
{
    "monitoringConfiguration": {
        "managedPersistenceMonitoringConfiguration": {
            "enabled": false
        }
    }
}
```

If your EMR Serverless application is in a private subnet with VPC endpoints for Amazon S3 and you attach an endpoint policy
to control access, add the following permissions for EMR Serverless to store and serve application logs. Replace `Resource` with the `AppInfo` buckets
from the available regions table
in [Sample policies for private subnets that access Amazon S3](../ManagementGuide/private-subnet-iampolicy.md#private-subnet-iampolicy-regions "../ManagementGuide/private-subnet-iampolicy.md#private-subnet-iampolicy-regions").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "EMRServerlessManagedLogging",
 "Effect": "Allow",
 "Action": [
 "s3:PutObject",
 "s3:PutObjectAcl"
 ],
 "Resource": [
 "arn:aws:s3:::prod.us-east-1.appinfo.src",
 "arn:aws:s3:::prod.us-east-1.appinfo.src/*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:PrincipalServiceName": "emr-serverless.amazonaws.com",
 "aws:SourceVpc": "vpc-12345678"
 }
 }
 }
 ]
}`

```

Additionally, use the `aws:SourceVpc` condition key to ensure that the request travels through the VPC that the VPC endpoint is attached to.

## Logging for EMR Serverless with Amazon S3

buckets

Before your jobs can send log data to Amazon S3, include the following
permissions in the permissions policy for the job runtime role. Replace
`amzn-s3-demo-logging-bucket` with the
name of your logging bucket.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "s3:PutObject"
 ],
 "Resource": [
 "arn:aws:s3:::`amzn-s3-demo-bucket`/*"
 ],
 "Sid": "AllowS3Putobject"
 }
 ]
}`

```

To set up an Amazon S3 bucket to store logs from the AWS CLI, use the
`s3MonitoringConfiguration` configuration when you start a job run.
To do this, provide the following `--configuration-overrides` in the
configuration.

```
{
    "monitoringConfiguration": {
        "s3MonitoringConfiguration": {
            "logUri": "s3://`amzn-s3-demo-logging-bucket`/logs/"
        }
    }
}
```

For batch jobs that don't have retries enabled, EMR Serverless sends the logs to the following path:

```
'/applications/<applicationId>/jobs/<jobId>'
```

Spark driver logs are stored in the following path by EMR Serverless

```
'/applications/<applicationId>/jobs/<jobId>/SPARK_DRIVER/'
```

Spark executor logs are stored in the following path by EMR Serverless

```
'/applications/<applicationId>/jobs/<jobId>/SPARK_EXECUTOR/<EXECUTOR-ID>'
```

The <EXECUTOR-ID> is an integer.

EMR Serverless releases 7.1.0 and higher support retry attempts for streaming jobs and batch jobs. If you run a job
with retries enabled, EMR Serverless automatically adds an attempt number
to the log path prefix, so you can better distinguish and track logs.

```
'/applications/<applicationId>/jobs/<jobId>/attempts/<attemptNumber>/'
```

## Logging for EMR Serverless with

Amazon CloudWatch

When you submit a job to an EMR Serverless application, choose Amazon CloudWatch
as an option to store your application logs. This allows you to use CloudWatch log
analysis features such as CloudWatch Logs Insights and Live Tail. You can also stream logs
from CloudWatch to other systems such as OpenSearch for further analysis.

EMR Serverless provides real-time logging for driver logs. You can access the logs
in real time with the CloudWatch live tail capability, or through CloudWatch CLI tail
commands.

By default, CloudWatch logging is disabled for EMR Serverless. To enable it, use the
configuration in [AWS CLI](#jobs-log-storage-cw-cli "#jobs-log-storage-cw-cli").

###### Note

Amazon CloudWatch publishes logs in real time, so it incurs more resources from
workers. If you choose a low worker capacity, the impact to your job run time
might increase. If you enable CloudWatch logging, we suggest that you choose a
greater worker capacity. It's also possible that log publication could throttle
if the transactions per second (TPS) rate is too low for
`PutLogEvents`. The CloudWatch throttling configuration is global to
all services, including EMR Serverless. For more information, refer to [How do
I determine throttling in my CloudWatch logs?](https://repost.aws/knowledge-center/cloudwatch-logs-throttling "https://repost.aws/knowledge-center/cloudwatch-logs-throttling") on _AWS
re:post_.

### Required permissions for

logging with CloudWatch

Before your jobs can send log data to Amazon CloudWatch, include the following
permissions in the permissions policy for the job runtime role.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "logs:DescribeLogGroups"
 ],
 "Resource": [
 "arn:aws:logs:*:123456789012:*"
 ],
 "Sid": "AllowLOGSDescribeloggroups"
 },
 {
 "Effect": "Allow",
 "Action": [
 "logs:PutLogEvents",
 "logs:CreateLogGroup",
 "logs:CreateLogStream",
 "logs:DescribeLogStreams"
 ],
 "Resource": [
 "arn:aws:logs:*:123456789012:log-group:my-log-group-name:*"
 ],
 "Sid": "AllowLOGSPutlogevents"
 }
 ]
}`

```

### AWS CLI

To set up Amazon CloudWatch to store logs for EMR Serverless from the AWS CLI, use the
`cloudWatchLoggingConfiguration` configuration when you start a
job run. To do this, provide the following configuration overrides. Optionally,
also provide a log group name, log stream prefix name, log types, and an
encryption key ARN.

If you don’t specify the optional values, then CloudWatch publishes the logs to a
default log group `/aws/emr-serverless`, with the default log stream
`/applications/`applicationId`/jobs/`jobId`/`worker-type``.

EMR Serverless releases 7.1.0 and higher support retry attempts for streaming jobs and batch jobs. If you enabled retries for a job,
EMR Serverless automatically adds an attempt number to the log path prefix, so you can better distinguish and track logs.

```
'/applications/`<applicationId>`/jobs/`<jobId>`/attempts/`<attemptNumber>`/worker-type'
```

The following demonstrates the minimum configuration that is required to turn on
Amazon CloudWatch logging with the default settings for EMR Serverless:

```
{
    "monitoringConfiguration": {
        "cloudWatchLoggingConfiguration": {
            "enabled": true
         }
     }
}
```

The following example shows all of the required and optional configurations
that specify when you turn on Amazon CloudWatch logging for EMR Serverless. The
supported `logTypes` values are also listed in the following this
example.

```
{
    "monitoringConfiguration": {
        "cloudWatchLoggingConfiguration": {
            "enabled": true, // Required
            "logGroupName": "Example_logGroup", // Optional
            "logStreamNamePrefix": "Example_logStream", // Optional
            "encryptionKeyArn": "key-arn", // Optional
            "logTypes": {
                "SPARK_DRIVER": ["stdout", "stderr"] //List of values
             }
         }
     }
}
```

By default, EMR Serverless publishes only the driver stdout and stderr logs
to CloudWatch. If you want other logs, then specify a container role and
corresponding log types with the `logTypes` field.

The following list shows the supported worker types that specify
for the `logTypes` configuration:

**Spark**

- `SPARK_DRIVER : ["STDERR", "STDOUT"]`
- `SPARK_EXECUTOR : ["STDERR", "STDOUT"]`

**Hive**

- `HIVE_DRIVER : ["STDERR", "STDOUT", "HIVE_LOG",
"TEZ_AM"]`
- `TEZ_TASK : ["STDERR", "STDOUT",
"SYSTEM_LOGS"]`
