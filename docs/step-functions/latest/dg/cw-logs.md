# Using CloudWatch Logs to log execution history in Step Functions

Standard Workflows record execution history in AWS Step Functions, although you can optionally
configure logging to Amazon CloudWatch Logs.

Unlike Standard Workflows, Express Workflows don't record execution history in AWS Step Functions. To
see execution history and results for an Express Workflow, you must configure logging to
Amazon CloudWatch Logs. Publishing logs doesn't block or slow down executions.

###### Log delivery guarantees

Amazon CloudWatch Logs are delivered on a best-effort basis. The completeness and timeliness of log entries are not guaranteed. If you require guaranteed workflow history in Express Workflows, we recommend that you implement workflow steps to record data in an appropriate data storage service such as Amazon DynamoDB. Alternatively, you might consider using **Standard Workflows** for guaranteed execution history.

###### Pricing information

When you configure logging, [CloudWatch Logs charges](https://aws.amazon.com/cloudwatch/pricing "https://aws.amazon.com/cloudwatch/pricing") will apply and you will be billed at the vended logs rate. For more information, see **Vended Logs** under the **Logs** tab on the CloudWatch Pricing page.

## Configure logging

When you create a Standard Workflow using the Step Functions console, that state machine will **not** be configured to send logs to CloudWatch Logs. When you create an Express Workflow using the Step Functions console, that state machine will by default
be configured to send logs to CloudWatch Logs.

For Express workflows, Step Functions can create a role with the necessary AWS Identity and Access Management (IAM) policy
for CloudWatch Logs. If you create a Standard Workflow, or an Express Workflow using the API, CLI, or
AWS CloudFormation, Step Functions will not enable logging by default, and you will need ensure your role has the
necessary permissions.

For each execution started from the console, Step Functions provides a link to CloudWatch Logs, configured
with the correct filter to fetch log events specific for that execution.

You can optionally configure customer managed AWS KMS keys to encrypt your logs. See [Data at rest encryption](encryption-at-rest.md "encryption-at-rest.md") for details and permission settings.

To configure logging, you can pass the [LoggingConfiguration](../apireference/API_LoggingConfiguration.md "../apireference/API_LoggingConfiguration.md") parameter when using [CreateStateMachine](../apireference/API_CreateStateMachine.md "../apireference/API_CreateStateMachine.md") or [UpdateStateMachine](../apireference/API_UpdateStateMachine.md "../apireference/API_UpdateStateMachine.md"). You can further analyze your data in CloudWatch Logs by using CloudWatch Logs
Insights. For more information see [Analyzing Log Data with CloudWatch
Logs Insights](../../../AmazonCloudWatch/latest/logs/AnalyzingLogData.md "../../../AmazonCloudWatch/latest/logs/AnalyzingLogData.md").

## CloudWatch Logs payloads

Execution history events may contain either input or output properties in their
definitions. If escaped
input or escaped output sent to CloudWatch Logs exceeds 248 KiB, it will be truncated as a result of
CloudWatch Logs quotas.

- You can determine whether a payload has been truncated by reviewing the
  `inputDetails` and `outputDetails` properties. For more
  information, see the [`HistoryEventExecutionDataDetails` Data Type](../apireference/API_HistoryEventExecutionDataDetails.md "../apireference/API_HistoryEventExecutionDataDetails.md").
- For Standard Workflows, you can see the full execution history by using [`GetExecutionHistory`](../apireference/API_GetExecutionHistory.md "../apireference/API_GetExecutionHistory.md").
- `GetExecutionHistory` is not available for Express Workflows. If you want to
  see the full input and output, you can use Amazon S3 ARNs. For more information, see [Using Amazon S3 ARNs instead of passing large payloads in Step Functions](sfn-best-practices.md#avoid-exec-failures "sfn-best-practices.md#avoid-exec-failures").

## IAM Policies for logging to CloudWatch Logs

You will also need to configure your state machine's execution IAM role to have the proper permission to log to CloudWatch Logs as shown in the following example.

###### IAM policy example

The following is an example policy you can use to configure your permissions. As shown in the following example, you need to specify **\*** in the `Resource` field. CloudWatch API actions, such as CreateLogDelivery and DescribeLogGroups, do not support [Resource types defined by Amazon CloudWatch Logs](../../../service-authorization/latest/reference/list_amazoncloudwatchlogs.md#amazoncloudwatchlogs-resources-for-iam-policies "../../../service-authorization/latest/reference/list_amazoncloudwatchlogs.md#amazoncloudwatchlogs-resources-for-iam-policies"). For more information, see [Actions defined by Amazon CloudWatch Logs](../../../service-authorization/latest/reference/list_amazoncloudwatchlogs.md#amazoncloudwatchlogs-actions-as-permissions "../../../service-authorization/latest/reference/list_amazoncloudwatchlogs.md#amazoncloudwatchlogs-actions-as-permissions").

- For information about CloudWatch resources, see [CloudWatch Logs resources and operations](../../../AmazonCloudWatch/latest/logs/iam-access-control-overview-cwl.md#CWL_ARN_Format "../../../AmazonCloudWatch/latest/logs/iam-access-control-overview-cwl.md#CWL_ARN_Format") in the _Amazon CloudWatch User Guide_.
- For information about the permissions you need to set up sending logs to CloudWatch Logs, see [User permissions](../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md#AWS-logs-infrastructure-CWL "../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md#AWS-logs-infrastructure-CWL") in the section titled _Logs sent to CloudWatch Logs_.

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "logs:CreateLogDelivery",
 "logs:CreateLogStream",
 "logs:GetLogDelivery",
 "logs:UpdateLogDelivery",
 "logs:DeleteLogDelivery",
 "logs:ListLogDeliveries",
 "logs:PutLogEvents",
 "logs:PutResourcePolicy",
 "logs:DescribeResourcePolicies",
 "logs:DescribeLogGroups"
 ],
 "Resource": "*"
 }
 ]
}`

```

## Log levels for Step Functions execution events

Log levels range from `ALL` to `ERROR` to `FATAL` to `OFF`. All event types are logged for `ALL`, no event types are logged when set to `OFF`. For `ERROR` and `FATAL`, see the following table.

For more information about the execution data displayed for Express Workflow executions based on these **Log levels**, see
[Standard and Express console experience differences](concepts-view-execution-details.md#console-exp-differences "concepts-view-execution-details.md#console-exp-differences").

| Event Type                   | `ALL`  | `ERROR`      | `FATAL`      | `OFF`        |
| ---------------------------- | ------ | ------------ | ------------ | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| ChoiceStateEntered           | Logged | _Not logged_ | _Not logged_ | _Not logged_ |
| ChoiceStateExited            | Logged | _Not logged_ | _Not logged_ | _Not logged_ |
| ExecutionAborted             | Logged | Logged       | Logged       | _Not logged_ |
| ExecutionFailed              | Logged | Logged       | Logged       | _Not logged_ |
| ExecutionStarted             | Logged | _Not logged_ | _Not logged_ | _Not logged_ |
| ExecutionSucceeded           | Logged | _Not logged_ | _Not logged_ | _Not logged_ |
| ExecutionTimedOut            | Logged | Logged       | Logged       | _Not logged_ |
| FailStateEntered             | Logged | Logged       | _Not logged_ | _Not logged_ |
| LambdaFunctionFailed         | Logged | Logged       | _Not logged_ | _Not logged_ |
| LambdaFunctionScheduled      | Logged | _Not logged_ | _Not logged_ | _Not logged_ |
| LambdaFunctionScheduleFailed | Logged | Logged       | _Not logged_ | _Not logged_ |
| LambdaFunctionStarted        | Logged | _Not logged_ | _Not logged_ | _Not logged_ |
| LambdaFunctionStartFailed    | Logged | Logged       | _Not logged_ | _Not logged_ |
| LambdaFunctionSucceeded      | Logged | _Not logged_ | _Not logged_ | _Not logged_ |
| LambdaFunctionTimedOut       | Logged | Logged       | _Not logged_ | _Not logged_ |
| MapIterationAborted          | Logged | Logged       | _Not logged_ | _Not logged_ |
| MapIterationFailed           | Logged | Logged       | _Not logged_ | _Not logged_ |
| MapIterationStarted          | Logged | _Not logged_ | _Not logged_ | _Not logged_ |
| MapIterationSucceeded        | Logged | _Not logged_ | _Not logged_ | _Not logged_ |
| MapRunAborted                | Logged | Logged       | _Not logged_ | _Not logged_ |
| MapRunFailed                 | Logged | Logged       | _Not logged_ | _Not logged_ |
| MapStateAborted              | Logged | Logged       | _Not logged_ | _Not logged_ |
| MapStateEntered              | Logged | _Not logged_ | _Not logged_ | _Not logged_ |
| MapStateExited               | Logged | _Not logged_ | _Not logged_ | _Not logged_ |
| MapStateFailed               | Logged | Logged       | _Not logged_ | _Not logged_ |
| MapStateStarted              | Logged | _Not logged_ | _Not logged_ | _Not logged_ |
| MapStateSucceeded            | Logged | _Not logged_ | _Not logged_ | _Not logged_ |
| ParallelStateAborted         | Logged | Logged       | _Not logged_ | _Not logged_ |
| ParallelStateEntered         | Logged | _Not logged_ | _Not logged_ | _Not logged_ |
| ParallelStateExited          | Logged | _Not logged_ | _Not logged_ | _Not logged_ |
| ParallelStateFailed          | Logged | Logged       | _Not logged_ | _Not logged_ |
| ParallelStateStarted         | Logged | _Not logged_ | _Not logged_ | _Not logged_ |
| ParallelStateSucceeded       | Logged | _Not logged_ | _Not logged_ | _Not logged_ |
| PassStateEntered             | Logged | _Not logged_ | _Not logged_ | _Not logged_ |
| PassStateExited              | Logged | _Not logged_ | _Not logged_ | _Not logged_ |
| SucceedStateEntered          | Logged | _Not logged_ | _Not logged_ | _Not logged_ |
| SucceedStateExited           | Logged | _Not logged_ | _Not logged_ | _Not logged_ |
| TaskFailed                   | Logged | Logged       | _Not logged_ | _Not logged_ |
| TaskScheduled                | Logged | _Not logged_ | _Not logged_ | _Not logged_ |
| TaskStarted                  | Logged | _Not logged_ | _Not logged_ | _Not logged_ |
| TaskStartFailed              | Logged | Logged       | _Not logged_ | _Not logged_ |
| TaskStateAborted             | Logged | Logged       | _Not logged_ | _Not logged_ |
| TaskStateEntered             | Logged | _Not logged_ | _Not logged_ | _Not logged_ |
| TaskStateExited              | Logged | _Not logged_ | _Not logged_ | _Not logged_ |
| TaskSubmitFailed             | Logged | Logged       | _Not logged_ | _Not logged_ |
| TaskSubmitted                | Logged | _Not logged_ | _Not logged_ | _Not logged_ |
| TaskSucceeded                | Logged | _Not logged_ | _Not logged_ | _Not logged_ |
| TaskTimedOut                 | Logged | Logged       | _Not logged_ | _Not logged_ |
| WaitStateAborted             | Logged | Logged       | _Not logged_ | _Not logged_ |
| WaitStateEntered             | Logged | _Not logged_ | _Not logged_ | _Not logged_ |
| WaitStateExited              | Logged | _Not logged_ | _Not logged_ | _Not logged_ | ## Troubleshooting logging to CloudWatch Logs If your state machine cannot send logs to CloudWatch Logs or you receive the error: "`AccessDeniedException : The state machine IAM Role is not authorized to access the Log Destination`", try the following steps: 1. Verify your state machine's execution role has permission to log to CloudWatch Logs. When you call [CreateStateMachine](../apireference/API_CreateStateMachine.md "../apireference/API_CreateStateMachine.md") or [UpdateStateMachine](../apireference/API_UpdateStateMachine.md "../apireference/API_UpdateStateMachine.md") API endpoints, make sure the IAM role specified in the `roleArn` parameter provides the necessary permissions, shown in the preceding IAM policy example. 2. Verify the CloudWatch Logs resource policy does not exceed the 5,120 character limit. If the policy exceeds the character limit, prefix your log group names with `/aws/vendedlogs/states` to grant permissions to your state machines and avoid the limit. When you create a log group in the Step Functions console, the suggested log group names are already prefixed with `/aws/vendedlogs/states`. For more information on logging best practices, see [Avoiding CloudWatch resource policy size limits](sfn-best-practices.md#bp-cwl "sfn-best-practices.md#bp-cwl"). 3. Verify the number of CloudWatch Logs log resource policies in the account is less than **ten**. CloudWatch Logs has a quota of ten resource policies per region, per account. If you try to enable logging on a state machine that already has ten resource policies, the state machine will not be created nor updated, and you will receive an error. For more information about logging quotas, see [CloudWatch Logs quotas](../../../AmazonCloudWatch/latest/logs/cloudwatch_limits_cwl.md "../../../AmazonCloudWatch/latest/logs/cloudwatch_limits_cwl.md") To verify the problem, check the number of resource policies using the CLI command: [`aws logs describe-resource-policies`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/describe-resource-policies.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/describe-resource-policies.html") To resolve the problem, modify your existing resource policies. First, back up the existing policies. Then, join similar actions or resources into a new policy and use the following CLI command to create a new delivery source in the account: [`aws logs put-delivery-source`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/put-delivery-source.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/put-delivery-source.html") After backing up and updating the policies, remove any unused policies with the following command: [`aws logs delete-resource-policy --policy-name <PolicyNameToBeDeleted>`](../../../cli/latest/reference/logs/delete-resource-policy.md "../../../cli/latest/reference/logs/delete-resource-policy.md") |
