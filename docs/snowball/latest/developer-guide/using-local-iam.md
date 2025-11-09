Effective November 7, 2025, AWS Snowball Edge will only be available to existing customers. If you would like to use AWS Snowball Edge,
sign up prior to that date. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/ "https://aws.amazon.com/datasync/") for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/ "https://aws.amazon.com/data-transfer-terminal/") for
secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/ "https://aws.amazon.com/outposts/").

# Using IAM locally on a Snowball Edge

AWS Identity and Access Management (IAM) helps you securely control access to AWS resources that
run on your AWS Snowball Edge device. You use IAM to control who is authenticated (signed in) and
authorized (has permissions) to use resources.

IAM is supported locally on your device. You can use the local IAM service to
create new users and attach IAM policies to them. You can use these policies to allow the
access necessary to perform assigned tasks. For example, you can give a user the ability to
transfer data, but limit their ability to create new Amazon EC2-compatible instances.

Additionally, you can create local, session-based credentials using AWS Security Token Service (AWS STS) on
your device. For information about the IAM service, see [Getting
started](../../../IAM/latest/GettingStartedGuide.md "../../../IAM/latest/GettingStartedGuide.md") in the _IAM User Guide_.

Your device's root credentials can't be disabled, and you can't use policies within your
account to explicitly deny access to the AWS account root user. We recommend
that you secure your root user access keys and create IAM user credentials for everyday
interaction with your device.

###### Important

The documentation in this section applies to using IAM locally on a AWS Snowball Edge device.
For information about using IAM in the AWS Cloud, see
[Identity and Access Management in AWS Snowball Edge](snowball-edge-iam.md "snowball-edge-iam.md").

For AWS services to work properly on a Snowball Edge, you must allow
the ports for the services. For details, see [Port requirements for AWS services on a Snowball Edge](port-requirements.md "port-requirements.md").

###### Topics

