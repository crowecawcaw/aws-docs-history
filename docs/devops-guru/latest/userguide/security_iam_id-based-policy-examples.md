# Identity-based policies for

Amazon DevOps Guru

By default, users and roles don't have permission to create or modify DevOps Guru
resources. To grant users permission to perform actions on the
resources that they need, an IAM administrator can create IAM policies.

To learn how to create an IAM identity-based policy by using these example JSON policy
documents, see [Create IAM policies (console)](../../../IAM/latest/UserGuide/access_policies_create-console.md "../../../IAM/latest/UserGuide/access_policies_create-console.md") in the
_IAM User Guide_.

For details about actions and resource types defined by DevOps Guru, including the format of the ARNs for each of the resource types, see [Actions, resources, and condition keys for Amazon DevOps Guru](../../../service-authorization/latest/reference/list_awskeymanagementservice.md "../../../service-authorization/latest/reference/list_awskeymanagementservice.md") in the _Service Authorization Reference_.

###### Topics

- [Policy best
  practices](#security_iam_service-with-iam-policy-best-practices "#security_iam_service-with-iam-policy-best-practices")
- [Using the DevOps Guru
  console](#security_iam_id-based-policy-examples-console "#security_iam_id-based-policy-examples-console")
- [Allow
  users to view their own permissions](#security_iam_id-based-policy-examples-view-own-permissions "#security_iam_id-based-policy-examples-view-own-permissions")
- [AWS managed (predefined) policies for
  DevOps Guru](#managed-policies "#managed-policies")

## Policy best

practices

Identity-based policies determine whether someone can create, access, or delete DevOps Guru resources in your
account. These actions can incur costs for your AWS account. When you create or edit identity-based policies, follow these guidelines and
recommendations:

- **Get started with AWS managed policies and move toward least-privilege permissions**
  – To get started granting permissions to your users and workloads, use the _AWS
  managed policies_ that grant permissions for many common use cases. They are
  available in your AWS account. We recommend that you reduce permissions further by
  defining AWS customer managed policies that are specific to your use cases. For more information, see
  [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") or [AWS managed policies for job functions](../../../IAM/latest/UserGuide/access_policies_job-functions.md "../../../IAM/latest/UserGuide/access_policies_job-functions.md") in the _IAM User Guide_.
- **Apply least-privilege permissions** –
  When you set permissions with IAM policies, grant only the permissions required to
  perform a task. You do this by defining the actions that can be taken on specific resources
  under specific conditions, also known as _least-privilege permissions_.
  For more information about using IAM to apply permissions, see [Policies and permissions in IAM](../../../IAM/latest/UserGuide/access_policies.md "../../../IAM/latest/UserGuide/access_policies.md") in the _IAM User Guide_.
- **Use conditions in IAM policies to further restrict access**
  – You can add a condition to your policies to limit access to actions and resources. For example, you can write a policy condition to specify that all requests must
  be sent using SSL. You can also use conditions to grant access to service actions
  if they are used through a specific AWS service, such as CloudFormation. For more information, see
  [IAM JSON policy elements: Condition](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md") in the _IAM User Guide_.
- **Use IAM Access Analyzer to validate your IAM policies to ensure secure and functional permissions**
  – IAM Access Analyzer validates new and existing policies so that the policies adhere to the IAM policy language (JSON) and IAM best practices.
  IAM Access Analyzer provides more than 100 policy checks and actionable recommendations to help
  you author secure and functional policies. For more information, see [Validate policies with IAM Access Analyzer](../../../IAM/latest/UserGuide/access-analyzer-policy-validation.md "../../../IAM/latest/UserGuide/access-analyzer-policy-validation.md") in the _IAM User Guide_.
- **Require multi-factor authentication (MFA)** –
  If you have a scenario that requires IAM users or a root user in your AWS account, turn on MFA for additional security. To require
  MFA when API operations are called, add MFA conditions to your policies. For
  more information, see [Secure API access with MFA](../../../IAM/latest/UserGuide/id_credentials_mfa_configure-api-require.md "../../../IAM/latest/UserGuide/id_credentials_mfa_configure-api-require.md") in the _IAM User Guide_.

For more information about best practices in IAM, see [Security best practices in IAM](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md") in the _IAM User Guide_.

## Using the DevOps Guru

console

To access the Amazon DevOps Guru console, you must have a minimum set of permissions.
These permissions must allow you to list and view details about the DevOps Guru resources
in your AWS account. If you create an identity-based policy that is more restrictive
than the minimum required permissions, the console won't function as intended for
entities (users or roles) with that policy.

You don't need to allow minimum console permissions for users that are making calls
only to the AWS CLI or the AWS API. Instead, allow access to only the actions that match
the API operation that they're trying to perform.

To ensure that users and roles can still use the DevOps Guru console, also attach
the DevOps Guru `AmazonDevOpsGuruReadOnlyAccess` or
`AmazonDevOpsGuruFullAccess` AWS managed policy to the entities.
For more information, see [Adding permissions to a user](../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console "../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console") in the
_IAM User Guide_.

## Allow

users to view their own permissions

This example shows how you might create a policy that allows IAM users to view the inline and managed policies that are attached to their user
identity. This policy includes permissions to complete this action on the console or programmatically using the AWS CLI or AWS API.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "ViewOwnUserInfo",
            "Effect": "Allow",
            "Action": [
                "iam:GetUserPolicy",
                "iam:ListGroupsForUser",
                "iam:ListAttachedUserPolicies",
                "iam:ListUserPolicies",
                "iam:GetUser"
            ],
            "Resource": ["arn:aws:iam::*:user/${aws:username}"]
        },
        {
            "Sid": "NavigateInConsole",
            "Effect": "Allow",
            "Action": [
                "iam:GetGroupPolicy",
                "iam:GetPolicyVersion",
                "iam:GetPolicy",
                "iam:ListAttachedGroupPolicies",
                "iam:ListGroupPolicies",
                "iam:ListPolicyVersions",
                "iam:ListPolicies",
                "iam:ListUsers"
            ],
            "Resource": "*"
        }
    ]
}
```

## AWS managed (predefined) policies for

DevOps Guru

AWS addresses many common use cases by providing standalone IAM policies that
are created and administered by AWS. These AWS-managed policies grant necessary
permissions for common use cases so you can avoid having to investigate what
permissions are needed. For more information, see [AWS Managed Policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") in the
_IAM User Guide_.

To create and manage DevOps Guru service roles, you must also attach the AWS-managed
policy named `IAMFullAccess`.

You can also create your own custom IAM policies to allow permissions for DevOps Guru
actions and resources. You can attach these custom policies to the users or
groups that require those permissions.

The following AWS-managed policies, which you can attach to users in your
account, are specific to DevOps Guru.

###### Topics

- [AmazonDevOpsGuruFullAccess](#managed-full-access "#managed-full-access")
- [AmazonDevOpsGuruConsoleFullAccess](#managed-full-console-access "#managed-full-console-access")
- [AmazonDevOpsGuruReadOnlyAccess](#managed-read-only-access "#managed-read-only-access")
- [AmazonDevOpsGuruOrganizationsAccess](#organizations-policy "#organizations-policy")

### AmazonDevOpsGuruFullAccess

`AmazonDevOpsGuruFullAccess` – Provides full access to
DevOps Guru, including permissions to create Amazon SNS topics, access Amazon CloudWatch metrics,
and access AWS CloudFormation stacks. Apply this only to administrative-level users to
whom you want to grant full control over DevOps Guru.

The `AmazonDevOpsGuruFullAccess` policy contains the following
statement.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "DevOpsGuruFullAccess",
 "Effect": "Allow",
 "Action": [
 "devops-guru:*"
 ],
 "Resource": "*"
 },
 {
 "Sid": "CloudFormationListStacksAccess",
 "Effect": "Allow",
 "Action": [
 "cloudformation:DescribeStacks",
 "cloudformation:ListStacks"
 ],
 "Resource": "*"
 },
 {
 "Sid": "CloudWatchGetMetricDataAccess",
 "Effect": "Allow",
 "Action": [
 "cloudwatch:GetMetricData"
 ],
 "Resource": "*"
 },
 {
 "Sid": "SnsListTopicsAccess",
 "Effect": "Allow",
 "Action": [
 "sns:ListTopics",
 "sns:ListSubscriptionsByTopic"
 ],
 "Resource": "*"
 },
 {
 "Sid": "SnsTopicOperations",
 "Effect": "Allow",
 "Action": [
 "sns:CreateTopic",
 "sns:GetTopicAttributes",
 "sns:SetTopicAttributes",
 "sns:Subscribe",
 "sns:Publish"
 ],
 "Resource": "arn:aws:sns:*:*:DevOps-Guru-*"
 },
 {
 "Sid": "DevOpsGuruSlrCreation",
 "Effect": "Allow",
 "Action": "iam:CreateServiceLinkedRole",
 "Resource": "arn:aws:iam::*:role/aws-service-role/devops-guru.amazonaws.com/AWSServiceRoleForDevOpsGuru",
 "Condition": {
 "StringLike": {
 "iam:AWSServiceName": "devops-guru.amazonaws.com"
 }
 }
 },
 {
 "Sid": "DevOpsGuruSlrDeletion",
 "Effect": "Allow",
 "Action": [
 "iam:DeleteServiceLinkedRole",
 "iam:GetServiceLinkedRoleDeletionStatus"
 ],
 "Resource": "arn:aws:iam::*:role/aws-service-role/devops-guru.amazonaws.com/AWSServiceRoleForDevOpsGuru"
 },
 {
 "Sid": "RDSDescribeDBInstancesAccess",
 "Effect": "Allow",
 "Action": [
 "rds:DescribeDBInstances"
 ],
 "Resource": "*"
 },
 {
 "Sid": "CloudWatchLogsFilterLogEventsAccess",
 "Effect": "Allow",
 "Action": [
 "logs:FilterLogEvents"
 ],
 "Resource": "arn:aws:logs:*:*:log-group:*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/DevOps-Guru-Analysis": "true"
 }
 }
 }
 ]
}`

```

### AmazonDevOpsGuruConsoleFullAccess

`AmazonDevOpsGuruConsoleFullAccess` – Provides full
access to DevOps Guru, including permissions to create Amazon SNS topics, access Amazon CloudWatch
metrics, and access AWS CloudFormation stacks. This policy has additional performance
insights permissions so you can view detailed analysis related to anomalous
Amazon RDS Aurora DB instances in the console. Apply this only to administrative-level
users to whom you want to grant full control over DevOps Guru.

The `AmazonDevOpsGuruConsoleFullAccess` policy contains the
following statement.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "DevOpsGuruFullAccess",
 "Effect": "Allow",
 "Action": [
 "devops-guru:*"
 ],
 "Resource": "*"
 },
 {
 "Sid": "CloudFormationListStacksAccess",
 "Effect": "Allow",
 "Action": [
 "cloudformation:DescribeStacks",
 "cloudformation:ListStacks"
 ],
 "Resource": "*"
 },
 {
 "Sid": "CloudWatchGetMetricDataAccess",
 "Effect": "Allow",
 "Action": [
 "cloudwatch:GetMetricData"
 ],
 "Resource": "*"
 },
 {
 "Sid": "SnsListTopicsAccess",
 "Effect": "Allow",
 "Action": [
 "sns:ListTopics",
 "sns:ListSubscriptionsByTopic"
 ],
 "Resource": "*"
 },
 {
 "Sid": "SnsTopicOperations",
 "Effect": "Allow",
 "Action": [
 "sns:CreateTopic",
 "sns:GetTopicAttributes",
 "sns:SetTopicAttributes",
 "sns:Subscribe",
 "sns:Publish"
 ],
 "Resource": "arn:aws:sns:*:*:DevOps-Guru-*"
 },
 {
 "Sid": "DevOpsGuruSlrCreation",
 "Effect": "Allow",
 "Action": "iam:CreateServiceLinkedRole",
 "Resource": "arn:aws:iam::*:role/aws-service-role/devops-guru.amazonaws.com/AWSServiceRoleForDevOpsGuru",
 "Condition": {
 "StringLike": {
 "iam:AWSServiceName": "devops-guru.amazonaws.com"
 }
 }
 },
 {
 "Sid": "DevOpsGuruSlrDeletion",
 "Effect": "Allow",
 "Action": [
 "iam:DeleteServiceLinkedRole",
 "iam:GetServiceLinkedRoleDeletionStatus"
 ],
 "Resource": "arn:aws:iam::*:role/aws-service-role/devops-guru.amazonaws.com/AWSServiceRoleForDevOpsGuru"
 },
 {
 "Sid": "RDSDescribeDBInstancesAccess",
 "Effect": "Allow",
 "Action": [
 "rds:DescribeDBInstances"
 ],
 "Resource": "*"
 },
 {
 "Sid": "PerformanceInsightsMetricsDataAccess",
 "Effect": "Allow",
 "Action": [
 "pi:GetResourceMetrics",
 "pi:DescribeDimensionKeys"
 ],
 "Resource": "*"
 },
 {
 "Sid": "CloudWatchLogsFilterLogEventsAccess",
 "Effect": "Allow",
 "Action": [
 "logs:FilterLogEvents"
 ],
 "Resource": "arn:aws:logs:*:*:log-group:*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/DevOps-Guru-Analysis": "true"
 }
 }
 }
 ]
}`

```

### AmazonDevOpsGuruReadOnlyAccess

`AmazonDevOpsGuruReadOnlyAccess` – Grants read-only access to
DevOps Guru and related resources in other AWS services. Apply this policy to users
to whom you want to grant the ability to view insights, but not to make any
updates to DevOps Guru's analysis coverage boundary, Amazon SNS topics, or Systems Manager OpsCenter
integration.

The `AmazonDevOpsGuruReadOnlyAccess` policy contains the following
statement.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "DevOpsGuruReadOnlyAccess",
 "Effect": "Allow",
 "Action": [
 "devops-guru:DescribeAccountHealth",
 "devops-guru:DescribeAccountOverview",
 "devops-guru:DescribeAnomaly",
 "devops-guru:DescribeEventSourcesConfig",
 "devops-guru:DescribeFeedback",
 "devops-guru:DescribeInsight",
 "devops-guru:DescribeResourceCollectionHealth",
 "devops-guru:DescribeServiceIntegration",
 "devops-guru:GetCostEstimation",
 "devops-guru:GetResourceCollection",
 "devops-guru:ListAnomaliesForInsight",
 "devops-guru:ListEvents",
 "devops-guru:ListInsights",
 "devops-guru:ListAnomalousLogGroups",
 "devops-guru:ListMonitoredResources",
 "devops-guru:ListNotificationChannels",
 "devops-guru:ListRecommendations",
 "devops-guru:SearchInsights",
 "devops-guru:StartCostEstimation"
 ],
 "Resource": "*"
 },
 {
 "Sid": "CloudFormationListStacksAccess",
 "Effect": "Allow",
 "Action": [
 "cloudformation:DescribeStacks",
 "cloudformation:ListStacks"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "iam:GetRole"
 ],
 "Resource": "arn:aws:iam::*:role/aws-service-role/devops-guru.amazonaws.com/AWSServiceRoleForDevOpsGuru"
 },
 {
 "Sid": "CloudWatchGetMetricDataAccess",
 "Effect": "Allow",
 "Action": [
 "cloudwatch:GetMetricData"
 ],
 "Resource": "*"
 },
 {
 "Sid": "RDSDescribeDBInstancesAccess",
 "Effect": "Allow",
 "Action": [
 "rds:DescribeDBInstances"
 ],
 "Resource": "*"
 },
 {
 "Sid": "SnsListTopicsAccess",
 "Effect": "Allow",
 "Action": [
 "sns:ListTopics",
 "sns:ListSubscriptionsByTopic"
 ],
 "Resource": "*"
 },
 {
 "Sid": "CloudWatchLogsFilterLogEventsAccess",
 "Effect": "Allow",
 "Action": [
 "logs:FilterLogEvents"
 ],
 "Resource": "arn:aws:logs:*:*:log-group:*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/DevOps-Guru-Analysis": "true"
 }
 }
 }
 ]
}`

```

### AmazonDevOpsGuruOrganizationsAccess

`AmazonDevOpsGuruOrganizationsAccess` – Provides
Organizations administrators access to the DevOps Guru multi-account view within an
organization. Apply this policy to your organization's administrator-level users
for whom you want to grant full access to DevOps Guru within an organization. You can
apply this policy in your organization's management account and delegated
administrator account for DevOps Guru. You can apply
`AmazonDevOpsGuruReadOnlyAccess` or
`AmazonDevOpsGuruFullAccess` in addition to this policy to
provide read-only or full access to DevOps Guru.

The `AmazonDevOpsGuruOrganizationsAccess` policy contains the
following statement.
