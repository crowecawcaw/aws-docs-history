# Start AWS Glue DataBrew jobs with Step Functions

Learn how you can use the DataBrew integration to add data cleaning and
data normalization steps into your analytics and machine learning workflows with Step Functions.

To learn about integrating with AWS services in Step Functions, see [Integrating services](integrate-services.md "integrate-services.md") and [Passing parameters to a service API in Step Functions](connect-parameters.md "connect-parameters.md").

The following includes a `Task` state that starts a request-response DataBrew
job.

```
"DataBrew StartJobRun": {
            "Type": "Task",
            "Resource": "arn:aws:states:::databrew:startJobRun",
            "Arguments": {
               "Name": "sample-proj-job-1"
            },
            "Next": "NEXT_STATE"
          },

```

The following includes a `Task` state that starts a sync DataBrew job.

```
"DataBrew StartJobRun": {
           "Type": "Task",
           "Resource": "arn:aws:states:::databrew:startJobRun.sync",
           "Arguments": {
              "Name": "sample-proj-job-1"
           },
           "Next": "NEXT_STATE"
          },

```

###### Parameters in Step Functions are expressed in PascalCase

Even if the native service API is in camelCase, for example the API action `startSyncExecution`, you specify parameters in PascalCase, such as: `StateMachineArn`.

## Supported DataBrew APIs

- `StartJobRun`

## IAM policies for calling DataBrew

The following example templates show how AWS Step Functions generates IAM policies based on the resources in your state machine definition. For more information, see [How Step Functions generates IAM policies for integrated
services](service-integration-iam-templates.md "service-integration-iam-templates.md") and [Discover service integration patterns in Step Functions](connect-to-resource.md "connect-to-resource.md").

Run a Job (.sync)

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "databrew:startJobRun",
 "databrew:listJobRuns",
 "databrew:stopJobRun"
 ],
 "Resource": [
 "arn:aws:databrew:`us-east-1`:`123456789012`:job/*"
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
 "databrew:startJobRun"
 ],
 "Resource": [
 "arn:aws:databrew:`us-east-1`:`123456789012`:job/*"
 ]
 }
 ]
}`

```