- [Using the AWS CLI and API Operations on a
  Snowball Edge](#local-iam-specify-region "#local-iam-specify-region")
- [List of Supported IAM AWS CLI Commands on a
  Snowball Edge](#local-iam-cli-commands "#local-iam-cli-commands")
- [IAM policy examples on Snowball Edge](#policy-examples "#policy-examples")
- [TrustPolicy example on a Snowball Edge](#role-policy-example-trust "#role-policy-example-trust")

## Using the AWS CLI and API Operations on a

Snowball Edge

When using the AWS CLI or API operations to issue IAM, AWS STS, Amazon S3, and Amazon EC2 commands
on Snowball Edge, you must specify the `region` as "`snow`." You
can do this using `aws configure` or within the command itself, as in the
following examples.

```

aws configure --profile abc
AWS Access Key ID [None]: AKIAIOSFODNN7EXAMPLE
AWS Secret Access Key [None]: 1234567
Default region name [None]: snow
Default output format [None]: json

```

Or

```

aws iam list-users --endpoint http://192.0.2.0:6078 --region snow --profile snowballEdge

```

###### Note

The access key ID and access secret key that are used locally on AWS Snowball Edge
can't be interchanged with the keys in the AWS Cloud.

## List of Supported IAM AWS CLI Commands on a

Snowball Edge

Following is a description of the subset of AWS CLI commands and options for IAM that
are supported on Snowball Edge devices. If a command or option isn't listed following,
it's not supported. Unsupported parameters for commands are noted in the
description.

- [attach-role-policy](../../../cli/latest/reference/iam/attach-role-policy.md "../../../cli/latest/reference/iam/attach-role-policy.md") – Attaches the specified managed policy to
  the specified IAM role.
- [attach-user-policy](../../../cli/latest/reference/iam/attach-user-policy.md "../../../cli/latest/reference/iam/attach-user-policy.md") – Attaches the specified managed policy to
  the specified user.
- [create-access-key](../../../cli/latest/reference/iam/create-access-key.md "../../../cli/latest/reference/iam/create-access-key.md")
  – Creates a new local IAM secret access key and corresponding AWS
  access key ID for the specified user.
- [create-policy](../../../cli/latest/reference/iam/create-policy.md "../../../cli/latest/reference/iam/create-policy.md") –
  Creates a new IAM managed policy for your device.
- [create-role](../../../cli/latest/reference/iam/create-role.md "../../../cli/latest/reference/iam/create-role.md") –
  Creates a new local IAM role for your device. The following parameters are
  **not** supported:
  - `Tags`
  - `PermissionsBoundary`

- [create-user](../../../cli/latest/reference/iam/create-user.md "../../../cli/latest/reference/iam/create-user.md") –
  Creates a new local IAM user for your device. The following parameters are
  **not** supported:
  - `Tags`
  - `PermissionsBoundary`

- [delete-access-key](../../../cli/latest/reference/iam/delete-access-key.md "../../../cli/latest/reference/iam/delete-access-key.md")
  – Deletes a new local IAM secret access key and corresponding AWS access key ID for the specified user.
- [delete-policy](../../../cli/latest/reference/iam/delete-policy.md "../../../cli/latest/reference/iam/delete-policy.md") –
  Deletes the specified managed policy.
- [delete-role](../../../cli/latest/reference/iam/delete-role.md "../../../cli/latest/reference/iam/delete-role.md") –
  Deletes the specified role.
- [delete-user](../../../cli/latest/reference/iam/delete-user.md "../../../cli/latest/reference/iam/delete-user.md") –
  Deletes the specified user.
- [detach-role-policy](../../../cli/latest/reference/iam/detach-role-policy.md "../../../cli/latest/reference/iam/detach-role-policy.md") – Removes the specified managed policy
  from the specified role.
- [detach-user-policy](../../../cli/latest/reference/iam/detach-user-policy.md "../../../cli/latest/reference/iam/detach-user-policy.md") – Removes the specified managed policy
  from the specified user.
- [get-policy](../../../cli/latest/reference/iam/get-policy.md "../../../cli/latest/reference/iam/get-policy.md") –
  Retrieves information about the specified managed policy, including the policy's
  default version and the total number of local IAM users, groups, and roles to
  which the policy is attached.
- [get-policy-version](../../../cli/latest/reference/iam/get-policy-version.md "../../../cli/latest/reference/iam/get-policy-version.md") – Retrieves information about the
  specified version of the specified managed policy, including the policy
  document.
- [get-role](../../../cli/latest/reference/iam/get-role.md "../../../cli/latest/reference/iam/get-role.md") – Retrieves
  information about the specified role, including the role's path, GUID, ARN, and
  the role's trust policy that grants permission to assume the role.
- [get-user](../../../cli/latest/reference/iam/get-user.md "../../../cli/latest/reference/iam/get-user.md") – Retrieves
  information about the specified IAM user, including the user's creation date,
  path, unique ID, and ARN.
- [list-access-keys](../../../cli/latest/reference/iam/list-access-keys.md "../../../cli/latest/reference/iam/list-access-keys.md")
  – Returns information about the access key IDs associated with the
  specified IAM user.
- [list-attached-role-policies](../../../cli/latest/reference/iam/list-attached-role-policies.md "../../../cli/latest/reference/iam/list-attached-role-policies.md") – Lists all managed policies that
  are attached to the specified IAM role.
- [list-attached-user-policies](../../../cli/latest/reference/iam/list-attached-user-policies.md "../../../cli/latest/reference/iam/list-attached-user-policies.md") – Lists all managed policies that
  are attached to the specified IAM user.
- [list-entities-for-policy](../../../cli/latest/reference/iam/list-entities-for-policy.md "../../../cli/latest/reference/iam/list-entities-for-policy.md") – Lists all local IAM users,
  groups, and roles that the specified managed policy is attached to.
  - `--EntityFilter`: Only the `user` and
    `role` values are supported.

- [list-policies](../../../cli/latest/reference/iam/list-policies.md "../../../cli/latest/reference/iam/list-policies.md") –
  Lists all the managed policies that are available in your local AWS account.
  The following parameter is **not**
  supported:
  - `--PolicyUsageFilter`

- [list-roles](../../../cli/latest/reference/iam/list-roles.md "../../../cli/latest/reference/iam/list-roles.md") – Lists
  the local IAM roles that have the specified path prefix.
- [list-users](../../../cli/latest/reference/iam/list-users.md "../../../cli/latest/reference/iam/list-users.md") – Lists
  the IAM users that have the specified path prefix.
- [update-access-key](../../../cli/latest/reference/iam/update-access-key.md "../../../cli/latest/reference/iam/update-access-key.md")
  – Changes the status of the specified access key from Active to Inactive,
  or vice versa.
- [update-assume-role-policy](../../../cli/latest/reference/iam/update-assume-role-policy.md "../../../cli/latest/reference/iam/update-assume-role-policy.md") – Updates the policy that grants an
  IAM entity permission to assume a role.
- [update-role](../../../cli/latest/reference/iam/update-role.md "../../../cli/latest/reference/iam/update-role.md") –
  Updates the description or maximum session duration setting of a role.
- [update-user](../../../cli/latest/reference/iam/update-user.md "../../../cli/latest/reference/iam/update-user.md") –
  Updates the name and/or the path of the specified IAM user.

### Supported IAM API operations on Snowball Edge

Following are the IAM API operations that you can use with a Snowball Edge,
with links to their descriptions in the IAM API Reference.

- [AttachRolePolicy](../../../IAM/latest/APIReference/API_AttachRolePolicy.md "../../../IAM/latest/APIReference/API_AttachRolePolicy.md") – Attaches the specified managed policy
  to the specified IAM role.
- [AttachUserPolicy](../../../IAM/latest/APIReference/API_AttachUserPolicy.md "../../../IAM/latest/APIReference/API_AttachUserPolicy.md") – Attaches the specified managed policy
  to the specified user.
- [CreateAccessKey](../../../IAM/latest/APIReference/API_CreateAccessKey.md "../../../IAM/latest/APIReference/API_CreateAccessKey.md")
  – Creates a new local IAM secret access key and corresponding AWS
  access key ID for the specified user.
- [CreatePolicy](../../../IAM/latest/APIReference/API_CreatePolicy.md "../../../IAM/latest/APIReference/API_CreatePolicy.md")
  – Creates a new IAM managed policy for your device.
- [CreateRole](../../../IAM/latest/APIReference/API_CreateRole.md "../../../IAM/latest/APIReference/API_CreateRole.md") –
  Creates a new local IAM role for your device.
- [CreateUser](../../../IAM/latest/APIReference/API_CreateUser.md "../../../IAM/latest/APIReference/API_CreateUser.md") –
  Creates a new local IAM user for your device.

The following parameters are **not**
supported:

    + `Tags`
    + `PermissionsBoundary`

- [DeleteAccessKey](../../../IAM/latest/APIReference/API_DeleteAccessKey.md "../../../IAM/latest/APIReference/API_DeleteAccessKey.md")– Deletes the specified access key.
- [DeletePolicy](../../../IAM/latest/APIReference/API_DeletePolicy.md "../../../IAM/latest/APIReference/API_DeletePolicy.md")
  – Deletes the specified managed policy.
- [DeleteRole](../../../IAM/latest/APIReference/API_DeleteRole.md "../../../IAM/latest/APIReference/API_DeleteRole.md") –
  Deletes the specified role.
- [DeleteUser](../../../IAM/latest/APIReference/API_DeleteUser.md "../../../IAM/latest/APIReference/API_DeleteUser.md") –
  Deletes the specified user.
- [DetachRolePolicy](../../../IAM/latest/APIReference/API_DetachRolePolicy.md "../../../IAM/latest/APIReference/API_DetachRolePolicy.md") – Removes the specified managed policy
  from the specified role.
- [DetachUserPolicy](../../../IAM/latest/APIReference/API_DetachUserPolicy.md "../../../IAM/latest/APIReference/API_DetachUserPolicy.md") – Removes the specified managed policy
  from the specified user.
- [GetPolicy](../../../IAM/latest/APIReference/API_GetPolicy.md "../../../IAM/latest/APIReference/API_GetPolicy.md") –
  Retrieves information about the specified managed policy, including the
  policy's default version and the total number of local IAM users, groups,
  and roles to which the policy is attached.
- [GetPolicyVersion](../../../IAM/latest/APIReference/API_GetPolicyVersion.md "../../../IAM/latest/APIReference/API_GetPolicyVersion.md") – Retrieves information about the
  specified version of the specified managed policy, including the policy
  document.
- [GetRole](../../../IAM/latest/APIReference/API_GetRole.md "../../../IAM/latest/APIReference/API_GetRole.md") –
  Retrieves information about the specified role, including the role's path,
  GUID, ARN, and the role's trust policy that grants permission to assume the
  role.
- [GetUser](../../../IAM/latest/APIReference/API_GetUser.md "../../../IAM/latest/APIReference/API_GetUser.md") –
  Retrieves information about the specified IAM user, including the user's
  creation date, path, unique ID, and ARN.
- [ListAccessKeys](../../../IAM/latest/APIReference/API_ListAccessKeys.md "../../../IAM/latest/APIReference/API_ListAccessKeys.md")
  – Returns information about the access key IDs associated with the
  specified IAM user.
- [ListAttachedRolePolicies](../../../IAM/latest/APIReference/API_ListAttachedRolePolicies.md "../../../IAM/latest/APIReference/API_ListAttachedRolePolicies.md") – Lists all managed policies
  that are attached to the specified IAM role.
- [ListAttachedUserPolicies](../../../IAM/latest/APIReference/API_ListAttachedUserPolicies.md "../../../IAM/latest/APIReference/API_ListAttachedUserPolicies.md") – Lists all managed policies
  that are attached to the specified IAM user.
- [ListEntitiesForPolicy](../../../IAM/latest/APIReference/API_ListEntitiesForPolicy.md "../../../IAM/latest/APIReference/API_ListEntitiesForPolicy.md") – Retrieves information about the
  specified IAM user, including the user's creation date, path, unique ID, and
  ARN.
  - `--EntityFilter`: Only the `user` and
    `role` values are supported.

- [ListPolicies](../../../IAM/latest/APIReference/API_ListPolicies.md "../../../IAM/latest/APIReference/API_ListPolicies.md")
  – Lists all the managed policies that are available in your local
  AWS account. The following parameter is **not** supported:
  - `--PolicyUsageFilter`

- [ListRoles](../../../IAM/latest/APIReference/API_ListRoles.md "../../../IAM/latest/APIReference/API_ListRoles.md") –
  Lists the local IAM roles that have the specified path prefix.
- [ListUsers](../../../IAM/latest/APIReference/API_ListUsers.md "../../../IAM/latest/APIReference/API_ListUsers.md") –
  Lists the IAM users that have the specified path prefix.
- [UpdateAccessKey](../../../IAM/latest/APIReference/API_UpdateAccessKey.md "../../../IAM/latest/APIReference/API_UpdateAccessKey.md")
  – Changes the status of the specified access key from Active to
  Inactive, or vice versa.
- [UpdateAssumeRolePolicy](../../../IAM/latest/APIReference/API_UpdateAssumeRolePolicy.md "../../../IAM/latest/APIReference/API_UpdateAssumeRolePolicy.md") – Updates the policy that grants
  an IAM entity permission to assume a role.
- [UpdateRole](../../../IAM/latest/APIReference/API_UpdateRole.md "../../../IAM/latest/APIReference/API_UpdateRole.md") –
  Updates the description or maximum session duration setting of a
  role.
- [UpdateUser](../../../IAM/latest/APIReference/API_UpdateUser.md "../../../IAM/latest/APIReference/API_UpdateUser.md") –
  Updates the name and/or the path of the specified IAM user.

### Supported IAM policy version and grammar on Snowball Edge

Following is the local IAM support version 2012-10-17 of the IAM policy and a
subset of the policy grammar.

| Policy type                                 | Supported grammar                                                                                                                               |
| ------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| Identity-based policies (user/role policy)  | "`Effect`", "`Action`" and<br>"`Resource`" NoteLocal IAM doesn't support "`Condition`",<br>"`NotAction`", "`NotResource`" and<br>"`Principal`". |
| Resource-based policies (role trust policy) | "`Effect`", "`Action`" and<br>"`Principal`" NoteFor Principal, only AWS account ID or<br>principal ID is allowed.                               |

## IAM policy examples on Snowball Edge

###### Note

AWS Identity and Access Management (IAM) users need `"snowballdevice:*"` permissions to use
the [AWS OpsHub for Snow Family application](aws-opshub.md "aws-opshub.md") to
manage Snowball Edge.

The following are examples of policies that grant permissions to a Snowball Edge
device.

### Allowing the GetUser call for a

sample user on a Snowball Edge through the IAM API

Use the following policy to allow the GetUser call for a sample user through the
IAM API.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "VisualEditor0",
 "Effect": "Allow",
 "Action": "iam:GetUser",
 "Resource": "arn:aws:iam::`111122223333`:user/`example-user`"
 }
 ]
}`

```

### Allowing full access to the

Amazon S3 API on a Snowball Edge

Use the following policy to allow full access to the Amazon S3 API.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "VisualEditor0",
 "Effect": "Allow",
 "Action": "s3:*",
 "Resource": "*"

 }
 ]
}`

```

