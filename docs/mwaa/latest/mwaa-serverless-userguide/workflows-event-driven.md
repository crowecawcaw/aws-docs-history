

# Start workflow runs with Amazon EventBridge events

You can start an Amazon MWAA Serverless workflow run automatically when an event occurs, instead of on a schedule or on demand. For example, you can start a run when a file arrives in an Amazon S3 bucket, when an AWS Glue job succeeds, when another Amazon MWAA Serverless workflow succeeds, or when your own application sends an event. You don't write or run any code to connect the event to the workflow.

To do this, you use an Amazon EventBridge *Custom Event Bus*. You create a *subscriber* on the bus that matches the events you're interested in. The subscriber uses a *universal target* to call the Amazon MWAA Serverless [`StartWorkflowRun`](https://docs.aws.amazon.com/mwaa-serverless/latest/APIReference/API_StartWorkflowRun.html) operation for each matching event. It can also pass values from the event to the workflow run as parameters.

**Important**  
This feature uses the EventBridge [Custom Event Bus](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-custom-bus.html), not the default event bus or a Custom Event Bus - Classic. Rules on the default bus and on a Custom Event Bus - Classic can't target an Amazon MWAA Serverless workflow directly. The Custom Event Bus is available in a subset of AWS Regions. The bus must be in the same Region as your workflow, because the subscriber calls `StartWorkflowRun` in the Region of the bus. Before you start, confirm that the Custom Event Bus is available in the Region of your workflow. For the list of Regions, refer to [Amazon EventBridge feature availability by AWS Region](https://docs.aws.amazon.com/eventbridge/latest/userguide/feature-availability.html) in the *Amazon EventBridge User Guide*.

