

# Migrating from Custom Event Bus - Classic to the Custom Event Bus
<a name="eb-custom-bus-migrate"></a>

Custom Event Bus - Classic remains available, and you can run both products side by side. Because the Custom Event Bus keeps the `events:` IAM namespace and the `events.amazonaws.com` service principal, your identity policies and delivery roles carry over. What changes is the routing model.


| Custom Event Bus - Classic | Custom Event Bus | 
| --- | --- | 
| A rule and one of its targets | One subscriber | 
| A rule with five targets | Five subscribers on the same bus | 
| Event pattern on a rule | A filter with a scope of DATA. When producers publish with PutEvents, the pattern is unchanged. | 
| Input transformer | A transformer with a type of JSONATA | 
| Dead-letter queue on a target | OnFailureConfiguration on the subscriber | 
| Retry policy on a target | RetryPolicy on the subscriber | 
| Archive and replay | Retention on the bus and a subscriber starting position | 
| Rules written by the bus owner for each consumer | Subscribers created by the consumers themselves | 
| events:PutEvents | events:PutEvents, plus events:PutRawEvents for non-JSON payloads | 

Four capabilities have no Custom Event Bus - Classic equivalent, so a migrated design can use them without a workaround: retention on the bus itself, a subscriber starting position, pause and resume with a backlog, and a second publish API for non-JSON payloads. You do not have to move everything: the two buses run side by side, a Custom Event Bus - Classic rule can target a Custom Event Bus, and a subscriber can target a Custom Event Bus - Classic, so you can move one consumer or one producer at a time. See [Event bus target: bus to bus](eb-custom-bus-target-bus.md).

## What does not change
<a name="eb-custom-bus-migrate-unchanged"></a>

The following stay the same, so the corresponding parts of your deployment carry over as they are.


| Unchanged | What it means for the move | 
| --- | --- | 
| IAM action namespace events: and the events.amazonaws.com service principal | Identity policies, bus resource policies, and delivery role trust policies are reused | 
| Target services: Amazon SQS, Lambda, Amazon SNS, Kinesis, Firehose, Step Functions, API Gateway, API destinations, event buses | Delivery roles keep the same target actions; each target has a parameter block with the same fields as its Classic counterpart. See [Targets for a Custom Event Bus subscriber](eb-custom-bus-targets.md) | 
| Event pattern syntax, except wildcards | Rule patterns become DATA filters unchanged for PutEvents traffic. See [Filtering events for a subscriber](eb-custom-bus-filtering.md) | 
| AWS service events and SaaS partner events | The same events reach a Custom Event Bus through an event source. See [Event sources for a Custom Event Bus](eb-custom-bus-event-sources.md) | 
| The PutEvents API and envelope | Producers change the endpoint and client, not the request | 
| Input transformation with JSONata | Expressions move to Transformer with the event under $events | 

## Defaults that differ
<a name="eb-custom-bus-migrate-defaults"></a>

**Important**  
A subscriber retries a failed delivery for 300 seconds and 5 attempts by default. A Custom Event Bus - Classic target retries for 24 hours and 185 attempts. If your consumers rely on a day of retries during an outage, set `RetryPolicy.MaxEventAgeInSeconds` to 86,400 and `MaxRetryAttempts` to 185 on each subscriber, and attach a dead-letter queue; otherwise events that fail for more than 5 minutes are dead-lettered rather than delivered late. See [Retry policies and dead-letter queues](eb-custom-bus-retry.md).

Two more defaults differ. A subscriber delivers a batch to a function or a state machine as a JSON array, where a rule delivered one event per invocation; set `BatchConfiguration.MaxBatchSize` to 1 to keep one event per call. And a bus retains events, so a subscriber created after an incident can read what it missed, where a rule created late saw nothing.

## Classic targets without a bespoke equivalent
<a name="eb-custom-bus-migrate-targets"></a>

Every Custom Event Bus - Classic target type that has no bespoke target on the Custom Event Bus is reached through a universal target that calls the service's API action. Set `TargetArn` to `arn:aws:events:::aws-sdk:{{service}}:{{apiAction}}` and build the request in `Input`; see [Universal targets for a Custom Event Bus](eb-custom-bus-universal-targets.md).


| Custom Event Bus - Classic target | Universal target action | 
| --- | --- | 
| Amazon ECS task | arn:aws:events:::aws-sdk:ecs:runTask | 
| AWS Batch job | arn:aws:events:::aws-sdk:batch:submitJob | 
| CodeBuild project | arn:aws:events:::aws-sdk:codebuild:startBuild | 
| CodePipeline pipeline | arn:aws:events:::aws-sdk:codepipeline:startPipelineExecution | 
| Systems Manager Run Command | arn:aws:events:::aws-sdk:ssm:sendCommand | 
| Systems Manager Automation | arn:aws:events:::aws-sdk:ssm:startAutomationExecution | 
| AWS Glue workflow | arn:aws:events:::aws-sdk:glue:startWorkflowRun | 
| SageMaker pipeline | arn:aws:events:::aws-sdk:sagemaker:startPipelineExecution | 
| Redshift Data API statement | arn:aws:events:::aws-sdk:redshiftdata:executeStatement | 
| CloudWatch Logs log group | arn:aws:events:::aws-sdk:cloudwatchlogs:putLogEvents | 
| Amazon EC2 actions (stop, reboot, terminate, create snapshot) | arn:aws:events:::aws-sdk:ec2:stopInstances, rebootInstances, terminateInstances, createSnapshot | 
| Inspector assessment | arn:aws:events:::aws-sdk:inspector:startAssessmentRun | 

The service and action names follow the universal-target naming rules; `CreateSubscriber` rejects a name it does not recognize, so confirm each one when you create the subscriber.

## Migration sequence
<a name="eb-custom-bus-migrate-steps"></a>

Move one bus at a time, in five steps, keeping the Custom Event Bus - Classic rules running until the last step. Each step is reversible until you delete the rules.

**Important**  
A pattern copied from a rule matches events published with `PutEvents`, because that API produces the same envelope as Custom Event Bus - Classic. The same pattern matches nothing on events published with `PutRawEvents`, because the payload is not nested under `detail`. See [Event structure: data, metadata, and system metadata](eb-custom-bus-addressing.md).

1. Create the Custom Event Bus with the retention period that you want, and wait for its state to become `ACTIVE`.

1. For each rule, create one subscriber for each of its targets. Use the rule's event pattern as a `DATA` filter, its input transformer as a `JSONATA` transformer, and its target role as the `RoleArn`. Attach a dead-letter queue and turn on logs before you send traffic.

1. Publish to both buses from your producers, and confirm at each target that both paths deliver the same events.

1. Move producers to the Custom Event Bus only.

1. Disable the rules on the Custom Event Bus - Classic. Delete them after the retry window and your own verification period have passed.