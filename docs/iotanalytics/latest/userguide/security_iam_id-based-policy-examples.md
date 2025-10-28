End of support notice:
On December 15, 2025, AWS will end support for AWS IoT Analytics. After December 15, 2025, you will no longer
be able to access the AWS IoT Analytics console, or AWS IoT Analytics resources.
For more information, see
[AWS IoT Analytics end of support](iotanalytics-end-of-support.md "iotanalytics-end-of-support.md").

# AWS IoT Analytics identity-based policy examples

By default, users and roles don't have permission to create or modify AWS IoT Analytics
resources. They also can't perform tasks using the AWS Management Console, AWS CLI, or AWS API. An IAM
administrator must create IAM policies that grant users and roles permission to perform
specific API operations on the specified resources they need. The administrator must then attach
those policies to the users or groups that require those permissions.

To learn how to create an IAM identity-based policy using these example JSON policy
documents, see [Creating
policies on the JSON tab](../../../IAM/latest/UserGuide/access_policies_create.md#access_policies_create-json-editor "../../../IAM/latest/UserGuide/access_policies_create.md#access_policies_create-json-editor") in the _IAM User Guide_

###### Topics on this page:

- [Policy best practices](#iam-policy-best-practices "#iam-policy-best-practices")
- [Using the AWS IoT Analytics console](#iam-id-based-policy-examples-console "#iam-id-based-policy-examples-console")
- [Allow users to view their own permissions](#iam-view-permissions "#iam-view-permissions")
- [Accessing one AWS IoT Analytics input](#iam-access-one-input "#iam-access-one-input")
- [Viewing AWS IoT Analytics channels based on tags](#iam-view-input-tags "#iam-view-input-tags")

## Policy best practices

Identity-based policies are very powerful. They determine whether someone can create,
access, or delete AWS IoT Analytics resources in your account. These actions can incur costs for your AWS
account. When you create or edit identity-based policies, follow these guidelines and
recommendations:

- **Get started using AWS managed policies** - To start
  using AWS IoT Analytics quickly, use AWS managed policies to give your employees the permissions they
  need. These policies are already available in your account and are maintained and update by
  AWS. For more information, see [Get started using
  permissions with AWS managed policies](../../../IAM/latest/UserGuide/best-practices.md#bp-use-aws-defined-policies "../../../IAM/latest/UserGuide/best-practices.md#bp-use-aws-defined-policies") in the
  _IAM User Guide_.
- **Grant least privilege** - When you create custom
  policies, grant only the permissions required to perform a task. Start with a minimum set of
  permissions and grant additional permissions as necessary. Doing so is more secure than
  starting with permissions that are too lenient and then trying to tighten them later. For
  more information, see [Grant least privilege](../../../IAM/latest/UserGuide/best-practices.md#grant-least-privilege "../../../IAM/latest/UserGuide/best-practices.md#grant-least-privilege") in the _IAM User Guide_.
- **Enable MFA for sensitive operations** - For extra
  security, require users to use multi-factor authentication (MFA) to access sensitive
  resources or API operations. For more information, see [Using multi-factor authentication (MFA) in
  AWS](../../../IAM/latest/UserGuide/id_credentials_mfa.md "../../../IAM/latest/UserGuide/id_credentials_mfa.md") in the _IAM User Guide_.
- **Use policy conditions for extra security** - To the
  extent that it's practical, define the conditions under which your identity-based policies
  allow access to a resource. For example, you can write condition to specify a range of
  allowable IP addresses that a request must come from. You can also write conditions to allow
  requests only within a specified date or time range, or to require the use of SSL or MFA. For
  more information, see [IAM JSON policy elements: Condition](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md") in the
  _IAM User Guide_.

## Using the AWS IoT Analytics console

To access the AWS IoT Analytics console, you must have a minimum set of permissions. These permissions
must allow you to list and view details about the AWS IoT Analytics resources in your AWS account. If you
create an identity-based policy that is more restrictive than the minimum required permissions.
the console won't function as intended for entities (users or roles) with that
policy.

To ensure that those entities can still use the AWS IoT Analytics console, also attach the following
AWS managed policy to the entities. For more information, see [Adding permissions to a user](../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console "../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console") in the _IAM User Guide_.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "iotanalytics:BatchPutMessage",
 "iotanalytics:CancelPipelineReprocessing",
 "iotanalytics:CreateChannel",
 "iotanalytics:CreateDataset",
 "iotanalytics:CreateDatasetContent",
 "iotanalytics:CreateDatastore",
 "iotanalytics:CreatePipeline",
 "iotanalytics:DeleteChannel",
 "iotanalytics:DeleteDataset",
 "iotanalytics:DeleteDatasetContent",
 "iotanalytics:DeleteDatastore",
 "iotanalytics:DeletePipeline",
 "iotanalytics:DescribeChannel",
 "iotanalytics:DescribeDataset",
 "iotanalytics:DescribeDatastore",
 "iotanalytics:DescribeLoggingOptions",
 "iotanalytics:DescribePipeline",
 "iotanalytics:GetDatasetContent",
 "iotanalytics:ListChannels",
 "iotanalytics:ListDatasetContents",
 "iotanalytics:ListDatasets",
 "iotanalytics:ListDatastores",
 "iotanalytics:ListPipelines",
 "iotanalytics:ListTagsForResource",
 "iotanalytics:PutLoggingOptions",
 "iotanalytics:RunPipelineActivity",
 "iotanalytics:SampleChannelData",
 "iotanalytics:StartPipelineReprocessing",
 "iotanalytics:TagResource",
 "iotanalytics:UntagResource",
 "iotanalytics:UpdateChannel",
 "iotanalytics:UpdateDataset",
 "iotanalytics:UpdateDatastore",
 "iotanalytics:UpdatePipeline"
 ],
 "Resource": "arn:aws:iotanalytics:`us-east-1`:`123456789012`:channel/`your-channel-name`",
 "Resource": "arn:aws:iotanalytics:`us-east-1`:`123456789012`:dataset/`your-datasetName`",
 "Resource": "arn:aws:iotanalytics:`us-east-1`:`123456789012`:datastore/`your-datastoreName`",
 "Resource": "arn:aws:iotanalytics:`us-east-1`:`123456789012`:pipeline/`your-pipelineName`"
 }
 ]
 }`

```

You don't need to allow minimum console permissions for users that are making calls only
to the AWS CLI or the AWS API. Instead, allow access to only the actions that match the API
operation that you're trying to perform.

## Allow users to view their own permissions

This example shows how you might create a policy that allows users to view the
inline and managed policies that are attached to their user identity. This policy includes
permissions to complete this action on the console or programmatically using the AWS CLI or AWS
API.

JSON

```
`{
 "Version":"2012-10-17",
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
 "Resource": [
 "arn:aws:iam:*:*:user/`username`"
 ]
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
}`

```

## Accessing one AWS IoT Analytics input

In this example, you want to grant a user in your AWS account access to one of
your AWS IoT Analytics channels, `exampleChannel`. You also want to allow the use to add,
update, and delete channels.

The policy grants the `iotanalytics:ListChannels, iotanalytics:DescribeChannel,
 iotanalytics:CreateChannel, iotanalytics:DeleteChannel, and iotanalytics:UpdateChannel`
permissions to the user. For an example walkthrough for the Amazon S3 service that grants
permissions to users and tests them using the console, see [An example walkthrough: Using user policies to control
access to your bucket](../../../AmazonS3/latest/userguide/walkthrough1.md "../../../AmazonS3/latest/userguide/walkthrough1.md").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Sid":"ListChannelsInConsole",
 "Effect":"Allow",
 "Action":[
 "iotanalytics:ListChannels"
 ],
 "Resource":"arn:aws:iotanalytics:*:*:*"
 },
 {
 "Sid":"ViewSpecificChannelInfo",
 "Effect":"Allow",
 "Action":[
 "iotanalytics:DescribeChannel"
 ],
 "Resource":"arn:aws:iotanalytics:*:*:exampleChannel"
 },
 {
 "Sid":"ManageChannels",
 "Effect":"Allow",
 "Action":[
 "iotanalytics:CreateChannel",
 "iotanalytics:DeleteChannel",
 "iotanalytics:DescribeChannel",
 "iotanalytics:ListChannels",
 "iotanalytics:UpdateChannel"
 ],
 "Resource":"arn:aws:iotanalytics:*:*:exampleChannel/*"
 }
 ]
}`

```

## Viewing AWS IoT Analytics channels based on tags

You can use conditions in your identity-based policy to control access to AWS IoT Analytics resources
based on tags. This example shows how you might create a policy that allows viewing a
`channel`. However, permissions is granted only if the `channel` tag
`Owner` has the value of that user's user name. This policy also grants the
permissions needed to complete this action on the console.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ListChannelsInConsole",
 "Effect": "Allow",
 "Action": "iotanalytics:ListChannels",
 "Resource": "*"
 },
 {
 "Sid": "ViewChannelsIfOwner",
 "Effect": "Allow",
 "Action": "iotanalytics:ListChannels",
 "Resource": "arn:aws:iotanalytics:*:*:channel/*",
 "Condition": {
 "StringEquals": {"iotanalytics:ResourceTag/Owner": "${aws:username}"}
 }
 }
 ]
}`

```

You can attach this policy to the users in your account. If a user named
`richard-roe` attempts to view an AWS IoT Analytics `channel`, the
`channel` must be tagged `Owner=richard-roe or owner=richard-roe`.
Otherwise, he is denied access. The condition tag key `Owner` matches both
`Owner` and `owner` because condition key names are not case sensitive.
For more information, see [IAM JSON policy elements: Condition](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md") in the
_IAM User Guide_.
