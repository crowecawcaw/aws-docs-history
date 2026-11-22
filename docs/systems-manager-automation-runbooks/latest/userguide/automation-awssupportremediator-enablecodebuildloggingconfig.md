

# `AWSSupportRemediator-EnableCodeBuildLoggingConfig`

**Description**

Enables Amazon CloudWatch Logs for the specified AWS CodeBuild project by calling the CodeBuild `UpdateProject` API directly.

This automation remediates findings identified by AWS Well-Architected Agent. It remediates findings from AWS Security Hub CSPM control [CodeBuild project environments should have a logging configuration](https://docs.aws.amazon.com/securityhub/latest/userguide/codebuild-controls.html#codebuild-4).

If the CodeBuild project does not exist, or if CloudWatch Logs or Amazon Simple Storage Service (Amazon S3) logging is already enabled for the project, the automation completes successfully without making changes.

For the enabled logging configuration to deliver logs, the CodeBuild service role attached to the project must have permissions to write to CloudWatch Logs (for example, `logs:CreateLogGroup`, `logs:CreateLogStream`, and `logs:PutLogEvents`). This runbook does not modify the service role.

Enabling CloudWatch Logs might increase your CloudWatch Logs ingestion and storage costs because builds emit log events. For more information about pricing, see [Amazon CloudWatch pricing](https://aws.amazon.com/cloudwatch/pricing/).

**Important considerations**  
You are responsible for reviewing automation actions before they run.
This automation might cause stack drift if the resource is part of an AWS CloudFormation stack.
Access to `AWSSupportRemediator-*` runbooks requires an active Business Support\+, Enterprise Support, or Unified Operations Support plan. For more information, see [Compare AWS Support Plans](https://aws.amazon.com/premiumsupport/plans/) on the AWS website.

**Document type**

Automation

**Owner**

Amazon

**Platforms**

Linux, macOS, Windows

**Parameters**
+ AutomationAssumeRole

  Type: String

  Description: (Optional) The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that allows Systems Manager Automation to perform the actions on your behalf. If no role is specified, Systems Manager Automation uses the permissions of the user that starts this runbook.
+ CodeBuildProjectArn

  Type: String

  Description: (Required) The Amazon Resource Name (ARN) of the CodeBuild project for which to enable CloudWatch Logs.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+ `codebuild:BatchGetProjects`
+ `codebuild:UpdateProject`

**Document Steps**

1. **validateProject** - Verifies that the CodeBuild project exists and determines whether its logging configuration requires a change.

1. **branchOnChangeRequired** - Branches on whether a logging configuration change is required for the CodeBuild project.

1. **enableCWLogs** - Enables CloudWatch Logs for the CodeBuild project by updating the project's logging configuration.

**Outputs**
+ validateProject.ChangeRequired: Whether a configuration change is required.
+ validateProject.ValidationMessage: A message describing the validation result.
+ enableCWLogs.UpdatedLogsConfig: The CodeBuild project logging configuration after the update.