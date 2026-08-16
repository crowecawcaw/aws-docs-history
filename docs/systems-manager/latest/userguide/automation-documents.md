# Creating your own runbooks

An Automation runbook defines the _actions_ that
Systems Manager performs on your managed instances and other AWS resources when an automation
runs. Automation is a tool in AWS Systems Manager. A runbook contains one or more steps that run
in sequential order. Each step is built around a single action. Output from one step can
be used as input in a later step.

The process of running these actions and their steps is called the _automation_.

Action types supported for runbooks let you automate a wide variety of operations in
your AWS environment. For example, using the `executeScript` action type,
you can embed a python or PowerShell script directly in your runbook. (When you create a
custom runbook, you can add your script inline, or attach it from an S3 bucket or from
your local machine.) You can automate management of your AWS CloudFormation resources by using
the `createStack` and `deleteStack` action types. In addition,
using the `executeAwsApi` action type, a step can run _any_ API operation in any AWS service, including creating or deleting
AWS resources, starting other processes, initiating notifications, and many more.

For a list of all 20 supported action types for Automation, see [Systems Manager Automation actions reference](automation-actions.md "automation-actions.md").

AWS Systems Manager Automation provides several runbooks with pre-defined steps that you can use
to perform common tasks like restarting one or more Amazon Elastic Compute Cloud (Amazon EC2) instances or
creating an Amazon Machine Image (AMI). You can also create your own runbooks and share them with
other AWS accounts, or make them public for all Automation users.

Runbooks are written using YAML or JSON. Using the **Document
Builder** in the Systems Manager Automation console, however, you can create a
runbook without having to author in native JSON or YAML.

###### Important

If you run an automation workflow that invokes other services by using an AWS Identity and Access Management
(IAM) service role, be aware that the service role must be configured with permission
to invoke those services. This requirement applies to all AWS Automation runbooks
(`AWS-*` runbooks) such as the `AWS-ConfigureS3BucketLogging`,
`AWS-CreateDynamoDBBackup`, and `AWS-RestartEC2Instance`
runbooks, to name a few. This requirement also applies to any custom Automation runbooks
you create that invoke other AWS services by using actions that call other services.
For example, if you use the `aws:executeAwsApi`,
`aws:createStack`, or `aws:copyImage` actions, configure the
service role with permission to invoke those services. You can give permissions to other
AWS services by adding an IAM inline policy to the role. For more information, see
[(Optional) Add an Automation inline policy or customer managed policy to invoke other AWS services](automation-setup-iam.md#add-inline-policy "automation-setup-iam.md#add-inline-policy").

For information about the actions that you can specify in a runbook, see [Systems Manager Automation actions reference](automation-actions.md "automation-actions.md").

For information about using the AWS Toolkit for Visual Studio Code to create runbooks, see [Working with Systems Manager Automation documents](../../../toolkit-for-vscode/latest/userguide/systems-manager-automation-docs.md "../../../toolkit-for-vscode/latest/userguide/systems-manager-automation-docs.md") in the
_AWS Toolkit for Visual Studio Code User Guide_.

For information about using the visual designer to create a custom runbook, see [Visual design experience for Automation runbooks](automation-visual-designer.md "automation-visual-designer.md").