### Allowing read and write

access to an Amazon S3 bucket on a Snowball Edge

Use the following policy to allow read and write access to a specific
bucket.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ListObjectsInBucket",
 "Effect": "Allow",
 "Action": "s3:ListBucket",
 "Resource": "arn:aws:s3:::bucket-name"
 },
 {
 "Sid": "AllObjectActions",
 "Effect": "Allow",
 "Action": "s3:*Object",
 "Resource": "arn:aws:s3:::bucket-name/*"
 }
 ]
}`

```

### Allowing list, get, and put

access to an Amazon S3 bucket on a Snowball Edge

Use the following policy to allow List, Get, and Put Access to a specific S3
bucket.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "s3:PutObject",
 "s3:GetObject",
 "s3:List*"
 ],
 "Resource": "arn:aws:s3:::amzn-s3-demo-bucket/*"
 }
 ]
}`

```

### Allowing full access to the Amazon EC2

API on a Snowball Edge

Use the following policy to allow full access to Amazon EC2.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "ec2:*",
 "Resource": "*"
 }
 ]
}`

```

### Allowing access to

start and stop Amazon EC2-compatible instances on a Snowball Edge

Use the following policy to allow access to start and stop Amazon EC2
instances.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ec2:StartInstances",
 "ec2:StopInstances"
 ],
 "Resource": "*"
 }
 ]
}`

```

