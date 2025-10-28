# Identity-based policy

examples for AWS End User Messaging SMS

By default, users and roles don't have permission to create or modify AWS End User Messaging SMS
resources. To grant users permission to perform actions on the
resources that they need, an IAM administrator can create IAM policies.

To learn how to create an IAM identity-based policy by using these example JSON policy
documents, see [Create IAM policies (console)](../../../IAM/latest/UserGuide/access_policies_create-console.md "../../../IAM/latest/UserGuide/access_policies_create-console.md") in the
_IAM User Guide_.

For details about actions and resource types defined by AWS End User Messaging SMS, including the format of the ARNs for each of the resource types, see [Actions, Resources, and Condition Keys for AWS End User Messaging SMS](../../../IAM/latest/UserGuide/list_amazonpinpointsmsvoicev2.md "../../../IAM/latest/UserGuide/list_amazonpinpointsmsvoicev2.md") in the _Service Authorization Reference_.

###### Topics

- [Policy best
  practices](#security_iam_service-with-iam-policy-best-practices "#security_iam_service-with-iam-policy-best-practices")
- [Using the AWS End User Messaging SMS
  console](#security_iam_id-based-policy-examples-console "#security_iam_id-based-policy-examples-console")
- [Allow users
  to view their own permissions](#security_iam_id-based-policy-examples-view-own-permissions "#security_iam_id-based-policy-examples-view-own-permissions")
- [Examples: Providing
  access to AWS End User Messaging SMS and Voice v2 API actions](#permissions-actions-examples-pin-sms-voice-api "#permissions-actions-examples-pin-sms-voice-api")
- [IAM role for streaming events to Kinesis](#permissions-streams "#permissions-streams")

## Policy best

practices

Identity-based policies determine whether someone can create, access, or delete AWS End User Messaging SMS resources in your
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

## Using the AWS End User Messaging SMS

console

To access the AWS End User Messaging SMS console, you must have a minimum set of permissions.
These permissions must allow you to list and view details about the AWS End User Messaging SMS resources
in your AWS account. If you create an identity-based policy that is more restrictive
than the minimum required permissions, the console won't function as intended for
entities (users or roles) with that policy.

You don't need to allow minimum console permissions for users that are making calls
only to the AWS CLI or the AWS API. Instead, allow access to only the actions that match
the API operation that they're trying to perform.

To ensure that users and roles can still use the AWS End User Messaging SMS console, also attach the
AWS End User Messaging SMS `ConsoleAccess` or `ReadOnly` AWS managed policy to
the entities. For more information, see [Adding permissions to a user](../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console "../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console") in the
_IAM User Guide_.

## Allow users

to view their own permissions

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

## Examples: Providing

access to AWS End User Messaging SMS and Voice v2 API actions

This section provides example policies that allow access to features that are
available from the AWS End User Messaging SMS and Voice v2 API. This is a supplemental API that provides
advanced options for using and managing the SMS and voice channels in AWS End User Messaging SMS. To learn
more about this API, see the [AWS End User Messaging SMS and Voice v2 API](../../../pinpoint/latest/apireference_smsvoicev2/Welcome.md "../../../pinpoint/latest/apireference_smsvoicev2/Welcome.md").

### Read-only

access

The following example policy allows read-only access to all AWS End User Messaging SMS and Voice v2 API
actions and resources in your AWS account:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "SMSVoiceReadOnly",
 "Effect": "Allow",
 "Action": [
 "sms-voice:List*",
 "sms-voice:DescribeAccountAttributes",
 "sms-voice:DescribeAccountLimits",
 "sms-voice:DescribeConfigurationSets",
 "sms-voice:DescribeKeywords",
 "sms-voice:DescribeOptedOutNumbers",
 "sms-voice:DescribeOptOutLists",
 "sms-voice:DescribePhoneNumbers",
 "sms-voice:DescribePools",
 "sms-voice:DescribeRegistrationAttachments",
 "sms-voice:DescribeRegistrationFieldDefinitions",
 "sms-voice:DescribeRegistrations",
 "sms-voice:DescribeRegistrationSectionDefinitions",
 "sms-voice:DescribeRegistrationTypeDefinitions",
 "sms-voice:DescribeRegistrationVersions",
 "sms-voice:DescribeSenderIds",
 "sms-voice:DescribeSpendLimits",
 "sms-voice:DescribeVerifiedDestinationNumbers"
 ],
 "Resource": "*"
 }
 ]
}`

```

### Administrator

access

The following example policy allows full access to all AWS End User Messaging SMS and Voice v2 API actions
and resources in your AWS account:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "SMSVoiceFullAccess",
 "Effect": "Allow",
 "Action": [
 "sms-voice:*"
 ],
 "Resource": "*"
 }
 ]
}`

```

## IAM role for streaming events to Kinesis

AWS End User Messaging SMS can automatically send app usage data, or _event data_, from
your app to an Amazon Kinesis data stream or Amazon Data Firehose delivery stream in your AWS account.
Before AWS End User Messaging SMS can begin streaming the event data, you must delegate the required
permissions to AWS End User Messaging SMS.

If you use the console to set up event streaming, AWS End User Messaging SMS automatically creates an
AWS Identity and Access Management (IAM) role with the required permissions.

If you want to create the role manually, attach the following policies to the role:

- A permissions policy that allows AWS End User Messaging SMS to send event data to your
  stream.
- A trust policy that allows AWS End User Messaging SMS to assume the role.

After you create the role, you can configure AWS End User Messaging SMS to automatically send events to
your stream. For more information, see [Set up an Amazon Data Firehose event destination in AWS End User Messaging SMS](configuration-sets-kinesis.md "configuration-sets-kinesis.md") in this guide.
