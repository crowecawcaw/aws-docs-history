**End of support notice:** On October
30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no
longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints,
segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of
support](../../../console/pinpoint/migration-guide.md "../../../console/pinpoint/migration-guide.md"). **Note:** APIs related to SMS, voice,
mobile push, OTP, and phone number validate are not impacted by this change and are
supported by AWS End User Messaging.

# Amazon Pinpoint identity-based

policy examples

By default, IAM users and roles don't have permission to create or modify
Amazon Pinpoint resources, and they also can't perform tasks using the AWS Management Console, AWS CLI, or
an AWS API. An IAM administrator must create IAM policies that grant users and roles
permission to perform specific API operations on the resources that they need. The
administrator must then attach those policies to the IAM users or groups that require
those permissions.

To learn how to create an IAM identity-based policy using these example JSON policy
documents, see [Creating IAM policies](../../../IAM/latest/UserGuide/access_policies_create.md#access_policies_create-json-editor "../../../IAM/latest/UserGuide/access_policies_create.md#access_policies_create-json-editor") in the _IAM User Guide_.

###### Topics

- [Policy best
  practices](#security_iam_service-with-iam-policy-best-practices "#security_iam_service-with-iam-policy-best-practices")
- [Using the
  Amazon Pinpoint console](#permissions-actions-examples-console-readonly "#permissions-actions-examples-console-readonly")
- [Example:
  Accessing a single Amazon Pinpoint project](#security_iam_id-based-policy-examples-access-one-project "#security_iam_id-based-policy-examples-access-one-project")
- [Example:
  Viewing Amazon Pinpoint resources based on tags](#security_iam_id-based-policy-examples-view-resource-tags "#security_iam_id-based-policy-examples-view-resource-tags")
- [Example:
  Allowing users to view their own permissions](#security_iam_id-based-policy-examples-view-own-permissions "#security_iam_id-based-policy-examples-view-own-permissions")
- [Examples: Providing access to
  Amazon Pinpoint API actions](#permissions-actions-examples-pin-api "#permissions-actions-examples-pin-api")
- [Examples: Providing
  access to Amazon Pinpoint SMS and voice API actions](#permissions-actions-examples-pin-sms-voice-api "#permissions-actions-examples-pin-sms-voice-api")
- [Example: Restricting Amazon Pinpoint project access to specific IP addresses](#security_iam_resource-based-policy-examples-restrict-project-access-by-ip "#security_iam_resource-based-policy-examples-restrict-project-access-by-ip")
- [Example:
  Restricting Amazon Pinpoint access based on tags](#security_iam_resource-based-policy-examples-restrict-access-by-tag "#security_iam_resource-based-policy-examples-restrict-access-by-tag")
- [Example: Allowing Amazon Pinpoint to send email using identities that were verified in
  Amazon SES](#security_iam_resource-based-policy-examples-access-ses-identities "#security_iam_resource-based-policy-examples-access-ses-identities")

## Policy best

practices

Identity-based policies determine whether someone can create, access, or delete Amazon Pinpoint resources in your
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

## Using the

Amazon Pinpoint console

To access the Amazon Pinpoint console, you must have a minimum set of
permissions. These permissions must allow you to list and view details about the
Amazon Pinpoint resources in your AWS account. If you create an identity-based policy
that applies permissions that are more restrictive than the minimum required
permissions, the console won't function as intended for entities (IAM users or roles)
with that policy. For those entities to use the Amazon Pinpoint console, you must
attach a policy to the entities. For more information, see [Adding permissions to a user](../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console "../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console") in the
_IAM User Guide_.

The following example policy provides read-only access to the Amazon Pinpoint console in a
specific AWS Region. It includes read-only access to other services that the Amazon Pinpoint
console depends on, such as Amazon Simple Email Service (Amazon SES), IAM, and Amazon Kinesis.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "UseConsole",
 "Effect": "Allow",
 "Action": [
 "mobiletargeting:Get*",
 "mobiletargeting:List*"
 ],
 "Resource": "arn:aws:mobiletargeting:`us-east-1`:`111122223333`:*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "firehose:ListDeliveryStreams",
 "iam:ListRoles",
 "kinesis:ListStreams",
 "s3:List*",
 "ses:Describe*",
 "ses:Get*",
 "ses:List*",
 "sns:ListTopics"
 ],
 "Resource": "*"
 }
 ]
}`

```

In the preceding policy example, replace `region` with the
name of an AWS Region, and replace `accountId` with your
AWS account ID.

You don't need to allow minimum console permissions for users that are making calls
only to the AWS CLI or the AWS API. Instead, only allow access to the actions that match
the API operation that they're trying to perform.

## Example:

Accessing a single Amazon Pinpoint project

You can also create read-only policies that only provide access to specific projects.
The following example policy lets users sign in to the console and view a list of
projects. It also lets users view information about related resources for other
AWS services that the Amazon Pinpoint console depends on, such as Amazon SES, IAM, and Amazon Kinesis.
However, the policy lets users only view additional information about the project that's
specified in the policy. You can modify this policy to allow access to additional
projects or AWS Regions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ViewProject",
 "Effect": "Allow",
 "Action": "mobiletargeting:GetApps",
 "Resource": "arn:aws:mobiletargeting:`us-east-1`:`111122223333`:*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "mobiletargeting:Get*",
 "mobiletargeting:List*"
 ],
 "Resource": [
 "arn:aws:mobiletargeting:`us-east-1`:`111122223333`:apps/`projectId`",
 "arn:aws:mobiletargeting:`us-east-1`:`111122223333`:apps/`projectId`/*",
 "arn:aws:mobiletargeting:`us-east-1`:`111122223333`:reports"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "ses:Get*",
 "kinesis:ListStreams",
 "firehose:ListDeliveryStreams",
 "iam:ListRoles",
 "ses:List*",
 "sns:ListTopics",
 "ses:Describe*",
 "s3:List*"
 ],
 "Resource": "*"
 }
 ]
}`

```

In the preceding example, replace `region` with the name of
an AWS Region, replace `accountId` with your AWS account
ID, and replace `projectId` with the ID of the Amazon Pinpoint project
that you want to provide access to.

Similarly, you can create policies that grant an IAM user in your AWS account with
limited write access to a specific Amazon Pinpoint project. In this case, you want to allow the
user to view, add, and update project components, such as segments and campaigns, but
not delete any components.

In addition to granting permissions for `mobiletargeting:Get` and
`mobiletargeting:List` actions, create a policy that grants permissions
for the following actions: `mobiletargeting:Create`;
`mobiletargeting:Update`; and `mobiletargeting:Put`. These are
the additional permissions required to create and manage most project components. For
example:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "LimitedWriteProject",
 "Effect": "Allow",
 "Action": "mobiletargeting:GetApps",
 "Resource": "arn:aws:mobiletargeting:`us-east-1`:`111122223333`:*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "mobiletargeting:Get*",
 "mobiletargeting:List*",
 "mobiletargeting:Create*",
 "mobiletargeting:Update*",
 "mobiletargeting:Put*"
 ],
 "Resource": [
 "arn:aws:mobiletargeting:`us-east-1`:`111122223333`:apps/`810c7aab86d42fb2b56c8c966example`",
 "arn:aws:mobiletargeting:`us-east-1`:`111122223333`:apps/`810c7aab86d42fb2b56c8c966example`/*",
 "arn:aws:mobiletargeting:`us-east-1`:`111122223333`:reports"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "ses:Get*",
 "kinesis:ListStreams",
 "firehose:ListDeliveryStreams",
 "iam:ListRoles",
 "ses:List*",
 "sns:ListTopics",
 "ses:Describe*",
 "s3:List*"
 ],
 "Resource": "*"
 }
 ]
}`

```

