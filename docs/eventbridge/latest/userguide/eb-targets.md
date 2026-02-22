# Event bus targets in Amazon EventBridge

A _target_ is a resource or endpoint that EventBridge sends an [event](eb-events.md "eb-events.md") to when the event matches the event pattern defined for
a [rule](eb-rules.md "eb-rules.md"). The rule processes the [event](eb-events.md "eb-events.md") data and sends the pertinent information to the target.
To deliver event data to a target, EventBridge needs permission to access the target resource. You
can define up to five targets for each rule.

When you add targets to a rule and that rule runs soon after, any new or updated targets
might not be immediately invoked. Allow a short period of time for changes to take
effect.

## Event bus targets available in the EventBridge

console

You can configure the following target types for rules in the EventBridge console:

- API destinations

API destinations are HTTPS endpoints that you can invoke as the target of an event bus rule.
When you specify an API destination as a rule target, EventBridge invokes the HTTPS endpoint for any event that matches the event pattern specified in the rule, and then delivers the event information with the request.
For more information, see [API destinations](eb-api-destinations.md "eb-api-destinations.md").

- Event buses

You can specify other event buses as targets for rules. This includes event buses in the same or different AWS accounts.

    + [Cross-account event buses as targets](eb-cross-account.md "eb-cross-account.md")
    + [Same account event buses as targets](eb-bus-to-bus.md "eb-bus-to-bus.md")

- AWS services

