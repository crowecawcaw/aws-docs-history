# Sink Declarations

_Sink declarations_ specify where and in what form logs, events, and
metrics should be sent to various AWS services. The following sections describe configurations for
the built-in sink types that are available in Amazon Kinesis Agent for Microsoft Windows. Because Kinesis Agent for Windows is extensible, you can add
custom sink types. Each sink type typically requires unique key-value pairs in the configuration
declarations that are relevant for that sink type.

All sink declarations can contain the following key-value pairs:

`Id`

A unique string that identifies a particular sink within the configuration file
(required).

`SinkType`

The name of the sink type for this sink (required). The sink type specifies the
destination of the log, event, or metric data that is being streamed by this sink.

`AccessKey`

Specifies the AWS access key to use when authorizing access to the AWS service that is
associated with the sink type. This key-value pair is optional. For more information, see [Sink Security
Configuration](#configuring-kinesis-agent-windows-sink-security-configuration "#configuring-kinesis-agent-windows-sink-security-configuration").

`SecretKey`

Specifies the AWS secret key to use when authorizing access to the AWS service that is
associated with the sink type. This key-value pair is optional. For more information, see [Sink Security
Configuration](#configuring-kinesis-agent-windows-sink-security-configuration "#configuring-kinesis-agent-windows-sink-security-configuration").

`Region`

Specifies which AWS Region contains the destination resources for streaming. This
key-value pair is optional.

`ProfileName`

Specifies which AWS profile to use for authentication. This key-value pair is optional,
but if specified, it overrides any specified access key and secret key. For more information,
see [Sink Security
Configuration](#configuring-kinesis-agent-windows-sink-security-configuration "#configuring-kinesis-agent-windows-sink-security-configuration").

`RoleARN`

Specifies the IAM role to use when accessing the AWS service that is associated with the
sink type. This option is useful when Kinesis Agent for Windows is running on an EC2 instance but a different role
would be more appropriate than the role referenced by the instance profile. For example, a
cross-account role can be used to target resources that are not in the same AWS account as the
EC2 instance. This key-value pair is optional.

`Format`

Specifies the kind of serialization that is applied to logs and event data before
streaming. Valid values are `json` and `xml`. This option is helpful when
downstream analytics in the data pipeline require or prefer data in a particular form. This
key-value pair is optional, and if not specified, ordinary text from the source is streamed
from the sink to the AWS service that is associated with the sink type.

`TextDecoration`

When no `Format` is specified, `TextDecoration` specifies what
additional text should be included when streaming log or event records. For more information,
see [Configuring Sink
Decorations](#configuring-kinesis-agent-windows-decoration-configuration "#configuring-kinesis-agent-windows-decoration-configuration"). This key-value pair is
optional.

`ObjectDecoration`

When `Format` is specified, `ObjectDecoration` specifies what
additional data is included in the log or event record before serialization and streaming. For
more information, see [Configuring Sink
Decorations](#configuring-kinesis-agent-windows-decoration-configuration "#configuring-kinesis-agent-windows-decoration-configuration"). This key-value pair is
optional.

`BufferInterval`

To minimize API calls to the AWS service that is associated with the sink type, Kinesis Agent for Windows
buffers up multiple log, event, or metric records before streaming. This can save money for
services that charge per API call. `BufferInterval` specifies the maximum length of
time (in seconds) that records should be buffered before streaming to the AWS service. This
key-value pair is optional, and if specified, use a string to represent the value.

`BufferSize`

To minimize API calls to the AWS service that is associated with the sink type, Kinesis Agent for Windows
buffers up multiple log, event, or metric records before streaming. This can save money for
services that charge per API call. `BufferSize` specifies the maximum number of
records to buffer before streaming to the AWS service. This key-value pair is optional, and if
it is specified, use a string to represent the value.

`MaxAttempts`

Specifies the maximum number of times Kinesis Agent for Windows tries to stream a set of log, event, and
metric records to an AWS service if the streaming consistently fails. This key-value pair is
optional. If it is specified, use a string to represent the value. The default value is
"`3`".

For examples of complete configuration files that use various kinds of sinks, see [Streaming from the Windows Application Event
Log to Sinks](configuring-kaw-examples.md#configuring-kaw-examples-sinks "configuring-kaw-examples.md#configuring-kaw-examples-sinks").

###### Topics

- [KinesisStream Sink
  Configuration](#sink-object-declarations-kinesis-stream "#sink-object-declarations-kinesis-stream")
- [KinesisFirehose Sink
  Configuration](#sink-object-declarations-kinesis-firehose "#sink-object-declarations-kinesis-firehose")
- [CloudWatch Sink Configuration](#sink-object-declarations-cloud-watch "#sink-object-declarations-cloud-watch")
- [CloudWatchLogs Sink
  Configuration](#sink-object-declarations-cloud-watch-logs "#sink-object-declarations-cloud-watch-logs")
- [Local FileSystem Sink Configuration](#sink-object-declarations-local-filesystem "#sink-object-declarations-local-filesystem")
- [Sink Security
  Configuration](#configuring-kinesis-agent-windows-sink-security-configuration "#configuring-kinesis-agent-windows-sink-security-configuration")
- [Configuring ProfileRefreshingAWSCredentialProvider to Refresh AWS Credentials](#configuring-credential-refresh "#configuring-credential-refresh")
- [Configuring Sink
  Decorations](#configuring-kinesis-agent-windows-decoration-configuration "#configuring-kinesis-agent-windows-decoration-configuration")
- [Configuring Sink Variable
  Substitutions](#configuring-kinesis-agent-windows-sink-variable-substitution "#configuring-kinesis-agent-windows-sink-variable-substitution")
- [Configuring Sink Queuing](#configuring-kinesis-agent-windows-queuing "#configuring-kinesis-agent-windows-queuing")
- [Configuring a Proxy for Sinks](#configuring-kinesis-agent-windows-sink-proxy "#configuring-kinesis-agent-windows-sink-proxy")
- [Configuring resolving variables in more sink attributes](#configuring-resolving-variables "#configuring-resolving-variables")
- [Configuring AWS STS Regional Endpoints When Using RoleARN Property in AWS Sinks](#configuring-sts-endpoints "#configuring-sts-endpoints")
- [Configuring VPC Endpoint for AWS Sinks](#configuring-vpc-endpoint "#configuring-vpc-endpoint")
- [Configuring An Alternate Means of Proxy](#configuring-alternate-proxy "#configuring-alternate-proxy")

## `KinesisStream` Sink

Configuration

The `KinesisStream` sink type streams log records and events to the Kinesis Data Streams
service. Typically, data that is streamed to Kinesis Data Streams is processed by one or more custom
applications that execute using various AWS services. Data is streamed to a named stream that is
configured using Kinesis Data Streams. For more information, see the _[Amazon Kinesis Data Streams Developer Guide](../../../streams/latest/dev.md "../../../streams/latest/dev.md")_.

The following is an example Kinesis Data Streams sink declaration:

```
{
    "Id": "TestKinesisStreamSink",
    "SinkType": "KinesisStream",
    "StreamName": "MyTestStream",
    "Region": "us-west-2"
}

```

All `KinesisStream` sink declarations can provide the following additional
key-value pairs:

`SinkType`

Must be specified, and the value must be the literal string
`KinesisStream`.

`StreamName`

Specifies the name of the Kinesis data stream that receives the data streamed from the
`KinesisStream` sink type (required). Before streaming the data, configure the
stream in the AWS Management Console, the AWS CLI, or through an application using the Kinesis Data Streams API.

`RecordsPerSecond`

Specifies the maximum number of records streamed to Kinesis Data Streams per second. This key-value pair
is optional. If it is specified, use an integer to represent the value. The default value is
1000 records.

`BytesPerSecond`

Specifies the maximum number of bytes streamed to Kinesis Data Streams per second. This key-value pair
is optional. If it is specified, use an integer to represent the value. The default value is 1
MB.

The default `BufferInterval` for this sink type is 1 second, and the default
`BufferSize` is 500 records.

## `KinesisFirehose` Sink

Configuration

The `KinesisFirehose` sink type streams log records and events to the Firehose
service. Firehose delivers the streamed data to other services for storage. Typically the stored
data is then analyzed in subsequent stages of the data pipeline. Data is streamed to a named
delivery stream that is configured using Firehose. For more information, see the
_[Amazon Data Firehose Developer Guide](../../../firehose/latest/dev.md "../../../firehose/latest/dev.md")_.

The following is an example Firehose sink declaration:

```
{
   "Id": "TestKinesisFirehoseSink",
   "SinkType": "KinesisFirehose",
   "StreamName": "MyTestFirehoseDeliveryStream",
   "Region": "`us-east-1`",
   "CombineRecords": "true"
}

```

All `KinesisFirehose` sink declarations can provide the following additional
key-value pairs:

`SinkType`

Must be specified, and the value must be the literal string
`KinesisFirehose`.

`StreamName`

Specifies the name of the Firehose delivery stream that receives the data streamed from the
`KinesisStream` sink type (required). Before streaming the data, configure the
delivery stream using the AWS Management Console, the AWS CLI, or through an application using the Firehose API.

`CombineRecords`
When set to `true`, specifies to combine multiple small records into a large record with a 5 KB maximum size. This key-value pair is optional. Records combined using this function are separated by `\n`. If you use AWS Lambda to transform a Firehose record, your Lambda function needs to account for the separator character.

`RecordsPerSecond`

Specifies the maximum number of records that are streamed to Kinesis Data Streams per second. This
key-value pair is optional. If it is specified, use an integer to represent the value. The
default value is 5000 records.

`BytesPerSecond`

Specifies the maximum number of bytes that are streamed to Kinesis Data Streams per second. This
key-value pair is optional. If it is specified, use an integer to represent the value. The
default value is 5 MB.

The default `BufferInterval` for this sink type is 1 second, and the default
`BufferSize` is 500 records.

## CloudWatch Sink Configuration

The `CloudWatch` sink type streams metrics to the CloudWatch service. You can view the
metrics in the AWS Management Console. For more information, see the
_[Amazon CloudWatch User Guide](../../../AmazonCloudWatch/latest/monitoring.md "../../../AmazonCloudWatch/latest/monitoring.md")_.

The following is an example `CloudWatch` sink declaration:

```
{
   "Id": "CloudWatchSink",
   "SinkType": "CloudWatch"
}

```

All `CloudWatch` sink declarations can provide the following additional key-value
pairs:

`SinkType`

Must be specified, and the value must be the literal string
`CloudWatch`.

`Interval`

Specifies how frequently (in seconds) Kinesis Agent for Windows reports metrics to the CloudWatch service. This
key-value pair is optional. If it is specified, use an integer to represent the value. The
default value is 60 seconds. Specify 1 second if you want high-resolution CloudWatch metrics.

`Namespace`

Specifies the CloudWatch namespace where the metric data is reported. CloudWatch namespaces group a
set of metrics together. This key-value pair is optional. The default value is
`KinesisTap`.

`Dimensions`

Specifies the CloudWatch dimensions that are used to isolate metric sets within a namespace.
This can be useful to provide separate sets of metric data for each desktop or server, for
example. This key-value pair is optional, and if specified, the value must comply with the
following format: `"`_key1_`=`_value1_;_key2_`=`_value2..._`"`. The
default value is `"ComputerName={computername};InstanceId={instance_id}"`. This
value supports sink variable substitution. For more information, see [Configuring Sink Variable
Substitutions](#configuring-kinesis-agent-windows-sink-variable-substitution "#configuring-kinesis-agent-windows-sink-variable-substitution").

`MetricsFilter`

Specifies which metrics are streamed to CloudWatch from the built-in Kinesis Agent for Windows metrics source. For
more information about the built-in Kinesis Agent for Windows metrics source, including the details of the syntax
of the value of this key-value pair, see [Kinesis Agent for Windows Built-In Metrics Source](source-object-declarations.md#kinesis-agent-builin-metrics-source "source-object-declarations.md#kinesis-agent-builin-metrics-source").

## `CloudWatchLogs` Sink

Configuration

The `CloudWatchLogs` sink type streams log records and events to Amazon CloudWatch Logs. You
can view logs in the AWS Management Console, or process them via additional stages of a data pipeline. Data is
streamed to a named log stream that is configured in CloudWatch Logs. Log streams are organized into named
log groups. For more information, see the _[Amazon CloudWatch Logs User Guide](../../../AmazonCloudWatch/latest/logs.md "../../../AmazonCloudWatch/latest/logs.md")_.

The following is an example CloudWatch Logs sink declaration:

```
{
   "Id": "MyCloudWatchLogsSink",
   "SinkType": "CloudWatchLogs",
   "BufferInterval": "60",
   "BufferSize": "100",
   "Region": "us-west-2",
   "LogGroup": "MyTestLogGroup",
   "LogStream": "MyTestStream"
}
```

All `CloudWatchLogs` sink declarations must provide the following additional
key-value pairs:

`SinkType`

Must be the literal string `CloudWatchLogs`.

`LogGroup`

Specifies the name of the CloudWatch Logs log group that contains the log stream that receives the
log and event records streamed by the `CloudWatchLogs` sink type. If the specified
log group does not exist, Kinesis Agent for Windows attempts to create it.

`LogStream`

Specifies the name of the CloudWatch Logs log stream that receives the log and event records stream
by the `CloudWatchLogs` sink type. This value supports sink variable substitution.
For more information, see [Configuring Sink Variable
Substitutions](#configuring-kinesis-agent-windows-sink-variable-substitution "#configuring-kinesis-agent-windows-sink-variable-substitution"). If the specified log
stream does not exist, Kinesis Agent for Windows attempts to create it.

The default `BufferInterval` for this sink type is 1 second, and the default
`BufferSize` is 500 records. The maximum buffer size is 10,000 records.

## Local `FileSystem` Sink Configuration

The sink type `FileSystem` saves log and event records to a file on the local file system instead of streaming them to AWS services. `FileSystem` sinks are useful for testing and diagnostics. For example, you can use this sink type to examine records before sending them to AWS.

With `FileSystem` sinks, you can also use configuration parameters to simulate batching, throttling, and retry-on-error to mimic the behavior of actual AWS sinks.

All records from all sources connected to a `FileSystem` sink are saved to the single file specified as `FilePath`. If `FilePath` is not specified, records are saved to a file named ``SinkId`.txt` in the `%TEMP%` directory, which is usually `C:\Users\`UserName`\AppData\Local\Temp`, where ``SinkId`is the unique identifier of the sink and`UserName`` is the Windows user name of the active user.

This sink type supports text decoration attributes. For more information, see [Configuring Sink
Decorations](#configuring-kinesis-agent-windows-decoration-configuration "#configuring-kinesis-agent-windows-decoration-configuration").

An example `FileSystem` sink type configuration is shown in the following example.

```
{
	   "Id": "LocalFileSink",
	   "SinkType": "FileSystem",
	   "FilePath": "C:\\ProgramData\\Amazon\\local_sink.txt",
	   "Format": "json",
	   "TextDecoration": "",
	   "ObjectDecoration": ""
}
```

The `FileSystem` configuration consists of the following key-value pairs.

`SinkType`
Must be the literal string `FileSystem`.

`FilePath`
Specifies the path and file where records are saved. This key-value pair is optional. If not specified, the default is ``TempPath`\\`SinkId`.txt`, where ``TempPath``is the folder stored in the `%TEMP%` variable and``SinkId`` is the unique identifier of the sink.

`Format`
Specifies the format of the event to be `json` or `xml`. This key value pair is optional and case-insensitive. If omitted, events are written to the file in plain text.

`TextDecoration`
Applies only to events written in plain text. This key-value pair is optional.

`ObjectDecoration`
Applies only to events where `Format` is set to `json`. This key-value pair is optional.

### Advanced Usage – Record Throttling and Failure Simulation

`FileSystem` can mimic the behavior of AWS sinks by simulating record throttling. You can use the following key-value pairs to specify record throttling and failure simulation attributes.

By acquiring a lock on the destination file and preventing writes to it, you can use `FileSystem` sinks to simulate and examine the behavior of AWS sinks when the network fails.

The following example shows a `FileSystem` configuration with simulation attributes.

```
{
	   "Id": "LocalFileSink",
	   "SinkType": "FileSystem",
	   "FilePath": "C:\\ProgramData\\Amazon\\local_sink.txt",
	   "TextDecoration": "",
	   "RequestsPerSecond": "100",
    "BufferSize": "10",
    "MaxBatchSize": "1024"
}
```

`RequestsPerSecond`
Optional and specified as a string type. If omitted, the default is `"5"`. Controls the rate of requests that the sink processes—that is, writes to file—not the number of records. Kinesis Agent for Windows makes batch requests to AWS endpoints, so a request may contain multiple records.

`BufferSize`
Optional and specified as string type. Specifies the maximum number of event records that the sink batches before saving to file.

`MaxBatchSize`
Optional and specified as a string type. Specifies the maximum amount of event record data in bytes that the sink batches before saving to file.

The maximum record rate limit is a function of `BufferSize`, which determines the maximum number of records per request, and `RequestsPerSecond`. You can calculate the record rate limit per second using the following formula.

**RecordRate** = `BufferSize` \* `RequestsPerSecond`

Given configuration values in the example above, there is a maximum record rate of 1000 records per second.

## Sink Security

Configuration

### Configuring Authentication

For Kinesis Agent for Windows to stream logs, events, and metrics to AWS services, access must be
authenticated. There are several ways to provide authentication for Kinesis Agent for Windows. How you do it depends
on the situation where Kinesis Agent for Windows is executing and the specific security requirements for a
particular organization.

- If Kinesis Agent for Windows is executing on an Amazon EC2 host, the most secure and simplest way to provide
  authentication is to create an IAM role with sufficient access to the required operations
  for the required AWS services, and an EC2 instance profile that references that role. For
  information about creating instance profiles, see [Using Instance Profiles](../../../IAM/latest/UserGuide/id_roles_use_switch-role-ec2_instance-profiles.md "../../../IAM/latest/UserGuide/id_roles_use_switch-role-ec2_instance-profiles.md"). For information about what policies to attach to the IAM
  role, see [Configuring Authorization](#configuring-kinesis-agent-windows-authorization "#configuring-kinesis-agent-windows-authorization").

After creating the instance profile, you can associate it with any EC2 instances that use
Kinesis Agent for Windows. If instances already have an associated instance profile, you can attach the
appropriate policies to the role that is associated with that instance profile.

- If Kinesis Agent for Windows executes on an EC2 host in one account, but the resources that are the target of
  the sink reside in a different account, you can create an IAM role for cross-account access.
  For more information, see [Tutorial:
  Delegate Access Across AWS accounts Using IAM Roles](../../../IAM/latest/UserGuide/tutorial_cross-account-with-roles.md "../../../IAM/latest/UserGuide/tutorial_cross-account-with-roles.md"). After creating the cross-account
  role, specify the Amazon Resource Name (ARN) for the cross-account role as the value of the
  `RoleARN` key-value pair in the sink declaration. Kinesis Agent for Windows then attempts to assume
  the specified cross-account role when accessing AWS resources that are associated with the
  sink type for that sink.
- If Kinesis Agent for Windows is executing outside of Amazon EC2 (for example, on-premises), several options
  exist:
  - If it is acceptable to register the on-premises server or desktop machine as an
    Amazon EC2 Systems Manager managed-instance, use the following process to configure authentication:

        1. Use the process described in [Setting Up AWS Systems Manager in Hybrid Environments](../../../systems-manager/latest/userguide/systems-manager-managedinstances.md "../../../systems-manager/latest/userguide/systems-manager-managedinstances.md") to create a service role,
         create an activation for a managed instance, and install the SSM agent.
        2. Attach the appropriate policies to the service role to enable Kinesis Agent for Windows to access the
         resources necessary for streaming data from the configured sinks. For information about
         what policies to attach to the IAM role, see [Configuring Authorization](#configuring-kinesis-agent-windows-authorization "#configuring-kinesis-agent-windows-authorization").
        3. Use the process described in [Configuring ProfileRefreshingAWSCredentialProvider to Refresh AWS Credentials](#configuring-credential-refresh "#configuring-credential-refresh") to refresh AWS credentials.

    This is the recommended approach for non-EC2 instances because credentials are securely
    managed by SSM and AWS.

  - If it's acceptable to run the `AWSKinesisTap` service for Kinesis Agent for Windows under a specific user
    instead of the default system account, use the following process:

        1. Create an IAM user in the AWS account where the AWS services will be used. Capture
         the access key and secret key of this user during the creation process. You need this
         information for later steps in this process.
        2. Attach policies to the IAM user that authorize access to the required operations
         for the required services. For information about what policies to attach to the IAM
         user, see [Configuring Authorization](#configuring-kinesis-agent-windows-authorization "#configuring-kinesis-agent-windows-authorization").
        3. Change the `AWSKinesisTap` service on each desktop or server so that it runs under a
         specific user rather than the default system account.
        4. Create a profile in the SDK store using the access key and secret key recorded
         earlier. For more information, see [Configuring
         AWS Credentials](../../../sdk-for-net/v3/developer-guide/net-dg-config-creds.md "../../../sdk-for-net/v3/developer-guide/net-dg-config-creds.md").
        5. Update the `AWSKinesisTap.exe.config` file in the
         `%PROGRAMFILES%\Amazon\AWSKinesisTap` directory to specify the name of
         the profile created in the previous step. For more information, see [Configuring
         AWS Credentials](../../../sdk-for-net/v3/developer-guide/net-dg-config-creds.md "../../../sdk-for-net/v3/developer-guide/net-dg-config-creds.md").

    This is the recommended approach for non-EC2 hosts that cannot be managed instances
    because the credentials are encrypted for the specific host and the specific user.

  - If it is required to run the `AWSKinesisTap` service for Kinesis Agent for Windows under the default system
    account, you must use a shared credential file. This is because the system account has no
    Windows user profile for enabling the SDK store. Shared credential files are not encrypted,
    so we do not recommend this approach. For information about how to use shared configuration
    files, see [Configuring
    AWS Credentials](../../../sdk-for-net/v3/developer-guide/net-dg-config-creds.md "../../../sdk-for-net/v3/developer-guide/net-dg-config-creds.md") in the _AWS SDK for .NET_. If you use this approach, we
    recommend that you use NTFS encryption and restricted file access to the shared
    configuration file. Keys should be rotated by a management platform, and the shared
    configuration file must be updated when the key rotation occurs.

Although it is possible to directly provide access keys and secret keys in the sink
declarations, this approach is discouraged because the declarations are not encrypted.

### Configuring Authorization

Attach the appropriate policies that follow to the IAM user or role that Kinesis Agent for Windows will use
to stream data to AWS services:

#### Kinesis Data Streams

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "VisualEditor0",
 "Effect": "Allow",
 "Action": [
 "kinesis:PutRecord",
 "kinesis:PutRecords"
 ],
 "Resource": "arn:aws:kinesis:*:*:stream/*"
 }
 ]
}`

```

To limit authorization to a specific Region, account, or stream name, replace the
appropriate asterisks in the ARN with specific values. For more information, see "Amazon
Resource Names (ARNs) for Kinesis Data Streams" in [Controlling Access to Amazon
Kinesis Data Streams Resources Using IAM](../../../streams/latest/dev/controlling-access.md "../../../streams/latest/dev/controlling-access.md").

#### Firehose

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "VisualEditor1",
 "Effect": "Allow",
 "Action": [
 "firehose:PutRecord",
 "firehose:PutRecordBatch"
 ],
 "Resource": "arn:aws:firehose:*:*:deliverystream/*"
 }
 ]
}`

```

To limit authorization to a specific Region, account, or delivery stream name, replace the
appropriate asterisks in the ARN with specific values. For more information, see [Controlling Access with
Amazon Kinesis Data Firehose](../../../firehose/latest/dev/controlling-access.md "../../../firehose/latest/dev/controlling-access.md") in the _Amazon Data Firehose Developer Guide_.

#### CloudWatch

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "VisualEditor2",
 "Effect": "Allow",
 "Action": "cloudwatch:PutMetricData",
 "Resource": "*"
 }
 ]
}`

```

For more information, see [Overview of Managing Access Permissions to Your CloudWatch Resources](../../../AmazonCloudWatch/latest/monitoring/iam-access-control-overview-cw.md "../../../AmazonCloudWatch/latest/monitoring/iam-access-control-overview-cw.md") in the
_Amazon CloudWatch Logs User Guide_.

#### CloudWatch Logs with an Existing Log Group and

Log Stream

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "VisualEditor3",
 "Effect": "Allow",
 "Action": [
 "logs:DescribeLogGroups",
 "logs:DescribeLogStreams",
 "logs:PutLogEvents"
 ],
 "Resource": "arn:aws:logs:*:*:log-group:*"
 },
 {
 "Sid": "VisualEditor4",
 "Effect": "Allow",
 "Action": "logs:PutLogEvents",
 "Resource": "arn:aws:logs:*:*:log-group:*:*:*"
 }
 ]
}`

```

To restrict access to a specific Region, account, log group, or log stream, replace the
appropriate asterisks in the ARNs with appropriate values. For more information, see [Overview of Managing Access Permissions to Your CloudWatch Logs Resources](../../../AmazonCloudWatch/latest/logs/iam-access-control-overview-cwl.md "../../../AmazonCloudWatch/latest/logs/iam-access-control-overview-cwl.md") in the
_Amazon CloudWatch Logs User Guide_.

#### CloudWatch Logs with Extra Permissions for Kinesis Agent for Windows

to Create Log Groups and Log Streams

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "VisualEditor5",
 "Effect": "Allow",
 "Action": [
 "logs:CreateLogStream",
 "logs:DescribeLogGroups",
 "logs:DescribeLogStreams",
 "logs:PutLogEvents"
 ],
 "Resource": "arn:aws:logs:*:*:log-group:*"
 },
 {
 "Sid": "VisualEditor6",
 "Effect": "Allow",
 "Action": "logs:PutLogEvents",
 "Resource": "arn:aws:logs:*:*:log-group:*:*:*"
 },
 {
 "Sid": "VisualEditor7",
 "Effect": "Allow",
 "Action": "logs:CreateLogGroup",
 "Resource": "*"
 }
 ]
}`

```

To restrict access to a specific Region, account, log group, or log stream, replace the
appropriate asterisks in the ARNs with appropriate values. For more information, see [Overview of Managing Access Permissions to Your CloudWatch Logs Resources](../../../AmazonCloudWatch/latest/logs/iam-access-control-overview-cwl.md "../../../AmazonCloudWatch/latest/logs/iam-access-control-overview-cwl.md") in the
_Amazon CloudWatch Logs User Guide_.

#### Permissions Required for EC2 Tag Variable Expansion

Using variable expansion with the `ec2tag` variable prefix requires the `ec2:Describe*` permission.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Sid": "VisualEditor8",
 "Effect": "Allow",
 "Action": "ec2:Describe*",
 "Resource": "*"
 }
 ]
}`

```

###### Note

You can combine multiple statements into a single policy as long as the `Sid`
for each statement is unique within that policy. For information about creating policies, see
[Creating IAM Policies](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md") in the _IAM User Guide_.

## Configuring `ProfileRefreshingAWSCredentialProvider` to Refresh AWS Credentials

If you use AWS Systems Manager for hybrid environments to manage AWS credentials, Systems Manager rotates session credentials in `c:\Windows\System32\config\systemprofile\.aws\credentials`. For more information about Systems Manager for hybrid environments, see [Setting up AWS Systems Manager for hybrid environments](../../../(systems-manager/latest/userguide/systems-manager-managedinstances.md "../../../(systems-manager/latest/userguide/systems-manager-managedinstances.md") in the _AWS Systems Manager User Guide_.

Because the AWS .net SDK does not pick up new credentials automatically, we provide the `ProfileRefreshingAWSCredentialProvider` plug-in to refresh credentials.

You can use the `CredentialRef` attribute of any AWS sync configuration to reference a `Credentials` definition where the `CredentialType` attribute is set to `ProfileRefreshingAWSCredentialProvider` as shown in the following example.

```
{
    "Sinks": [{
		      "Id": "myCloudWatchLogsSink",
		      "SinkType": "CloudWatchLogs",
		      "CredentialRef": "ssmcred",
		      "Region": "`us-west-2`",
		      "LogGroup": "myLogGroup",
		      "LogStream": "myLogStream"
    }],
    "Credentials": [{
        "Id": "ssmcred",
        "CredentialType": "ProfileRefreshingAWSCredentialProvider",
        "Profile": "default",
        "FilePath": "`%USERPROFILE%//.aws//credentials`",
        "RefreshingInterval": `300`
    }]
}
```

A credential definition consists of the following attributes as key-value pairs.

`Id`
Defines the string that sink definitions can specify using `CredentialRef` to reference this credential configuration.

`CredentialType`
Set to the literal string `ProfileRefreshingAWSCredentialProvider`.

`Profile`
Optional. The default is `default`.

`FilePath`
Optional. Specifies the path to the AWS credentials file. If omitted, `%USERPROFILE%/.aws/credentials` is the default.

`RefreshingInterval`
Optional. The frequency at which credentials are refreshed, in seconds. If omitted, `300` is the default.

## Configuring Sink

Decorations

Sink declarations can optionally include key-value pairs that specify additional data to
stream to various AWS services to enhance the records gathered from the source.

`TextDecoration`

Use this key-value pair when no `Format` is specified in the sink declaration.
The value is a special format string where variable substitution occurs. For example, suppose
that a `TextDecoration` of `"{ComputerName}:::{timestamp:yyyy-MM-dd
 HH:mm:ss}:::{_record}"` is provided for a sink. When a source emits a log record that
contains the text `The system has resumed from sleep.`, and that source is
connected to the sink via a pipe, then the text `MyComputer1:::2017-10-26 06:14:22:::The
 system has resumed from sleep.` is streamed to the AWS service associated with the sink
type. The `{_record}` variable references the original text record delivered by the
source.

`ObjectDecoration`

Use this key-value pair when `Format` is specified in the sink declaration to
add additional data before record serialization. For example, suppose that an
`ObjectDecoration` of `"ComputerName={ComputerName};DT={timestamp:yyyy-MM-dd
 HH:mm:ss}"` is provided for a sink that specifies JSON `Format`. The
resulting JSON streamed to the AWS service associated with the sink type includes the
following key-value pairs in addition to the original data from the source:

```
{
    ComputerName: "MyComputer2",
    DT: "2017-10-17 21:09:04"
}
```

For an example of using `ObjectDecoration`, see [Tutorial: Stream JSON Log Files to Amazon S3 Using
Kinesis Agent for Windows](directory-source-to-s3-tutorial.md "directory-source-to-s3-tutorial.md").

`ObjectDecorationEx`
Specifies an expression, which allows for more flexible data extraction and formatting as compared to `ObjectDecoration`. This field can be used when the format of the sink is `json`. The expression syntax is shown in the following.

```
"ObjectDecorationEx": "`attribute1`={`expression1`};`attribute2`={`expression2`};`attribute3`={`expression3`}(;...)"
```

For example, the following `ObjectDecorationEx` attribute:

```
"ObjectDecorationEx": "host={env:ComputerName};message={upper(_record)};time={format(_timestamp, 'yyyyMMdd')}"
```

Transforms the literal record:

`System log message`

Into a JSON object as follows, with the values returned by the expressions:

```
{
    "host": "`EC2AMAZ-1234`",
    "message": "SYSTEM LOG MESSAGE",
    "time": "`20210201`"
}
```

For more information about formulating expressions, see [Tips for Writing Expressions](#configuring-expressions "#configuring-expressions"). Most of the `ObjectDecoration` declaration should work using the new syntax with the exception of timestamp variables. A `{timestamp:yyyyMMdd}` field in `ObjectDecoration` is expressed as `{format(_timestamp,'yyyyMMdd')}` in `ObjectDecorationEx`.

`TextDecorationEx`
Specifies an expression, which allows for more flexible data extraction and formatting as compared to `TextDecoration`, as shown in the following example.

```
"TextDecorationEx": "Message '{lower(_record)}' at {format(_timestamp, 'yyyy-MM-dd')}"
```

You can use `TextDecorationEx` to compose JSON objects. Use ‘@{’ to escape open curly brace, as shown in the following example.

```
"TextDecorationEx": "@{ \"var\": \"{upper($myvar1)}\" }"
```

If the source type of the source connected to the sink is `DirectorySource`, then
the sink can use three additional variables:

`_FilePath`

The full path to the log file.

`_FileName`

The file name and file name extension of the file.

`_Position`

An integer that represents where the record is located in the log file.

These variables are useful when you use a source that gathers log records from multiple
files connected to a sink that streams all the records to a single stream. Injecting the values
of these variables into the streaming records enables downstream analytics in the data pipeline
to order the records by file and by location within each file.

### Tips for Writing Expressions

An expression can be any of the following:

- A variable expression.
- A constant expression, for example, `'hello'`, `1`, `1.21`, `null`, `true`, `false`.
- An invocation expression that calls a function, as shown in the following example.

```
regexp_extract('Info: MID 118667291 ICID 197973259 RID 0 To: <jd@acme.com>', 'To: (\\\\S+)', 1)
```

#### Special Characters

Two backslashes are required to escape special characters.

#### Nesting

Function invocations can be nested, as shown in the following example.

```
format(date(2018, 11, 28), 'MMddyyyy')
```

#### Variables

There are three types of variables: local, meta, and global.

- **Local variables** start with a `$` such as `$message`. They are used to resolve the property of the event object, an entry if the event is a dictionary, or an attribute if the event is a JSON object. If the local variable contains space or special characters, use a quoted local variable such as `$'date created'`.
- **Meta variables** start with an underscore (`_`) and are used to resolve to the metadata of the event. All event types support the following meta variables.

`_timestamp`
The time stamp of the event.

`_record`
The raw text representation of the event.

Log events support the following additional meta variables.

`_filepath`

`_filename`

`_position`

`_linenumber`

- **Global variables** resolve to environment variables, EC2 instance metadata, or EC2tag. For better performance, we recommend that you use the prefix to limit search scope, such as `{env:ComputerName}`, `{ec2:InstanceId}`, and `{ec2tag:Name}`.

#### Built-in Functions

Kinesis Agent for Windows supports the following built-in functions. If any of the arguments are `NULL` and the function is not designed to handle `NULL`, a `NULL` object is returned.

```
//string functions
int length(string input)
string lower(string input)
string lpad(string input, int size, string padstring)
string ltrim(string input)
string rpad(string input, int size, string padstring)
string rtrim(string input)
string substr(string input, int start)
string substr(string input, int start, int length)
string trim(string input)
string upper(string str)

//regular expression functions
string regexp_extract(string input, string pattern)
string regexp_extract(string input, string pattern, int group)

//date functions
DateTime date(int year, int month, int day)
DateTime date(int year, int month, int day, int hour, int minute, int second)
DateTime date(int year, int month, int day, int hour, int minute, int second, int millisecond)

//conversion functions
int? parse_int(string input)
decimal? parse_decimal(string input)
DateTime? parse_date(string input, string format)
string format(object o, string format)

//coalesce functions
object coalesce(object obj1, object obj2)
object coalesce(object obj1, object obj2, object obj3)
object coalesce(object obj1, object obj2, object obj3, object obj4)
object coalesce(object obj1, object obj2, object obj3, object obj4, object obj5)
object coalesce(object obj1, object obj2, object obj3, object obj4, object obj5, object obj6)
```

## Configuring Sink Variable

Substitutions

The `KinesisStream`, `KinesisFirehose`, and
`CloudWatchLogs` sink declarations require either a `LogStream` or
`StreamName` key-value pair. The value of these key-values can contain variable
references that are automatically resolved by Kinesis Agent for Windows. For `CloudWatchLogs`, the
`LogGroup` key-value pair is also required and can contain variables references that
are automatically resolved by Kinesis Agent for Windows. The variables are specified using the template
`{`_`prefix`_`:`_`variablename`_`}` where _`prefix`_`:` is optional. The supported prefixes are as
follows:

- `env` — The variable reference is resolved to the value of the
  environment variable of the same name.
- `ec2` — The variable reference is resolved to the EC2 instance metadata
  of the same name.
- `ec2tag` — The variable reference is resolved to the value of the EC2
  instance tag of the same name. The `ec2:Describe*` permission is required to access
  instance tags. For more information, see [Permissions Required for EC2 Tag Variable Expansion](#ec2-permissions "#ec2-permissions").

If the prefix isn't specified, if there is an environment variable with the same name as
`variablename`, the variable reference is resolved to the value of the environment
variable. Otherwise, if `variablename` is `instance_id` or
`hostname`, the variable reference is resolved to the value of the EC2 metadata of
the same name. Otherwise, the variable reference is not resolved.

The following are examples of valid key-value pairs using variable references:

```

"LogStream": "LogStream_{instance_id}"
"LogStream": "LogStream_{hostname}"
"LogStream": "LogStream_{ec2:local-hostname}"
"LogStream": "LogStream_{computername}"
"LogStream": "LogStream_{env:computername}"

```

The `CloudWatchLogs` sink declarations support a special format timestamp
variable that allows the timestamp of the original log or event record from the source to alter
the name of the log stream. The format is
`{timestamp:``timeformat``}`. See the following example:

```
"LogStream": "LogStream_{timestamp:yyyyMMdd}"
```

If the log or event record was generated on June 5, 2017, the value of the
`LogStream` key-value pair in the previous example would resolve to
`"LogStream_20170605"`.

If authorized, the `CloudWatchLogs` sink type can automatically create new log
streams when required based on the generated names. You cannot do this for other sink types
because they require additional configuration beyond the name of the stream.

There are special variable substitutions that occur in text and object decoration. For more
information, see [Configuring Sink
Decorations](#configuring-kinesis-agent-windows-decoration-configuration "#configuring-kinesis-agent-windows-decoration-configuration").

## Configuring Sink Queuing

The `KinesisStream`, `KinesisFirehose`, and
`CloudWatchLogs` sink declarations can optionally enable queuing of records that have
failed to stream to the AWS service associated with those sink types due to transient
connectivity issues. To enable queuing and automatic streaming retries when connectivity is
restored, use the following key-value pairs in the sink declarations:

`QueueType`

Specifies the kind of queuing mechanism to use. The only supported value is
`file`, which indicates that records should be queued up in a file. This key-value
pair is required in order to enable the queuing feature of Kinesis Agent for Windows. If it is not specified, the default
behavior is to queue in memory only, and fail to stream when in memory queueing limits are reached.

`QueuePath`

Specifies the path to the folder that contains the files of queued records. This
key-value pair is optional. The default value is
`%PROGRAMDATA%\KinesisTap\Queue\`_SinkId_ where
_SinkId_ is the identifier you assigned as the value of the
`Id` for the sink declaration.

`QueueMaxBatches`

Limits the total amount of space that Kinesis Agent for Windows can consume when queuing records for
streaming. The amount of space is limited to the value of this key-value pair multiplied by
the maximum number of bytes per batch. The maximum bytes per batch for the
`KinesisStream`, `KinesisFirehose`, and `CloudWatchLogs`
sink types are 5 MB, 4 MB, and 1 MB respectively. When this limit is reached, any streaming
failures are not queued and are reported as non-recoverable failures. This key-value pair is
optional. The default value is 10,000 batches.

## Configuring a Proxy for Sinks

To configure a proxy for all the Kinesis Agent for Windows sink types that access AWS services, edit the Kinesis Agent for Windows
configuration file located at `%Program
 Files%\Amazon\KinesisTap\AWSKinesisTap.exe.config`. For instructions, see the
`proxy` section in [Configuration Files Reference for AWS SDK for .NET](../../../sdk-for-net/v2/developer-guide/net-dg-config-ref.md#net-dg-config-ref-elements-proxy "../../../sdk-for-net/v2/developer-guide/net-dg-config-ref.md#net-dg-config-ref-elements-proxy") in the _AWS SDK for .NET Developer
Guide_.

## Configuring resolving variables in more sink attributes

The following example shows a sink configuration that uses the `Region` environment variable for the value of the `Region` attribute key-value pair. For `RoleARN`, it specifies the EC2 tag key `MyRoleARN`, which evaluates to the value associated with that key.

```
"Id": "myCloudWatchLogsSink",
"SinkType": "CloudWatchLogs",
"LogGroup": "EC2Logs",
"LogStream": "logs-{instance_id}"
"Region": "{env:Region}"
"RoleARN": "{ec2tag:MyRoleARN}"
```

## Configuring AWS STS Regional Endpoints When Using RoleARN Property in AWS Sinks

This feature only applies if you are using KinesisTap on Amazon EC2 and using the `RoleARN` property of AWS sinks to assume an external IAM role to authenticate with the destination AWS services.

By setting `UseSTSRegionalEndpoints` to `true`, you can specify that an agent use the regional endpoint (for example, `https://sts.us-east-1.amazonaws.com`) instead of the global endpoint (for example, `https://sts.amazonaws.com`). Using a Regional STS endpoint reduces round-trip latency for the operation and limits the impact of failures in the global endpoint service.

## Configuring VPC Endpoint for AWS Sinks

You can specify a VPC endpoint in the sink configuration for `CloudWatchLogs`, `CloudWatch`, `KinesisStreams`, and `KinesisFirehose` sink types. A VPC endpoint enables you to privately connect your VPC to supported AWS services and VPC endpoint services powered by AWS PrivateLink without requiring an internet gateway, NAT device, VPN connection, or AWS Direct Connect connection. Instances in your VPC do not require public IP addresses to communicate with resources in the service. Traffic between your VPC and the other service does not leave the Amazon network. For more information, see [VPC endpoints](../../../vpc/latest/userguide/vpc-endpoints.md "../../../vpc/latest/userguide/vpc-endpoints.md") in the _Amazon VPC User Guide_.

You specify the VPC endpoint using the `ServiceURL` property as shown in the following example of a `CloudWatchLogs` sink configuration. Set the value of `ServiceURL` to the value shown on the **VPC endpoint details** tab using the Amazon VPC console.

```
{
    "Id": "myCloudWatchLogsSink",
    "SinkType": "CloudWatchLogs",
    "LogGroup": "EC2Logs",
    "LogStream": "logs-{instance_id}",
    "ServiceURL":"`https://vpce-ab1c234de56-ab7cdefg.logs.us-east-1.vpce.amazonaws.com`"
}
```

## Configuring An Alternate Means of Proxy

This feature allows you to configure a proxy server in a sink configuration using the proxy support built in to the AWS SDK instead of .NET. Previously, the only way to configure the agent to use a proxy was to use a native feature of .NET, which automatically routed all HTTP/S requests through the proxy defined in the proxy file.

If you are currently using the agent with a proxy server, you do not need to change over to use this method.

You can use the `ProxyHost` and `ProxyPort` properties to configure an alternate proxy as shown in the following example.

```
{
    "Id": "myCloudWatchLogsSink",
    "SinkType": "CloudWatchLogs",
    "LogGroup": "EC2Logs",
    "LogStream": "logs-{instance_id}",
    "Region": "`us-west-2`",
    "ProxyHost": "`myproxy.mydnsdomain.com`",
    "ProxyPort": "`8080`"
}
```
