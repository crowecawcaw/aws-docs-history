# Prevent failed StackSets deployments using target
 account gates

An account gate is an optional feature that helps you verify that a target account meets
 certain requirements before CloudFormation begins StackSets operations in that account. This
 verification is performed through an AWS Lambda function that acts as a prerequisite check.

A common example of an account gate is verifying that there are no CloudWatch alarms active or
 unresolved on the target account. CloudFormation invokes the Lambda function each time you start
 stack operations in the target account, and only continues if the function returns a
 `SUCCEEDED` code. If the Lambda function returns a status of `FAILED`,
 CloudFormation doesn't continue with your requested operation. If you don't have an account gating
 Lambda function configured, CloudFormation skips the check, and continues with your
 operation.

If your target account fails an account gate check, the failed operation counts toward your
 specified failure tolerance number or percentage of stacks. For more information about failure
 tolerance, see [StackSet operation options](stacksets-concepts.md#stackset-ops-options "stacksets-concepts.md#stackset-ops-options").

Account gating is only available for StackSets operations. This feature isn't
 available for other CloudFormation operations outside of StackSets.


## Requirements


The following requirements must be met for account gating:



* Your Lambda function must be named `AWSCloudFormationStackSetAccountGate` to
 use this feature.
* The **AWSCloudFormationStackSetExecutionRole** must have permissions to
 invoke your Lambda function. Without these permissions, CloudFormation will skip the account
 gating check and proceed with stack operations.
* The Lambda `InvokeFunction` permission must be added to target accounts for account gating to work.
 The target account trust policy must have a trust relationship with the administrator account. The following is an
 example of a policy statement that grants Lambda `InvokeFunction` permissions.



JSON





```
`{
 "Version":"2012-10-17", 
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "lambda:InvokeFunction"
 ],
 "Resource": "*"
 }
 ]
}`

```

## CloudFormation templates for creating Lambda
 functions


Use the following sample templates to create Lambda
 `AWSCloudFormationStackSetAccountGate` functions. To create a new stack using either
 of these templates, see [Create a stack from the CloudFormation console](cfn-console-create-stack.md "cfn-console-create-stack.md").




| Template location | Description |
| --- | --- |
| [https://s3.amazonaws.com/cloudformation-stackset-sample-templates-us-east-1/AccountGateSucceeded.yml](https://s3.amazonaws.com/cloudformation-stackset-sample-templates-us-east-1/AccountGateSucceeded.yml "https://s3.amazonaws.com/cloudformation-stackset-sample-templates-us-east-1/AccountGateSucceeded.yml") | Creates a stack that implements a Lambda account gate function that will return a status
 of `SUCCEEDED`. |
| [https://s3.amazonaws.com/cloudformation-stackset-sample-templates-us-east-1/AccountGateFailed.yml](https://s3.amazonaws.com/cloudformation-stackset-sample-templates-us-east-1/AccountGateFailed.yml "https://s3.amazonaws.com/cloudformation-stackset-sample-templates-us-east-1/AccountGateFailed.yml") | Creates a stack that implements a Lambda account gate function that will return a status
 of `FAILED`. |
