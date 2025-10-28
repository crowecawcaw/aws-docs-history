# Identity-based policy examples

for AWS Config

By default, users and roles don't have permission to create or modify AWS Config
resources. To grant users permission to perform actions on the
resources that they need, an IAM administrator can create IAM policies.

To learn how to create an IAM identity-based policy by using these example JSON policy
documents, see [Create IAM policies (console)](../../../IAM/latest/UserGuide/access_policies_create-console.md "../../../IAM/latest/UserGuide/access_policies_create-console.md") in the
_IAM User Guide_.

For details about actions and resource types defined by AWS Config, including the format of the ARNs for each of the resource types, see [Actions, resources, and condition keys for AWS Config](../../../service-authorization/latest/reference/list_awsconfig.md "../../../service-authorization/latest/reference/list_awsconfig.md") in the _Service Authorization Reference_.

###### Topics

- [Policy best
  practices](#security_iam_service-with-iam-policy-best-practices "#security_iam_service-with-iam-policy-best-practices")
- [Sign up for an AWS account](#sign-up-for-aws "#sign-up-for-aws")
- [Create a user with administrative access](#create-an-admin "#create-an-admin")
- [Using the console](#security_iam_id-based-policy-examples-console "#security_iam_id-based-policy-examples-console")
- [Allow
  users to view their own permissions](#security_iam_id-based-policy-examples-view-own-permissions "#security_iam_id-based-policy-examples-view-own-permissions")
- [Read-only access to AWS Config](#read-only-config-permission "#read-only-config-permission")
- [Full access to AWS Config](#full-config-permission "#full-config-permission")
- [Controlling Access to AWS Config Rules](#supported-resource-level-permissions "#supported-resource-level-permissions")
- [Controlling Access to Aggregated Data](#resource-level-permission "#resource-level-permission")

## Policy best

practices

Identity-based policies determine whether someone can create, access, or delete AWS Config resources in your
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
  if they are used through a specific AWS service, such as AWS CloudFormation. For more information, see
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

## Sign up for an AWS account

If you do not have an AWS account, complete the following steps to create one.

###### To sign up for an AWS account

1. Open [https://portal.aws.amazon.com/billing/signup](https://portal.aws.amazon.com/billing/signup "https://portal.aws.amazon.com/billing/signup").
2. Follow the online instructions.

Part of the sign-up procedure involves receiving a phone call or text message and entering
a verification code on the phone keypad.

When you sign up for an AWS account, an _AWS account root user_ is created. The root user has access to all AWS services
and resources in the account. As a security best practice, assign administrative access to a user, and use only the root user to perform [tasks that require root user access](../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks "../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks").

AWS sends you a confirmation email after the sign-up process is
complete. At any time, you can view your current account activity and manage your account by
going to [https://aws.amazon.com/](https://aws.amazon.com/ "https://aws.amazon.com/") and choosing **My
Account**.

## Create a user with administrative access

After you sign up for an AWS account, secure your AWS account root user, enable AWS IAM Identity Center, and create an administrative user so that you
don't use the root user for everyday tasks.

###### Secure your AWS account root user

1. Sign in to the [AWS Management Console](https://console.aws.amazon.com/ "https://console.aws.amazon.com/") as the account owner by choosing **Root user** and entering your AWS account email address. On the next page, enter your password.

For help signing in by using root user, see [Signing in as the root user](../../../signin/latest/userguide/console-sign-in-tutorials.md#introduction-to-root-user-sign-in-tutorial "../../../signin/latest/userguide/console-sign-in-tutorials.md#introduction-to-root-user-sign-in-tutorial") in the _AWS Sign-In User Guide_. 2. Turn on multi-factor authentication (MFA) for your root user.

For instructions, see [Enable a virtual MFA device for your AWS account root user (console)](../../../IAM/latest/UserGuide/enable-virt-mfa-for-root.md "../../../IAM/latest/UserGuide/enable-virt-mfa-for-root.md") in the _IAM User Guide_.

###### Create a user with administrative access

1. Enable IAM Identity Center.

For instructions, see [Enabling
AWS IAM Identity Center](../../../singlesignon/latest/userguide/get-set-up-for-idc.md "../../../singlesignon/latest/userguide/get-set-up-for-idc.md") in the
_AWS IAM Identity Center User Guide_. 2. In IAM Identity Center, grant administrative access to a user.

For a tutorial about using the IAM Identity Center directory as your identity source, see [Configure user access with the default IAM Identity Center directory](../../../singlesignon/latest/userguide/quick-start-default-idc.md "../../../singlesignon/latest/userguide/quick-start-default-idc.md") in the
_AWS IAM Identity Center User Guide_.

###### Sign in as the user with administrative access

- To sign in with your IAM Identity Center user, use the sign-in URL that was sent to your email address when you created the IAM Identity Center user.

For help signing in using an IAM Identity Center user, see [Signing in to the AWS access portal](../../../signin/latest/userguide/iam-id-center-sign-in-tutorial.md "../../../signin/latest/userguide/iam-id-center-sign-in-tutorial.md") in the _AWS Sign-In User Guide_.

###### Assign access to additional users

1. In IAM Identity Center, create a permission set that follows the best practice of applying least-privilege permissions.

For instructions, see [Create a permission set](../../../singlesignon/latest/userguide/get-started-create-a-permission-set.md "../../../singlesignon/latest/userguide/get-started-create-a-permission-set.md") in the _AWS IAM Identity Center User Guide_. 2. Assign users to a group, and then assign single sign-on access to the group.

For instructions, see [Add groups](../../../singlesignon/latest/userguide/addgroups.md "../../../singlesignon/latest/userguide/addgroups.md") in the _AWS IAM Identity Center User Guide_.

## Using the AWS Config

console

To access the AWS Config console, you must have a minimum set of permissions.
These permissions must allow you to list and view details about the AWS Config resources
in your AWS account. If you create an identity-based policy that is more restrictive
than the minimum required permissions, the console won't function as intended for
entities (users or roles) with that policy.

You don't need to allow minimum console permissions for users that are making calls
only to the AWS CLI or the AWS API. Instead, allow access to only the actions that match
the API operation that they're trying to perform.

To ensure that users and roles can still use the AWS Config console, also attach
the AWS Config `AWSConfigUserAccess` AWS
managed policy to the entities. For more information, see [Adding permissions to a user](../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console "../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console") in the
_IAM User Guide_.

You must give users permissions to interact with AWS Config. For users who need full
access to AWS Config, use the [Full access to AWS Config](security_iam_id-based-policy-examples.md#full-config-permission "security_iam_id-based-policy-examples.md#full-config-permission") managed policy.

To provide access, add permissions to your users, groups, or roles:

- Users and groups in AWS IAM Identity Center:

Create a permission set. Follow the instructions in [Create a permission set](../../../singlesignon/latest/userguide/howtocreatepermissionset.md "../../../singlesignon/latest/userguide/howtocreatepermissionset.md") in the _AWS IAM Identity Center User Guide_.

- Users managed in IAM through an identity provider:

Create a role for identity federation. Follow the instructions in [Create a role for a third-party identity provider (federation)](../../../IAM/latest/UserGuide/id_roles_create_for-idp.md "../../../IAM/latest/UserGuide/id_roles_create_for-idp.md")
in the _IAM User Guide_.

- IAM users:
  - Create a role that your user can assume. Follow the instructions in [Create a role for an IAM user](../../../IAM/latest/UserGuide/id_roles_create_for-user.md "../../../IAM/latest/UserGuide/id_roles_create_for-user.md") in the _IAM User Guide_.
  - (Not recommended) Attach a policy directly to a user or add a user to a user group. Follow the instructions in [Adding permissions to a user (console)](../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console "../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console") in the _IAM User Guide_.

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

## Read-only access to AWS Config

The following example shows an AWS managed policy,
`AWSConfigUserAccess` that grants read-only access to AWS Config.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "config:Get*",
 "config:Describe*",
 "config:Deliver*",
 "config:List*",
 "config:Select*",
 "tag:GetResources",
 "tag:GetTagKeys",
 "cloudtrail:DescribeTrails",
 "cloudtrail:GetTrailStatus",
 "cloudtrail:LookupEvents"
 ],
 "Resource": "*"
 }
 ]
}`

```

In the policy statements, the `Effect` element specifies whether the
actions are allowed or denied. The `Action` element lists the specific
actions that the user is allowed to perform. The `Resource` element lists
the AWS resources the user is allowed to perform those actions on. For policies
that control access to AWS Config actions, the `Resource` element is always set
to `*`, a wildcard that means "all resources."

The values in the `Action` element correspond to the APIs that the
services support. The actions are preceded by `config:` to indicate that
they refer to AWS Config actions. You can use the `*` wildcard character in the
`Action` element, such as in the following examples:

- `"Action": ["config:*ConfigurationRecorder"]`

This allows all AWS Config actions that end with "ConfigurationRecorder"
(`StartConfigurationRecorder`,
`StopConfigurationRecorder`).

- `"Action": ["config:*"]`

This allows all AWS Config actions, but not actions for other AWS
services.

- `"Action": ["*"]`

This allows all AWS actions. This permission is suitable for a user who
acts as an AWS administrator for your account.

The read-only policy doesn't grant user permission for the actions such as
`StartConfigurationRecorder`, `StopConfigurationRecorder`,
and `DeleteConfigurationRecorder`. Users with this policy are not allowed
to start configuration recorder, stop configuration recorder, or delete
configuration recorder. For the list of AWS Config actions, see the [AWS Config API Reference](../APIReference.md "../APIReference.md").

## Full access to AWS Config

The following example shows a policy that grants full access to AWS Config. It grants
users the permission to perform all AWS Config actions. It also lets users manage files in
Amazon S3 buckets and manage Amazon SNS topics in the account that the user is associated
with.

###### Important

This policy grants broad permissions. Before granting full access, consider
starting with a minimum set of permissions and granting additional permissions
as necessary. Doing so is better practice than starting with permissions that
are too lenient and then trying to tighten them later.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "sns:AddPermission",
 "sns:CreateTopic",
 "sns:DeleteTopic",
 "sns:GetTopicAttributes",
 "sns:ListPlatformApplications",
 "sns:ListTopics",
 "sns:SetTopicAttributes"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:CreateBucket",
 "s3:GetBucketAcl",
 "s3:GetBucketLocation",
 "s3:GetBucketNotification",
 "s3:GetBucketPolicy",
 "s3:GetBucketRequestPayment",
 "s3:GetBucketVersioning",
 "s3:ListAllMyBuckets",
 "s3:ListBucket",
 "s3:ListBucketMultipartUploads",
 "s3:ListBucketVersions",
 "s3:PutBucketPolicy"
 ],
 "Resource": "arn:aws:s3:::*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "iam:CreateRole",
 "iam:GetRole",
 "iam:GetRolePolicy",
 "iam:ListRolePolicies",
 "iam:ListRoles",
 "iam:PutRolePolicy",
 "iam:AttachRolePolicy",
 "iam:CreatePolicy",
 "iam:CreatePolicyVersion",
 "iam:DeletePolicyVersion",
 "iam:CreateServiceLinkedRole"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "iam:PassRole"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "iam:PassedToService": [
 "config.amazonaws.com",
 "ssm.amazonaws.com"
 ]
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "cloudtrail:DescribeTrails",
 "cloudtrail:GetTrailStatus",
 "cloudtrail:LookupEvents"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "config:*",
 "tag:Get*"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "ssm:DescribeDocument",
 "ssm:GetDocument",
 "ssm:DescribeAutomationExecutions",
 "ssm:GetAutomationExecution",
 "ssm:ListDocuments",
 "ssm:StartAutomationExecution"
 ],
 "Resource": "*"
 }

 ]
}`

```

## Supported Resource-Level

Permissions for AWS Config Rule API Actions

Resource-level permissions refers to the ability to specify which resources users
are allowed to perform actions on. AWS Config supports resource-level permissions for
certain AWS Config rule API actions. This means that for certain AWS Config rule actions, you
can control the conditions under which when users are allowed to use those actions.
These
conditions
can be actions that must be fulfilled, or specific resources that users are allowed
to use.

The following table describes the AWS Config rule API actions that currently support
resource-level permissions. It also describes the supported resources and their ARNs
for each action. When specifying an ARN, you can use the \* wildcard in your paths;
for example, when you cannot or do not want to specify exact resource IDs.

###### Important

If an AWS Config rule API action is not listed in this table, then it does not
support resource-level permissions. If an AWS Config rule action does not support
resource-level permissions, you can grant users permissions to use the action,
but you have to specify a \* for the resource element of your policy statement.

| API Action                         | Resources                                                                                                                             |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| DeleteConfigRule                   | Config Rule arn:aws:config:`region:accountID`:config-rule/config-rule-`ID`                                                            |
| DeleteEvaluationResults            | Config Rule arn:aws:config:`region:accountID`:config-rule/config-rule-`ID`                                                            |
| DescribeComplianceByConfigRule     | Config Rule arn:aws:config:`region:accountID`:config-rule/config-rule-`ID`                                                            |
| DescribeConfigRuleEvaluationStatus | Config Rule arn:aws:config:`region:accountID`:config-rule/config-rule-`ID`                                                            |
| GetComplianceDetailsByConfigRule   | Config Rule arn:aws:config:`region:accountID`:config-rule/config-rule-`ID`                                                            |
| PutConfigRule                      | Config Rule arn:aws:config:`region:accountID`:config-rule/config-rule-`ID`                                                            |
| StartConfigRulesEvaluation         | Config Rule arn:aws:config:`region:accountID`:config-rule/config-rule-`ID`                                                            |
| PutRemediationConfigurations       | Remediation Configuration arn:aws:config:`region:accountId`:remediation-configuration/`config rule name/remediation configuration id` |
| DescribeRemediationConfigurations  | Remediation Configuration arn:aws:config:`region:accountId`:remediation-configuration/`config rule name/remediation configuration id` |
| DeleteRemediationConfiguration     | Remediation Configuration arn:aws:config:`region:accountId`:remediation-configuration/`config rule name/remediation configuration id` |
| PutRemediationExceptions           | Remediation Configuration arn:aws:config:`region:accountId`:remediation-configuration/`config rule name/remediation configuration id` |
| DescribeRemediationExceptions      | Remediation Configuration arn:aws:config:`region:accountId`:remediation-configuration/`config rule name/remediation configuration id` |
| DeleteRemediationExceptions        | Remediation Configuration arn:aws:config:`region:accountId`:remediation-configuration/`config rule name/remediation configuration id` | For example, you want to allow read access and deny write access to specific rules to specific users. In the first policy, you allow the AWS Config rule read actions such as `DescribeConfigRuleEvaluationStatus` on the specified rules. JSON `` `{ "Version":"2012-10-17", "Statement": [ { "Sid": "VisualEditor0", "Effect": "Allow", "Action": [ "config:StartConfigRulesEvaluation", "config:DescribeComplianceByConfigRule", "config:DescribeConfigRuleEvaluationStatus", "config:GetComplianceDetailsByConfigRule" ], "Resource": [ "arn:aws:config:`us-east-1`:`123456789012`:config-rule/config-rule-`ID`", "arn:aws:config:`us-east-1`:`123456789012`:config-rule/config-rule-`ID`" ] } ] }` `` In the second policy, you deny the AWS Config rule write actions on the specific rule. JSON `` `{ "Version":"2012-10-17", "Statement": [ { "Sid": "VisualEditor0", "Effect": "Deny", "Action": [ "config:PutConfigRule", "config:DeleteConfigRule", "config:DeleteEvaluationResults" ], "Resource": "arn:aws:config:`us-east-1`:`123456789012`:config-rule/config-rule-`ID`" } ] }` `` With resource-level permissions, you can allow read access and deny write access to perform specific actions on AWS Config rule API actions. ## Supported Resource-Level Permissions for Multi-Account Multi-Region Data Aggregation You can use resource-level permissions to control a user's ability to perform specific actions on multi-account multi-region data aggregation. The following AWS Config `Aggregator` APIs support resource level permissions: <br>• [BatchGetAggregateResourceConfig](../APIReference/API_BatchGetAggregateResourceConfig.md "../APIReference/API_BatchGetAggregateResourceConfig.md") <br>• [DeleteConfigurationAggregator](../APIReference/API_DeleteConfigurationAggregator.md "../APIReference/API_DeleteConfigurationAggregator.md") <br>• [DescribeAggregateComplianceByConfigRules](../APIReference/API_DescribeAggregateComplianceByConfigRules.md "../APIReference/API_DescribeAggregateComplianceByConfigRules.md") <br>• [DescribeAggregateComplianceByConformancePacks](../APIReference/API_DescribeAggregateComplianceByConformancePacks.md "../APIReference/API_DescribeAggregateComplianceByConformancePacks.md") <br>• [DescribeConfigurationAggregatorSourcesStatus](../APIReference/API_DescribeConfigurationAggregatorSourcesStatus.md "../APIReference/API_DescribeConfigurationAggregatorSourcesStatus.md") <br>• [GetAggregateComplianceDetailsByConfigRule](../APIReference/API_GetAggregateComplianceDetailsByConfigRule.md "../APIReference/API_GetAggregateComplianceDetailsByConfigRule.md") <br>• [GetAggregateConfigRuleComplianceSummary](../APIReference/API_GetAggregateConfigRuleComplianceSummary.md "../APIReference/API_GetAggregateConfigRuleComplianceSummary.md") <br>• [GetAggregateConformancePackComplianceSummary](../APIReference/API_GetAggregateConformancePackComplianceSummary.md "../APIReference/API_GetAggregateConformancePackComplianceSummary.md") <br>• [GetAggregateDiscoveredResourceCounts](../APIReference/API_GetAggregateDiscoveredResourceCounts.md "../APIReference/API_GetAggregateDiscoveredResourceCounts.md") <br>• [GetAggregateResourceConfig](../APIReference/API_GetAggregateResourceConfig.md "../APIReference/API_GetAggregateResourceConfig.md") <br>• [ListAggregateDiscoveredResources](../APIReference/API_ListAggregateDiscoveredResources.md "../APIReference/API_ListAggregateDiscoveredResources.md") <br>• [PutConfigurationAggregator](../APIReference/API_PutConfigurationAggregator.md "../APIReference/API_PutConfigurationAggregator.md") <br>• [SelectAggregateResourceConfig](../APIReference/API_SelectAggregateResourceConfig.md "../APIReference/API_SelectAggregateResourceConfig.md") For example, you can restrict access to resource data from specific users by creating two aggregators `AccessibleAggregator` and `InAccessibleAggregator` and attaching an IAM policy that allows access to `AccessibleAggregator` but denies access to `InAccessibleAggregator`. **IAM Policy for AccessibleAggregator** In this policy, you allow access to the supported aggregator actions for the AWS Config Amazon Resource Name (ARN) that you specify. In this example, the AWS Config ARN is `arn:aws:config:ap-northeast-1:`AccountID`:config-aggregator/config-aggregator-mocpsqhs`. JSON `` `{ "Version":"2012-10-17", "Statement": [ { "Sid": "ConfigAllow", "Effect": "Allow", "Action": [ "config:BatchGetAggregateResourceConfig", "config:DeleteConfigurationAggregator", "config:DescribeAggregateComplianceByConfigRules", "config:DescribeAggregateComplianceByConformancePacks", "config:DescribeConfigurationAggregatorSourcesStatus", "config:GetAggregateComplianceDetailsByConfigRule", "config:GetAggregateConfigRuleComplianceSummary", "config:GetAggregateConformancePackComplianceSummary", "config:GetAggregateDiscoveredResourceCounts", "config:GetAggregateResourceConfig", "config:ListAggregateDiscoveredResources", "config:PutConfigurationAggregator", "config:SelectAggregateResourceConfig" ], "Resource": "arn:aws:config:ap-northeast-1:`111122223333`:config-aggregator/config-aggregator-mocpsqhs" } ] }` `` **IAM Policy for InAccessibleAggregator** In this policy, you deny access to the supported aggregator actions for the AWS Config ARN that you specify. In this example, the AWS Config ARN is `arn:aws:config:ap-northeast-1:`AccountID`:config-aggregator/config-aggregator-pokxzldx`. JSON `` `{ "Version":"2012-10-17", "Statement": [ { "Sid": "ConfigDeny", "Effect": "Deny", "Action": [ "config:BatchGetAggregateResourceConfig", "config:DeleteConfigurationAggregator", "config:DescribeAggregateComplianceByConfigRules", "config:DescribeAggregateComplianceByConformancePacks", "config:DescribeConfigurationAggregatorSourcesStatus", "config:GetAggregateComplianceDetailsByConfigRule", "config:GetAggregateConfigRuleComplianceSummary", "config:GetAggregateConformancePackComplianceSummary", "config:GetAggregateDiscoveredResourceCounts", "config:GetAggregateResourceConfig", "config:ListAggregateDiscoveredResources", "config:PutConfigurationAggregator", "config:SelectAggregateResourceConfig" ], "Resource": "arn:aws:config:ap-northeast-1:`111122223333`:config-aggregator/config-aggregator-pokxzldx" } ] }` `` If a user of the developer group tries to perform any of these actions on the AWS Config ARN that you specified, that user will get an access denied exception. **Checking User Access Permissions** To show the aggregators that you have created, run the following AWS CLI command: `aws configservice describe-configuration-aggregators` When command has successfully completed, you will be able to see the details for all the aggregators associated with your account. In this example, those are `AccessibleAggregator` and `InAccessibleAggregator`: `{ "ConfigurationAggregators": [ { "ConfigurationAggregatorArn": "arn:aws:config:ap-northeast-1:AccountID:config-aggregator/config-aggregator-mocpsqhs", "CreationTime": 1517942461.442, "ConfigurationAggregatorName": "AccessibleAggregator", "AccountAggregationSources": [ { "AllAwsRegions": true, "AccountIds": [ "AccountID1", "AccountID2", "AccountID3" ] } ], "LastUpdatedTime": 1517942461.455 }, { "ConfigurationAggregatorArn": "arn:aws:config:ap-northeast-1:AccountID:config-aggregator/config-aggregator-pokxzldx", "CreationTime": 1517942461.442, "ConfigurationAggregatorName": "InAccessibleAggregator", "AccountAggregationSources": [ { "AllAwsRegions": true, "AccountIds": [ "AccountID1", "AccountID2", "AccountID3" ] } ], "LastUpdatedTime": 1517942461.455 } ] }` ###### Note For `account-aggregation-sources` enter a comma-separated list of AWS account IDs for which you want to aggregate data. Wrap the account IDs in square brackets, and be sure to escape quotation marks (for example, `"[{\"AccountIds\": [\"`AccountID1`\",\"`AccountID2`\",\"`AccountID3`\"],\"AllAwsRegions\": true}]"`). Attach the following IAM policy to deny access to `InAccessibleAggregator`, or the aggregator to which you want to deny access. JSON `` `{ "Version":"2012-10-17", "Statement": [ { "Sid": "ConfigDeny", "Effect": "Deny", "Action": [ "config:BatchGetAggregateResourceConfig", "config:DeleteConfigurationAggregator", "config:DescribeAggregateComplianceByConfigRules", "config:DescribeAggregateComplianceByConformancePacks", "config:DescribeConfigurationAggregatorSourcesStatus", "config:GetAggregateComplianceDetailsByConfigRule", "config:GetAggregateConfigRuleComplianceSummary", "config:GetAggregateConformancePackComplianceSummary", "config:GetAggregateDiscoveredResourceCounts", "config:GetAggregateResourceConfig", "config:ListAggregateDiscoveredResources", "config:PutConfigurationAggregator", "config:SelectAggregateResourceConfig" ], "Resource": "arn:aws:config:ap-northeast-1:`111122223333`:config-aggregator/config-aggregator-pokxzldx" } ] }` `` Next, you can confirm that the IAM policy works for restricting access to rules for a specific aggregator: `` aws configservice get-aggregate-compliance-details-by-config-rule --configuration-aggregator-name InAccessibleAggregator --config-rule-name `rule name` --account-id `AccountID` --aws-region `AwsRegion` `` The command should return an access denied exception: ``An error occurred (AccessDeniedException) when calling the GetAggregateComplianceDetailsByConfigRule operation: User: arn:aws:iam::`AccountID`:`user/` is not authorized to perform: config:GetAggregateComplianceDetailsByConfigRule on resource: arn:aws:config:`AwsRegion`-1:`AccountID`:config-aggregator/config-aggregator-pokxzldx`` |
