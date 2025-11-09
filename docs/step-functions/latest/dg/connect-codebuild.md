# Manage AWS CodeBuild builds with Step Functions

You can integrate Step Functions with AWS CodeBuild to start, stop, and manage builds. This page lists the supported
CodeBuild APIs you can use with Step Functions.

To learn about integrating with AWS services in Step Functions, see [Integrating services](integrate-services.md "integrate-services.md") and [Passing parameters to a service API in Step Functions](connect-parameters.md "connect-parameters.md").

With the Step Functions integration with AWS CodeBuild you can use Step Functions to trigger,
stop, and manage builds, and to share build reports. Using Step Functions, you can design and run
continuous integration pipelines for validating your software changes for
applications.

###### Key features of Optimized CodeBuild integration

- The [Run a Job (.sync)](connect-to-resource.md#connect-sync "connect-to-resource.md#connect-sync") integration
  pattern is supported.
- After you call `StopBuild` or `StopBuildBatch`, the
  build or build batch is not immediately deletable until some internal work is
  completed within CodeBuild to finalize the state of the build or builds.

If you attempt to use `BatchDeleteBuilds` or
`DeleteBuildBatch` during this period, the build or build batch may
not be deleted.

The optimized service integrations for `BatchDeleteBuilds` and
`DeleteBuildBatch` include an internal retry to simplify the use case
of deleting immediately after stopping.
Not all APIs support all integration patterns, as shown in the following table.

| API               | Request Response | Run a Job (.sync) |
| ----------------- | ---------------- | ----------------- |
| StartBuild        | Supported        | Supported         |
| StopBuild         | Supported        | _Not supported_   |
| BatchDeleteBuilds | Supported        | _Not supported_   |
| BatchGetReports   | Supported        | _Not supported_   |
| StartBuildBatch   | Supported        | Supported         |
| StopBuildBatch    | Supported        | _Not supported_   |
| RetryBuildBatch   | Supported        | Supported         |
| DeleteBuildBatch  | Supported        | _Not supported_   |

###### Parameters in Step Functions are expressed in PascalCase

Even if the native service API is in camelCase, for example the API action `startSyncExecution`, you specify parameters in PascalCase, such as: `StateMachineArn`.

## Optimized CodeBuild APIs

- [`StartBuild`](../../../codebuild/latest/APIReference/API_StartBuild.md#API_StartBuild_RequestSyntax "../../../codebuild/latest/APIReference/API_StartBuild.md#API_StartBuild_RequestSyntax")
- [`StopBuild`](../../../codebuild/latest/APIReference/API_StopBuild.md "../../../codebuild/latest/APIReference/API_StopBuild.md")
- [`BatchDeleteBuilds`](../../../codebuild/latest/APIReference/API_BatchDeleteBuilds.md "../../../codebuild/latest/APIReference/API_BatchDeleteBuilds.md")
- [`BatchGetReports`](../../../codebuild/latest/APIReference/API_BatchGetReports.md "../../../codebuild/latest/APIReference/API_BatchGetReports.md")
- [`StartBuildBatch`](../../../codebuild/latest/APIReference/API_StartBuildBatch.md "../../../codebuild/latest/APIReference/API_StartBuildBatch.md")
- [`StopBuildBatch`](../../../codebuild/latest/APIReference/API_StopBuildBatch.md "../../../codebuild/latest/APIReference/API_StopBuildBatch.md")
- [`RetryBuildBatch`](../../../codebuild/latest/APIReference/API_RetryBuildBatch.md "../../../codebuild/latest/APIReference/API_RetryBuildBatch.md")
- [`DeleteBuildBatch`](../../../codebuild/latest/APIReference/API_DeleteBuildBatch.md "../../../codebuild/latest/APIReference/API_DeleteBuildBatch.md")

###### Note

When using JSONPath, you can use the recursive descent operator (`..`)
to provide parameters for `BatchDeleteBuilds`. With the returned array, you can transform
the `Arn` field from `StartBuild` into a plural
`Ids` parameter, as shown in the following example.

```
"BatchDeleteBuilds": {
    "Type": "Task",
    "Resource": "arn:aws:states:::codebuild:batchDeleteBuilds",
    "Arguments": {
        "Ids.$": "$.Build`..`Arn"
    },
    "Next": "MyNextState"
},
```

## IAM policies for calling AWS CodeBuild

The following example templates show how AWS Step Functions generates IAM policies based on the resources in your state machine definition. For more information, see [How Step Functions generates IAM policies for integrated
services](service-integration-iam-templates.md "service-integration-iam-templates.md") and [Discover service integration patterns in Step Functions](connect-to-resource.md "connect-to-resource.md").

_Resources_:

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "sns:Publish"
 ],
 "Resource": [
 "arn:aws:sns:sa-east-1:`123456789012`:StepFunctionsSample-CodeBuildExecution1111-2222-3333-wJalrXUtnFEMI-SNSTopic-bPxRfiCYEXAMPLEKEY"
 ],
 "Effect": "Allow"
 },
 {
 "Action": [
 "codebuild:StartBuild",
 "codebuild:StopBuild",
 "codebuild:BatchGetBuilds",
 "codebuild:BatchGetReports"
 ],
 "Resource": "*",
 "Effect": "Allow"
 },
 {
 "Action": [
 "events:PutTargets",
 "events:PutRule",
 "events:DescribeRule"
 ],
 "Resource": [
 "arn:aws:events:sa-east-1:`123456789012`:rule/StepFunctionsGetEventForCodeBuildStartBuildRule"
 ],
 "Effect": "Allow"
 }
 ]
}`

```

