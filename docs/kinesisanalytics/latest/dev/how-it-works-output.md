After careful consideration, we have decided to discontinue Amazon Kinesis
Data Analytics for SQL applications:

1. From **September 1, 2025**, we won't provide any bug fixes for Amazon Kinesis Data Analytics for SQL applications because we will have limited support for it, given the upcoming discontinuation.

2. From **October 15, 2025**, you will not be able to create new Kinesis Data Analytics for SQL
   applications.

3. We will delete your applications starting **January 27, 2026**. You will not be able to
   start or operate your Amazon Kinesis Data Analytics for SQL applications. Support will no longer
   be available for Amazon Kinesis Data Analytics for SQL from that time. For more information, see
   [Amazon Kinesis Data Analytics for SQL Applications discontinuation](discontinuation.md "discontinuation.md").

# Configuring Application Output

In your application code, you write the output of SQL statements to one or more
in-application streams. You can optionally add an output configuration to your
application.
to persist everything written to an in-application stream to an external destination such as
an Amazon Kinesis data stream, a Firehose delivery stream, or an AWS Lambda function.

There is a limit on the number of external destinations you can use to persist an
application output. For more information, see [Limits](limits.md "limits.md").

###### Note

We recommend that you use one external destination to persist in-application error
stream data so that you can investigate the errors.

In each of these output configurations, you provide the following:

- **In-application stream name** – The stream
  that you want to persist to an external destination.

Kinesis Data Analytics looks for the in-application stream that you specified in the output
configuration. (The stream name is case sensitive and must match exactly.) Make sure
that your application code creates this in-application stream.

- **External destination** – You can persist data
  to a Kinesis data stream, a Firehose delivery stream, or a Lambda function. You provide the
  Amazon Resource Name (ARN) of the stream or function. You also provide an IAM role
  that Kinesis Data Analytics can assume to write to the stream or function on your behalf. You
  describe the record format (JSON, CSV) to Kinesis Data Analytics to use when writing to the external
  destination.
  If Kinesis Data Analytics can't write to the streaming or Lambda destination, the service continues to try
  indefinitely. This creates back pressure, causing your application to fall behind. If this
  issue is not resolved, your application eventually stops processing new data. You can
  monitor [Kinesis Data Analytics
  Metrics](../../../AmazonCloudWatch/latest/monitoring/aka-metricscollected.md "../../../AmazonCloudWatch/latest/monitoring/aka-metricscollected.md") and set alarms for failures. For more information about metrics and
  alarms, see [Using Amazon CloudWatch
  Metrics](../../../AmazonCloudWatch/latest/monitoring/working_with_metrics.md "../../../AmazonCloudWatch/latest/monitoring/working_with_metrics.md") and [Creating Amazon CloudWatch
  Alarms](../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md "../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md").

You can configure the application output using the AWS Management Console. The console makes the API
call to save the configuration.

## Creating an Output Using the AWS CLI

This section describes how to create the `Outputs` section of the request
body for a `CreateApplication` or `AddApplicationOutput`
operation.

### Creating a Kinesis Stream

Output

The following JSON fragment shows the `Outputs` section in the
`CreateApplication` request body for creating an Amazon Kinesis data stream
destination.

```
"Outputs": [
   {
       "DestinationSchema": {
           "RecordFormatType": "string"
       },
       "KinesisStreamsOutput": {
           "ResourceARN": "string",
           "RoleARN": "string"
       },
       "Name": "string"
   }

]

```

### Creating a Firehose Delivery Stream

Output

The following JSON fragment shows the `Outputs` section in the
`CreateApplication` request body for creating an Amazon Data Firehose delivery
stream destination.

```
"Outputs": [
   {
       "DestinationSchema": {
           "RecordFormatType": "string"
       },
       "KinesisFirehoseOutput": {
           "ResourceARN": "string",
           "RoleARN": "string"
       },
       "Name": "string"
   }
]

```

### Creating a Lambda Function

Output

The following JSON fragment shows the `Outputs` section in the
`CreateApplication` request body for creating an AWS Lambda function
destination.

```
"Outputs": [
   {
       "DestinationSchema": {
           "RecordFormatType": "string"
       },
       "LambdaOutput": {
           "ResourceARN": "string",
           "RoleARN": "string"
       },
       "Name": "string"
   }
]

```
