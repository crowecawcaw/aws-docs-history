# `AWSSupport-TroubleshootLambdaS3Event`

**Description**

The `AWSSupport-TroubleshootLambdaS3Event` runbook provides an
automated solution for the procedures outlined in the AWS Knowledge Center
articles [Why doesn't my Amazon S3 event notification trigger my Lambda function?](https://aws.amazon.com/premiumsupport/knowledge-center/lambda-configure-s3-event-notification/ "https://aws.amazon.com/premiumsupport/knowledge-center/lambda-configure-s3-event-notification/") and
[Why do I get the error "Unable to validate the following destination
configurations" when creating an Amazon S3 event notification to trigger my Lambda
function?](https://aws.amazon.com/premiumsupport/knowledge-center/lambda-invoke-error-s3-bucket-permission/ "https://aws.amazon.com/premiumsupport/knowledge-center/lambda-invoke-error-s3-bucket-permission/") This runbook helps you identify why an Amazon Simple Storage Service (Amazon S3) event
notification failed to trigger the AWS Lambda function you specified. If the runbook
output suggests validating and configuring your Lambda function concurrency, see
[Asynchronous invocation](../../../lambda/latest/dg/invocation-async.md "../../../lambda/latest/dg/invocation-async.md")
and [AWS Lambda Function scaling](../../../lambda/latest/dg/scaling.md "../../../lambda/latest/dg/scaling.md") .

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-TroubleshootLambdaS3Event "https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-TroubleshootLambdaS3Event")

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

Description: (Required) The ARN of the Lambda function that the Amazon S3 event
notification triggers.

- S3BucketName

Type: String

Description: (Required) The name of the Amazon S3 bucket whose event
notifications triggers the Lambda function.
**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

- `lambda:GetPolicy`
- `s3:GetBucketNotification`

**Document Steps**

- `aws:executeScript` - Runs the script to validate configuration
  settings for the Amazon S3 event notification. Validates the resource-based IAM
  policy for your Lambda function, and generates an AWS Command Line Interface (AWS CLI) command
  to add the needed permissions if the required permissions are missing from
  the policy. Validates other Lambda functions resource policies which are part
  of event notifications for the same S3 bucket and generates an AWS CLI command
  as output if the required permissions are missing.

**Outputs**

lambdaS3Event.output
