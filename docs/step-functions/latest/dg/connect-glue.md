# Start an AWS Glue job with Step Functions

Learn to use Step Functions to start a job run on AWS Glue. This page lists the supported API actions and provides an
example `Task` state to start a AWS Glue job.

To learn about integrating with AWS services in Step Functions, see [Integrating services](integrate-services.md "integrate-services.md") and [Passing parameters to a service API in Step Functions](connect-parameters.md "connect-parameters.md").

###### Key features of Optimized AWS Glue integration

- The [Run a Job (.sync)](connect-to-resource.md#connect-sync "connect-to-resource.md#connect-sync") integration pattern is available.
- The `JobName` field is extracted from the request and inserted into the response, which normally only contains `JobRunID`.
  The following includes a `Task` state that starts an AWS Glue job.

```
"Glue StartJobRun": {
      "Type": "Task",
      "Resource": "arn:aws:states:::glue:startJobRun.sync",
      "Arguments": {
        "JobName": "GlueJob-JTrRO5l98qMG"
      },
      "Next": "ValidateOutput"
    },

```

###### Parameters in Step Functions are expressed in PascalCase

Even if the native service API is in camelCase, for example the API action `startSyncExecution`, you specify parameters in PascalCase, such as: `StateMachineArn`.

## Optimized AWS Glue APIs

- [`StartJobRun`](../../../glue/latest/dg/aws-glue-api-jobs-runs.md#aws-glue-api-jobs-runs-StartJobRun "../../../glue/latest/dg/aws-glue-api-jobs-runs.md#aws-glue-api-jobs-runs-StartJobRun")

## IAM policies for calling AWS Glue

The following example templates show how AWS Step Functions generates IAM policies based on the resources in your state machine definition. For more information, see [How Step Functions generates IAM policies for integrated
services](service-integration-iam-templates.md "service-integration-iam-templates.md") and [Discover service integration patterns in Step Functions](connect-to-resource.md "connect-to-resource.md").

AWS Glue does not have resource-based control.

Run a Job (.sync)

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "glue:StartJobRun",
 "glue:GetJobRun",
 "glue:GetJobRuns",
 "glue:BatchStopJobRun"
 ],
 "Resource": "*"
 }
 ]
}`

```

Request Response and Callback (.waitForTaskToken)

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "glue:StartJobRun"
 ],
 "Resource": "*"
 }
 ]
}`

```