### `StartBuild`

_Static resources_

Run a Job (.sync)

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "codebuild:StartBuild",
 "codebuild:StopBuild",
 "codebuild:BatchGetBuilds"
 ],
 "Resource": [
 "arn:aws:codebuild:`us-east-1`:`123456789012`:project/`myProjectName`"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "events:PutTargets",
 "events:PutRule",
 "events:DescribeRule"
 ],
 "Resource": [
 "arn:aws:events:`us-east-1`:`123456789012`:rule/StepFunctionsGetEventForCodeBuildStartBuildRule"
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
 "codebuild:StartBuild"
 ],
 "Resource": [
 "arn:aws:codebuild:`us-east-1`:`123456789012`:project/`myProjectName`"
 ]
 }
 ]
}`

```

_Dynamic resources_

Run a Job (.sync)

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "codebuild:StartBuild",
 "codebuild:StopBuild",
 "codebuild:BatchGetBuilds"
 ],
 "Resource": [
 "arn:aws:codebuild:`us-east-1`:*:project/*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "events:PutTargets",
 "events:PutRule",
 "events:DescribeRule"
 ],
 "Resource": [
 "arn:aws:events:`us-east-1`:`123456789012`:rule/StepFunctionsGetEventForCodeBuildStartBuildRule"
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
 "codebuild:StartBuild"
 ],
 "Resource": [
 "arn:aws:codebuild:`us-east-1`:*:project/*"
 ]
 }
 ]
}`

```

### `StopBuild`

_Static resources_

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "codebuild:StopBuild"
 ],
 "Resource": [
 "arn:aws:codebuild:`us-east-1`:`123456789012`:project/``myProjectName``"
 ]
 }
 ]
}`

```

_Dynamic resources_

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "codebuild:StopBuild"
 ],
 "Resource": [
 "arn:aws:codebuild:`us-east-1`:*:project/*"
 ]
 }
 ]
}`

```

### `BatchDeleteBuilds`

_Static resources_

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "codebuild:BatchDeleteBuilds"
 ],
 "Resource": [
 "arn:aws:codebuild:`us-east-1`:`123456789012`:project/`myProjectName`"
 ]
 }
 ]
}`

```

_Dynamic resources_

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "codebuild:BatchDeleteBuilds"
 ],
 "Resource": [
 "arn:aws:codebuild:`us-east-1`:*:project/*"
 ]
 }
 ]
}`

```

### `BatchGetReports`

