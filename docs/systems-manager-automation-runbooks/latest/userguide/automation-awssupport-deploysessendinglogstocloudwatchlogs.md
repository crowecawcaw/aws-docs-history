# `AWSSupport-DeploySESSendingLogsToCloudWatchLogs`

**Description**

**The AWSSupport-DeploySESSendingLogsToCloudWatchLogs** automation runbook helps configure the infrastructure required for Amazon Simple Email Service (Amazon SES) event publishing to Amazon CloudWatch Logs (CloudWatch Logs). This runbook sets up the components needed to capture email sending events and store them in CloudWatch Logs for monitoring and analysis. For more information about Amazon SES event publishing, see [Monitor email sending using Amazon SES event publishing](../../../ses/latest/dg/monitor-using-event-publishing.md "../../../ses/latest/dg/monitor-using-event-publishing.md").

When the `ApproveDeployAnalyticEnvironment` parameter is set to `approve`, this runbook creates new AWS resources in your AWS account. The CloudFormation stack is automatically deleted after the time specified in the `SleepTime` parameter unless set to `0`.

**How does it work?**

This runbook performs the following actions:

- Lists existing configuration sets that have event destinations configured for Amazon Simple Notification Service (Amazon SNS) topics or delivery streams.
- Creates the infrastructure required for Amazon SES event publishing to CloudWatch Logs when the `ApproveDeployAnalyticEnvironment` parameter is set to `approve`.
  When the `ApproveDeployAnalyticEnvironment` parameter is set to `approve`, the runbook creates the following resources:

- An CloudFormation stack named `AWSSupport-SESSendingLogsToCloudWatchLogs` that includes:
  - Amazon SNS topic with AWS Key Management Service (AWS KMS) encryption
  - Amazon Simple Queue Service (Amazon SQS) queue
  - AWS Lambda function for processing email sending events
  - AWS Identity and Access Management (IAM) execution role with permissions for Amazon SQS and CloudWatch Logs
  - CloudWatch Logs log group
  - AWS KMS key for encryption
  - Amazon SES configuration set with event destinations

- The infrastructure processes email sending events in the following flow: Amazon SES Email Sending Events → Amazon SES Configuration Set → Amazon SNS Topic → Amazon SQS Queue → Lambda Function → CloudWatch Logs
- Associates the created configuration set as the default configuration set for a specified Amazon SES identity when the `SesIdentity` parameter is provided.

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-DeploySESSendingLogsToCloudWatchLogs "https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-DeploySESSendingLogsToCloudWatchLogs")

**Document type**

Automation

**Owner**

Amazon

**Platforms**

/

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

- `cloudformation:CreateStack`
- `cloudformation:DeleteStack`
- `cloudformation:DescribeStackEvents`
- `cloudformation:DescribeStacks`
- `iam:CreateRole`
- `iam:AttachRolePolicy`
- `iam:PassRole`
- `kms:CreateKey`
- `kms:CreateAlias`
- `lambda:CreateFunction`
- `lambda:AddPermission`
- `logs:CreateLogGroup`
- `logs:PutRetentionPolicy`
- `ses:CreateConfigurationSet`
- `ses:CreateConfigurationSetEventDestination`
- `ses:ListConfigurationSets`
- `ses:PutEmailIdentityConfigurationSetAttributes`
- `sns:CreateTopic`
- `sns:Subscribe`
- `sqs:CreateQueue`
- `sqs:SetQueueAttributes`
- `ssm:DescribeAutomationExecutions`
  Example Policy:

```
{
       "Version": "2012-10-17",
       "Statement": [
           {
           "Effect": "Allow",
           "Action": [
               "cloudformation:CreateStack",
               "cloudformation:DeleteStack",
               "cloudformation:DescribeStackEvents",
               "cloudformation:DescribeStacks",
               "iam:CreateRole",
               "iam:AttachRolePolicy",
               "iam:PassRole",
               "kms:CreateKey",
               "kms:CreateAlias",
               "lambda:CreateFunction",
               "lambda:AddPermission",
               "logs:CreateLogGroup",
               "logs:PutRetentionPolicy",
               "ses:CreateConfigurationSet",
               "ses:CreateConfigurationSetEventDestination",
               "ses:ListConfigurationSets",
               "ses:PutEmailIdentityConfigurationSetAttributes",
               "sns:CreateTopic",
               "sns:Subscribe",
               "sqs:CreateQueue",
               "sqs:SetQueueAttributes",
               "ssm:DescribeAutomationExecutions"
           ],
           "Resource": "*"
           }
       ]
       }
```

**Instructions**

Follow these steps to configure the automation:

