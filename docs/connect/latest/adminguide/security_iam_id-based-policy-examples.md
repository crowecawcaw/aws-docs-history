# Amazon Connect identity-based

policy examples

By default, IAM entities don't have permission to create or modify Amazon Connect
resources. They also can't perform tasks using the AWS Management Console, AWS CLI, or AWS API. An IAM
administrator must create IAM policies that grant IAM entities permission to perform
specific API operations on the specified resources they need. The IAM administrator must
then attach those policies to the IAM entities that require those permissions.

To learn how to create an IAM identity-based policy using these example JSON policy
documents, see [Creating Policies on the JSON Tab](../../../IAM/latest/UserGuide/access_policies_create.md#access_policies_create-json-editor "../../../IAM/latest/UserGuide/access_policies_create.md#access_policies_create-json-editor") in the
_IAM User Guide_.

###### Contents

- [Policy best
  practices](#security_iam_service-with-iam-policy-best-practices "#security_iam_service-with-iam-policy-best-practices")
- [Allow IAM
  users to view their own permissions](#security_iam_id-based-policy-examples-view-own-permissions "#security_iam_id-based-policy-examples-view-own-permissions")
- [Grant "View
  User" permissions](#security_iam_id-based-policy-example-view-user-permissions "#security_iam_id-based-policy-example-view-user-permissions")
- [Allow users to
  integrate with external applications](#security_iam_id-based-policy-examples-integrate "#security_iam_id-based-policy-examples-integrate")
- [Describe and
  update Amazon Connect users based on tags](#security_iam_id-based-policy-examples-view-widget-tags "#security_iam_id-based-policy-examples-view-widget-tags")
- [Create Amazon Connect users based on
  tags](#connect-access-control-resources-example1 "#connect-access-control-resources-example1")
- [Create and view Amazon AppIntegrations
  resources](#appintegration-resources-example1 "#appintegration-resources-example1")
- [Create and view Amazon Q in Connect
  Assistants](#wisdom-resources-example1 "#wisdom-resources-example1")
- [Manage outbound campaigns
  resources](#outboundcommunications-policy-example1 "#outboundcommunications-policy-example1")

## Policy best

practices

Identity-based policies determine whether someone can create, access, or delete Amazon Connect resources in your
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

## Allow IAM

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

## Grant "View

User" permissions

When you create a user or [group](../../../IAM/latest/UserGuide/id.md#id_iam-groups "../../../IAM/latest/UserGuide/id.md#id_iam-groups") in your AWS account,
you can associate an IAM policy with that group or user, which specifies the permissions
that you want to grant.

For example, imagine you have a group of entry-level developers. You can create an
IAM group named `Junior application developers`, and include all entry-level
developers. Then, associate a policy with that group that grants them permissions to
view Amazon Connect users. In this scenario, you might have a policy such as the following
sample.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "connect:DescribeUser",
 "connect:ListUsers"
 ],
 "Resource": "*"
 }
 ]
}`

```

This sample policy grants permissions to API actions listed in the
`Action` element.

###### Note

If you don't specify a user ARN or ID in your statement, you must also grant the
permission to use all resources for the action using the \* wildcard for the
`Resource` element.

## Allow users to

integrate with external applications

This example shows how you might create a policy that allows users to interact with
their external application integrations.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowAllAppIntegrationsActions",
 "Effect": "Allow",
 "Action": [
 "app-integrations:ListEventIntegrations",
 "app-integrations:CreateEventIntegration",
 "app-integrations:GetEventIntegration",
 "app-integrations:UpdateEventIntegration",
 "app-integrations:DeleteEventIntegration",
 "app-integrations:ListDataIntegrations",
 "app-integrations:CreateDataIntegration",
 "app-integrations:GetDataIntegration",
 "app-integrations:UpdateDataIntegration",
 "app-integrations:DeleteDataIntegration"
 ],
 "Resource": "*"
 }
 ]
}`

```

## Describe and

update Amazon Connect users based on tags

In an IAM policy, you can optionally specify conditions that control when a policy is
in effect. For example, you can define a policy that allows users to update only an
Amazon Connect user who is working in the test environment.

You can define some conditions that are specific to Amazon Connect, and define other
conditions that apply to all of AWS. For more information and a list of AWS-wide
conditions, see Condition in [IAM JSON Policy
Elements Reference](../../../IAM/latest/UserGuide/reference_policies_elements.md#Condition "../../../IAM/latest/UserGuide/reference_policies_elements.md#Condition") in the _IAM User Guide_.

The following sample policy allows the "describe" and "update" actions for users with
specific tags.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "connect:DescribeUser",
 "connect:UpdateUser*"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/Department": "Test"
 }
 }
 }
 ]
}`

```

This policy allows "describe user" and "update user" but only for those Amazon Connect users
tagged with tag "Department: Test" where "Department" is the tag key and "Test" is the
tag value.

## Create Amazon Connect users based on

tags

The following sample policy allows the create actions for users with specific request
tags.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "connect:CreateUser",
 "connect:TagResource"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:RequestTag/Owner": "TeamA"
 }
 }
 }
 ]
}`

```

This policy allows "create user" and "tag resource" but the tag "Owner: TeamA" must
be present in the requests.

## Create and view Amazon AppIntegrations

resources

The following sample policy allows event integrations to be created, listed, and
fetched.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "app-integrations:CreateEventIntegration",
 "app-integrations:GetEventIntegration",
 "app-integrations:ListEventIntegrations"
 ],
 "Resource": "*"
 }
 ]
}`

```

