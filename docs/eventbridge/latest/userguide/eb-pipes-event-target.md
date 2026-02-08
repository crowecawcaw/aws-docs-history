# Amazon EventBridge Pipes targets

You can send data in your pipe to a specific target. You can configure the following targets
when setting up a pipe in EventBridge:

- [API destination](eb-api-destinations.md "eb-api-destinations.md")
- [API Gateway](eb-api-gateway-target.md "eb-api-gateway-target.md")
- [Batch job queue](#pipes-targets-specifics-batch "#pipes-targets-specifics-batch")
- [CloudWatch log group](#pipes-targets-specifics-cwl "#pipes-targets-specifics-cwl")
- [ECS task](#pipes-targets-specifics-ecs-task "#pipes-targets-specifics-ecs-task")
- [Event bus in the same account and Region](#pipes-targets-specifics-eventbridge "#pipes-targets-specifics-eventbridge")
- Firehose delivery stream
- Inspector assessment template
- Kinesis stream
- [Lambda function (SYNC or
  ASYNC)](#pipes-targets-specifics-lambda-stepfunctions "#pipes-targets-specifics-lambda-stepfunctions")
- Redshift cluster data API queries
- SageMaker AI Pipeline
- Amazon SNS topic (SNS FIFO topics not supported)
- Amazon SQS queue
- [Step Functions state
  machine](#pipes-targets-specifics-lambda-stepfunctions "#pipes-targets-specifics-lambda-stepfunctions")
  - Express workflows (SYNC or ASYNC)
  - Standard workflows (ASYNC)

- [Timestream for LiveAnalytics table](#pipes-targets-specifics-timestream "#pipes-targets-specifics-timestream")

## Target parameters

Some target services don't send the event payload to the target, instead, they treat the
event as a trigger for invoking a specific API. EventBridge uses the [`PipeTargetParameters`](../pipes-reference/API_PipeTargetParameters.md "../pipes-reference/API_PipeTargetParameters.md") to specify what information gets sent to that
API. These include the following:

- API destinations (The data sent to an API destination must match the structure of the
  API. You must use the [`InputTemplate`](../pipes-reference/API_PipeTargetParameters.md#pipes-Type-PipeTargetParameters-InputTemplate "../pipes-reference/API_PipeTargetParameters.md#pipes-Type-PipeTargetParameters-InputTemplate") object to make sure the data is structured
  correctly. If you want to include the original event payload, reference it in the [`InputTemplate`](../pipes-reference/API_PipeTargetParameters.md#pipes-Type-PipeTargetParameters-InputTemplate "../pipes-reference/API_PipeTargetParameters.md#pipes-Type-PipeTargetParameters-InputTemplate").)
- API Gateway (The data sent to API Gateway must match the structure of the API. You must use
  the [`InputTemplate`](../pipes-reference/API_PipeTargetParameters.md#pipes-Type-PipeTargetParameters-InputTemplate "../pipes-reference/API_PipeTargetParameters.md#pipes-Type-PipeTargetParameters-InputTemplate") object to make sure the data is structured
  correctly. If you want to include the original event payload, reference it in the [`InputTemplate`](../pipes-reference/API_PipeTargetParameters.md#pipes-Type-PipeTargetParameters-InputTemplate "../pipes-reference/API_PipeTargetParameters.md#pipes-Type-PipeTargetParameters-InputTemplate").)
- [`PipeTargetRedshiftDataParameters`](../pipes-reference/API_PipeTargetRedshiftDataParameters.md "../pipes-reference/API_PipeTargetRedshiftDataParameters.md") (Amazon Redshift Data API clusters)
- [`PipeTargetSageMakerPipelineParameters`](../pipes-reference/API_PipeTargetSageMakerPipelineParameters.md "../pipes-reference/API_PipeTargetSageMakerPipelineParameters.md") (Amazon SageMaker Runtime Model
  Building Pipelines)
- [`PipeTargetBatchJobParameters`](../pipes-reference/API_PipeTargetBatchJobParameters.md "../pipes-reference/API_PipeTargetBatchJobParameters.md") (AWS Batch)

###### Note

EventBridge does not support all JSON Path syntax and evaluate it at runtime.
Supported syntax includes:

- dot notation (for example,`$.detail`)
- dashes
- underscores
- alphanumeric characters
- array indices
- wildcards (\*)

### Dynamic path parameters

EventBridge Pipes target parameters support optional dynamic JSON path syntax. You can use this
syntax to specify JSON paths instead of static values (for example
`$.detail.state`). The entire value has to be a JSON path, not only part of it.
For example, `RedshiftParameters.Sql` can be `$.detail.state` but it
can't be `"SELECT * FROM $.detail.state"`. These paths are replaced dynamically
at runtime with data from the event payload itself at the specified path. Dynamic path
parameters can't reference new or transformed values resulting from input transformation.
The supported syntax for dynamic parameter JSON paths is the same as when transforming
input. For more information, see [Amazon EventBridge Pipes input transformation](eb-pipes-input-transformation.md "eb-pipes-input-transformation.md").

Dynamic syntax can be used on all string, non-enum fields of all EventBridge Pipes enrichment
and target parameters except:

- [`PipeTargetCloudWatchLogsParameters.LogStreamName`](../pipes-reference/API_PipeTargetCloudWatchLogsParameters.md "../pipes-reference/API_PipeTargetCloudWatchLogsParameters.md")
- [`PipeTargetEventBridgeEventBusParameters.EndpointId`](../pipes-reference/API_PipeTargetEventBridgeEventBusParameters.md "../pipes-reference/API_PipeTargetEventBridgeEventBusParameters.md")
- [`PipeEnrichmentHttpParameters.HeaderParameters`](../pipes-reference/API_PipeEnrichmentHttpParameters.md "../pipes-reference/API_PipeEnrichmentHttpParameters.md")
- [`PipeTargetHttpParameters.HeaderParameters`](../pipes-reference/API_PipeTargetHttpParameters.md "../pipes-reference/API_PipeTargetHttpParameters.md")

For example, to set the `PartitionKey` of a pipe Kinesis target to a custom key
from your source event, set the [KinesisTargetParameter.PartitionKey](../../../index.md "../../../index.md") to:

- `"$.data.`someKey`"` for a Kinesis source
- `"$.body.`someKey`"` for an Amazon SQS source

Then, if the event payload is a valid JSON string, such as
`{"`someKey`":"`someValue`"}`,
EventBridge extracts the value from the JSON path and uses it as the target parameter. In this
example, EventBridge would set the Kinesis `PartitionKey` to
"`someValue`".

## Permissions

To make API calls on the resources that you own, EventBridge Pipes needs appropriate permission.
EventBridge PIpes uses the IAM role that you specify on the pipe for enrichment and target calls
using the IAM principal `pipes.amazonaws.com`.

## Invoking targets

EventBridge has the following ways to invoke a target:

- Synchronously (invocation type set to
  `REQUEST_RESPONSE`) – EventBridge waits for a response from the target before
  proceeding.
- Asynchronously (invocation type set to
  `FIRE_AND_FORGET`) – EventBridge doesn't wait for a response before
  proceeding.

By default, for pipes with ordered sources, EventBridge invokes targets synchronously because a
response from the target is needed before proceeding to the next event.

If an source doesn't enforce order, such as a standard Amazon SQS queue, EventBridge can invoke a
supported target synchronously or asynchronously.

With Lambda functions and Step Functions state machines, you can configure the invocation
type.

###### Note

For Step Functions state machines, [Standard
workflows](../../../step-functions/latest/dg/concepts-standard-vs-express.md "../../../step-functions/latest/dg/concepts-standard-vs-express.md") must be invoked asynchronously.

## Payload size limits

EventBridge Pipes supports payloads up to 6 MB. However, the effective payload size limit is determined by whichever is smaller: the Pipes limit of 6 MB or the target service's maximum payload size. For example:

- Lambda functions support payloads up to 6 MB, so the effective limit for a pipe targeting Lambda is 6 MB.
- EventBridge event buses support payloads up to 1 MB, so the effective limit for a pipe targeting an event bus is 1 MB.
- Step Functions state machines support payloads up to 256 KB, so the effective limit for a pipe targeting Step Functions is 256 KB.

When configuring your pipe, ensure your payload size, including any transformations applied by enrichment or input transformation, does not exceed the target's maximum payload size.

## AWS Batch job queues target specifics

All AWS Batch `submitJob` parameters are configured explicitly with
`BatchParameters`, and as with all Pipe parameters, these can be dynamic using
a JSON path to your incoming event payload.

## CloudWatch Logs group target specifics

Whether you use an input transformer or not, the event payload is used as the log
message. You can set the `Timestamp` (or the explicit `LogStreamName`
of your destination) through `CloudWatchLogsParameters` in
`PipeTarget`. As with all pipe parameters, these parameters can be dynamic when
using a JSON path to your incoming event payload.

## Amazon ECS task target specifics

All Amazon ECS `runTask` parameters are configured explicitly through
`EcsParameters`. As with all pipe parameters, these parameters can be dynamic
when using a JSON path to your incoming event payload.

## Lambda functions and Step Functions

workflow target specifics

Lambda and Step Functions do not have a batch API. To process batches of events from a pipe
source, the batch is converted to a JSON array and passed to as input to the Lambda or Step Functions
target. For more information, see [Amazon EventBridge Pipes batching and concurrency](eb-pipes-batching-concurrency.md "eb-pipes-batching-concurrency.md").

## Timestream for LiveAnalytics table target specifics

Considerations when specifying a Timestream for LiveAnalytics table as a pipe target include:

- Apache Kafka streams (including fromAmazon MSK or third-party providers) are not
  currently supported as a pipe source.
- If you have specified a Kinesis or DynamoDB stream as the pipe
  source, you must specify the number of retry attempts.

For more information, see [Configuring the pipe settings](eb-pipes-create.md#pipes-configure-pipe-settings "eb-pipes-create.md#pipes-configure-pipe-settings").

## EventBridge event bus target specifics

When you configure an EventBridge event bus as a pipe target, the payload from your pipe is automatically placed in the `detail` section of the EventBridge event. Use [`PipeTargetEventBridgeEventBusParameters`](../pipes-reference/API_PipeTargetEventBridgeEventBusParameters.md "../pipes-reference/API_PipeTargetEventBridgeEventBusParameters.md") to configure the event's `source` and `detail-type` fields. Both fields support dynamic JSON path syntax to extract values from your event payload. For example, set `Source` to `$.body.source` or `DetailType` to `$.data.eventType`. You can also use input transformers to modify the event structure before it's placed in the `detail` field. For more information, see [Amazon EventBridge Pipes input transformation](eb-pipes-input-transformation.md "eb-pipes-input-transformation.md").