_Static resources_

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "codebuild:BatchGetReports"
 ],
 "Resource": [
 "arn:aws:codebuild:`us-east-1`:`123456789012`:report-group/myReportName"
 ]
 }
 ]
}`

```

_Dynamic resources_

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "codebuild:BatchGetReports"
 ],
 "Resource": [
 "arn:aws:codebuild:`us-east-1`:*:report-group/*"
 ]
 }
 ]
}`

```

### `StartBuildBatch`

_Static resources_

Run a Job (.sync)

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "codebuild:StartBuildBatch",
 "codebuild:StopBuildBatch",
 "codebuild:BatchGetBuildBatches"
 ],
 "Resource": [
 "arn:aws:codebuild:`us-east-1`:`123456789012`:project/`myProjectName`"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "events:PutTargets",
 "events:PutRule",
 "events:DescribeRule"
 ],
 "Resource": [
 "arn:aws:events:`us-east-1`:`123456789012`:rule/StepFunctionsGetEventForCodeBuildStartBuildBatchRule"
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
 "codebuild:StartBuildBatch"
 ],
 "Resource": [
 "arn:aws:codebuild:`us-east-1`:`123456789012`:project/`myProjectName`"
 ]
 }
 ]
}`

```

_Dynamic resources_

Run a Job (.sync)

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "codebuild:StartBuildBatch",
 "codebuild:StopBuildBatch",
 "codebuild:BatchGetBuildBatches"
 ],
 "Resource": [
 "arn:aws:codebuild:`us-east-1`:`123456789012`:project/*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "events:PutTargets",
 "events:PutRule",
 "events:DescribeRule"
 ],
 "Resource": [
 "arn:aws:events:`us-east-1`:`123456789012`:rule/StepFunctionsGetEventForCodeBuildStartBuildBatchRule"
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
 "codebuild:StartBuildBatch"
 ],
 "Resource": [
 "arn:aws:codebuild:`us-east-1`:`123456789012`:project/*"
 ]
 }
 ]
}`

```

### `StopBuildBatch`

_Static resources_

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "codebuild:StopBuildBatch"
 ],
 "Resource": [
 "arn:aws:codebuild:`us-east-1`:`123456789012`:project/`myProjectName`"
 ]
 }
 ]
}`

```

_Dynamic resources_

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "codebuild:StopBuildBatch"
 ],
 "Resource": [
 "arn:aws:codebuild:`us-east-1`:`123456789012`:project/*"
 ]
 }
 ]
}`

```

### `RetryBuildBatch`

_Static resources_

Run a Job (.sync)

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "codebuild:RetryBuildBatch",
 "codebuild:StopBuildBatch",
 "codebuild:BatchGetBuildBatches"
 ],
 "Resource": [
 "arn:aws:codebuild:`us-east-1`:`123456789012`:project/`myProjectName`"
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
 "codebuild:RetryBuildBatch"
 ],
 "Resource": [
 "arn:aws:codebuild:`us-east-1`:`123456789012`:project/`myProjectName`"
 ]
 }
 ]
}`

```

_Dynamic resources_

Run a Job (.sync)

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "codebuild:RetryBuildBatch",
 "codebuild:StopBuildBatch",
 "codebuild:BatchGetBuildBatches"
 ],
 "Resource": [
 "arn:aws:codebuild:`us-east-1`:`123456789012`:project/*"
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
 "codebuild:RetryBuildBatch"
 ],
 "Resource": [
 "arn:aws:codebuild:`us-east-1`:`123456789012`:project/*"
 ]
 }
 ]
}`

```

### `DeleteBuildBatch`

_Static resources_

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "codebuild:DeleteBuildBatch"
 ],
 "Resource": [
 "arn:aws:codebuild:`us-east-1`:`123456789012`:project/`myProjectName`"
 ]
 }
 ]
}`

```

_Dynamic resources_

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "codebuild:DeleteBuildBatch"
 ],
 "Resource": [
 "arn:aws:codebuild:`us-east-1`:`123456789012`:project/*"
 ]
 }
 ]
}`

```
