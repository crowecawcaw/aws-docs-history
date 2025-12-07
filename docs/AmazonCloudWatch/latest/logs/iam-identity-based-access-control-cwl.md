# Using identity-based policies

(IAM policies) for CloudWatch Logs

This topic provides examples of identity-based policies in which an account
administrator can attach permissions policies to IAM identities (that is, users,
groups, and roles).

###### Important

We recommend that you first review the introductory topics that explain the basic
concepts and options available for you to manage access to your CloudWatch Logs resources. For
more information, see [Overview of managing access
permissions to your CloudWatch Logs resources](iam-access-control-overview-cwl.md "iam-access-control-overview-cwl.md").

This topic covers the following:

- [Permissions required to use the CloudWatch
  console](#console-permissions-cwl "#console-permissions-cwl")
- [AWS managed (predefined) policies for
  CloudWatch Logs](#managed-policies-cwl "#managed-policies-cwl")
- [Customer managed policy
  examples](#customer-managed-policies-cwl "#customer-managed-policies-cwl")
  The following is an example of a permissions policy:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "logs:CreateLogGroup",
 "logs:CreateLogStream",
 "logs:PutLogEvents",
 "logs:DescribeLogStreams"
 ],
 "Resource": [
 "arn:aws:logs:*:*:*"
 ]
 }
 ]
}`

```

This policy has one statement that grants permissions to create log groups and log
streams, to upload log events to log streams, and to list details about log
streams.

The wildcard character (\*) at the end of the `Resource` value means that
the statement allows permission for the `logs:CreateLogGroup`,
`logs:CreateLogStream`, `logs:PutLogEvents`, and
`logs:DescribeLogStreams` actions on any log group. To limit this
permission to a specific log group, replace the wildcard character (\*) in the resource
ARN with the specific log group ARN. For more information about the sections within an
IAM policy statement, see [IAM Policy
Elements Reference](../../../IAM/latest/UserGuide/AccessPolicyLanguage_ElementDescriptions.md "../../../IAM/latest/UserGuide/AccessPolicyLanguage_ElementDescriptions.md") in _IAM User Guide_. For a list
showing all of the CloudWatch Logs actions, see [CloudWatch Logs permissions reference](permissions-reference-cwl.md "permissions-reference-cwl.md").

## Permissions required to use the CloudWatch

console

For a user to work with CloudWatch Logs in the CloudWatch console, that user must have a minimum
set of permissions that allows the user to describe other AWS resources in their
AWS account. In order to use CloudWatch Logs in the CloudWatch console, you must have permissions
from the following services:

- CloudWatch
- CloudWatch Logs
- OpenSearch Service
- IAM
- Kinesis
- Lambda
- Amazon S3

