# `AWSSupport-RemediateLambdaS3Event`

**Description**

The `AWSSupport-TroubleshootLambdaS3Event` runbook provides an
automated solution for the procedures outlined in the AWS Knowledge Center
articles [Why doesn't my Amazon S3 event notification trigger my Lambda function?](https://aws.amazon.com/premiumsupport/knowledge-center/lambda-configure-s3-event-notification/ "https://aws.amazon.com/premiumsupport/knowledge-center/lambda-configure-s3-event-notification/") and
[Why do I get the error "Unable to validate the following destination
configurations" when creating an Amazon S3 event notification to trigger my Lambda
function?](https://aws.amazon.com/premiumsupport/knowledge-center/lambda-invoke-error-s3-bucket-permission/ "https://aws.amazon.com/premiumsupport/knowledge-center/lambda-invoke-error-s3-bucket-permission/") This runbook helps you identify and remediate why an Amazon Simple Storage Service
(Amazon S3) event notification failed to trigger the AWS Lambda function you specified. If
the runbook output suggests validating and configuring your Lambda function
concurrency, see [Asynchronous
invocation](../../../lambda/latest/dg/invocation-async.md "../../../lambda/latest/dg/invocation-async.md") and [AWS Lambda Function
scaling](../../../lambda/latest/dg/scaling.md "../../../lambda/latest/dg/scaling.md") .

###### Note

"Unable to validate the following destination configurations" errors can also
occur due to incorrect Amazon Simple Notification Service (Amazon SNS) and Amazon Simple Queue Service (Amazon SQS) Amazon S3 event
configurations. This runbook only checks Lambda function configurations. If after
using the runbook, you are still receiving the "Unable to validate the following
destination configurations" error, please review any existing Amazon SNS and Amazon SQS
Amazon S3 event configurations.

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-RemediateLambdaS3Event "https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-RemediateLambdaS3Event")

**Document type**

Automation

**Owner**

Amazon

**Platforms**

Linux, macOS, Windows

**Parameters**

- AutomationAssumeRole

Type: String

Description: (Optional) The Amazon Resource Name (ARN) of the AWS Identity and Access Management
(IAM) role that allows Systems Manager Automation to perform the actions on your
behalf. If no role is specified, Systems Manager Automation uses the permissions of
the user that starts this runbook.

- LambdaFunctionArn

Type: String

Description: (Required) The ARN of the Lambda function.

- S3BucketName

Type: String

Description: (Required) The name of the Amazon S3 bucket whose event
notifications triggers the Lambda function.

- Action

Type: String

Valid values: Troubleshoot | Remediate

Description: (Required) The action you want the runbook to perform. The
`Troubleshoot` option helps identify any issues, but does not
perform any mutating actions to resolve the issue. The
`Remediate` option helps identify and attempts to resolve
issues for you.
**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

- `ssm:StartAutomationExecution`
- `ssm:GetDocument`
- `ssm:ListDocuments`
- `ssm:DescribeAutomationExecutions`
- `ssm:DescribeAutomationStepExecutions`
- `ssm:GetAutomationExecution`
- `lambda:GetPolicy`
- `lambda:AddPermission`
- `s3:GetBucketNotification`

**Document Steps**

- `aws:branch` - Branches based on the input specified for the
  `Action` parameter.

If the value specified is `Troubleshoot` :

    + `aws:executeAutomation` - Runs the
     `AWSSupport-TroubleshootLambdaS3Event` runbook.
    + `aws:executeAwsApi` - Checks the output of the
     `AWSSupport-TroubleshootLambdaS3Event` runbook that
     ran in the previous step.

If the value specified is `Remediate` :

    + `aws:executeScript` - Runs a script to remediate the
     issues outlined in the [Why doesn't my Amazon S3 event notification trigger my Lambda
     function?](https://aws.amazon.com/premiumsupport/knowledge-center/lambda-configure-s3-event-notification/ "https://aws.amazon.com/premiumsupport/knowledge-center/lambda-configure-s3-event-notification/") and  [Why do I get the error "Unable to validate the following
     destination configurations" when creating an Amazon S3 event
     notification to trigger my Lambda function?](https://aws.amazon.com/premiumsupport/knowledge-center/lambda-invoke-error-s3-bucket-permission/ "https://aws.amazon.com/premiumsupport/knowledge-center/lambda-invoke-error-s3-bucket-permission/") Knowledge
     Center articles.

**Outputs**

checkoutput.Output

remediatelambdas3event.Output
