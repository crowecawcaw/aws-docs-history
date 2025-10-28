# Run AWS Batch workloads with Step Functions

You can integrate Step Functions with AWS Batch to run batch computing workloads in the AWS cloud. This page lists the supported
AWS Batch APIs and provides an example `Task` state to perform a batch-processing task.

To learn about integrating with AWS services in Step Functions, see [Integrating services](integrate-services.md "integrate-services.md") and [Passing parameters to a service API in Step Functions](connect-parameters.md "connect-parameters.md").

###### Key features of Optimized AWS Batch integration

- The [Run a Job (.sync)](connect-to-resource.md#connect-sync "connect-to-resource.md#connect-sync") integration pattern is available.
  Note that there are no specific optimizations for the [Request Response](connect-to-resource.md#connect-default "connect-to-resource.md#connect-default") or [Wait for a Callback with Task Token](connect-to-resource.md#connect-wait-token "connect-to-resource.md#connect-wait-token") integration patterns.

The following shows an example `Task` state that submits an AWS Batch job and waits
for it to complete. Many of the arguments shown are optional.

```
"Submit Batch Job": {
    "Type": "Task",
    "Resource": "arn:aws:states:::batch:submitJob.sync",
    "Arguments": {
        "JobName": "`BATCH_NAME`",
        "JobQueue": "`BATCH_QUEUE_ARN`",
        "JobDefinition": "`BATCH_JOB_DEFINITION_ARN`",
        "ArrayProperties": {
        "Size": 10
        },
        "ContainerOverrides": {
        "ResourceRequirements": [
            {
            "Type": "VCPU",
            "Value": "4"
            }
        ]
        },
        "DependsOn": [
        {
            "JobId": "myJobId",
            "Type": "SEQUENTIAL"
        }
        ],
        "PropagateTags": true,
        "Arguments": {
        "Key1": "value1",
        "Key2": 100
        },
        "RetryStrategy": {
        "Attempts": 1
        },
        "Tags": {
        "Tag": "`TAG`"
        },
        "Timeout": {
        "AttemptDurationSeconds": 10
        }
    }
}
```

## Optimized AWS Batch APIs:

- [`SubmitJob`](../../../batch/latest/APIReference/API_SubmitJob.md "../../../batch/latest/APIReference/API_SubmitJob.md")

###### Parameters in Step Functions are expressed in PascalCase

Even if the native service API is in camelCase, for example the API action `startSyncExecution`, you specify parameters in PascalCase, such as: `StateMachineArn`.

## IAM policies for calling AWS Batch

The following example templates show how AWS Step Functions generates IAM policies based on the resources in your state machine definition. For more information, see [How Step Functions generates IAM policies for integrated
services](service-integration-iam-templates.md "service-integration-iam-templates.md") and [Discover service integration patterns in Step Functions](connect-to-resource.md "connect-to-resource.md").

Because job ids for `SubmitJob` and `TerminateJob` are generated and therefore only known at runtime, you cannot create a policy that restricts access based on a specific resource.

###### Tip for fine grained access

To add fine grained access to `SubmitJob` and `TerminateJob`, consider using tags for jobs and creating a policy that limits access based on your tags. In addition, the job queue, definition, and consumable resources can be restricted for `SubmitJob` using known resources.

Run a Job (.sync)

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "batch:SubmitJob",
 "batch:DescribeJobs",
 "batch:TerminateJob"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "events:PutTargets",
 "events:PutRule",
 "events:DescribeRule"
 ],
 "Resource": [
 "arn:aws:events:`us-east-1`:`123456789012`:rule/StepFunctionsGetEventsForBatchJobsRule"
 ]
 }
 ]
}`

```

Request Response

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "batch:SubmitJob"
 ],
 "Resource": "*"
 }
 ]
}`

```
