# Introduction to testing in the cloud with sam remote invoke

Use the AWS Serverless Application Model Command Line Interface (AWS SAM CLI) `sam remote invoke` command to interact with supported AWS resources in the AWS Cloud. You
can use `sam remote invoke` to invoke the following resources:

- **Amazon Kinesis Data Streams** – Send data records to Kinesis Data Streams applications.
- **AWS Lambda** – Invoke and pass events to your Lambda functions.
- **Amazon Simple Queue Service (Amazon SQS)** – Send messages to Amazon SQS queues.
- **AWS Step Functions** – Invoke Step Functions state machines to start execution.
  For an introduction to the AWS SAM CLI, see [What is the AWS SAM CLI?](what-is-sam-overview.md#what-is-sam-cli "what-is-sam-overview.md#what-is-sam-cli")

For an example of using `sam remote invoke` during a typical development
workflow, see [Step 5: Interact with your function in the AWS Cloud](serverless-getting-started-hello-world.md#serverless-getting-started-hello-world-remote-invoke "serverless-getting-started-hello-world.md#serverless-getting-started-hello-world-remote-invoke").

###### Topics

- [Using the sam remote invoke command](#using-sam-cli-remote-invoke-use "#using-sam-cli-remote-invoke-use")
- [Using sam remote invoke command options](#using-sam-cli-remote-invoke-options "#using-sam-cli-remote-invoke-options")
- [Configure your project configuration
  file](#using-sam-cli-remote-invoke-configure "#using-sam-cli-remote-invoke-configure")
- [Examples](#using-sam-cli-remote-invoke-examples "#using-sam-cli-remote-invoke-examples")
- [Related links](#using-sam-cli-remote-invoke-links "#using-sam-cli-remote-invoke-links")
  To use `sam remote invoke`, install the AWS SAM CLI by completing the
  following:

- [AWS SAM prerequisites](prerequisites.md "prerequisites.md").
- [Install the AWS SAM CLI](install-sam-cli.md "install-sam-cli.md").
  We also recommend upgrading to the latest version of the AWS SAM CLI. To learn more, see
  [Upgrading the AWS SAM CLI](manage-sam-cli-versions.md#manage-sam-cli-versions-upgrade "manage-sam-cli-versions.md#manage-sam-cli-versions-upgrade").

Before using `sam remote invoke`, we recommend a basic understanding of the
following:

- [Configuring the AWS SAM CLI](using-sam-cli-configure.md "using-sam-cli-configure.md").
- [Create your application in AWS SAM](using-sam-cli-init.md "using-sam-cli-init.md").
- [Introduction to building with AWS SAM](using-sam-cli-build.md "using-sam-cli-build.md").
- [Introduction to deploying with AWS SAM](using-sam-cli-deploy.md "using-sam-cli-deploy.md").
- [Introduction to using sam sync to sync to AWS Cloud](using-sam-cli-sync.md "using-sam-cli-sync.md").

## Using the sam remote invoke command

Before using this command, your resource must be deployed to the AWS Cloud.

Use the following command structure and run from your project's root directory:

```
`$` `sam remote invoke `<arguments> <options>``
```

###### Note

This page will show options being provided at the command prompt. You can also configure
options in your project’s configuration file instead of passing them at the command prompt.
To learn more, [Configure project settings](using-sam-cli-configure.md#using-sam-cli-configure-project "using-sam-cli-configure.md#using-sam-cli-configure-project").

For a description of `sam remote invoke` arguments and options, see [sam remote invoke](sam-cli-command-reference-remote-invoke.md "sam-cli-command-reference-remote-invoke.md").

### Using with Kinesis Data Streams

You can send data records to a Kinesis Data Streams application. The AWS SAM CLI will send your data record and return a shard ID and sequence number. The following is an
example:

```
`$` `sam remote invoke `KinesisStream` --stack-name `kinesis-example` --event `hello-world``

	Putting record to Kinesis data stream KinesisStream
	Auto converting value 'hello-world' into JSON '"hello-world"'. If you don't want auto-conversion, please provide
	a JSON string as event
	{
	  "ShardId": "shardId-000000000000",
	  "SequenceNumber": "49646251411914806775980850790050483811301135051202232322"
	}%
```

###### To send a data record

1. Provide a resource ID value as an argument for your Kinesis Data Streams application. For information on valid resource IDs, see
   [Resource ID](sam-cli-command-reference-remote-invoke.md#sam-cli-command-reference-remote-invoke-args-resource-id "sam-cli-command-reference-remote-invoke.md#sam-cli-command-reference-remote-invoke-args-resource-id").
2. Provide the data record as an event to send to your Kinesis Data Streams application. You can provide the event at the command line using the `--event` option, or from a file
   using `--event-file`. If you don’t provide an event, the AWS SAM CLI sends an empty event.

### Using with Lambda functions

You can invoke a Lambda function in the cloud and pass an empty event or provide an event at the command line or from a file. The AWS SAM CLI will invoke your
Lambda function and return its response. The following is an example:

```
`$` `sam remote invoke `HelloWorldFunction` --stack-name `sam-app``

Invoking Lambda Function HelloWorldFunction
START RequestId: d5ef494b-5f45-4086-86fd-d7322fa1a1f9 Version: $LATEST
END RequestId: d5ef494b-5f45-4086-86fd-d7322fa1a1f9
REPORT RequestId: d5ef494b-5f45-4086-86fd-d7322fa1a1f9  Duration: 6.62 ms       Billed Duration: 7 ms     Memory Size: 128 MB     Max Memory Used: 67 MB  Init Duration: 164.06 ms
{"statusCode":200,"body":"{\"message\":\"hello world\"}"}%
```

###### To invoke a Lambda function

1. Provide a resource ID value as an argument for your Lambda function. For information on valid resource IDs, see
   [Resource ID](sam-cli-command-reference-remote-invoke.md#sam-cli-command-reference-remote-invoke-args-resource-id "sam-cli-command-reference-remote-invoke.md#sam-cli-command-reference-remote-invoke-args-resource-id").
2. Provide an event to send to your Lambda function. You can provide the event at the command line using the `--event` option, or from a file using
   `--event-file`. If you don’t provide an event, the AWS SAM CLI sends an empty event.

#### Lambda functions configured with

response streaming

The `sam remote invoke` command supports Lambda functions that are configured
to stream responses. You can configure a Lambda function to stream responses using the
`FunctionUrlConfig`
property in your AWS SAM templates. When you use `sam remote invoke`, the AWS SAM CLI
will automatically detect your Lambda configuration and invoke with response
streaming.

For an example, see [Invoke a Lambda function
configured to stream responses](#using-sam-cli-remote-invoke-examples-lambda-stream "#using-sam-cli-remote-invoke-examples-lambda-stream").

#### Pass shareable test events to a Lambda function in the cloud

Shareable test events are test events that you can share with others in the same AWS account. To learn more, see [Shareable test events](../../../lambda/latest/dg/testing-functions.md#creating-shareable-events "../../../lambda/latest/dg/testing-functions.md#creating-shareable-events") in the _AWS Lambda Developer Guide_.

##### Accessing and managing shareable test events

You can use the AWS SAM CLI `sam remote test-event` command to access and manage shareable test events. For example, you can use
`sam remote test-event` to do the following:

- Retrieve shareable test events from the Amazon EventBridge schema registry.
- Modify shareable test events locally and upload them to the EventBridge schema registry.
- Delete shareable test events from the EventBridge schema registry.

To learn more, see [Introduction to cloud testing with sam remote test-event](using-sam-cli-remote-test-event.md "using-sam-cli-remote-test-event.md").

##### Pass a shareable test event to a Lambda function in the cloud

To pass a shareable test event from the EventBridge schema registry to your Lambda function in the cloud, use the `--test-event-name` option and provide the name of
the shareable test event. The following is an example:

```
`$` `sam remote invoke `HelloWorldFunction` --stack-name `sam-app` --test-event-name `demo-event``
```

If you save the shareable test event locally, you can use the `--event-file` option and provide the file path and name of the local test event. The following is
an example:

```
`$` `sam remote invoke `HelloWorldFunction` --stack-name `sam-app` --event-file `demo-event.json``
```

### Using with Amazon SQS

You can send messages to Amazon SQS queues. The AWS SAM CLI returns the following:

- Message ID
- MD5 of message body
- Response metadata

The following is an example:

```
`$` `sam remote invoke `MySqsQueue` --stack-name `sqs-example` -event `hello``

Sending message to SQS queue MySqsQueue
{
  "MD5OfMessageBody": "5d41402abc4b2a76b9719d911017c592",
  "MessageId": "05c7af65-9ae8-4014-ae28-809d6d8ec652"
}%
```

###### To send a message

1. Provide a resource ID value as an argument for the Amazon SQS queue. For information on valid resource IDs, see
   [Resource ID](sam-cli-command-reference-remote-invoke.md#sam-cli-command-reference-remote-invoke-args-resource-id "sam-cli-command-reference-remote-invoke.md#sam-cli-command-reference-remote-invoke-args-resource-id").
2. Provide an event to send to your Amazon SQS queue. You can provide the event at the command line using the `--event` option, or from a file using
   `--event-file`. If you don’t provide an event, the AWS SAM CLI sends an empty event.

### Using with Step Functions

You can invoke a Step Functions state machine to start execution. The AWS SAM CLI will wait for the state machine workflow to complete and return an output of the
last step in the execution. The following is an example:

```
`$` `sam remote invoke `HelloWorldStateMachine` --stack-name `state-machine-example` --event `'{"is_developer": true}'``

Invoking Step Function HelloWorldStateMachine
"Hello Developer World"%
```

###### To invoke a state machine

1. Provide a resource ID value as an argument for the Step Functions state machine. For information on valid resource IDs, see
   [Resource ID](sam-cli-command-reference-remote-invoke.md#sam-cli-command-reference-remote-invoke-args-resource-id "sam-cli-command-reference-remote-invoke.md#sam-cli-command-reference-remote-invoke-args-resource-id").
2. Provide an event to send to your state machine. You can provide the event at the command line using the `--event` option, or from a file using
   `--event-file`. If you don’t provide an event, the AWS SAM CLI sends an empty event.

## Using sam remote invoke command options

This section covers some of the main options that you can use with the `sam remote invoke` command. For a full list of options, see
[sam remote invoke](sam-cli-command-reference-remote-invoke.md "sam-cli-command-reference-remote-invoke.md").

### Pass an event to your resource

Use the following options to pass events to your resources in the cloud:

- `--event` – Pass an event at the command line.
- `--event-file` – Pass an event from a file.

#### Lambda examples

**Use `--event` to pass an event at the command line as a string value:**

```
`$` `sam remote invoke `HelloWorldFunction` --stack-name `sam-app` --event `'{"message": "hello!"}'``

Invoking Lambda Function HelloWorldFunction
START RequestId: b992292d-1fac-4aa2-922a-c9dc5c6fceab Version: $LATEST
END RequestId: b992292d-1fac-4aa2-922a-c9dc5c6fceab
REPORT RequestId: b992292d-1fac-4aa2-922a-c9dc5c6fceab  Duration: 16.41 ms      Billed Duration: 17 ms  Memory Size: 128 MB     Max Memory Used: 67 MB  Init Duration: 185.96 ms
{"statusCode":200,"body":"{\"message\":\"hello!\"}"}%
```

**Use `--event-file` to pass an event from a file and provide the path to the file:**

```
`$` `cat event.json`

{"message": "hello from file"}%

`$` `sam remote invoke `HelloWorldFunction` --stack-name `sam-app` --event-file `event.json``

Invoking Lambda Function HelloWorldFunction
START RequestId: 3bc71f7d-153a-4b1e-8c9a-901d91b1bec9 Version: $LATEST
END RequestId: 3bc71f7d-153a-4b1e-8c9a-901d91b1bec9
REPORT RequestId: 3bc71f7d-153a-4b1e-8c9a-901d91b1bec9  Duration: 21.15 ms      Billed Duration: 22 ms  Memory Size: 128 MB     Max Memory Used: 67 MB
{"statusCode":200,"body":"{\"message\":\"hello from file\"}"}%
```

**Pass an event using `stdin`:**

```
`$` `cat event.json`

{"message": "hello from file"}%

`$` `cat `event.json` | sam remote invoke `HelloWorldFunction` --stack-name `sam-app` --event-file -`

Reading event from stdin (you can also pass it from file with --event-file)
Invoking Lambda Function HelloWorldFunction
START RequestId: 85ecc902-8ad0-4a2b-a8c8-9bb4f65f5a7a Version: $LATEST
END RequestId: 85ecc902-8ad0-4a2b-a8c8-9bb4f65f5a7a
REPORT RequestId: 85ecc902-8ad0-4a2b-a8c8-9bb4f65f5a7a  Duration: 1.36 ms       Billed Duration: 2 ms   Memory Size: 128 MB       Max Memory Used: 67 MB
{"statusCode":200,"body":"{\"message\":\"hello from file\"}"}%
```

### Configure the AWS SAM CLI response output

When you invoke a supported resource with `sam remote invoke`, the AWS SAM CLI
returns a response that contains the following:

- **Request metadata** – Metadata associated with
  the request. This includes a request ID and request start time.
- **Resource response** – The response from your resource after being invoked in the cloud.

You can use the `--output` option to configure the AWS SAM CLI output response.
The following option values are available:

- `json` – Metadata and resource response are returned in a
  JSON structure. The response contains the full SDK
  output.
- `text` – Metadata is returned in text structure. The resource response
  is returned in the output format of the resource.

The following is an example of a `json` output:

```
`$` `sam remote invoke --stack-name `sam-app` --output `json``

Invoking Lambda Function HelloWorldFunction
{
  "ResponseMetadata": {
    "RequestId": "3bdf9a30-776d-4a90-94a6-4cccc0fc7b41",
    "HTTPStatusCode": 200,
    "HTTPHeaders": {
      "date": "Mon, 19 Jun 2023 17:15:46 GMT",
      "content-type": "application/json",
      "content-length": "57",
      "connection": "keep-alive",
      "x-amzn-requestid": "3bdf9a30-776d-4a90-94a6-4cccc0fc7b41",
      "x-amzn-remapped-content-length": "0",
      "x-amz-executed-version": "$LATEST",
      "x-amz-log-result": "U1RBUlQgUmVxdWVzdElkOiAzYmRmOWEzMC03NzZkLTRhOTAtOTRhNi00Y2NjYzBmYzdiNDEgVmVyc2lvbjogJExBVEVTVApFTkQgUmVxdWVzdElkOiAzYmRmOWEzMC03NzZkLTRhOTAtOTRhNi00Y2NjYzBmYzdiNDEKUkVQT1JUIFJlcXVlc3RJZDogM2JkZjlhMzAtNzc2ZC00YTkwLTk0YTYtNGNjY2MwZmM3YjQxCUR1cmF0aW9uOiA4LjIzIG1zCUJpbGxlZCBEdXJhdGlvbjogOSBtcwlNZW1vcnkgU2l6ZTogMTI4IE1CCU1heCBNZW1vcnkgVXNlZDogNjggTUIJCg==",
      "x-amzn-trace-id": "root=1-64908d42-17dab270273fcc6b527dd6b8;sampled=0;lineage=2301f8dc:0"
    },
    "RetryAttempts": 0
  },
  "StatusCode": 200,
  "LogResult": "U1RBUlQgUmVxdWVzdElkOiAzYmRmOWEzMC03NzZkLTRhOTAtOTRhNi00Y2NjYzBmYzdiNDEgVmVyc2lvbjogJExBVEVTVApFTkQgUmVxdWVzdElkOiAzYmRmOWEzMC03NzZkLTRhOTAtOTRhNi00Y2NjYzBmYzdiNDEKUkVQT1JUIFJlcXVlc3RJZDogM2JkZjlhMzAtNzc2ZC00YTkwLTk0YTYtNGNjY2MwZmM3YjQxCUR1cmF0aW9uOiA4LjIzIG1zCUJpbGxlZCBEdXJhdGlvbjogOSBtcwlNZW1vcnkgU2l6ZTogMTI4IE1CCU1heCBNZW1vcnkgVXNlZDogNjggTUIJCg==",
  "ExecutedVersion": "$LATEST",
  "Payload": "{\"statusCode\":200,\"body\":\"{\\\"message\\\":\\\"hello world\\\"}\"}"
}%
```

When you specify a `json` output, the entire response is returned to
`stdout`. The following is an example:

```
`$` `sam remote invoke --stack-name `sam-app` --output `json` 1> `stdout.log``

Invoking Lambda Function HelloWorldFunction

`$` `cat `stdout.log``

{
  "ResponseMetadata": {
    "RequestId": "d30d280f-8188-4372-bc94-ce0f1603b6bb",
    "HTTPStatusCode": 200,
    "HTTPHeaders": {
      "date": "Mon, 19 Jun 2023 17:35:56 GMT",
      "content-type": "application/json",
      "content-length": "57",
      "connection": "keep-alive",
      "x-amzn-requestid": "d30d280f-8188-4372-bc94-ce0f1603b6bb",
      "x-amzn-remapped-content-length": "0",
      "x-amz-executed-version": "$LATEST",
      "x-amz-log-result": "U1RBUlQgUmVxdWVzdElkOiBkMzBkMjgwZi04MTg4LTQzNzItYmM5NC1jZTBmMTYwM2I2YmIgVmVyc2lvbjogJExBVEVTVApFTkQgUmVxdWVzdElkOiBkMzBkMjgwZi04MTg4LTQzNzItYmM5NC1jZTBmMTYwM2I2YmIKUkVQT1JUIFJlcXVlc3RJZDogZDMwZDI4MGYtODE4OC00MzcyLWJjOTQtY2UwZjE2MDNiNmJiCUR1cmF0aW9uOiA0LjE2IG1zCUJpbGxlZCBEdXJhdGlvbjogNSBtcwlNZW1vcnkgU2l6ZTogMTI4IE1CCU1heCBNZW1vcnkgVXNlZDogNjcgTUIJSW5pdCBEdXJhdGlvbjogMTU4LjM5IG1zCQo=",
      "x-amzn-trace-id": "root=1-649091fc-771473c7778689627a6122b7;sampled=0;lineage=2301f8dc:0"
    },
    "RetryAttempts": 0
  },
  "StatusCode": 200,
  "LogResult": "U1RBUlQgUmVxdWVzdElkOiBkMzBkMjgwZi04MTg4LTQzNzItYmM5NC1jZTBmMTYwM2I2YmIgVmVyc2lvbjogJExBVEVTVApFTkQgUmVxdWVzdElkOiBkMzBkMjgwZi04MTg4LTQzNzItYmM5NC1jZTBmMTYwM2I2YmIKUkVQT1JUIFJlcXVlc3RJZDogZDMwZDI4MGYtODE4OC00MzcyLWJjOTQtY2UwZjE2MDNiNmJiCUR1cmF0aW9uOiA0LjE2IG1zCUJpbGxlZCBEdXJhdGlvbjogNSBtcwlNZW1vcnkgU2l6ZTogMTI4IE1CCU1heCBNZW1vcnkgVXNlZDogNjcgTUIJSW5pdCBEdXJhdGlvbjogMTU4LjM5IG1zCQo=",
  "ExecutedVersion": "$LATEST",
  "Payload": "{\"statusCode\":200,\"body\":\"{\\\"message\\\":\\\"hello world\\\"}\"}"
}%
```

The following is an example of a `text` output:

```
`$` `sam remote invoke --stack-name `sam-app` --output `text``

Invoking Lambda Function HelloWorldFunction
START RequestId: 4dbacc43-1ec6-47c2-982b-9dc4620144d6 Version: $LATEST
END RequestId: 4dbacc43-1ec6-47c2-982b-9dc4620144d6
REPORT RequestId: 4dbacc43-1ec6-47c2-982b-9dc4620144d6  Duration: 9.13 ms       Billed Duration: 10 ms  Memory Size: 128 MB     Max Memory Used: 67 MB  Init Duration: 165.50 ms
{"statusCode":200,"body":"{\"message\":\"hello world\"}"}%
```

When you specify a `text` output, the Lambda function runtime output (for
example, logs) is returned to `stderr`. The Lambda function payload is returned to
`stdout`. The following is an example:

```
`$` `sam remote invoke --stack-name `sam-app` --output `text` 2> `stderr.log``

{"statusCode":200,"body":"{\"message\":\"hello world\"}"}%

`$` `cat `stderr.log``

Invoking Lambda Function HelloWorldFunction
START RequestId: 82273c3b-aa3a-4d16-8f1c-1d2ad3ace891 Version: $LATEST
END RequestId: 82273c3b-aa3a-4d16-8f1c-1d2ad3ace891
REPORT RequestId: 82273c3b-aa3a-4d16-8f1c-1d2ad3ace891  Duration: 40.62 ms      Billed Duration: 41 ms  Memory Size: 128 MB     Max Memory Used: 68 MB

`$` `sam remote invoke --stack-name `sam-app` --output `text` 1> `stdout.log``

Invoking Lambda Function HelloWorldFunction
START RequestId: 74acaa9f-5b80-4a5c-b3b8-ffaccb84cbbd Version: $LATEST
END RequestId: 74acaa9f-5b80-4a5c-b3b8-ffaccb84cbbd
REPORT RequestId: 74acaa9f-5b80-4a5c-b3b8-ffaccb84cbbd  Duration: 2.31 ms       Billed Duration: 3 ms   Memory Size: 128 MB     Max Memory Used: 67 MB

`$` `cat `stdout.log``

{"statusCode":200,"body":"{\"message\":\"hello world\"}"}%
```

### Customize Boto3

parameters

For `sam remote invoke`, the AWS SAM CLI utilizes the AWS SDK for Python (Boto3) to interact
with your resources in the cloud. You can use the `--parameter` option to
customize Boto3 parameters. For a list of supported parameters that you can
customize, see `--parameter`.

#### Examples

**Invoke a Lambda function to validate parameter values and verify permissions:**

```
`$` `sam remote invoke `HelloWorldFunction` --stack-name `sam-app` --parameter `InvocationType="DryRun"``
```

**Use the `--parameter` option multiple times in a single command to provide multiple parameters:**

```
`$` `sam remote invoke `HelloWorldFunction` --stack-name `sam-app` --parameter `InvocationType="Event"` --parameter `LogType="None"``
```

### Other options

For a full list of `sam remote invoke` options, see [sam remote invoke](sam-cli-command-reference-remote-invoke.md "sam-cli-command-reference-remote-invoke.md").

## Configure your project configuration

file

To configure `sam remote invoke` in your configuration file, use
`remote_invoke` in your table. The following is an example of a
`samconfig.toml` file that configures default values for the `sam
 remote invoke` command.

```
...
version =0.1

[default]
...
[default.remote_invoke.parameters]
stack_name = "cloud-app"
event = '{"message": "Hello!"}'
```

## Examples

For a basic example of using `sam remote invoke`, see [Testing AWS Lambda
functions with AWS SAM remote](https://aws.amazon.com/blogs/compute/testing-aws-lambda-functions-with-aws-sam-remote-invoke/ "https://aws.amazon.com/blogs/compute/testing-aws-lambda-functions-with-aws-sam-remote-invoke/") in the _AWS Compute Blog_.

### Kinesis Data Streams examples

#### Basic examples

**Send a data record to a Kinesis Data Streams application from a file. The Kinesis Data Streams application is identified by providing an ARN for the resource ID:**

```
`$` `sam remote invoke `arn:aws:kinesis:us-west-2:01234567890:stream/kinesis-example-KinesisStream-BgnLcAey4xUQ` --event-file `event.json``
```

**Send an event provided at the command line to a Kinesis Data Streams application:**

```
`$` `sam remote invoke `KinesisStream` --stack-name `kinesis-example` --event `hello-world``

Putting record to Kinesis data stream KinesisStream
Auto converting value 'hello-world' into JSON '"hello-world"'. If you don't want auto-conversion, please provide
a JSON string as event
{
  "ShardId": "shardId-000000000000",
  "SequenceNumber": "49646251411914806775980903986194508740483329854174920706"
}%
```

**Obtain the physical ID of the Kinesis Data Streams application. Then, provide an event at the command line:**

```
`$` `sam list resources --stack-name `kinesis-example` --output `json``

[
  {
    "LogicalResourceId": "KinesisStream",
    "PhysicalResourceId": "kinesis-example-KinesisStream-ZgnLcQey4xUQ"
  }
]

`$` `sam remote invoke `kinesis-example-KinesisStream-ZgnLcQey4xUQ` --event `hello``

Putting record to Kinesis data stream KinesisStream
Auto converting value 'hello' into JSON '"hello"'. If you don't want auto-conversion, please provide a JSON
string as event
{
  "ShardId": "shardId-000000000000",
  "SequenceNumber": "49646251411914806775980904340716841045751814812900261890"
}%
```

**Provide a JSON string at the command line as an event:**

```
`$` `sam remote invoke `KinesisStream` --stack-name `kinesis-example` --event `'{"method": "GET", "body": ""}'``

Putting record to Kinesis data stream KinesisStream
{
  "ShardId": "shardId-000000000000",
  "SequenceNumber": "49646251411914806775980904492868617924990209230536441858"
}%
```

**Send an empty event to the Kinesis Data Streams application:**

```
`$` `sam remote invoke `KinesisStream` --stack-name `kinesis-example``

Putting record to Kinesis data stream KinesisStream
{
  "ShardId": "shardId-000000000000",
  "SequenceNumber": "49646251411914806775980904866469008589597168190416224258"
}%
```

**Return the AWS SAM CLI response in JSON format:**

```
`$` `sam remote invoke `KinesisStream` --stack-name `kinesis-example` --event `'{"hello": "world"}'` --output `json``

Putting record to Kinesis data stream KinesisStream
{
  "ShardId": "shardId-000000000000",
  "SequenceNumber": "49646251411914806775980905078409420803696667195489648642",
  "ResponseMetadata": {
    "RequestId": "ebbbd307-3e9f-4431-b67c-f0715e9e353e",
    "HTTPStatusCode": 200,
    "HTTPHeaders": {
      "x-amzn-requestid": "ebbbd307-3e9f-4431-b67c-f0715e9e353e",
      "x-amz-id-2": "Q3yBcgTwtPaQTV26IKclbECmZikUYOzKY+CzcxA84ZHgCkc5T2N/ITWg6RPOQcWw8Gn0tNPcEJBEHyVVqboJAPgCritqsvCu",
      "date": "Thu, 09 Nov 2023 18:13:10 GMT",
      "content-type": "application/x-amz-json-1.1",
      "content-length": "110"
    },
    "RetryAttempts": 0
  }
}%
```

**Return the JSON output to stdout:**

```
`$` `sam remote invoke `KinesisStream` --stack-name `kinesis-example` --event `'{"hello": "world"}'` --output `json 1> stdout.log``

Putting record to Kinesis data stream KinesisStream

`$` `cat `stdout.log``
{
  "ShardId": "shardId-000000000000",
  "SequenceNumber": "49646251411914806775980906397777867595039988349006774274",
  "ResponseMetadata": {
    "RequestId": "f4290006-d84b-b1cd-a9ee-28306eeb2939",
    "HTTPStatusCode": 200,
    "HTTPHeaders": {
      "x-amzn-requestid": "f4290006-d84b-b1cd-a9ee-28306eeb2939",
      "x-amz-id-2": "npCqz+IBKpoL4sQ1ClbUmxuJlbeA24Fx1UgpIrS6mm2NoIeV2qdZSN5AhNurdssykXajBrXaC9anMhj2eG/h7Hnbf+bPuotU",
      "date": "Thu, 09 Nov 2023 18:33:26 GMT",
      "content-type": "application/x-amz-json-1.1",
      "content-length": "110"
    },
    "RetryAttempts": 0
  }
}%
```

### Lambda examples

#### Basic examples

**Invoke a Lambda function by providing the ARN as a resource ID:**

```
`$` `sam remote invoke `arn:aws:lambda:us-west-2:012345678910:function:sam-app-HelloWorldFunction-ohRFEn2RuAvp``
```

**Invoke a Lambda function by providing the logical ID as a resource ID:**

You must also provide the CloudFormation stack name using the `--stack-name` option. The following is an example:

```
`$` `sam remote invoke `HelloWorldFunction` --stack-name `sam-app``
```

If your application contains a single Lambda function, you don’t have to specify it’s logical ID. You can provide the `--stack-name` option only. The following is an
example:

```
`$` `sam remote invoke --stack-name `sam-app``
```

**Invoke a Lambda function by providing the physical ID as a resource ID:**

The physical ID gets created when you deploy using CloudFormation.

```
`$` `sam remote invoke `sam-app-HelloWorldFunction-TZvxQRFNv0k4``
```

**Invoke a Lambda function of a child stack:**

For this example, our application contains the following directory structure:

```
lambda-example
├── childstack
│   ├── function
│   │   ├── __init__.py
│   │   ├── app.py
│   │   └── requirements.txt
│   └── template.yaml
├── events
│   └── event.json
├── samconfig.toml
└── template.yaml
```

To invoke the Lambda function of our `childstack`, we run the following:

```
`$` `sam remote invoke `ChildStack/HelloWorldFunction` --stack-name `lambda-example``

Invoking Lambda Function HelloWorldFunction
START RequestId: 207a864b-e67c-4307-8478-365b004d4bcd Version: $LATEST
END RequestId: 207a864b-e67c-4307-8478-365b004d4bcd
REPORT RequestId: 207a864b-e67c-4307-8478-365b004d4bcd  Duration: 1.27 ms       Billed Duration: 2 ms   Memory Size: 128 MB     Max Memory Used: 36 MB  Init Duration: 111.07 ms
{"statusCode": 200, "body": "{\"message\": \"Hello\", \"received_event\": {}}"}%
```

#### Invoke a Lambda function

configured to stream responses

In this example, we use the AWS SAM CLI to initialize a new serverless application that
contains a Lambda function configured to stream its response. We deploy our application to
the AWS Cloud and use the `sam remote invoke` to interact with our function in
the cloud.

We start by running the `sam init` command to create a new serverless
application. We select the **Lambda Response Streaming** quick start
template and name our application **lambda-streaming-nodejs-app**.

```
`$` `sam init`

	You can preselect a particular runtime or package type when using the `sam init` experience.
	Call `sam init --help` to learn more.

	Which template source would you like to use?
	        1 - AWS Quick Start Templates
	        2 - Custom Template Location
	Choice: `1`

	Choose an AWS Quick Start application template
	        1 - Hello World Example
	        ...
	        9 - Lambda Response Streaming
	        ...
	        15 - Machine Learning
	Template: `9`

	Which runtime would you like to use?
	        1 - go (provided.al2)
	        2 - nodejs18.x
	        3 - nodejs16.x
	Runtime: `2`

	Based on your selections, the only Package type available is Zip.
	We will proceed to selecting the Package type as Zip.

	Based on your selections, the only dependency manager available is npm.
	We will proceed copying the template using npm.

	Would you like to enable X-Ray tracing on the function(s) in your application?  [y/N]: `ENTER`

	Would you like to enable monitoring using CloudWatch Application Insights?
	For more info, please view https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch-application-insights.html [y/N]: `ENTER`

	Project name [sam-app]: `lambda-streaming-nodejs-app`

	    -----------------------
	    Generating application:
	    -----------------------
	    Name: lambda-streaming-nodejs-app
	    Runtime: nodejs18.x
	    Architectures: x86_64
	    Dependency Manager: npm
	    Application Template: response-streaming
	    Output Directory: .
	    Configuration file: lambda-streaming-nodejs-app/samconfig.toml

	    Next steps can be found in the README file at lambda-streaming-nodejs-app/README.md


	Commands you can use next
	=========================
	[*] Create pipeline: cd lambda-streaming-nodejs-app && sam pipeline init --bootstrap
	[*] Validate SAM template: cd lambda-streaming-nodejs-app && sam validate
	[*] Test Function in the Cloud: cd lambda-streaming-nodejs-app && sam sync --stack-name {stack-name} --watch
```

The AWS SAM CLI creates our project with the following structure:

```
lambda-streaming-nodejs-app
	├── README.md
	├── __tests__
	│   └── unit
	│       └── index.test.js
	├── package.json
	├── samconfig.toml
	├── src
	│   └── index.js
	└── template.yaml
```

The following is an example of our Lambda function code:

```
exports.handler = awslambda.streamifyResponse(
	  async (event, responseStream, context) => {
	    const httpResponseMetadata = {
	      statusCode: 200,
	      headers: {
	        "Content-Type": "text/html",
	        "X-Custom-Header": "Example-Custom-Header"
	      }
	    };

	    responseStream = awslambda.HttpResponseStream.from(responseStream, httpResponseMetadata);
	    // It's recommended to use a `pipeline` over the `write` method for more complex use cases.
	    // Learn more: https://docs.aws.amazon.com/lambda/latest/dg/configuration-response-streaming.html
	    responseStream.write("<html>");
	    responseStream.write("<p>First write!</p>");

	    responseStream.write("<h1>Streaming h1</h1>");
	    await new Promise(r => setTimeout(r, 1000));
	    responseStream.write("<h2>Streaming h2</h2>");
	    await new Promise(r => setTimeout(r, 1000));
	    responseStream.write("<h3>Streaming h3</h3>");
	    await new Promise(r => setTimeout(r, 1000));

	    // Long strings will be streamed
	    const loremIpsum1 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque vitae mi tincidunt tellus ultricies dignissim id et diam. Morbi pharetra eu nisi et finibus. Vivamus diam nulla, vulputate et nisl cursus, pellentesque vehicula libero. Cras imperdiet lorem ante, non posuere dolor sollicitudin a. Vestibulum ipsum lacus, blandit nec augue id, lobortis dictum urna. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Morbi auctor orci eget tellus aliquam, non maximus massa porta. In diam ante, pulvinar aliquam nisl non, elementum hendrerit sapien. Vestibulum massa nunc, mattis non congue vitae, placerat in quam. Nam vulputate lectus metus, et dignissim erat varius a.";
	    responseStream.write(`<p>${loremIpsum1}</p>`);
	    await new Promise(r => setTimeout(r, 1000));

	    responseStream.write("<p>DONE!</p>");
	    responseStream.write("</html>");
	    responseStream.end();
	  }
	);
```

The following is an example of our `template.yaml` file. Response
streaming for our Lambda function is configured using the `FunctionUrlConfig`
property.

```
AWSTemplateFormatVersion: '2010-09-09'
	Transform: AWS::Serverless-2016-10-31

	Description: >
	  Sample SAM Template for lambda-streaming-nodejs-app

	Resources:
	  StreamingFunction:
	    Type: AWS::Serverless::Function
	    Properties:
	      CodeUri: src/
	      Handler: index.handler
	      Runtime: nodejs18.x
	      Architectures:
	        - x86_64
	      Timeout: 10
	      FunctionUrlConfig:
	        AuthType: AWS_IAM
	        InvokeMode: RESPONSE_STREAM

	Outputs:
	  StreamingFunction:
	    Description: "Streaming Lambda Function ARN"
	    Value: !GetAtt StreamingFunction.Arn
	  StreamingFunctionURL:
	    Description: "Streaming Lambda Function URL"
	    Value: !GetAtt StreamingFunctionUrl.FunctionUrl
```

Typically, you can use `sam build` and `sam deploy --guided` to
build and deploy a production application. In this example, we’ll assume a development
environment and use the `sam sync` command to build and deploy our
application.

###### Note

The `sam sync` command is recommended for development environments. To
learn more, see [Introduction to using sam sync to sync to AWS Cloud](using-sam-cli-sync.md "using-sam-cli-sync.md").

Before running `sam sync`, we verify that our project is configured correctly
in our `samconfig.toml` file. Most importantly, we verify the values for
`stack_name` and `watch`. With these values specified in our
configuration file, we don't have to provide them at the command line.

```
version = 0.1

	[default]
	[default.global.parameters]
	stack_name = "lambda-streaming-nodejs-app"

	[default.build.parameters]
	cached = true
	parallel = true

	[default.validate.parameters]
	lint = true

	[default.deploy.parameters]
	capabilities = "CAPABILITY_IAM"
	confirm_changeset = true
	resolve_s3 = true
	s3_prefix = "lambda-streaming-nodejs-app"
	region = "us-west-2"
	image_repositories = []

	[default.package.parameters]
	resolve_s3 = true

	[default.sync.parameters]
	watch = true

	[default.local_start_api.parameters]
	warm_containers = "EAGER"

	[default.local_start_lambda.parameters]
	warm_containers = "EAGER"
```

Next, we run `sam sync` to build and deploy our application. Since the
`--watch` option is configured in our configuration file, the AWS SAM CLI will
build our application, deploy our application, and watch for changes.

```
`$` `sam sync`

	The SAM CLI will use the AWS Lambda, Amazon API Gateway, and AWS StepFunctions APIs to upload your code
	without
	performing a CloudFormation deployment. This will cause drift in your CloudFormation stack.
	**The sync command should only be used against a development stack**.

	Queued infra sync. Waiting for in progress code syncs to complete...
	Starting infra sync.
	Building codeuri:
	/Users/.../lambda-streaming-nodejs-app/src runtime: nodejs18.x metadata: {} architecture: x86_64 functions: StreamingFunction
	package.json file not found. Continuing the build without dependencies.
	Running NodejsNpmBuilder:CopySource

	Build Succeeded

	Successfully packaged artifacts and wrote output template to file /var/folders/45/5ct135bx3fn2551_ptl5g6_80000gr/T/tmpavrzdhgp.
	Execute the following command to deploy the packaged template
	sam deploy --template-file /var/folders/45/5ct135bx3fn2551_ptl5g6_80000gr/T/tmpavrzdhgp --stack-name <YOUR STACK NAME>


	        Deploying with following values
	        ===============================
	        Stack name                   : lambda-streaming-nodejs-app
	        Region                       : us-west-2
	        Disable rollback             : False
	        Deployment s3 bucket         : aws-sam-cli-managed-default-samclisam-s3-demo-bucket-1a4x26zbcdkqr
	        Capabilities                 : ["CAPABILITY_NAMED_IAM", "CAPABILITY_AUTO_EXPAND"]
	        Parameter overrides          : {}
	        Signing Profiles             : null

	Initiating deployment
	=====================


	2023-06-20 12:11:16 - Waiting for stack create/update to complete

	CloudFormation events from stack operations (refresh every 0.5 seconds)
	-----------------------------------------------------------------------------------------------------
	ResourceStatus            ResourceType              LogicalResourceId         ResourceStatusReason
	-----------------------------------------------------------------------------------------------------
	CREATE_IN_PROGRESS        AWS::CloudFormation::St   lambda-streaming-         Transformation
	                          ack                       nodejs-app                succeeded
	CREATE_IN_PROGRESS        AWS::IAM::Role            StreamingFunctionRole     -
	CREATE_IN_PROGRESS        AWS::CloudFormation::St   AwsSamAutoDependencyLay   -
	                          ack                       erNestedStack
	CREATE_IN_PROGRESS        AWS::IAM::Role            StreamingFunctionRole     Resource creation
	                                                                              Initiated
	CREATE_IN_PROGRESS        AWS::CloudFormation::St   AwsSamAutoDependencyLay   Resource creation
	                          ack                       erNestedStack             Initiated
	CREATE_COMPLETE           AWS::IAM::Role            StreamingFunctionRole     -
	CREATE_COMPLETE           AWS::CloudFormation::St   AwsSamAutoDependencyLay   -
	                          ack                       erNestedStack
	CREATE_IN_PROGRESS        AWS::Lambda::Function     StreamingFunction         -
	CREATE_IN_PROGRESS        AWS::Lambda::Function     StreamingFunction         Resource creation
	                                                                              Initiated
	CREATE_COMPLETE           AWS::Lambda::Function     StreamingFunction         -
	CREATE_IN_PROGRESS        AWS::Lambda::Url          StreamingFunctionUrl      -
	CREATE_IN_PROGRESS        AWS::Lambda::Url          StreamingFunctionUrl      Resource creation
	                                                                              Initiated
	CREATE_COMPLETE           AWS::Lambda::Url          StreamingFunctionUrl      -
	CREATE_COMPLETE           AWS::CloudFormation::St   lambda-streaming-         -
	                          ack                       nodejs-app
	-----------------------------------------------------------------------------------------------------

	CloudFormation outputs from deployed stack
	-------------------------------------------------------------------------------------------------------
	Outputs
	-------------------------------------------------------------------------------------------------------
	Key                 StreamingFunction
	Description         Streaming Lambda Function ARN
	Value               arn:aws:lambda:us-west-2:012345678910:function:lambda-streaming-nodejs-app-
	StreamingFunction-gUmhO833A0vZ

	Key                 StreamingFunctionURL
	Description         Streaming Lambda Function URL
	Value               https://wxgkcc2dyntgtrwhf2dgdcvylu0rnnof.lambda-url.us-west-2.on.aws/
	-------------------------------------------------------------------------------------------------------


	Stack creation succeeded. Sync infra completed.

	Infra sync completed.
```

Now that our function is deployed to the cloud, we can use `sam remote
 invoke` to interact with our function. The AWS SAM CLI automatically detects that our
function is configured for response streaming and immediately begins outputting a streamed
response of our function in real time.

```
`$` `sam remote invoke `StreamingFunction``

	Invoking Lambda Function StreamingFunction
	{"statusCode":200,"headers":{"Content-Type":"text/html","X-Custom-Header":"Example-Custom-Header"}}<html><p>First write!</p><h1>Streaming h1</h1><h2>Streaming h2</h2><h3>Streaming h3</h3><p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque vitae mi tincidunt tellus ultricies dignissim id et diam. Morbi pharetra eu nisi et finibus. Vivamus diam nulla, vulputate et nisl cursus, pellentesque vehicula libero. Cras imperdiet lorem ante, non posuere dolor sollicitudin a. Vestibulum ipsum lacus, blandit nec augue id, lobortis dictum urna. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Morbi auctor orci eget tellus aliquam, non maximus massa porta. In diam ante, pulvinar aliquam nisl non, elementum hendrerit sapien. Vestibulum massa nunc, mattis non congue vitae, placerat in quam. Nam vulputate lectus metus, et dignissim erat varius a.</p><p>DONE!</p></html>START RequestId: 1e4cdf04-60de-4769-b3a2-c1481982deb4 Version: $LATEST
	END RequestId: 1e4cdf04-60de-4769-b3a2-c1481982deb4
	REPORT RequestId: 1e4cdf04-60de-4769-b3a2-c1481982deb4  Duration: 4088.66 ms    Billed Duration: 4089 ms        Memory Size: 128 MB     Max Memory Used: 68 MB  Init Duration: 168.45 ms
```

When we modify our function code, the AWS SAM CLI instantly detects and immediately
deploys our changes. Here is an example of the AWS SAM CLI output after changes are made to
our function code:

```
Syncing Lambda Function StreamingFunction...
	Building codeuri:
	/Users/.../lambda-streaming-nodejs-app/src runtime: nodejs18.x metadata: {} architecture:
	x86_64 functions: StreamingFunction
	package.json file not found. Continuing the build without dependencies.
	Running NodejsNpmBuilder:CopySource
	Finished syncing Lambda Function StreamingFunction.
	Syncing Layer StreamingFunctione9cfe924DepLayer...
	SyncFlow [Layer StreamingFunctione9cfe924DepLayer]: Skipping resource update as the
	content didn't change
	Finished syncing Layer StreamingFunctione9cfe924DepLayer.
```

We can now use `sam remote invoke` again to interact with our function in the
cloud and test our changes.

### SQS examples

#### Basic examples

**Invoke an Amazon SQS queue by providing the ARN as a resource ID:**

```
`$` `sam remote invoke `arn:aws:sqs:us-west-2:01234567890:sqs-example-4DonhBsjsW1b` --event `'{"hello": "world"}'` --output `json``

Sending message to SQS queue MySqsQueue
{
  "MD5OfMessageBody": "49dfdd54b01cbcd2d2ab5e9e5ee6b9b9",
  "MessageId": "4f464cdd-15ef-4b57-bd72-3ad225d80adc",
  "ResponseMetadata": {
    "RequestId": "95d39377-8323-5ef0-9223-ceb198bd09bd",
    "HTTPStatusCode": 200,
    "HTTPHeaders": {
      "x-amzn-requestid": "95d39377-8323-5ef0-9223-ceb198bd09bd",
      "date": "Wed, 08 Nov 2023 23:27:26 GMT",
      "content-type": "application/x-amz-json-1.0",
      "content-length": "106",
      "connection": "keep-alive"
    },
    "RetryAttempts": 0
  }
}%
```

### Step Functions examples

#### Basic examples

**Invoke a state machine by providing its physical ID as a resource ID:**

First, we use `sam list resources` to obtain our physical ID:

```
`$` `sam list resources --stack-name `state-machine-example` --output `json``

[
  {
    "LogicalResourceId": "HelloWorldStateMachine",
    "PhysicalResourceId": "arn:aws:states:us-west-2:513423067560:stateMachine:HelloWorldStateMachine-z69tFEUx0F66"
  },
  {
    "LogicalResourceId": "HelloWorldStateMachineRole",
    "PhysicalResourceId": "simple-state-machine-HelloWorldStateMachineRole-PduA0BDGuFXw"
  }
]
```

Next, we invoke our state machine using the physical ID as a resource ID. We pass in an event at the command line with the `--event` option:

```
`$` `sam remote invoke `arn:aws:states:us-west-2:01234567890:stateMachine:HelloWorldStateMachine-z69tFEUx0F66` --event `'{"is_developer": true}'``

Invoking Step Function arn:aws:states:us-west-2:01234567890:stateMachine:HelloWorldStateMachine-z69tFEUx0F66
"Hello Developer World"%
```

**Invoke a state machine by passing an empty event:**

```
`$` `sam remote invoke `HelloWorldStateMachine` --stack-name `state-machine-example``

Invoking Step Function HelloWorldStateMachine
"Hello World"%
```

## Related links

For documentation related to `sam remote invoke` and using the AWS SAM CLI, see
the following:

- [sam remote invoke](sam-cli-command-reference-remote-invoke.md "sam-cli-command-reference-remote-invoke.md")
- [AWS SAM CLI troubleshooting](sam-cli-troubleshooting.md "sam-cli-troubleshooting.md")