You can have EventBridge send events to a number of AWS service resources. These include:

    + [API Gateway](eb-api-gateway-target.md "eb-api-gateway-target.md")
    + [AWS AppSync](target-appsync.md "target-appsync.md")
    + [Batch job queue](#targets-specifics-batch "#targets-specifics-batch")
    + [CloudWatch log group](#targets-specifics-cwl "#targets-specifics-cwl")
    + [CodeBuild project](#targets-specifics-codebuild "#targets-specifics-codebuild")
    + CodePipeline
    + Amazon EBS `CreateSnapshot` API call
    + EC2 Image Builder
    + EC2 `RebootInstances` API call
    + EC2 `StopInstances` API call
    + EC2 `TerminateInstances` API call
    + [ECS task](#targets-specifics-ecs-task "#targets-specifics-ecs-task")
    + Firehose delivery stream
    + Glue workflow
    + [Incident Manager response plan](../../../incident-manager/latest/userguide/incident-creation.md#incident-tracking-auto-eventbridge "../../../incident-manager/latest/userguide/incident-creation.md#incident-tracking-auto-eventbridge")
    + Inspector assessment template
    + Kinesis stream
    + Lambda function (ASYNC)
    + [Amazon Redshift cluster data API queries](../../../redshift/latest/mgmt/data-api-calling-event-bridge.md "../../../redshift/latest/mgmt/data-api-calling-event-bridge.md")
    + [Amazon Redshift Serverless workgroup data API queries](../../../redshift/latest/mgmt/data-api-calling-event-bridge.md "../../../redshift/latest/mgmt/data-api-calling-event-bridge.md")
    + SageMaker AI Pipeline
    + Amazon SNS topic
    + [Amazon SQS standard, fair, and FIFO
     queues](#targets-specifics-sqs "#targets-specifics-sqs")
    + Step Functions state machine (ASYNC)
    + Systems Manager Automation
    + Systems Manager OpsItem
    + Systems Manager Run Command

## Target parameters

Some targets don't send the information in the event payload to the target, instead, they treat the event as a
trigger for invoking a specific API. EventBridge uses the [Target](../APIReference/API_Target.md "../APIReference/API_Target.md") parameters to determine what happens with that target. These include the following:

- API destinations

The data sent to an API destination must match the structure of the API. Use the [`InputTransformer`](../APIReference/API_InputTransformer.md "../APIReference/API_InputTransformer.md") object to
make sure the data is structured correctly. If you want to include the original event payload, reference it in the [`InputTransformer`](../APIReference/API_InputTransformer.md "../APIReference/API_InputTransformer.md").

- API Gateway

The data sent to API Gateway must match the structure of the API. Use the [`InputTransformer`](../APIReference/API_InputTransformer.md "../APIReference/API_InputTransformer.md") object to
make sure the data is structured correctly. If you want to include the original event payload, reference it in the [`InputTransformer`](../APIReference/API_InputTransformer.md "../APIReference/API_InputTransformer.md").

- Amazon EC2 Image Builder
- Amazon Redshift Data API clusters

Use [`RedshiftDataParameters`](../APIReference/API_RedshiftDataParameters.md "../APIReference/API_RedshiftDataParameters.md").

- Amazon SageMaker Runtime Model Building Pipelines

Use [`SageMakerPipelineParameters`](../APIReference/API_SageMakerPipelineParameters.md "../APIReference/API_SageMakerPipelineParameters.md").

- Amazon SQS fair and FIFO queues

Use [`SqsParameters`](../APIReference/API_SqsParameters.md "../APIReference/API_SqsParameters.md") to specify the message group to use as the target.

###### Note

EventBridge does not support all JSON Path syntax and evaluate it at runtime.
Supported syntax includes:

- dot notation (for example,`$.detail`)
- dashes
- underscores
- alphanumeric characters
- array indices
- wildcards (\*)
- forward slashes

### Dynamic path parameters

Dynamic path parameters let you use JSON path syntax to reference event data at runtime instead of static values.

You can use dynamic JSON path syntax with target parameters to specify JSON paths instead of static values (for example, `$.detail.state`).

#### Requirements

The entire value must be a JSON path, not just part of it. For example:

- ✓ Correct: `RedshiftParameters.Sql` can be `$.detail.state`
- ✗ Incorrect: `RedshiftParameters.Sql` cannot be `"SELECT * FROM $.detail.state"`

EventBridge replaces these paths at runtime with data from the event payload at the specified path.

#### Limitations

Dynamic path parameters cannot reference new or transformed values from input transformation. The JSON path syntax is the same as input transformation syntax. For more information, see [Amazon EventBridge input transformation](eb-transform-target-input.md "eb-transform-target-input.md").

#### Supported parameters

You can use dynamic syntax on all string, non-enum fields of these parameters:

- [`EcsParameters`](../APIReference/API_EcsParameters.md "../APIReference/API_EcsParameters.md")
- [`HttpParameters`](../APIReference/API_HttpParameters.md "../APIReference/API_HttpParameters.md") (except `HeaderParameters` keys)
- [`RedshiftDataParameters`](../APIReference/API_RedshiftDataParameters.md "../APIReference/API_RedshiftDataParameters.md")
- [`SageMakerPipelineParameters`](../APIReference/API_SageMakerPipelineParameters.md "../APIReference/API_SageMakerPipelineParameters.md")
- [`SqsParameters`](../APIReference/API_SqsParameters.md "../APIReference/API_SqsParameters.md")

## Permissions

To make API calls on the resources that you own, EventBridge needs appropriate permissions.
Specify an IAM execution role [using the EventBridge
console](eb-create-rule-wizard.md#eb-create-rule-target "eb-create-rule-wizard.md#eb-create-rule-target"), or by setting the `RoleARN` parameter in [`PutTargets`](../APIReference/API_PutTargets.md "../APIReference/API_PutTargets.md").

For example, the following policy defines permission to send messages to an
Amazon SQS queue:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "sqs:SendMessage"
 ],
 "Resource": [
 "arn:aws:sqs:`us-east-1`:`111122223333`:`sqs-queue-name`"
 ]
 }
 ]
}`

```

And the following trust policy enables EventBridge to assume the role:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "events.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

You can invoke an API Gateway
endpoint with configured IAM authorization, but the role is optional if you
haven't configured authorization. For more information, see [Amazon EventBridge and AWS Identity and Access Management](eb-iam.md "eb-iam.md").

If another account is in the same Region and has granted you permission, then
you can send events to that account.

For more information, see [Sending and receiving events between AWS accounts in Amazon EventBridge](eb-cross-account.md "eb-cross-account.md").

If your target, such as an Amazon SQS queue, uses AWS Key Management Service (AWS KMS) encryption, you must include the following section in your KMS key policy:

```
{
  "Sid": "Allow EventBridge to use the key",
  "Effect": "Allow",
  "Principal": {
    "Service": "events.amazonaws.com"
  },
  "Action": [
    "kms:Decrypt",
    "kms:GenerateDataKey"
  ],
  "Resource": "*"
}
```

## AWS Batch job queues as targets

Certain parameters to AWS Batch `submitJob` can be configured via [BatchParameters](../APIReference/API_BatchParameters.md "../APIReference/API_BatchParameters.md").

Others can be specified in the event payload. If the event payload (passed through or via [InputTransformers](eb-transform-target-input.md "eb-transform-target-input.md")) contains the following keys, they are mapped to `submitJob` [request parameters](../../../batch/latest/APIReference/API_SubmitJob.md#API_SubmitJob_RequestSyntax "../../../batch/latest/APIReference/API_SubmitJob.md#API_SubmitJob_RequestSyntax"):

- `ContainerOverrides: containerOverrides`

###### Note

This includes only command, environment, memory, and vcpus

- `DependsOn: dependsOn`

###### Note

This includes only jobId

- `Parameters: parameters`

## CloudWatch Logs groups as targets

If you don’t use an [InputTransformer](eb-transform-target-input.md "eb-transform-target-input.md") with a CloudWatch Logs target, the event payload is used as the log message, and the source of the event as the timestamp. If you do use an InputTransformer, the template must be:

`{"timestamp":<timestamp>,"message":<message>}`

EventBridge batches the entries sent to a log stream; therefore, EventBridge may deliver a single or multiple events to a log stream, depending on traffic.

## CodeBuild projects as targets

EventBridge supports both standard and batch builds as targets.

If you use an [input transformer](eb-transform-target-input.md "eb-transform-target-input.md") to shape the source event to match the [StartBuildRequest](../../../codebuild/latest/APIReference/API_StartBuild.md#API_StartBuild_RequestSyntax "../../../codebuild/latest/APIReference/API_StartBuild.md#API_StartBuild_RequestSyntax") structure before it is delivered to a CodeBuild target, the parameters will be mapped 1-to-1 and
passed through to `codeBuild.StartBuild` by default.

To pass the parameters to `codeBuild.StartBuildBatch` instead,
transform the source event to match the [StartBuildBatchRequest](../../../codebuild/latest/APIReference/API_StartBuildBatch.md#API_StartBuildBatch_RequestSyntax "../../../codebuild/latest/APIReference/API_StartBuildBatch.md#API_StartBuildBatch_RequestSyntax") structure, and add the following key/value pair to
the root of the transformed event:

`"buildType": "BATCH"`

## Amazon ECS tasks as targets

If you use [InputTransformers](eb-transform-target-input.md "eb-transform-target-input.md") to shape the input event to a Target to match the Amazon ECS RunTask [TaskOverride](../../../AmazonECS/latest/APIReference/API_TaskOverride.md "../../../AmazonECS/latest/APIReference/API_TaskOverride.md") structure, the parameters will be mapped 1-to-1 and passed through to `ecs.RunTask`.

## Incident Manager response plans as targets

If the matched event came from CloudWatch Alarms, the alarm state change details are populated into the trigger details of the StartIncidentRequest call to Incident Manager.

## Amazon SQS queues as targets

EventBridge does not support using Amazon SQS queues that are encrypted with an AWS owned key. This includes targets, as well as Amazon SQS queues specified as dead-letter queues for targets.
For more information on AWS owned keys, see [AWS
owned keys](../../../kms/latest/developerguide/concepts.md#aws-owned-cmk "../../../kms/latest/developerguide/concepts.md#aws-owned-cmk") in the _AWS Key Management Service
Developer Guide_.