## Create and view Amazon Q in Connect

Assistants

The following sample policy allows Amazon Q in Connect assistants to be created, listed,
fetched, and deleted.

JSON

```
`{
"Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "wisdom:CreateContent",
 "wisdom:DeleteContent",
 "wisdom:CreateKnowledgeBase",
 "wisdom:GetAssistant",
 "wisdom:GetKnowledgeBase",
 "wisdom:GetContent",
 "wisdom:GetRecommendations",
 "wisdom:GetSession",
 "wisdom:NotifyRecommendationsReceived",
 "wisdom:QueryAssistant",
 "wisdom:StartContentUpload",
 "wisdom:UpdateContent",
 "wisdom:UntagResource",
 "wisdom:TagResource",
 "wisdom:CreateSession"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/AmazonConnectEnabled": "True"
 }
 }
 },
 {
 "Action": [
 "wisdom:ListAssistants",
 "wisdom:ListKnowledgeBases"
 ],
 "Effect": "Allow",
 "Resource": "*"
 }
 ]
}`

```

## Manage outbound campaigns

resources

Onboarding permissions: The following sample policy allows Amazon Connect instances to be
onboarded to outbound campaigns.

```
"Sid": "VisualEditor0",
             "Effect": "Allow",
             "Action": [
                 "kms:DescribeKey",
                 "kms:CreateGrant"
             ],
             "Resource": [
                 "arn:aws:kms:`region`:`account-id`:key/`key-id`"
                   ]
        },
        {
             "Sid": "VisualEditor1",
             "Effect": "Allow",
             "Action": [
                 "connect:DescribeInstance"
             ],
             "Resource": [

                 "arn:aws:connect:`region`:`account-id`:instance/`instance-id`"
             ]
        },
        {
             "Sid": "VisualEditor2",
             "Effect": "Allow",
             "Action": [
                 "events:PutTargets",
                 "events:PutRule",
                 "iam:CreateServiceLinkedRole",
                 "iam:AttachRolePolicy",
                 "iam:PutRolePolicy",
                 "ds:DescribeDirectories",
                 "connect-campaigns:StartInstanceOnboardingJob",
                 "connect-campaigns:GetConnectInstanceConfig",
                 "connect-campaigns:GetInstanceOnboardingJobStatus",
                 "connect-campaigns:DeleteInstanceOnboardingJob",
                 "connect:DescribeInstanceAttribute",
                 "connect:UpdateInstanceAttribute",
                 "connect:ListInstances",
                 "kms:ListAliases"
             ],
             "Resource": "*"
        }
```

To disable outbound campaigns for an instance, add the following permissions:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "VisualEditor0",
 "Effect": "Allow",
 "Action": [
 "kms:DescribeKey",
 "kms:RetireGrant"
 ],
 "Resource": [
 "arn:aws:kms:`us-east-1`:`111122223333`:key/`KeyId`"
 ]
 },
 {
 "Sid": "VisualEditor1",
 "Effect": "Allow",
 "Action": [
 "events:DeleteRule",
 "events:RemoveTargets",
 "events:DescribeRule",
 "iam:DeleteRolePolicy",
 "events:ListTargetsByRule",
 "iam:DeleteServiceLinkedRole",
 "connect-campaigns:DeleteConnectInstanceConfig"
 ],
 "Resource": "*"
 }
 ]
}`

```

Management permissions: The following sample policy allows all read and write
operations on outbound campaigns.

```
{
    "Sid": "AllowConnectCampaignsOperations",
    "Effect": "Allow",
    "Action": [
        "connect-campaigns:CreateCampaign",
        "connect-campaigns:DeleteCampaign",
        "connect-campaigns:DescribeCampaign",
        "connect-campaigns:UpdateCampaignName",
        "connect-campaigns:GetCampaignState"
        "connect-campaigns:UpdateOutboundCallConfig",
        "connect-campaigns:UpdateDialerConfig",
        "connect-campaigns:PauseCampaign",
        "connect-campaigns:ResumeCampaign",
        "connect-campaigns:StopCampaign",
        "connect-campaigns:GetCampaignStateBatch",
        "connect-campaigns:ListCampaigns"
    ],
    "Resource": "*"
}
```

ReadOnly permissions: The following sample policy allows read-only access to the
campaigns.

```
{
    "Sid": "AllowConnectCampaignsReadOnlyOperations",
    "Effect": "Allow",
    "Action": [
        "connect-campaigns:DescribeCampaign",
        "connect-campaigns:GetCampaignState",
        "connect-campaigns:GetCampaignStateBatch",
        "connect-campaigns:ListCampaigns"
     ],
    "Resource": "*",
}
```

Tag-based permissions: The following sample policy restricts access to the campaigns
integrated with a particular Amazon Connect instance using tags. More permissions can be added
based on the use case.

```
{
    "Sid": "AllowConnectCampaignsOperations",
    "Effect": "Allow",
    "Action": [
        "connect-campaigns:DescribeCampaign",
        "connect-campaigns:GetCampaignState"
    ],
    "Resource": "*",
    "Condition": {
        "StringEquals": {
             "aws:ResourceTag/owner": "arn:aws:connect:`region`:`customer_account_id`:instance/`connect_instance_id`"
         }
    }
}
```

###### Note

`connect-campaigns:ListCampaigns` and
`connect-campaigns:GetCampaignStateBatch` operations cannot be
restricted by Tag.
