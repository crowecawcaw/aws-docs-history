

# Event bus targets in Amazon EventBridge
<a name="eb-targets"></a>

A *target* is a resource or endpoint that EventBridge sends an [event](eb-events.md) to when the event matches the event pattern defined for a [rule](eb-rules.md). **The rule processes the [event](eb-events.md) data and sends the pertinent information to the target. To deliver event data to a target, EventBridge needs permission to access the target resource. You can define up to five targets for each rule.

When you add targets to a rule and that rule runs soon after, any new or updated targets might not be immediately invoked. Allow a short period of time for changes to take effect.

## Event bus targets available in the EventBridge console
<a name="eb-console-targets"></a>

You can configure the following target types for rules in the EventBridge console:
+ API destinations

  API destinations are HTTPS endpoints that you can invoke as the target of an event bus rule. When you specify an API destination as a rule target, EventBridge invokes the HTTPS endpoint for any event that matches the event pattern specified in the rule, and then delivers the event information with the request. For more information, see [API destinations](eb-api-destinations.md).
+ Event buses

  You can specify other event buses as targets for rules. This includes event buses in the same or different AWS accounts.
  + [Cross-account event buses as targets](eb-cross-account.md)
  + [Same account event buses as targets](eb-bus-to-bus.md)
+ AWS services

  You can have EventBridge send events to a number of AWS service resources. These include:
  + [API Gateway](eb-api-gateway-target.md)
  + [AWS AppSync](target-appsync.md)
  + [Batch job queue](#targets-specifics-batch)
  + [CloudWatch log group](#targets-specifics-cwl)
  + [CodeBuild project](#targets-specifics-codebuild)
  + CodePipeline
  + Amazon EBS `CreateSnapshot` API call
  + EC2 Image Builder
  + EC2 `RebootInstances` API call
  + EC2 `StopInstances` API call
  + EC2 `TerminateInstances` API call
  + [ECS task](#targets-specifics-ecs-task)
  + Firehose delivery stream
  + Glue workflow
  + [Incident Manager response plan](https://docs.aws.amazon.com//incident-manager/latest/userguide/incident-creation.html#incident-tracking-auto-eventbridge)
  + Inspector assessment template
  + Kinesis stream
  + Lambda function (ASYNC)
  + [Amazon Redshift cluster data API queries](https://docs.aws.amazon.com/redshift/latest/mgmt/data-api-calling-event-bridge.html) 
  + [Amazon Redshift Serverless workgroup data API queries](https://docs.aws.amazon.com/redshift/latest/mgmt/data-api-calling-event-bridge.html)
  + SageMaker AI Pipeline
  + Amazon SNS topic
  + [Amazon SQS standard, fair, and FIFO queues](#targets-specifics-sqs)
  + Step Functions state machine (ASYNC)
  + Systems Manager Automation
  + Systems Manager OpsItem
  + Systems Manager Run Command

## Target parameters
<a name="targets-specific-parms"></a>

Some targets don't send the information in the event payload to the target, instead, they treat the event as a trigger for invoking a specific API. EventBridge uses the [Target](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_Target.html) parameters to determine what happens with that target. These include the following:
+ API destinations

  The data sent to an API destination must match the structure of the API. Use the [`InputTransformer`](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_InputTransformer.html) object to make sure the data is structured correctly. If you want to include the original event payload, reference it in the [`InputTransformer`](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_InputTransformer.html).
+ API Gateway 

  The data sent to API Gateway must match the structure of the API. Use the [`InputTransformer`](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_InputTransformer.html) object to make sure the data is structured correctly. If you want to include the original event payload, reference it in the [`InputTransformer`](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_InputTransformer.html).
+ Amazon EC2 Image Builder
+ Amazon Redshift Data API clusters

  Use [`RedshiftDataParameters`](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_RedshiftDataParameters.html).
+ Amazon SageMaker Runtime Model Building Pipelines

  Use [`SageMakerPipelineParameters`](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_SageMakerPipelineParameters.html).
+ Amazon SQS fair and FIFO queues

  Use [`SqsParameters`](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_SqsParameters.html) to specify the message group to use as the target.
+ Systems Manager Run Command

  Use [`RunCommandParameters`](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_RunCommandParameters.html) to specify the SSM document and target instances. For more information, see [Systems Manager Run Command as a target](#targets-specifics-ssm-run-command).

**Note**  
EventBridge does not support all JSON Path syntax and evaluate it at runtime. Supported syntax includes:   
dot notation (for example,`$.detail`)
dashes
underscores
alphanumeric characters
array indices
wildcards (\*)
forward slashes

### Dynamic path parameters
<a name="dynamic-path-parameters"></a>

Dynamic path parameters let you use JSON path syntax to reference event data at runtime instead of static values.

You can use dynamic JSON path syntax with target parameters to specify JSON paths instead of static values (for example, `$.detail.state`).

#### Requirements
<a name="requirements"></a>

The entire value must be a JSON path, not just part of it. For example:
+ ✓ Correct: `RedshiftParameters.Sql` can be `$.detail.state`
+ ✗ Incorrect: `RedshiftParameters.Sql` cannot be `"SELECT * FROM $.detail.state"`

EventBridge replaces these paths at runtime with data from the event payload at the specified path.

#### Limitations
<a name="limitations"></a>

Dynamic path parameters cannot reference new or transformed values from input transformation. The JSON path syntax is the same as input transformation syntax. For more information, see [Amazon EventBridge input transformation](eb-transform-target-input.md).

#### Supported parameters
<a name="supported-parameters"></a>

You can use dynamic syntax on all string, non-enum fields of these parameters:
+ [`EcsParameters`](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_EcsParameters.html)
+ [`HttpParameters`](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_HttpParameters.html) (except `HeaderParameters` keys)
+ [`RedshiftDataParameters`](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_RedshiftDataParameters.html)
+ [`SageMakerPipelineParameters`](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_SageMakerPipelineParameters.html)
+ [`SqsParameters`](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_SqsParameters.html)

## Permissions
<a name="targets-permissions"></a>

To make API calls on the resources that you own, EventBridge needs appropriate permissions. Specify an IAM execution role [using the EventBridge console](eb-create-rule-wizard.md#eb-create-rule-target), or by setting the `RoleARN` parameter in [`PutTargets`](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_PutTargets.html).

For example, the following policy defines permission to send messages to an Amazon SQS queue:

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "sqs:SendMessage"
            ],
            "Resource": [
                "arn:aws:sqs:{{us-east-1}}:{{111122223333}}:{{sqs-queue-name}}"
            ]
        }
    ]
}
```

------

And the following trust policy enables EventBridge to assume the role:

------
#### [ JSON ]

****  

```
{
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
}
```

------

You can invoke an API Gateway endpoint with configured IAM authorization, but the role is optional if you haven't configured authorization. For more information, see [Amazon EventBridge and AWS Identity and Access Management](eb-iam.md).

If another account is in the same Region and has granted you permission, then you can send events to that account. 

For more information, see [Sending and receiving events between AWS accounts in Amazon EventBridge](eb-cross-account.md). 

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
<a name="targets-specifics-batch"></a>

Certain parameters to AWS Batch `submitJob` can be configured via [BatchParameters](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_BatchParameters.html).

Others can be specified in the event payload. If the event payload (passed through or via [InputTransformers](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-transform-target-input.html)) contains the following keys, they are mapped to `submitJob` [request parameters](https://docs.aws.amazon.com/batch/latest/APIReference/API_SubmitJob.html#API_SubmitJob_RequestSyntax):
+ `ContainerOverrides: containerOverrides`
**Note**  
This includes only command, environment, memory, and vcpus
+ `DependsOn: dependsOn`
**Note**  
This includes only jobId
+ `Parameters: parameters`

## CloudWatch Logs groups as targets
<a name="targets-specifics-cwl"></a>

If you don’t use an [InputTransformer](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-transform-target-input.html) with a CloudWatch Logs target, the event payload is used as the log message, and the source of the event as the timestamp. If you do use an InputTransformer, the template must be:

`{"timestamp":<timestamp>,"message":<message>}`

EventBridge batches the entries sent to a log stream; therefore, EventBridge may deliver a single or multiple events to a log stream, depending on traffic.

## CodeBuild projects as targets
<a name="targets-specifics-codebuild"></a>

EventBridge supports both standard and batch builds as targets. 

If you use an [input transformer](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-transform-target-input.html) to shape the source event to match the [StartBuildRequest](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_StartBuild.html#API_StartBuild_RequestSyntax) structure before it is delivered to a CodeBuild target, the parameters will be mapped 1-to-1 and passed through to `codeBuild.StartBuild` by default. 

To pass the parameters to `codeBuild.StartBuildBatch` instead, transform the source event to match the [StartBuildBatchRequest](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_StartBuildBatch.html#API_StartBuildBatch_RequestSyntax) structure, and add the following key/value pair to the root of the transformed event:

`"buildType": "BATCH"`

## Amazon ECS tasks as targets
<a name="targets-specifics-ecs-task"></a>

If you use [InputTransformers](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-transform-target-input.html) to shape the input event to a Target to match the Amazon ECS RunTask [TaskOverride](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_TaskOverride.html) structure, the parameters will be mapped 1-to-1 and passed through to `ecs.RunTask`.

## Incident Manager response plans as targets
<a name="targets-specifics-incident-manager"></a>

If the matched event came from CloudWatch Alarms, the alarm state change details are populated into the trigger details of the StartIncidentRequest call to Incident Manager.

## Systems Manager Run Command as a target
<a name="targets-specifics-ssm-run-command"></a>

When you specify Systems Manager Run Command as a target, EventBridge calls the [`SendCommand`](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_SendCommand.html) API on your behalf. Configure the target using [`RunCommandParameters`](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_RunCommandParameters.html), which specifies the SSM document to run and the target instances or tags.

`RunCommandParameters` contains the following fields:
+ `RunCommandTargets` — (Required) A list of key-value pairs that specify the target instances. Use `Key` set to `InstanceIds` with a list of instance IDs, or `Key` set to `tag:{{tag-name}}` with tag values to target instances by tag. You can specify between 1 and 5 run command targets.

To specify which SSM document to run and pass parameters to it, use the `Input` field on the [`Target`](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_Target.html) object. The `Input` value must be a JSON object with the following structure:

```
{
  "DocumentName": "{{document-name}}",
  "DocumentVersion": "{{version}}",
  "Parameters": {
    "{{parameter-key}}": ["{{parameter-value}}"]
  }
}
```

Where:
+ `DocumentName` — The name or ARN of the SSM document to run.
+ `DocumentVersion` — (Optional) The version of the document. If omitted, the default version is used.
+ `Parameters` — (Optional) A map of parameter names to value arrays, matching the parameters defined in the SSM document.

For example, the following AWS CLI command creates a rule that runs the `AWS-RunShellScript` document on a specific instance when an EventBridge event matches:

```
aws events put-targets --rule "my-rule" --targets '[{
  "Id": "ssm-target-1",
  "Arn": "arn:aws:ssm:{{region}}:{{account-id}}:document/AWS-RunShellScript",
  "RoleArn": "arn:aws:iam::{{account-id}}:role/{{EventBridgeSSMRole}}",
  "Input": "{\\"Parameters\\":{\\"commands\\":[\\"echo Hello from EventBridge\\"]}}",
  "RunCommandParameters": {
    "RunCommandTargets": [{
      "Key": "InstanceIds",
      "Values": ["{{i-0123456789abcdef0}}"]
    }]
  }
}]'
```

**Note**  
The `Input` field on the `Target` object is used to pass the document name and parameters to Systems Manager Run Command. This is different from the [`InputTransformer`](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_InputTransformer.html), which transforms the event payload. When using Systems Manager Run Command as a target, set the document parameters in `Input` and specify the target instances in `RunCommandParameters`.

## Amazon SQS queues as targets
<a name="targets-specifics-sqs"></a>

EventBridge does not support using Amazon SQS queues that are encrypted with an AWS owned key. This includes targets, as well as Amazon SQS queues specified as dead-letter queues for targets. For more information on AWS owned keys, see [AWS owned keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-owned-cmk) in the *AWS Key Management Service Developer Guide*.