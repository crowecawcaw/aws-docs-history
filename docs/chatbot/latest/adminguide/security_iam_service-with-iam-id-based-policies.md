AWS Chatbot is now Amazon Q Developer. [Learn more](service-rename.md "service-rename.md")

# Identity-based IAM

policies for Amazon Q Developer

A policy is an object in AWS that, when you attach it to an identity, defines their
permissions. When you create a policy to restrict or allow access to a resource, you can use
an identity-based policy.

You can attach IAM identity-based policies to IAM entities such as a user in your
AWS account, an IAM group, or an IAM role. You can define allowed or denied actions
and resources, and the conditions under which actions are allowed or denied.
Amazon Q Developer supports specific actions, resources, and condition keys.

###### Note

To learn about all of the elements that you use in a JSON policy, see [IAM JSON Policy Elements
Reference](../../../IAM/latest/UserGuide/reference_policies_elements.md "../../../IAM/latest/UserGuide/reference_policies_elements.md") in the _IAM User Guide_.

For information about the specific IAM JSON policy elements that Amazon Q Developer in chat applications supports, see
[Actions,
Resources, and Condition Keys for Amazon Q Developer in chat applications](../../../IAM/latest/UserGuide/list_awschatbot.md#awschatbot-policy-keys "../../../IAM/latest/UserGuide/list_awschatbot.md#awschatbot-policy-keys") in the
_IAM User Guide_.

###### Topics

- [Identity-based policies for
  Amazon Q Developer in chat applications](#security_iam_id-based-policy-examples "#security_iam_id-based-policy-examples")
- [Identity-based
  policy best practices](#security_iam_service-with-iam-policy-best-practices "#security_iam_service-with-iam-policy-best-practices")
- [Applying Amazon Q Developer in chat applications permissions to an IAM
  identity](#ChatbotCompleteRoleExample "#ChatbotCompleteRoleExample")
- [Allowing
  users to view their permissions](#security_iam_id-based-policy-examples-view-own-permissions "#security_iam_id-based-policy-examples-view-own-permissions")

## Identity-based policies for

Amazon Q Developer in chat applications

By default, IAM users, groups, and roles don't have permission to create or modify
Amazon Q Developer resources. They also can't perform tasks using the AWS Management Console or
AWS Command Line Interface (AWS CLI). An IAM administrator can create
IAM identity-based policies that grant entities permission to perform specific console
and CLI operations on the resources that they need. The administrator attaches
those policies to the IAM entities that require those permissions.

###### Note

In an identity-based policy, you don't specify the principal who gets the
permission (the `Principal` element) because the policy gets attached to
the entity that needs to use it.

To learn about all of the elements that you use in a policy, see [IAM JSON Policy Elements
Reference](../../../IAM/latest/UserGuide/reference_policies_elements.md "../../../IAM/latest/UserGuide/reference_policies_elements.md") in the _IAM User Guide_. For information
about the specific IAM JSON policy elements that Amazon Q Developer in chat applications supports, see [Actions, Resources,
and Condition Keys for Amazon Q Developer in chat applications](../../../IAM/latest/UserGuide/list_awschatbot.md#awschatbot-policy-keys "../../../IAM/latest/UserGuide/list_awschatbot.md#awschatbot-policy-keys") in the _IAM User Guide_.

### Amazon Q Developer in chat applications

actions for identity-based policies

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Action` element of a JSON policy describes the
actions that you can use to allow or deny access in a policy. Include actions in a policy to grant permissions to perform the associated operation.

Actions in an Amazon Q Developer policy use the following prefix before the action.

`"Action": [`

`"chatbot:"`

`]`

For example, to grant a user permission to view the list of all Slack channels
using the `DescribeSlackChannels` operation, you include the
`chatbot:DescribeSlackChannels` action in the user's policy. Policy
statements must include either an `Action` or `NotAction`
element. Amazon Q Developer defines its own set of actions that describe tasks that
you can perform with this service. To see the list of Amazon Q Developer actions, see
[Actions, Resources, and
Condition Keys for AWS Chatbot](../../../IAM/latest/UserGuide/list_awschatbot.md "../../../IAM/latest/UserGuide/list_awschatbot.md") in the _IAM User
Guide._

To specify multiple actions in a single statement, separate them with
commas.

`"Action": [`

`"chatbot:DescribeSlackChannels",`

`"chatbot:DescribeSlackWorkspaces"`

`]`

###### Important

Although you can specify multiple actions of like type in a policy using
wildcards (\*), we strongly discourage doing
so. Follow the practice of granting least
privileges and narrowing the permissions necessary for a user to perform their
work.

## Identity-based

policy best practices

Identity-based policies determine whether someone can create, access, or delete Amazon Q Developer resources in your
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

## Applying Amazon Q Developer in chat applications permissions to an IAM

identity

The following example of an Amazon Q Developer in chat applications identity-based policy controls all aspects of Slack
chat room configuration. It grants full read-only permissions to Amazon CloudWatch and Amazon CloudWatch Logs,
and Amazon Simple Notification Service (Amazon SNS) topics. It enables Slack chat room configuration through both the
Amazon Q Developer in chat applications console and CLI actions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllChatbotPermissions",
 "Action": [
 "cloudwatch:Describe*",
 "cloudwatch:Get*",
 "cloudwatch:List*",
 "logs:Get*",
 "logs:List*",
 "logs:Describe*",
 "logs:TestMetricFilter",
 "logs:FilterLogEvents",
 "sns:Get*",
 "sns:List*"
 ],
 "Effect": "Allow",
 "Resource": "*"
 },
 {
 "Sid": "AllSlackPermissions",
 "Effect": "Allow",
 "Action": [
 "chatbot:Describe*",
 "chatbot:UpdateSlackChannelConfiguration",
 "chatbot:CreateSlackChannelConfiguration",
 "chatbot:DeleteSlackChannelConfiguration"
 ],
 "Resource": "*"
 }
 ]
}`

```

In this example, `"Resource": "*"` refers to all applicable Slack
resources. You attach the policy to an IAM user, group, or role who needs access to
all Slack resources.

## Allowing

users to view their permissions

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