1. Navigate to [`AWSSupport-DeploySESSendingLogsToCloudWatchLogs`](https://console.aws.amazon.com/systems-manager/documents/AWSSupport-DeploySESSendingLogsToCloudWatchLogs/description "https://console.aws.amazon.com/systems-manager/documents/AWSSupport-DeploySESSendingLogsToCloudWatchLogs/description") in Systems Manager under Documents.
2. Select **Execute automation.**
3. For the input parameters, enter the following:
   - **AutomationAssumeRole (Optional):**
     - Description: (Optional) The Amazon Resource Name (ARN) of the IAM role that allows Systems Manager Automation to perform the actions on your behalf. If no role is specified, Systems Manager Automation uses the permissions of the user that starts this runbook.
     - Type: `AWS::IAM::Role::Arn`

   - **ApproveDeployAnalyticEnvironment (Optional):**
     - Description: (Optional) Approval to deploy the Amazon SES event publishing infrastructure. Enter `approve` to create the CloudFormation stack and related resources. If left empty, the runbook only displays existing configuration sets with or Amazon SNS event destinations in the current region.
     - Type: `String`
     - Allow Pattern: `^$|^approve$`
     - Default: `""`

   - **SesIdentity (Optional):**
     - Description: (Optional) Amazon SES identity (email address or domain) to associate with the newly created configuration set as the default configuration set. This will overwrite any existing default configuration set for the specified identity.
     - Type: `String`
     - Default: `""`

   - **CloudWatchLogGroupName (Optional):**
     - Description: (Optional) Name of the CloudWatch Logs log group to create for storing Amazon SES email sending events.
     - Type: `String`
     - Allow Pattern: `^[0-9a-zA-Z_.#/\\-]{1,512}$`
     - Default: `/ses/sending_event_logs`

   - **MaskPIIData (Optional):**
     - Description: (Optional) Specify whether to mask personally identifiable information (PII) data such as destination email addresses and email subjects in CloudWatch Logs. Set to `False` to include this information in the logs.
     - Type: `String`
     - Allowed Values: `[True, False]`
     - Default: `True`

   - **SleepTime (Optional):**
     - Description: (Optional) Number of minutes to wait before automatically deleting the CloudFormation stack. The default is 24 hours (1,440 minutes), maximum is 7 days (10,080 minutes). Set to `0` to prevent automatic deletion.
     - Type: `String`
     - Allow Pattern: `^(?:[0-9]|[1-9]\\d{1,3}|100[0-7][0-9])$`
     - Default: `1440`

   - **RetainCloudWatchLogsOnDeletion (Optional):**
     - Description: (Optional) Specify whether to retain the CloudWatch Logs log group when the CloudFormation stack is deleted. Set to `False` to delete the log group along with the stack.
     - Type: `String`
     - Allowed Values: `[True, False]`
     - Default: `True`

   - **UniqueId (Optional):**
     - Description: (Optional) A unique identifier for the workflow.
     - Type: `String`
     - Allow Pattern: `\\{\\{ automation:EXECUTION_ID \\}\\}|[a-zA-Z0-9-]+`
     - Default: `{{ automation:EXECUTION_ID }}`
     - ax Characters: `64`

4. Select **Execute**.
5. The automation initiates.
6. The document performs the following steps:
   - **BranchOnValueOfParameterApproveDeployAnalyticEnvironment**

   Determines whether to deploy the Amazon SES event publishing infrastructure based on the `ApproveDeployAnalyticEnvironment` parameter value.
   - **GetEligibleConfigurationSets**

   Retrieves existing Amazon SES configuration sets and identifies those with event destinations configured for delivery streams or Amazon SNS topics.
   - **CheckConcurrency**

   Verifies that no existing stack exists and that no other concurrent executions of this runbook are creating the same stack.
   - **DeploySesEventDestinations**

   Creates the CloudFormation stack containing the Amazon SES event publishing infrastructure including Amazon SNS topic, Amazon SQS queue, Lambda function, and CloudWatch Logs log group.
   - **RelateConfigurationSetAsDefaultConfigurationSet**

   Associates the newly created Amazon SES configuration set as the default configuration set for the specified Amazon SES identity (if provided).
   - **SleepBeforeDeleteCloudFormationStack**

   Waits for the specified duration in the SleepTime parameter before proceeding to delete the CloudFormation stack.
   - **DeleteCloudFormationStack**

   Deletes the CloudFormation stack after the specified time period.

7. After completion, review the **Outputs** section for the detailed results of the execution.

**References**

Systems Manager Automation

- [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/documents/AWSSupport-DeploySESSendingLogsToCloudWatchLogs/description "https://console.aws.amazon.com/systems-manager/documents/AWSSupport-DeploySESSendingLogsToCloudWatchLogs/description")
- [Run an automation](../../../systems-manager/latest/userguide/automation-working-executing.md "../../../systems-manager/latest/userguide/automation-working-executing.md")
- [Setting up an Automation](../../../systems-manager/latest/userguide/automation-setup.md "../../../systems-manager/latest/userguide/automation-setup.md")
- [Support Automation Workflows landing page](https://aws.amazon.com/premiumsupport/technology/saw/ "https://aws.amazon.com/premiumsupport/technology/saw/")