## Example:

Viewing Amazon Pinpoint resources based on tags

You can use conditions in an identity-based policy to control access to
Amazon Pinpoint resources based on tags. This example policy shows how you might create
this kind of policy to allow viewing Amazon Pinpoint resources. However, permission is granted
only if the `Owner` resource tag has the value of that user's user name. This
policy also grants the permissions necessary to complete this action on the
console.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ListResources",
 "Effect": "Allow",
 "Action": [
 "mobiletargeting:Get*",
 "mobiletargeting:List*"
 ],
 "Resource": "*"
 },
 {
 "Sid": "ViewResourceIfOwner",
 "Effect": "Allow",
 "Action": [
 "mobiletargeting:Get*",
 "mobiletargeting:List*"
 ],
 "Resource": "arn:aws:mobiletargeting:*:*:*",
 "Condition": {
 "StringEquals": {"aws:ResourceTag/Owner": "${aws:username}"}
 }
 }
 ]
}`

```

You can attach this type of policy to the IAM users in your account. If a user named
`richard-roe` attempts to view an Amazon Pinpoint resource, the resource
must be tagged `Owner=richard-roe` or `owner=richard-roe`.
Otherwise, he is denied access. The condition tag key `Owner` matches both
`Owner` and `owner` because condition key names are not
case-sensitive. For more information, see [IAM JSON policy
elements: Condition](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md") in the _IAM User Guide_.

## Example:

Allowing users to view their own permissions

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

## Examples: Providing access to

Amazon Pinpoint API actions

This section provides example policies that allow you to access features that are
available from the Amazon Pinpoint API, which is the primary API for Amazon Pinpoint. To learn more about
this API, see the [Amazon Pinpoint API Reference](../apireference.md "../apireference.md").

### Read-only access

The following example policy allows you read-only access to all the resources in
your Amazon Pinpoint account in a specific AWS Region.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ViewAllResources",
 "Effect": "Allow",
 "Action": [
 "mobiletargeting:Get*",
 "mobiletargeting:List*"
 ],
 "Resource": "arn:aws:mobiletargeting:`us-east-1`:`111122223333`:*"
 }
 ]
}`

```

