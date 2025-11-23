# Identity-based policy examples

for Amazon SQS

By default, users and roles don't have permission to create or modify Amazon SQS
resources. To grant users permission to perform actions on the
resources that they need, an IAM administrator can create IAM policies.

To learn how to create an IAM identity-based policy by using these example JSON policy
documents, see [Create IAM policies (console)](../../../IAM/latest/UserGuide/access_policies_create-console.md "../../../IAM/latest/UserGuide/access_policies_create-console.md") in the
_IAM User Guide_.

For details about actions and resource types defined by Amazon SQS, including the format of the ARNs for each of the resource types, see [Actions, Resources, and Condition Keys for Amazon Simple Queue Service](../../../IAM/latest/UserGuide/list_amazonsqs.md "../../../IAM/latest/UserGuide/list_amazonsqs.md") in the _Service Authorization Reference_.

###### Note

When you configure lifecycle hooks for Amazon EC2 Auto Scaling, you don't need to write a
policy to send messages to an Amazon SQS queue. For more information, see [Amazon EC2 Auto Scaling Lifecycle Hooks](../../../autoscaling/ec2/userguide/lifecycle-hooks.md "../../../autoscaling/ec2/userguide/lifecycle-hooks.md") in
the _Amazon EC2 User Guide_.

## Policy best

practices

Identity-based policies determine whether someone can create, access, or delete Amazon SQS resources in your
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

## Using the

Amazon SQS console

To access the Amazon Simple Queue Service console, you must have a minimum set of permissions.
These permissions must allow you to list and view details about the Amazon SQS resources
in your AWS account. If you create an identity-based policy that is more restrictive
than the minimum required permissions, the console won't function as intended for
entities (users or roles) with that policy.

You don't need to allow minimum console permissions for users that are making calls
only to the AWS CLI or the AWS API. Instead, allow access to only the actions that match
the API operation that they're trying to perform.

To ensure that users and roles can still use the Amazon SQS console, also
attach the Amazon SQS `AmazonSQSReadOnlyAccess` AWS managed policy
to the entities. For more information, see [Adding permissions to a user](../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console "../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console") in the
_IAM User Guide_.

## Allow users to view their own permissions

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

## Allow a user to create queues

In the following example, we create a policy for Bob that lets him access all
Amazon SQS actions, but only with queues whose names are prefixed with the literal
string `alice_queue_`.

Amazon SQS doesn't automatically grant the creator of a queue permissions to use
the queue. Therefore, we must explicitly grant Bob permissions to use all Amazon SQS
actions in addition to `CreateQueue` action in the IAM
policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Effect": "Allow",
 "Action": "sqs:*",
 "Resource": "arn:aws:sqs:*:123456789012:alice_queue_*"
 }]
}`

```

## Allow developers to write

messages to a shared queue

In the following example, we create a group for developers and attach a policy
that lets the group use the Amazon SQS `SendMessage` action, but only with
the queue that belongs to the specified AWS account and is named
`MyCompanyQueue`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Effect": "Allow",
 "Action": "sqs:SendMessage",
 "Resource": "arn:aws:sqs:*:123456789012:MyCompanyQueue"
 }]
}`

```

You can use `*` instead of `SendMessage` to grant the
following actions to a principal on a shared queue:
`ChangeMessageVisibility`, `DeleteMessage`,
`GetQueueAttributes`, `GetQueueUrl`,
`ReceiveMessage`, and `SendMessage`.

###### Note

Although `*` includes access provided by other permission
types, Amazon SQS considers permissions separately. For example, it is possible
to grant both `*` and `SendMessage` permissions to a
user, even though a `*` includes the access provided by
`SendMessage`.

This concept also applies when you remove a permission. If a principal has
only a `*` permission, requesting to remove a
`SendMessage` permission _doesn't_ leave
the principal with an _everything-but_ permission.
Instead, the request has no effect, because the principal doesn't possess an
explicit `SendMessage` permission. To leave the principal with
only the `ReceiveMessage` permission, first add the
`ReceiveMessage` permission and then remove the
`*` permission.

## Allow managers to get the general size of

queues

In the following example, we create a group for managers and attach a policy
that lets the group use the Amazon SQS `GetQueueAttributes` action with
all of the queues that belong to the specified AWS account.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Effect": "Allow",
 "Action": "sqs:GetQueueAttributes",
 "Resource": "*"
 }]
}`

```

## Allow a partner to send

messages to a specific queue

You can accomplish this task using an Amazon SQS policy or an IAM policy. If your
partner has an AWS account, it might be easier to use an Amazon SQS policy.
However, any user in the partner's company who possesses the AWS security
credentials can send messages to the queue. If you want to limit access to a
particular user or application, you must treat the partner like a user in your
own company and use an IAM policy instead of an Amazon SQS policy.

This example performs the following actions:

1. Create a group called WidgetCo to represent the partner
   company.
2. Create a user for the specific user or application at the partner's
   company who needs access.
3. Add the user to the group.
4. Attach a policy that gives the group access only to the
   `SendMessage` action for only the queue named
   `WidgetPartnerQueue`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Effect": "Allow",
 "Action": "sqs:SendMessage",
 "Resource": "arn:aws:sqs:*:123456789012:WidgetPartnerQueue"
 }]
}`

```