### Denying calls to

DescribeLaunchTemplates but allowing all calls to DescribeImages on a Snowball Edge

Use the following policy to deny calls to `DescribeLaunchTemplates`
but allow all calls to `DescribeImages`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Deny",
 "Action": [
 "ec2:DescribeLaunchTemplates"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "ec2:DescribeImages"
 ],
 "Resource": "*"
 }
 ]
}`

```

### Policy for API calls on a Snowball Edge

Lists all the managed policies that are available on your Snow device, including
your own customer-defined managed policies. More details in [list-policies](../../../cli/latest/reference/iam/list-policies.md "../../../cli/latest/reference/iam/list-policies.md").

```
aws iam list-policies --endpoint http://`ip-address`:6078 --region snow --profile snowballEdge
{
    "Policies": [
        {
            "PolicyName": "Administrator",
            "Description": "Root user admin policy for Account 123456789012",
            "CreateDate": "2020-03-04T17:44:59.412Z",
            "AttachmentCount": 1,
            "IsAttachable": true,
            "PolicyId": "`policy-id`",
            "DefaultVersionId": "v1",
            "Path": "/",
            "Arn": "arn:aws:iam::123456789012:policy/Administrator",
            "UpdateDate": "2020-03-04T19:10:45.620Z"
        }
    ]
}
```

## TrustPolicy example on a Snowball Edge

A trust policy returns a set of temporary security credentials that you can use to
access AWS resources that you might normally not have access to. These
temporary credentials consist of an access key ID, a secret access key, and a security
token. Typically, you use `AssumeRole` in your account for cross-account
access.

The following is an example of a trust policy. For more information about trust
policy, see [AssumeRole](../../../STS/latest/APIReference/API_AssumeRole.md "../../../STS/latest/APIReference/API_AssumeRole.md") in the _AWS Security Token Service API Reference_.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "AWS": [
 "arn:aws:iam::`111122223333`:root"
 ]
 },
 "Action": [
 "sts:AssumeRole"
 ]
 }
 ]
}`

```