In the preceding example, replace `region` with the name
of an AWS Region, and replace `accountId` with your
AWS account ID.

### Administrator access

The following example policy allows you full access to all Amazon Pinpoint actions and
resources in your Amazon Pinpoint account in all AWS Regions:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "FullAccess",
 "Effect": "Allow",
 "Action": [
 "mobiletargeting:*"
 ],
 "Resource": "arn:aws:mobiletargeting:*:`111122223333`:*"
 }
 ]
}`

```

In the preceding example, replace `accountId` with your
AWS account ID.

## Examples: Providing

access to Amazon Pinpoint SMS and voice API actions

This section provides example policies that allow you to access features that are
available from the Amazon Pinpoint SMS and Voice API. This is a supplemental API that provides
advanced options for using and managing the SMS and voice channels in Amazon Pinpoint. To learn
more about this API, see the [Amazon Pinpoint SMS and voice
API reference](../../../pinpoint-sms-voice/latest/APIReference.md "../../../pinpoint-sms-voice/latest/APIReference.md").

### Read-only

access

The following example policy allows you read-only access to all
Amazon Pinpoint SMS and Voice API actions and resources in your AWS account in all
AWS Regions:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ViewAllResources",
 "Effect": "Allow",
 "Action": [
 "sms-voice:Get*",
 "sms-voice:List*"
 ],

 "Resource": "*"
 }
 ]
}`

```

### Administrator

access

The following example policy allows you full access to all Amazon Pinpoint SMS and Voice API
actions and resources in your AWS account in all AWS Regions:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "FullAccess",
 "Effect": "Allow",
 "Action": [
 "sms-voice:*"
 ],

 "Resource": "*"
 }
 ]
}`

```

## Example: Restricting Amazon Pinpoint project access to specific IP addresses

The following example policy grants permissions to any user to perform any Amazon Pinpoint
action on a specified project (`projectId`). However, the
request must originate from the range of IP addresses that are specified in the
condition.

