# AWS managed policies for Amazon Q Business

An AWS managed policy is a standalone policy that is created and administered by AWS. AWS managed policies are designed
to provide permissions for many common use cases so that you can start assigning permissions to users, groups, and roles.

Keep in mind that AWS managed policies might not grant least-privilege permissions for your specific use cases because
they're available for all AWS customers to use. We recommend that you reduce permissions further by defining
[customer managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#customer-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#customer-managed-policies") that are specific to your use cases.

You cannot change the permissions defined in AWS managed policies. If AWS updates the permissions defined in an AWS
managed policy, the update affects all principal identities (users, groups, and roles) that the policy is attached to. AWS is
most likely to update an AWS managed policy when a new AWS service is launched or new API operations become available for
existing services.

For more information, see [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") in the
_IAM User Guide_.

###### Topics

- [AWS managed policy:
  QBusinessServiceRolePolicy](#security-iam-awsmanpol-amazonq-app-role-policy "#security-iam-awsmanpol-amazonq-app-role-policy")
- [AWS managed policy:
  QBusinessQuicksightPluginPolicy](#security-iam-awsmanpol-amazonq-quicksight-policy "#security-iam-awsmanpol-amazonq-quicksight-policy")
- [Amazon Q Business updates to AWS
  managed policies](#security-iam-awsmanpol-updates "#security-iam-awsmanpol-updates")

## AWS managed policy:

QBusinessServiceRolePolicy

Amazon Q Business uses a `QBusinessServiceRolePolicy` to enable an
Amazon Q Business application to access CloudWatch resources and write CloudWatch logs. You
can't attach `QBusinessServiceRolePolicy` to your IAM entities. This policy is
attached to a service-linked role that allows Amazon Q Business to perform actions on
your behalf. For more information, see [Using service-linked roles for Amazon Q Business](using-service-linked-roles.md "using-service-linked-roles.md").

**Permissions details**

This policy includes the following permissions.

- `logs` – Allows Amazon Q Business to describe and write to
  CloudWatch log streams.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "QBusinessPutMetricDataPermission",
 "Effect": "Allow",
 "Action": [
 "cloudwatch:PutMetricData"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "cloudwatch:namespace": "AWS/QBusiness"
 }
 }
 },
 {
 "Sid": "QBusinessCreateLogGroupPermission",
 "Effect": "Allow",
 "Action": [
 "logs:CreateLogGroup"
 ],
 "Resource": [
 "arn:aws:logs:*:*:log-group:/aws/qbusiness/*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:ResourceAccount": "${aws:PrincipalAccount}"
 }
 }
 },
 {
 "Sid": "QBusinessDescribeLogGroupsPermission",
 "Effect": "Allow",
 "Action": [
 "logs:DescribeLogGroups"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceAccount": "${aws:PrincipalAccount}"
 }
 }
 },
 {
 "Sid": "QBusinessLogStreamPermission",
 "Effect": "Allow",
 "Action": [
 "logs:DescribeLogStreams",
 "logs:CreateLogStream",
 "logs:PutLogEvents"
 ],
 "Resource": [
 "arn:aws:logs:*:*:log-group:/aws/qbusiness/*:log-stream:*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:ResourceAccount": "${aws:PrincipalAccount}"
 }
 }
 }
 ]
}`

```

## AWS managed policy:

QBusinessQuicksightPluginPolicy

Amazon Q Business uses a `QBusinessQuicksightPluginPolicy` to enable an
Amazon Q Business application to access Amazon Quick Suite topics and dashboards for the
Amazon Q Business Quick Suite plugin. When you configure the plugin, you specify a
service role that has `PredictQAResults` permissions for Quick Suite topics and
dashboards. You can use the following `QBusinessQuicksightPluginPolicy` policy
to grant these permissions.

###### Note

To grant the necessary permissions, the trust policy of the role must grant Quick Suite
assume role permissions. For more information see [Using the Quick Suite plugin to get insights from
structured data](quicksight-plugin.md "quicksight-plugin.md").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "QBusinessToQuickSightPredictQAResultsInvocation",
 "Effect": "Allow",
 "Action": [
 "quicksight:PredictQAResults"
 ],
 "Resource": [
 "arn:aws:quicksight:*:*:topic/*",
 "arn:aws:quicksight:*:*:dashboard/*"
 ]
 }
 ]
}`

```

## Amazon Q Business updates to AWS

managed policies

View details about updates to AWS managed policies for Amazon Q Business since
this service began tracking these changes. For automatic alerts about changes to this page,
subscribe to the RSS feed on the [Amazon Q Business Document history page](../business-use-dg/doc-history.md "../business-use-dg/doc-history.md").

| Change                                              | Description                                                                                                                   | Date             |
| --------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| AWS managed policy: QBusinessQuicksightPluginPolicy | Added AWS managed policy QBusinessQuicksightPluginPolicy to access<br>Amazon Quick Suite resources for the QuickSight plugin. | December 3, 2024 |
| Amazon Q Business started tracking changes          | Amazon Q Business started tracking changes for its AWS managed<br>policies.                                                   | April 30, 2024   |