**Topics**
+ [How event-driven workflow runs work](#workflows-event-driven-how)
+ [Prerequisites](#workflows-event-driven-prereqs)
+ [Set up an event-driven workflow](#workflows-event-driven-setup)
+ [Batch events](#workflows-event-driven-batching)
+ [Avoid duplicate workflow runs](#workflows-event-driven-duplicates)
+ [Identify runs started by events](#workflows-event-driven-identify)
+ [Example: Start a run when another workflow succeeds](#workflows-event-driven-examples)
+ [Troubleshoot event-driven workflow runs](#workflows-event-driven-troubleshooting)

## How event-driven workflow runs work
<a name="workflows-event-driven-how"></a>

An event-driven workflow run uses the following EventBridge resources. All of them are in the AWS account and Region of the workflow. To use events from other AWS accounts, share the bus with those accounts. For more information, refer to [Sharing a Custom Event Bus with other accounts](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-custom-bus-sharing.html). To use events from another Region, forward them to a Custom Event Bus in the Region of the workflow. For more information, refer to [Event bus target: bus to bus](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-custom-bus-target-bus.html).
+ **Custom Event Bus.** The bus receives and retains events. For more information, refer to [What is the EventBridge Custom Event Bus?](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-custom-bus-what-is.html)
+ **Event source (for AWS service events).** AWS services publish their events to the default event bus of your account. For the AWS services that send events and the events that each one sends, refer to [Events](https://docs.aws.amazon.com/eventbridge/latest/ref/events.html) in the *Amazon EventBridge Events Reference*. An event source brings the events of one AWS service onto your Custom Event Bus. Your own applications publish to the Custom Event Bus directly and don't need an event source. For more information, refer to [Event sources for a Custom Event Bus](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-custom-bus-event-sources.html).
+ **Subscriber.** A subscriber filters the events on the bus and delivers each match to one target. The subscriber also defines batching, retries, and a dead-letter queue. For more information, refer to [Subscribing to events on a Custom Event Bus](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-custom-bus-subscribers.html).
+ **Universal target.** Use a universal target to call an AWS API operation directly. To start a workflow run, set the target to `arn:aws:events:::aws-sdk:mwaaserverless:startWorkflowRun`. You provide the `StartWorkflowRun` request as a JSONata expression that can read values from the event. For more information, refer to [Universal targets for a Custom Event Bus](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-custom-bus-universal-targets.html).
+ **Delivery role.** EventBridge assumes an IAM role that you create to call `StartWorkflowRun`. The role must allow `airflow-serverless:StartWorkflowRun` on the workflow.

When an event occurs, the following happens:

1. The event arrives on the Custom Event Bus, through an event source or from a `PutEvents` call.

1. The subscriber's filter matches the event.

1. EventBridge assumes the delivery role and calls `StartWorkflowRun` with the request that your expression builds from the event.

1. Amazon MWAA Serverless starts a workflow run of the current version of the workflow, with the parameters from the request. If the request uses the event ID as the client token, a repeated delivery of the same event returns the existing run instead of starting a new one. Because the run starts through `StartWorkflowRun`, its run type is `ON_DEMAND`, the same as a run that you start from the console or the AWS CLI. To find out which runs an event started, refer to [Identify runs started by events](#workflows-event-driven-identify).

1. If the call fails, EventBridge retries it according to the subscriber's retry policy. After the last retry, EventBridge sends a record of the event to the dead-letter queue.

Each subscriber evaluates every event on its own. A subscriber can't wait for several different events, for example two upstream jobs, before it starts a run. If a run depends on several jobs, run those jobs as tasks in the same workflow, so that the workflow controls the dependencies between them.

## Prerequisites
<a name="workflows-event-driven-prereqs"></a>
+ **A workflow.** The workflow can't be **Disabled**, because a disabled workflow rejects all runs. A workflow can be scheduled and event-driven at the same time. For instructions, refer to [Manage your Amazon MWAA Serverless workflows](workflows.md#workflows-manage).
+ **A supported Region.** The Custom Event Bus must be available in the Region of your workflow. Refer to [Amazon EventBridge feature availability by AWS Region](https://docs.aws.amazon.com/eventbridge/latest/userguide/feature-availability.html).
+ **The AWS CLI version that supports the Custom Event Bus.** The examples in this topic use the `aws eventsv2` commands, which manage the Custom Event Bus. Update the AWS CLI to the latest version. For the command reference, refer to [eventsv2](https://docs.aws.amazon.com/cli/latest/reference/eventsv2/index.html) in the *AWS CLI Command Reference*.
+ **An Amazon SQS standard queue for failed events.** Configure a dead-letter queue for the subscriber, so that you can find events that didn't start a run.
+ **Parameters in the workflow definition (optional).** To pass values from the event to the run, declare them under `params` in the workflow definition.

## Set up an event-driven workflow
<a name="workflows-event-driven-setup"></a>

The following procedure starts a workflow run each time an AWS Glue job succeeds. To use another event, change the event source and the subscriber's filter. For an example that starts a run when another workflow succeeds, refer to [Example: Start a run when another workflow succeeds](#workflows-event-driven-examples).

Replace the Region, account ID, workflow ARN, job name, and resource names in the examples with your own.

**To start a workflow run when an AWS Glue job succeeds**

1. **Create the delivery role.** Create an IAM role with the following JSON trust policy. The `aws:SourceAccount` condition allows only EventBridge resources in your account to assume the role. For more information, refer to [Cross-service confused deputy prevention](cross-service-confused-deputy-prevention.md).

   ```json
   {
     "Version": "2012-10-17", 		 	 	 
     "Statement": [
       {
         "Effect": "Allow",
         "Principal": { "Service": "events.amazonaws.com" },
         "Action": "sts:AssumeRole",
         "Condition": { "StringEquals": { "aws:SourceAccount": "{{111122223333}}" } }
       }
     ]
   }
   ```

   Attach the following permissions policy to the role. The first statement allows the role to start runs of the workflow. The second statement allows EventBridge to write failed events to the dead-letter queue.

   ```json
   {
     "Version": "2012-10-17", 		 	 	 
     "Statement": [
       {
         "Effect": "Allow",
         "Action": "airflow-serverless:StartWorkflowRun",
         "Resource": "arn:aws:airflow-serverless:{{us-east-1}}:{{111122223333}}:workflow/{{my-workflow-a1b2c3d4e5}}"
       },
       {
         "Effect": "Allow",
         "Action": "sqs:SendMessage",
         "Resource": "arn:aws:sqs:{{us-east-1}}:{{111122223333}}:{{my-workflow-events-dlq}}"
       }
     ]
   }
   ```

1. **Create a Custom Event Bus.** Run the following [`create-event-bus`](https://docs.aws.amazon.com/cli/latest/reference/eventsv2/create-event-bus.html) command. Note the `EventBusArn` in the output. A Custom Event Bus ARN has the form `arn:aws:events:{{region}}:{{account-id}}:event-busv2/{{bus-name}}/{{bus-id}}`. For more information, refer to [Names, endpoints, and IAM permissions for the Custom Event Bus](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-custom-bus-names.html). For more options, such as retention and encryption, refer to [Creating a bus](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-custom-bus-create.html).

   ```bash
   aws eventsv2 create-event-bus \
       --name {{orchestration-bus}} \
       --region {{us-east-1}}
   ```

1. **Bring the AWS Glue events onto the bus.** Run the following [`create-event-source`](https://docs.aws.amazon.com/cli/latest/reference/eventsv2/create-event-source.html) command to create an event source for `aws.glue`. The pattern admits only job state change events.

   ```bash
   aws eventsv2 create-event-source \
       --name {{glue-job-events}} \
       --event-bus-arn {{arn:aws:events:us-east-1:111122223333:event-busv2/orchestration-bus/EXAMPLE1234567890abcdef}} \
       --configuration '{"AwsServiceEventsConfiguration": {"AwsService": "aws.glue", "Pattern": "{\"detail-type\": [\"Glue Job State Change\"]}"}}' \
       --region {{us-east-1}}
   ```

   If your application publishes its own events, it calls `PutEvents` on the Custom Event Bus instead, and you can skip this step. For more information, refer to [Publishing events to a Custom Event Bus](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-custom-bus-publish.html).

1. **Create the subscriber.** Run the following [`create-subscriber`](https://docs.aws.amazon.com/cli/latest/reference/eventsv2/create-subscriber.html) command. The subscriber matches `SUCCEEDED` events for the job {{my-glue-job}} and starts a run of the workflow for each one.

   ```bash
   aws eventsv2 create-subscriber \
       --name {{start-my-workflow}} \
       --event-bus-arn {{arn:aws:events:us-east-1:111122223333:event-busv2/orchestration-bus/EXAMPLE1234567890abcdef}} \
       --filter-configuration '{
           "Filters": [
               { "Scope": "SYSTEM_METADATA", "Pattern": "{\"aws:Source\": [\"aws.glue\"]}" },
               { "Scope": "DATA", "Pattern": "{\"detail-type\": [\"Glue Job State Change\"], \"detail\": {\"jobName\": [\"{{my-glue-job}}\"], \"state\": [\"SUCCEEDED\"]}}" }
           ]
       }' \
       --invoke-configuration '{
           "TargetArn": "arn:aws:events:::aws-sdk:mwaaserverless:startWorkflowRun",
           "RoleArn": "{{arn:aws:iam::111122223333:role/my-workflow-events-role}}",
           "UniversalTargetParameters": {
               "Input": "{% {\"WorkflowArn\": \"{{arn:aws:airflow-serverless:us-east-1:111122223333:workflow/my-workflow-a1b2c3d4e5}}\", \"ClientToken\": $events[0].SystemMetadata.`aws:EventId`, \"OverrideParameters\": {\"glue_job_run_id\": $events[0].Data.detail.jobRunId}} %}"
           }
       }' \
       --batch-configuration '{"MaxBatchSize": 1, "MaxBatchWindowInSeconds": 0}' \
       --retry-policy '{"MaxRetryAttempts": 5, "MaxEventAgeInSeconds": 3600}' \
       --on-failure-configuration '{"Arn": "{{arn:aws:sqs:us-east-1:111122223333:my-workflow-events-dlq}}"}' \
       --region {{us-east-1}}
   ```

   The subscriber uses the following settings:
   + `FilterConfiguration` – The `SYSTEM_METADATA` filter matches only events that AWS Glue produced. The `DATA` filter matches the job name and state. For the filter syntax, refer to [Filtering events for a subscriber](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-custom-bus-filtering.html).
   + `TargetArn` – The universal target for `StartWorkflowRun`. The ARN has no Region or account ID.
   + `Input` – The `StartWorkflowRun` request, as a JSONata expression between `{%` and `%}`. `$events` is an array of the events in the batch. `WorkflowArn` is required. `ClientToken` uses the event ID so that EventBridge retries don't start duplicate runs. `OverrideParameters` passes the job run ID to the workflow as a parameter. In events from an event source or `PutEvents`, the event's fields are under `Data.detail`. For more information, refer to [Event structure: data, metadata, and system metadata](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-custom-bus-addressing.html) and [Avoid duplicate workflow runs](#workflows-event-driven-duplicates).
   + `BatchConfiguration` – Starts one run for each event. If you don't set it, the subscriber can deliver up to 10 events in one call, which starts only one run. For more information, refer to [Batch events](#workflows-event-driven-batching).
   + `RetryPolicy` and `OnFailureConfiguration` – How long EventBridge retries a failed call, and where it sends events that it can't deliver. For more information, refer to [Retry policies and dead-letter queues](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-custom-bus-retry.html).

1. **Verify the setup.** Run the AWS Glue job. After the job succeeds, list the runs of the workflow. A new run appears within a few seconds to a minute.

   ```bash
   aws mwaa-serverless list-workflow-runs \
       --workflow-arn {{arn:aws:airflow-serverless:us-east-1:111122223333:workflow/my-workflow-a1b2c3d4e5}} \
       --region {{us-east-1}}
   ```

   If no run appears, check the dead-letter queue and the subscriber's metrics. For more information, refer to [Troubleshoot event-driven workflow runs](#workflows-event-driven-troubleshooting).

You can also create these resources with CloudFormation. For more information, refer to [Creating Custom Event Bus resources with CloudFormation](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-custom-bus-cloudformation.html).

## Batch events
<a name="workflows-event-driven-batching"></a>

When many similar events arrive close together, for example many files in an Amazon S3 prefix, you can start one run for a group of events. The subscriber collects events into a batch and calls `StartWorkflowRun` once for each batch, so each batch starts one run. Batching reduces the number of runs and lets one run process several events.

Set batching in the subscriber's `BatchConfiguration`:



| Setting | Valid values | Description | 
| --- | --- | --- | 
| MaxBatchSize | 1–500. The default is 10. | The maximum number of events in a batch. | 
| MaxBatchWindowInSeconds | 0–300. The default is 0. | The maximum time to wait for a batch to fill. | 

The subscriber starts a run when the batch reaches `MaxBatchSize` or when `MaxBatchWindowInSeconds` ends, whichever comes first. A batch can contain fewer events than `MaxBatchSize`, including a single event. Batching doesn't wait for a specific number or combination of events. You can't raise these limits. For more information, refer to [Batching and the $events array](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-custom-bus-universal-targets.html#eb-custom-bus-universal-targets-batching) and [Custom Event Bus quotas](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-quota.html#eb-custom-bus-quotas).

## Avoid duplicate workflow runs
<a name="workflows-event-driven-duplicates"></a>

Because events can be delivered more than once, `StartWorkflowRun` might be called more than once for the same event, for example after a timeout. To make repeated calls safe, set `ClientToken` to the event ID, `$events[0].SystemMetadata.`aws:EventId``. When Amazon MWAA Serverless receives a request with a client token that it has already seen for the same request, it returns the existing run instead of starting a new one.

Amazon MWAA Serverless remembers a client token for 8 hours. Set the subscriber's `RetryPolicy.MaxEventAgeInSeconds` to 28800 or less, so that EventBridge stops retrying an event before Amazon MWAA Serverless forgets its client token.

Use a value that is unique to each event, such as the event ID. If you use the same client token for different requests, for example a fixed string, Amazon MWAA Serverless rejects the later requests with a `ConflictException`.

## Identify runs started by events
<a name="workflows-event-driven-identify"></a>

A run that an EventBridge subscriber starts has the run type `ON_DEMAND`, because EventBridge starts it with `StartWorkflowRun`. To find the runs that EventBridge started, look for `StartWorkflowRun` events in AWS CloudTrail. In each event record:
+ `userIdentity.arn` is the delivery role, with a session name that starts with `AssumedByEventBridge`, for example `arn:aws:sts::{{111122223333}}:assumed-role/{{my-workflow-events-role}}/AssumedByEventBridge.{{a1b2c3d4}}`.
+ `requestParameters.clientToken` is the event ID, if the subscriber uses the event ID as the client token.
+ `responseElements.runId` is the ID of the run that the call started.

For more information, refer to [Logging Amazon MWAA Serverless APIs with CloudTrail](log-apis-with-cloudtrail.md).

## Example: Start a run when another workflow succeeds
<a name="workflows-event-driven-examples"></a>

Amazon MWAA Serverless sends workflow run and task state change events to EventBridge. For the events and their fields, refer to [Amazon MWAA Serverless events](https://docs.aws.amazon.com/eventbridge/latest/ref/events-ref-airflow-serverless.html) in the *Amazon EventBridge Events Reference*.

To start a downstream workflow when an upstream workflow succeeds, follow the procedure in [Set up an event-driven workflow](#workflows-event-driven-setup) with the following values.

In step 3, create an event source for `aws.airflow-serverless` with the following configuration:

```json
{"AwsServiceEventsConfiguration": {"AwsService": "aws.airflow-serverless", "Pattern": "{\"detail-type\": [\"MWAA Serverless Workflow Run Succeeded\"]}"}}
```

In step 4, use the following `FilterConfiguration`. Replace the ARN with the ARN of the upstream workflow:

```json
{
  "Filters": [
    { "Scope": "SYSTEM_METADATA", "Pattern": "{\"aws:Source\": [\"aws.airflow-serverless\"]}" },
    { "Scope": "DATA", "Pattern": "{\"detail-type\": [\"MWAA Serverless Workflow Run Succeeded\"], \"resources\": [\"{{arn:aws:airflow-serverless:us-east-1:111122223333:workflow/upstream-workflow-f6g7h8i9j0}}\"]}" }
  ]
}
```

In step 4, use the following `Input`. Replace the ARN with the ARN of the downstream workflow. The downstream workflow declares `upstream_run_id` under `params` in its workflow definition.

```
{% {
  "WorkflowArn": "{{arn:aws:airflow-serverless:us-east-1:111122223333:workflow/downstream-workflow-a1b2c3d4e5}}",
  "ClientToken": $events[0].SystemMetadata.`aws:EventId`,
  "OverrideParameters": { "upstream_run_id": $events[0].Data.detail.workflowRunId }
} %}
```

**Important**  
Don't let a workflow start itself. If the filter matches the downstream workflow's own events, each run starts another run. Always filter on the upstream workflow's ARN in `resources`.

The event source also brings AWS CloudTrail events for Amazon MWAA Serverless API calls onto the bus, with the detail type `AWS API Call via CloudTrail`. Keep `detail-type` in the event source pattern or the subscriber filter so that only state change events match.

## Troubleshoot event-driven workflow runs
<a name="workflows-event-driven-troubleshooting"></a>

If an event doesn't start a workflow run, check the following:
+ **The dead-letter queue.** When a call to `StartWorkflowRun` fails after all retries, EventBridge sends a record to the dead-letter queue. The record's `errorMessage` contains the error that Amazon MWAA Serverless returned. Amazon MWAA Serverless returns all client errors, including access denied errors, with HTTP status 400, so EventBridge reports them with the error code `CUSTOMER_VALIDATION`. Read `errorMessage` for the cause.
+ **The filter.** A filter that is written for the wrong event structure matches nothing, without an error. Check the subscriber's `FilterEvaluated` and `FilterMatched` metrics, and turn on subscriber logs to see the request that EventBridge sent. For more information, refer to [Observability for the Custom Event Bus: metrics, logs, and CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-custom-bus-observability.html).