The condition in this statement identifies the `54.240.143.*` range of
allowed Internet Protocol version 4 (IPv4) addresses, with one exception:
`54.240.143.188`. The `Condition` block uses the
`IpAddress` and `NotIpAddress` conditions and the
`aws:SourceIp` condition key, which is an AWS-wide condition key. For
more information about these condition keys, see [Specifying conditions in a
policy](../../../AmazonS3/latest/userguide/amazon-s3-policy-keys.md "../../../AmazonS3/latest/userguide/amazon-s3-policy-keys.md")
_IAM User Guide_. The `aws:SourceIp` IPv4
values use standard CIDR notation. For more information, see [IP address condition operators](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md#Conditions_IPAddress "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md#Conditions_IPAddress") in the _IAM User Guide_.

JSON

```
`{
 "Version":"2012-10-17",
 "Id": "AMZPinpointPolicyId1",
 "Statement": [
 {
 "Sid": "IPAllow",
 "Effect": "Allow",
 "Principal": "*",
 "Action": "mobiletargeting:*",
 "Resource": [
 "arn:aws:mobiletargeting:*:*:apps/`projectId`",
 "arn:aws:mobiletargeting:*:*:apps/`projectId`/*"
 ],
 "Condition": {
 "IpAddress": {"aws:SourceIp": "54.240.143.0/24"},
 "NotIpAddress": {"aws:SourceIp": "54.240.143.188/32"}
 }
 }
 ]
}`

```

## Example:

Restricting Amazon Pinpoint access based on tags

The following example policy grants you permissions to perform any Amazon Pinpoint action on a
specified project (`projectId`). However, permissions are
granted only if the request originates from a user whose name is a value in the
`Owner` resource tag for the project, as specified in the
condition.

The `Condition` block uses the `StringEquals` condition and the
`aws:`ResourceTag/${TagKey}`` condition key. For more
information about conditions and condition keys, see [Bucket policy examples using condition
keys](../../../AmazonS3/latest/userguide/amazon-s3-policy-keys.md "../../../AmazonS3/latest/userguide/amazon-s3-policy-keys.md") in the _IAM User Guide_.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ModifyResourceIfOwner",
 "Effect": "Allow",
 "Action": "mobiletargeting:*",
 "Resource": [
 "arn:aws:mobiletargeting:*:*:apps/`projectId`",
 "arn:aws:mobiletargeting:*:*:apps/`projectId`/*"
 ],
 "Condition": {
 "StringEquals": {"aws:ResourceTag/Owner": "${aws:username}"}
 }
 }
 ]
}`

```

## Example: Allowing Amazon Pinpoint to send email using identities that were verified in

Amazon SES

When you verify an email identity (such as an email address or domain) through the
Amazon Pinpoint console, that identity is automatically configured so that it can be used by both
Amazon Pinpoint and Amazon SES. However, if you verify an email identity through Amazon SES, and you want to
use that identity with Amazon Pinpoint, you must apply a policy to that identity.

The following example policy grants Amazon Pinpoint permission to send email using an email
identity that was verified through Amazon SES.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "PinpointEmail",
 "Effect": "Allow",
 "Principal": {
 "Service": "pinpoint.amazonaws.com"
 },
 "Action": "ses:*",
 "Resource": "arn:aws:ses:`us-east-1`:`111122223333`:identity/`emailId`",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "`111122223333`"
 },
 "ArnLike": {
 "aws:SourceArn": "arn:aws:mobiletargeting:`us-east-1`:`111122223333`:apps/`*`"
 }
 }
 }
 ]
}`

```

If you use Amazon Pinpoint in the AWS GovCloud (US-West) Region, use the following policy example
instead:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "PinpointEmail",
 "Effect": "Allow",
 "Principal": {
 "Service": "pinpoint.amazonaws.com"
 },
 "Action": "ses:*",
 "Resource": "arn:aws-us-gov:ses:us-gov-west-1:`111122223333`:identity/`emailId`",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "`111122223333`"
 },
 "ArnLike": {
 "aws:SourceArn": "arn:aws-us-gov:mobiletargeting:us-gov-west-1:`111122223333`:apps/`*`"
 }
 }
 }
 ]
}`

```
