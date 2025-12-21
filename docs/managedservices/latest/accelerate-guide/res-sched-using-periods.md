# Using AMS Resource Scheduler

How to use AMS Resource Scheduler periods in AMS Accelerate accounts.

Use the following set of AWS Systems Manager automation runbooks to administer the required schedule and period in AMS Resource Scheduler.

###### Note

These SSM automation runbooks are available in the primary AWS Region of your account.

- `AWSManagedServices-AddOrUpdatePeriod`
- `AWSManagedServices-AddOrUpdateSchedule`
- `AWSManagedServices-DeleteScheduleOrPeriod`
- `AWSManagedServices-DescribeScheduleOrPeriods`
- `AWSManagedServices-EnableOrDisableAMSResourceScheduler`
  Additionally, AMS provisions an AWS Identity and Access Management role, `ams_resource_scheduler_ssm_automation_role`, that AWS Systems Manager requires and assumes
  in order to use the runbooks. The IAM role is scoped down with a least privilege inline policy granting SSM permissions required for the functionality
  of the runbooks.

**Prerequisites**

Perform the following steps before you begin using the SSM automation runbook and AMS Resource Scheduler.

Attach the following policy to the appropriate IAM entity (user, group or role) that you want to allow to use the automation runbooks
to administer the schedule and period in AMS Resource Scheduler.
_The policy is not required if your IAM entity has Administrator or PowerUser permission in your account_.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowPassingResourceSchedulerRole",
 "Effect": "Allow",
 "Action": "iam:PassRole",
 "Resource": "arn:aws:iam::`111122223333`:role/ams_resource_scheduler_ssm_automation_role",
 "Condition": {
 "StringEquals": {
 "iam:PassedToService": "ssm.amazonaws.com"
 }
 }
 },
 {
 "Sid": "ListAndDescribeAutomationExecutions",
 "Effect": "Allow",
 "Action": [
 "ssm:GetAutomationExecution",
 "ssm:DescribeAutomationStepExecutions"
 ],
 "Resource": "arn:aws:ssm:*:`111122223333`:automation-execution/*"
 },
 {
 "Sid": "ListAndDescribeResourceSchedulerSSMDocuments",
 "Effect": "Allow",
 "Action": [
 "ssm:ListDocumentVersions",
 "ssm:DescribeDocument",
 "ssm:ListDocumentMetadataHistory",
 "ssm:DescribeDocumentParameters",
 "ssm:GetDocument",
 "ssm:DescribeDocumentPermission"
 ],
 "Resource": [
 "arn:aws:ssm:*::document/AWSManagedServices-AddOrUpdatePeriod",
 "arn:aws:ssm:*::document/AWSManagedServices-AddOrUpdateSchedule",
 "arn:aws:ssm:*::document/AWSManagedServices-DeleteScheduleOrPeriod",
 "arn:aws:ssm:*::document/AWSManagedServices-DescribeScheduleOrPeriods",
 "arn:aws:ssm:*::document/AWSManagedServices-EnableOrDisableAMSResourceScheduler"
 ]
 },
 {
 "Sid": "AllowExecutionOfResourceSchedulerSSMDocuments",
 "Effect": "Allow",
 "Action": [
 "ssm:StartAutomationExecution"
 ],
 "Resource": [
 "arn:aws:ssm:*::document/AWSManagedServices-AddOrUpdatePeriod",
 "arn:aws:ssm:*::document/AWSManagedServices-AddOrUpdateSchedule",
 "arn:aws:ssm:*::document/AWSManagedServices-DeleteScheduleOrPeriod",
 "arn:aws:ssm:*::document/AWSManagedServices-DescribeScheduleOrPeriods",
 "arn:aws:ssm:*::document/AWSManagedServices-EnableOrDisableAMSResourceScheduler",
 "arn:aws:ssm:*:`111122223333`:automation-execution/*"
 ]
 },
 {
 "Sid": "AllowListingAllDocuments",
 "Effect": "Allow",
 "Action": "ssm:ListDocuments",
 "Resource": "*"
 },
 {
 "Sid": "AllowListingAllSSMExecutions",
 "Effect": "Allow",
 "Action": "ssm:DescribeAutomationExecutions",
 "Resource": "*"
 },
 {
 "Sid": "AllowListingIAMRolesForStartingExecutionViaConsole",
 "Effect": "Allow",
 "Action": "iam:ListRoles",
 "Resource": "*"
 }
 ]
}`

```

You can run the automation either from AWS Systems Manager console or using the AWS CLI. If using the AWS CLI, you might need to install and
configure it or the AWS tools for PowerShell, if you haven't already. For information, see
[Install or upgrade AWS command line tools](../../../systems-manager/latest/userguide/getting-started-cli.md "../../../systems-manager/latest/userguide/getting-started-cli.md").