If you create an IAM policy that is more restrictive than the minimum required
permissions, the console won't function as intended for users with that IAM
policy. To ensure that those users can still use the CloudWatch console, also attach the
`CloudWatchReadOnlyAccess` managed policy to the user, as described
in [AWS managed (predefined) policies for
CloudWatch Logs](#managed-policies-cwl "#managed-policies-cwl").

You don't need to allow minimum console permissions for users that are making
calls only to the AWS CLI or the CloudWatch Logs API.

The full set of permissions required to work with the CloudWatch console for a user who
is not using the console to manage log subscriptions are:

- cloudwatch:GetMetricData
- cloudwatch:ListMetrics
- logs:CancelExportTask
- logs:CreateExportTask
- logs:CreateLogGroup
- logs:CreateLogStream
- logs:DeleteLogGroup
- logs:DeleteLogStream
- logs:DeleteMetricFilter
- logs:DeleteQueryDefinition
- logs:DeleteRetentionPolicy
- logs:DeleteSubscriptionFilter
- logs:DescribeExportTasks
- logs:DescribeLogGroups
- logs:DescribeLogStreams
- logs:DescribeMetricFilters
- logs:DescribeQueryDefinitions
- logs:DescribeQueries
- logs:DescribeSubscriptionFilters
- logs:FilterLogEvents
- logs:GetLogEvents
- logs:GetLogGroupFields
- logs:GetLogRecord
- logs:GetQueryResults
- logs:PutMetricFilter
- logs:PutQueryDefinition
- logs:PutRetentionPolicy
- logs:StartQuery
- logs:StopQuery
- logs:PutSubscriptionFilter
- logs:TestMetricFilter

For a user who will also be using the console to manage log subscriptions, the
following permissions are also required:

- es:DescribeElasticsearchDomain
- es:ListDomainNames
- iam:AttachRolePolicy
- iam:CreateRole
- iam:GetPolicy
- iam:GetPolicyVersion
- iam:GetRole
- iam:ListAttachedRolePolicies
- iam:ListRoles
- kinesis:DescribeStreams
- kinesis:ListStreams
- lambda:AddPermission
- lambda:CreateFunction
- lambda:GetFunctionConfiguration
- lambda:ListAliases
- lambda:ListFunctions
- lambda:ListVersionsByFunction
- lambda:RemovePermission
- s3:ListBuckets

## AWS managed (predefined) policies for

CloudWatch Logs

AWS addresses many common use cases by providing standalone IAM policies that
are created and administered by AWS. Managed policies grant necessary permissions
for common use cases so you can avoid having to investigate what permissions are
needed. For more information, see [AWS Managed Policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") in the
_IAM User Guide_.

The following AWS managed policies, which you can attach to users and roles in
your account, are specific to CloudWatch Logs:

- **CloudWatchLogsFullAccess** – Grants full access
  to CloudWatch Logs.
- **CloudWatchLogsReadOnlyAccess** – Grants read-only
  access to CloudWatch Logs.

### CloudWatchLogsFullAccess

The **CloudWatchLogsFullAccess** policy grants full access
to CloudWatch Logs. The policy includes the `cloudwatch:GenerateQuery` and
`cloudwatch:GenerateQueryResultsSummary` permissions, so that
users with this policy can generate a [CloudWatch Logs
Insights](AnalyzingLogData.md "AnalyzingLogData.md") query string from a natural language prompt. To see the
full contents of the policy, see [CloudWatchLogsFullAccess](../../../aws-managed-policy/latest/reference/CloudWatchLogsFullAccess.md "../../../aws-managed-policy/latest/reference/CloudWatchLogsFullAccess.md") in the _AWS Managed Policy
Reference Guide_.

### CloudWatchLogsReadOnlyAccess

The **CloudWatchLogsReadOnlyAccess** policy grants read-only
access to CloudWatch Logs.

It includes the `cloudwatch:GenerateQuery` and
`cloudwatch:GenerateQueryResultsSummary` permissions, so that
users with this policy can generate a [CloudWatch Logs
Insights](AnalyzingLogData.md "AnalyzingLogData.md") query string from a natural language prompt. To see the
full contents of the policy, see [CloudWatchLogsReadOnlyAccess](../../../aws-managed-policy/latest/reference/CloudWatchLogsReadOnlyAccess.md "../../../aws-managed-policy/latest/reference/CloudWatchLogsReadOnlyAccess.md") in the _AWS Managed Policy
Reference Guide_.

### CloudWatchOpenSearchDashboardsFullAccess

The **CloudWatchOpenSearchDashboardsFullAccess** policy
grants access to create, manage, and delete integrations with OpenSearch Service, and to
create delete and manage vended log dashboards in those integrations. For more
information, see [Analyze with Amazon OpenSearch Service](CloudWatchLogs-OpenSearch-Dashboards.md "CloudWatchLogs-OpenSearch-Dashboards.md").

To see the full contents of the policy, see [CloudWatchOpenSearchDashboardsFullAccess](../../../aws-managed-policy/latest/reference/CloudWatchOpenSearchDashboardsFullAccess.md "../../../aws-managed-policy/latest/reference/CloudWatchOpenSearchDashboardsFullAccess.md") in the _AWS
Managed Policy Reference Guide_.

### CloudWatchOpenSearchDashboardAccess

The **CloudWatchOpenSearchDashboardAccess** policy grants
access to view vended logs dashboards that are created with
Amazon OpenSearch Service analytics. For more information, see [Analyze with Amazon OpenSearch Service](CloudWatchLogs-OpenSearch-Dashboards.md "CloudWatchLogs-OpenSearch-Dashboards.md").

###### Important

In addition to granting this policy, to enable a role or user to be able
to view vended log dashboards, you must also specify them when you create
the integration with OpenSearch Service. For more information, see [Step 1: Create the integration with
OpenSearch Service](OpenSearch-Dashboards-Integrate.md "OpenSearch-Dashboards-Integrate.md").

To see the full contents of the policy, see [CloudWatchOpenSearchDashboardAccess](../../../aws-managed-policy/latest/reference/CloudWatchOpenSearchDashboardAccess.md "../../../aws-managed-policy/latest/reference/CloudWatchOpenSearchDashboardAccess.md") in the _AWS Managed
Policy Reference Guide_.

#### CloudWatchLogsCrossAccountSharingConfiguration

The **CloudWatchLogsCrossAccountSharingConfiguration**
policy grants access to create, manage, and view Observability Access
Manager links for sharing CloudWatch Logs resources between accounts. For more
information, see [CloudWatch cross-account observability](../monitoring/CloudWatch-Unified-Cross-Account.md "../monitoring/CloudWatch-Unified-Cross-Account.md").

To see the full contents of the policy, see [CloudWatchLogsCrossAccountSharingConfiguration](../../../aws-managed-policy/latest/reference/CloudWatchLogsCrossAccountSharingConfiguration.md "../../../aws-managed-policy/latest/reference/CloudWatchLogsCrossAccountSharingConfiguration.md") in the
_AWS Managed Policy Reference Guide_.

### CloudWatch Logs updates to AWS managed

policies

View details about updates to AWS managed policies for CloudWatch Logs since this
service began tracking these changes. For automatic alerts about changes to this
page, subscribe to the RSS feed on the CloudWatch Logs Document history page.

| Change                                                                                                                                                                                                        | Description                                                                                                                                                                                                                                                                                                                                                                                                                               | Date              |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| [CloudWatchLogsFullAccess](#managed-policies-cwl-CloudWatchLogsFullAccess "#managed-policies-cwl-CloudWatchLogsFullAccess") –<br>Update to an existing policy.                                                | CloudWatch Logs added permissions to **CloudWatchLogsFullAccess**.<br>Permissions for observability administration actions were added to allow read-only<br>access to telemetry pipelines and S3 table integrations.                                                                                                                                                                                                                      | December 02, 2025 |
| [CloudWatchLogsReadOnlyAccess](#managed-policies-cwl-CloudWatchLogsReadOnlyAccess "#managed-policies-cwl-CloudWatchLogsReadOnlyAccess") –<br>Update to an existing policy.                                    | CloudWatch Logs added permissions to **CloudWatchLogsReadOnlyAccess**.<br>Permissions for observability administration actions were added to allow read-only<br>access to telemetry pipelines and S3 table integrations.                                                                                                                                                                                                                  | December 02, 2025 |
| [CloudWatchLogsFullAccess](#managed-policies-cwl-CloudWatchLogsFullAccess "#managed-policies-cwl-CloudWatchLogsFullAccess") – Update to an<br>existing policy.                                                | CloudWatch Logs added permissions to<br>**CloudWatchLogsFullAccess**.<br>Permissions for<br>`cloudwatch:GenerateQueryResultsSummary` were<br>added to allow for generation of a natural language summary<br>of the query results.                                                                                                                                                                                                         | May 20, 2025      |
| [CloudWatchLogsReadOnlyAccess](#managed-policies-cwl-CloudWatchLogsReadOnlyAccess "#managed-policies-cwl-CloudWatchLogsReadOnlyAccess") – Update to<br>an existing policy.                                    | CloudWatch Logs added permissions to<br>**CloudWatchLogsReadOnlyAccess**.<br>Permissions for<br>`cloudwatch:GenerateQueryResultsSummary` were<br>added to allow for generation of a natural language summary<br>of the query results.                                                                                                                                                                                                     | May 20, 2025      |
| [CloudWatchLogsFullAccess](#managed-policies-cwl-CloudWatchLogsFullAccess "#managed-policies-cwl-CloudWatchLogsFullAccess") – Update to an<br>existing policy.                                                | CloudWatch Logs added permissions to<br>**CloudWatchLogsFullAccess**.<br>Permissions for Amazon OpenSearch Service and IAM<br>were added, to enable CloudWatch Logs integration with OpenSearch Service for some<br>features.                                                                                                                                                                                                             | December 1, 2024  |
| [CloudWatchOpenSearchDashboardsFullAccess](#managed-policies-cwl-CloudWatchOpenSearchDashboardsFullAccess "#managed-policies-cwl-CloudWatchOpenSearchDashboardsFullAccess")<br>– New IAM policy.              | CloudWatch Logs added a new IAM policy,<br>**CloudWatchOpenSearchDashboardsFullAccess**.-<br>This policy grants access to create, manage, and delete<br>integrations with OpenSearch Service, and to create, manage, and delete<br>vended log dashboards in those integrations. For more<br>information, see [Analyze with Amazon OpenSearch Service](CloudWatchLogs-OpenSearch-Dashboards.md "CloudWatchLogs-OpenSearch-Dashboards.md"). | December 1, 2024  |
| [CloudWatchOpenSearchDashboardAccess](#managed-policies-cwl-CloudWatchOpenSearchDashboardAccess "#managed-policies-cwl-CloudWatchOpenSearchDashboardAccess") – New<br>IAM policy.                             | CloudWatch Logs added a new IAM policy,<br>**CloudWatchOpenSearchDashboardAccess**.-<br>This policy grants access to view vended logs dashboards<br>powered by Amazon OpenSearch Service. For more<br>information, see [Analyze with Amazon OpenSearch Service](CloudWatchLogs-OpenSearch-Dashboards.md "CloudWatchLogs-OpenSearch-Dashboards.md").                                                                                       | December 1, 2024  |
| [CloudWatchLogsFullAccess](#managed-policies-cwl-CloudWatchLogsFullAccess "#managed-policies-cwl-CloudWatchLogsFullAccess") – Update to an<br>existing policy.                                                | CloudWatch Logs added a permission to<br>**CloudWatchLogsFullAccess**.<br>The `cloudwatch:GenerateQuery` permission was<br>added, so that users with this policy can generate a [CloudWatch Logs Insights](AnalyzingLogData.md "AnalyzingLogData.md") query string from a natural<br>language prompt.                                                                                                                                     | November 27, 2023 |
| [CloudWatchLogsReadOnlyAccess](#managed-policies-cwl-CloudWatchLogsReadOnlyAccess "#managed-policies-cwl-CloudWatchLogsReadOnlyAccess") – Update to<br>an existing policy.                                    | CloudWatch added a permission to<br>**CloudWatchLogsReadOnlyAccess**.<br>The `cloudwatch:GenerateQuery` permission was<br>added, so that users with this policy can generate a [CloudWatch Logs Insights](AnalyzingLogData.md "AnalyzingLogData.md") query string from a natural<br>language prompt.                                                                                                                                      | November 27, 2023 |
| [CloudWatchLogsReadOnlyAccess](#managed-policies-cwl-CloudWatchLogsReadOnlyAccess "#managed-policies-cwl-CloudWatchLogsReadOnlyAccess") – Update to<br>an existing policy                                     | CloudWatch Logs added permissions to<br>**CloudWatchLogsReadOnlyAccess**.<br>The `logs:StartLiveTail` and<br>`logs:StopLiveTail` permissions were added so<br>that users with this policy can use the console to start and<br>stop CloudWatch Logs live tail sessions. For more information, see<br>[Use live tail to view logs in near real<br>time](CloudWatchLogs_LiveTail.md "CloudWatchLogs_LiveTail.md").                           | June 6, 2023      |
| [CloudWatchLogsCrossAccountSharingConfiguration](#managed-policies-cwl-CloudWatchLogsCrossAccountSharingConfiguration "#managed-policies-cwl-CloudWatchLogsCrossAccountSharingConfiguration")<br>– New policy | CloudWatch Logs added a new policy to enable you to manage CloudWatch<br>cross-account observability links that share CloudWatch Logs log<br>groups.<br>For more information, see [CloudWatch cross-account observability](../monitoring/CloudWatch-Unified-Cross-Account.md "../monitoring/CloudWatch-Unified-Cross-Account.md")                                                                                                         | November 27, 2022 |
| [CloudWatchLogsReadOnlyAccess](#managed-policies-cwl-CloudWatchLogsReadOnlyAccess "#managed-policies-cwl-CloudWatchLogsReadOnlyAccess") – Update to<br>an existing policy                                     | CloudWatch Logs added permissions to<br>**CloudWatchLogsReadOnlyAccess**.<br>The `oam:ListSinks` and<br>`oam:ListAttachedLinks` permissions were<br>added so that users with this policy can use the console to<br>view data shared from source accounts in CloudWatch cross-account<br>observability.                                                                                                                                    | November 27, 2022 |

### Customer managed policy

examples

You can create your own custom IAM policies to allow permissions for CloudWatch Logs
actions and resources. You can attach these custom policies to the users or
groups that require those permissions.

In this section, you can find example user policies that grant permissions for
various CloudWatch Logs actions. These policies work when you are using the CloudWatch Logs API,
AWS SDKs, or the AWS CLI.

###### Examples

- [Example 1: Allow full access to CloudWatch Logs](#w2aac53c15c15c23c19b9 "#w2aac53c15c15c23c19b9")
- [Example 2: Allow read-only access to CloudWatch Logs](#w2aac53c15c15c23c19c11 "#w2aac53c15c15c23c19c11")
- [Example 3: Allow access to one log group](#w2aac53c15c15c23c19c13 "#w2aac53c15c15c23c19c13")

#### Example 1: Allow full access to CloudWatch Logs

The following policy allows a user to access all CloudWatch Logs actions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "logs:*"
 ],
 "Effect": "Allow",
 "Resource": "*"
 }
 ]
}`

```

#### Example 2: Allow read-only access to CloudWatch Logs

AWS provides a **CloudWatchLogsReadOnlyAccess** policy
that enables read-only access to CloudWatch Logs data. This policy includes the
following permissions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "logs:Describe*",
 "logs:Get*",
 "logs:List*",
 "logs:StartQuery",
 "logs:StopQuery",
 "logs:TestMetricFilter",
 "logs:FilterLogEvents",
 "logs:StartLiveTail",
 "logs:StopLiveTail",
 "cloudwatch:GenerateQuery"
 ],
 "Effect": "Allow",
 "Resource": "*"
 }
 ]
}`

```

#### Example 3: Allow access to one log group

The following policy allows a user to read and write log events in one
specified log group.

###### Important

The `:*` at the end of the log group name in the
`Resource` line is required to indicate that the policy
applies to all log streams in this log group. If you omit
`:*`, the policy will not be enforced.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Action": [
 "logs:CreateLogStream",
 "logs:DescribeLogStreams",
 "logs:PutLogEvents",
 "logs:GetLogEvents"
 ],
 "Effect": "Allow",
 "Resource": "arn:aws:logs:us-west-2:123456789012:log-group:SampleLogGroupName:*"
 }
 ]
}`

```

### Use tagging and IAM policies for

control at the log group level

You can grant users access to certain log groups while preventing them from
accessing other log groups. To do so, tag your log groups and use IAM policies
that refer to those tags. To apply tags to a log group, you need to have either
the `logs:TagResource` or `logs:TagLogGroup` permission.
This applies both if you are assigning tags to the log group when you create it.
or assigning them later.

For more information about tagging log groups, see [Tag log groups in Amazon CloudWatch Logs](Working-with-log-groups-and-streams.md#log-group-tagging "Working-with-log-groups-and-streams.md#log-group-tagging").

When you tag log groups, you can then grant an IAM policy to a user to allow
access to only the log groups with a particular tag. For example, the following
policy statement grants access to only log groups with the value of
`Green` for the tag key `Team`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "logs:*"
 ],
 "Effect": "Allow",
 "Resource": "*",
 "Condition": {
 "StringLike": {
 "aws:ResourceTag/Team": "Green"
 }
 }
 }
 ]
}`

```

The **StopQuery** and **StopLiveTail** API
operations don't interact with AWS resources in the traditional sense. They
don't return any data, put any data, or modify a resource in any way. Instead,
they operate only on a given live tail session or a given CloudWatch Logs Insights query,
which are not categorized as resources. As a result, when you specify the
`Resource` field in IAM policies for these operations, you must
set the value of the `Resource` field as `*`, as in the
following example.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":
 [ {
 "Effect": "Allow",
 "Action": [
 "logs:StopQuery",
 "logs:StopLiveTail"
 ],
 "Resource": "*"
 }
 ]
}`

```

For more information about using IAM policy statements, see [Controlling Access Using
Policies](../../../IAM/latest/UserGuide/access_controlling.md "../../../IAM/latest/UserGuide/access_controlling.md") in the _IAM User Guide_.
