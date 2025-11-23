# EventSource

The object describing the source of events which trigger the function. Each event consists
of a type and a set of properties that depend on that type. For more information about the
properties of each event source, see the topic corresponding to that type.

## Syntax

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following
syntax.

### YAML

```
  Properties: `AlexaSkill | Api | CloudWatchEvent | CloudWatchLogs | Cognito | DocumentDB | DynamoDB | EventBridgeRule | HttpApi | IoTRule | Kinesis | MQ | MSK | S3 | Schedule | ScheduleV2 | SelfManagedKafka | SNS | SQS`
  Type: `String`

```

## Properties

`Properties`

Object describing properties of this event mapping. The set of properties must
conform to the defined Type.

_Type_: [AlexaSkill](sam-property-function-alexaskill.md "sam-property-function-alexaskill.md") |
[Api](sam-property-function-api.md "sam-property-function-api.md") |
[CloudWatchEvent](sam-property-function-cloudwatchevent.md "sam-property-function-cloudwatchevent.md") |
[CloudWatchLogs](sam-property-function-cloudwatchlogs.md "sam-property-function-cloudwatchlogs.md") |
[Cognito](sam-property-function-cognito.md "sam-property-function-cognito.md") |
[DocumentDB](sam-property-function-documentdb.md "sam-property-function-documentdb.md") |
[DynamoDB](sam-property-function-dynamodb.md "sam-property-function-dynamodb.md") |
[EventBridgeRule](sam-property-function-eventbridgerule.md "sam-property-function-eventbridgerule.md") |
[HttpApi](sam-property-function-httpapi.md "sam-property-function-httpapi.md") |
[IoTRule](sam-property-function-iotrule.md "sam-property-function-iotrule.md") |
[Kinesis](sam-property-function-kinesis.md "sam-property-function-kinesis.md") |
[MQ](sam-property-function-mq.md "sam-property-function-mq.md") |
[MSK](sam-property-function-msk.md "sam-property-function-msk.md") |
[S3](sam-property-function-s3.md "sam-property-function-s3.md") |
[Schedule](sam-property-function-schedule.md "sam-property-function-schedule.md") |
[ScheduleV2](sam-property-function-schedulev2.md "sam-property-function-schedulev2.md") |
[SelfManagedKafka](sam-property-function-selfmanagedkafka.md "sam-property-function-selfmanagedkafka.md") |
[SNS](sam-property-function-sns.md "sam-property-function-sns.md") |
[SQS](sam-property-function-sqs.md "sam-property-function-sqs.md")

_Required_: Yes

_CloudFormation compatibility_: This property is unique to AWS SAM and
doesn't have an CloudFormation equivalent.

`Type`

The event type.

_Valid values_: `AlexaSkill`, `Api`,
`CloudWatchEvent`, `CloudWatchLogs`, `Cognito`, `DocumentDB`,
`DynamoDB`, `EventBridgeRule`, `HttpApi`, `IoTRule`,
`Kinesis`, `MQ`, `MSK`, `S3`, `Schedule`,
`ScheduleV2`, `SelfManagedKafka`, `SNS`, `SQS`

_Type_: String

_Required_: Yes

_CloudFormation compatibility_: This property is unique to AWS SAM and
doesn't have an CloudFormation equivalent.

## Examples

### APIEvent

Example of using an API event

#### YAML

```
ApiEvent:
  Type: Api
  Properties:
    Method: get
    Path: /group/{user}
    RestApiId:
      Ref: MyApi

```
