# Example IAM policies for Amazon EBS

By default, users and roles don't have permission to create or modify Amazon EBS
resources. They also can't perform tasks by using the AWS Management Console, AWS Command Line Interface (AWS CLI), or AWS API.
To grant users permission to perform actions on the resources that they need, an IAM
administrator can create IAM policies. The administrator can then add the IAM policies
to roles, and users can assume the roles.

To learn how to create an IAM identity-based policy by using these example JSON policy
documents, see [Creating IAM policies](../../../IAM/latest/UserGuide/access_policies_create-console.md "../../../IAM/latest/UserGuide/access_policies_create-console.md") in the _IAM User Guide_.

###### Topics

- [Policy best
  practices](#security_iam_service-with-iam-policy-best-practices "#security_iam_service-with-iam-policy-best-practices")
- [Allow users to use the Amazon EBS
  console](#security_iam_id-based-policy-examples-console "#security_iam_id-based-policy-examples-console")
- [Allow users
  to view their own permissions](#security_iam_id-based-policy-examples-view-own-permissions "#security_iam_id-based-policy-examples-view-own-permissions")
- [Allow users to work with volumes](#iam-example-manage-volumes "#iam-example-manage-volumes")
- [Allow users to work with snapshots](#iam-example-manage-snapshots "#iam-example-manage-snapshots")

## Policy best

practices

Identity-based policies determine whether someone can create, access, or delete Amazon EBS resources in your
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

## Allow users to use the Amazon EBS

console

To access the Amazon Elastic Block Store console, you must have a minimum set of permissions.
These permissions must allow you to list and view details about the Amazon EBS resources
in your AWS account. If you create an identity-based policy that is more restrictive
than the minimum required permissions, the console won't function as intended for
entities (users or roles) with that policy.

You don't need to allow minimum console permissions for users that are making calls
only to the AWS CLI or the AWS API. Instead, allow access to only the actions that match
the API operation that they're trying to perform.

To ensure that users and roles can still use the Amazon EBS console, also attach the
Amazon EBS `ConsoleAccess` or `ReadOnly` AWS managed policy to
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

## Allow users to work with volumes

###### Examples

- [Example: Attach and detach
  volumes](#iam-example-manage-volumes-attach-detach "#iam-example-manage-volumes-attach-detach")
- [Example: Create a volume](#iam-example-manage-volumes-create "#iam-example-manage-volumes-create")
- [Example: Create a volume with tags](#iam-example-manage-volumes-tags "#iam-example-manage-volumes-tags")
- [Example: Work with volumes using the Amazon EC2 console](#ex-volumes "#ex-volumes")

### Example: Attach and detach

volumes

When an API action requires a caller to specify multiple resources, you
must create a policy statement that allows users to access all required
resources. If you need to use a `Condition` element with one or
more of these resources, you must create multiple statements as shown in
this example.

The following policy allows users to attach volumes with the tag
"`volume_user`=_iam-user-name_" to instances with
the tag "`department=dev`", and to detach those volumes from those
instances. If you attach this policy to an IAM group, the
`aws:username` policy variable gives each user in the group
permission to attach or detach volumes from the instances with a tag named
`volume_user` that has their username as a value.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ec2:AttachVolume",
 "ec2:DetachVolume"
 ],
 "Resource": "arn:aws:ec2:us-east-1:`111122223333`:instance/*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/department": "dev"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "ec2:AttachVolume",
 "ec2:DetachVolume"
 ],
 "Resource": "arn:aws:ec2:us-east-1:`111122223333`:volume/*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/volume_user": "${aws:username}"
 }
 }
 }
 ]
}`

```

### Example: Create a volume

The following policy allows users to use the [CreateVolume](../../../AWSEC2/latest/APIReference/API_CreateVolume.md "../../../AWSEC2/latest/APIReference/API_CreateVolume.md") API
action. The user is allowed to create a volume only if the volume is
encrypted and only if the volume size is less than 20 GiB.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ec2:CreateVolume"
 ],
 "Resource": "arn:aws:ec2:us-east-1:`111122223333`:volume/*",
 "Condition": {
 "NumericLessThan": {
 "ec2:VolumeSize": "20"
 },
 "Bool": {
 "ec2:Encrypted": "true"
 }
 }
 }
 ]
}`

```

### Example: Create a volume with tags

The following policy includes the `aws:RequestTag` condition key that requires
users to tag any volumes they create with the tags `costcenter=115` and
`stack=prod`. If users don't pass these specific tags, or if they don't specify
tags at all, the request fails.

For resource-creating actions that apply tags, users must also have permissions to use
the `CreateTags` action. The second statement uses the
`ec2:CreateAction` condition key to allow users to create tags only
in the context of `CreateVolume`. Users cannot tag existing volumes or
any other resources.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowCreateTaggedVolumes",
 "Effect": "Allow",
 "Action": "ec2:CreateVolume",
 "Resource": "arn:aws:ec2:us-east-1:`111122223333`:volume/*",
 "Condition": {
 "StringEquals": {
 "aws:RequestTag/costcenter": "115",
 "aws:RequestTag/stack": "prod"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "ec2:CreateTags"
 ],
 "Resource": "arn:aws:ec2:us-east-1:`111122223333`:volume/*",
 "Condition": {
 "StringEquals": {
 "ec2:CreateAction": "CreateVolume"
 }
 }
 }
 ]
}`

```

The following policy allows users to create a volume without having to
specify tags. The `CreateTags` action is only evaluated if tags
are specified in the `CreateVolume` request. If users do specify
tags, the tag must be `purpose=test`. No other tags are allowed
in the request.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "ec2:CreateVolume",
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "ec2:CreateTags"
 ],
 "Resource": "arn:aws:ec2:us-east-1:`111122223333`:volume/*",
 "Condition": {
 "StringEquals": {
 "aws:RequestTag/purpose": "test",
 "ec2:CreateAction": "CreateVolume"
 },
 "ForAllValues:StringEquals": {
 "aws:TagKeys": "purpose"
 }
 }
 }
 ]
}`

```

### Example: Work with volumes using the Amazon EC2 console

The following policy grants users permission to view and create volumes, and
attach and detach volumes to specific instances using the Amazon EC2 console.

Users can attach any volume to instances that have the tag
"`purpose=test`", and also detach volumes from those instances.
To attach a volume using the Amazon EC2 console, it is helpful for users to have
permission to use the `ec2:DescribeInstances` action, as this allows
them to select an instance from a pre-populated list in the **Attach
Volume** dialog box. However, this also allows users to view all
instances on the **Instances** page in the console, so you can
omit this action.

In the first statement, the `ec2:DescribeAvailabilityZones` action is necessary
to ensure that a user can select an Availability Zone when creating a volume.

Users cannot tag the volumes that they create (either during or after volume
creation).

## Allow users to work with snapshots

The following are example policies for both `CreateSnapshot` (point-in-time
snapshot of an EBS volume) and `CreateSnapshots` (multi-volume snapshots).

###### Examples

- [Example: Create a snapshot](#iam-creating-snapshot "#iam-creating-snapshot")
- [Example: Create snapshots](#iam-creating-snapshots "#iam-creating-snapshots")
- [Example: Create a snapshot with
  tags](#iam-creating-snapshot-with-tags "#iam-creating-snapshot-with-tags")
- [Example: Create multi-volume snapshots with
  tags](#iam-creating-snapshots-with-tags "#iam-creating-snapshots-with-tags")
- [Example: Copying snapshots](#iam-copy-snapshot "#iam-copy-snapshot")
- [Example: Modify permission settings for
  snapshots](#iam-modifying-snapshot-with-tags "#iam-modifying-snapshot-with-tags")

### Example: Create a snapshot

The following policy allows customers to use the [CreateSnapshot](../../../AWSEC2/latest/APIReference/API_CreateSnapshot.md "../../../AWSEC2/latest/APIReference/API_CreateSnapshot.md") API action. The customer
can create snapshots only if the volume is encrypted and only if the volume size is less
than 20 GiB.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "ec2:CreateSnapshot",
 "Resource": "arn:aws:ec2:us-east-1::snapshot/*"
 },
 {
 "Effect": "Allow",
 "Action": "ec2:CreateSnapshot",
 "Resource": "arn:aws:ec2:us-east-1:`111122223333`:volume/*",
 "Condition": {
 "NumericLessThan": {
 "ec2:VolumeSize": "20"
 },
 "Bool": {
 "ec2:Encrypted": "true"
 }
 }
 }
 ]
}`

```

### Example: Create snapshots

The following policy allows customers to use the [CreateSnapshots](../../../AWSEC2/latest/APIReference/API_CreateSnapshots.md "../../../AWSEC2/latest/APIReference/API_CreateSnapshots.md") API action. The
customer can create snapshots only if all of the volumes on the instance are type
GP2.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect":"Allow",
 "Action":"ec2:CreateSnapshots",
 "Resource":[
"arn:aws:ec2:us-east-1::snapshot/*",
"arn:aws:ec2:*:*:instance/*"
 ]
 },
 {
 "Effect":"Allow",
 "Action":"ec2:CreateSnapshots",
 "Resource":"arn:aws:ec2:us-east-1:*:volume/*",
 "Condition":{
 "StringLikeIfExists":{
 "ec2:VolumeType":"gp2"
 }
 }

 }
 ]
}`

```

### Example: Create a snapshot with

tags

The following policy includes the `aws:RequestTag` condition key that requires the
customer to apply the tags `costcenter=115` and `stack=prod` to any new
snapshot. If users don't pass these specific tags, or if they don't specify tags at all, the
request fails.

For resource-creating actions that apply tags, customers must also have permissions to
use the `CreateTags` action. The third statement uses the
`ec2:CreateAction` condition key to allow customers to create tags only in the
context of `CreateSnapshot`. Customers cannot tag existing volumes or any other
resources.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "ec2:CreateSnapshot",
 "Resource": "arn:aws:ec2:us-east-1:`111122223333`:volume/*"
 },
 {
 "Sid": "AllowCreateTaggedSnapshots",
 "Effect": "Allow",
 "Action": "ec2:CreateSnapshot",
 "Resource": "arn:aws:ec2:us-east-1::snapshot/*",
 "Condition": {
 "StringEquals": {
 "aws:RequestTag/costcenter": "115",
 "aws:RequestTag/stack": "prod"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": "ec2:CreateTags",
 "Resource": "arn:aws:ec2:us-east-1::snapshot/*",
 "Condition": {
 "StringEquals": {
 "ec2:CreateAction": "CreateSnapshot"
 }
 }
 }
 ]
}`

```

### Example: Create multi-volume snapshots with

tags

The following policy includes the `aws:RequestTag` condition key that requires the
customer to apply the tags `costcenter=115` and `stack=prod` when creating
a multi-volume snapshot set. If users don't pass these specific tags, or if they don't specify
tags at all, the request fails.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect":"Allow",
 "Action":"ec2:CreateSnapshots",
 "Resource":[
"arn:aws:ec2:us-east-1::snapshot/*",
"arn:aws:ec2:*:*:instance/*",
"arn:aws:ec2:*:*:volume/*"

 ]
 },
 {
 "Sid":"AllowCreateTaggedSnapshots",
 "Effect":"Allow",
 "Action":"ec2:CreateSnapshots",
 "Resource":"arn:aws:ec2:us-east-1::snapshot/*",
 "Condition":{
 "StringEquals":{
 "aws:RequestTag/costcenter":"115",
 "aws:RequestTag/stack":"prod"
 }
 }
 },
 {
 "Effect":"Allow",
 "Action":"ec2:CreateTags",
 "Resource":"arn:aws:ec2:us-east-1::snapshot/*",
 "Condition":{
 "StringEquals":{
 "ec2:CreateAction":"CreateSnapshots"
 }
 }
 }
 ]
}`

```

The following policy allows customers to create a snapshot without having to specify
tags. The `CreateTags` action is evaluated only if tags are specified in the
`CreateSnapshot` or `CreateSnapshots` request. Tags can be omitted
in the request. If a tag is specified, the tag must be `purpose=test`. No
other tags are allowed in the request.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect":"Allow",
 "Action":"ec2:CreateSnapshot",
 "Resource":"*"
 },
 {
 "Effect":"Allow",
 "Action":"ec2:CreateTags",
 "Resource":"arn:aws:ec2:us-east-1::snapshot/*",
 "Condition":{
 "StringEquals":{
 "aws:RequestTag/purpose":"test",
 "ec2:CreateAction":"CreateSnapshot"
 },
 "ForAllValues:StringEquals":{
 "aws:TagKeys":"purpose"
 }
 }
 }
 ]
}`

```

The following policy allows customers to create multi-volume snapshot sets without having
to specify tags. The `CreateTags` action is evaluated only if tags are specified
in the `CreateSnapshot` or `CreateSnapshots` request. Tags can be
omitted in the request. If a tag is specified, the tag must be `purpose=test`. No
other tags are allowed in the request.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect":"Allow",
 "Action":"ec2:CreateSnapshots",
 "Resource":"*"
 },
 {
 "Effect":"Allow",
 "Action":"ec2:CreateTags",
 "Resource":"arn:aws:ec2:us-east-1::snapshot/*",
 "Condition":{
 "StringEquals":{
 "aws:RequestTag/purpose":"test",
 "ec2:CreateAction":"CreateSnapshots"
 },
 "ForAllValues:StringEquals":{
 "aws:TagKeys":"purpose"
 }
 }
 }
 ]
}`

```

The following policy allows snapshots to be created only if the source volume is tagged
with `User:*username*` for the customer, and the
snapshot itself is tagged with `Environment:Dev` and `User:*username*`. The customer can add additional tags to the
snapshot.

The following policy for `CreateSnapshots` allows snapshots to be created
only if the source volume is tagged with `User:*username*` for the customer, and the snapshot itself is tagged with
`Environment:Dev` and `User:*username*`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "ec2:CreateSnapshots",
 "Resource": "arn:aws:ec2:us-east-1:*:instance/*"
 },
 {
 "Effect": "Allow",
 "Action": "ec2:CreateSnapshots",
 "Resource": "arn:aws:ec2:us-east-1:`111122223333`:volume/*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/User": "${aws:username}"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": "ec2:CreateSnapshots",
 "Resource": "arn:aws:ec2:us-east-1::snapshot/*",
 "Condition": {
 "StringEquals": {
 "aws:RequestTag/Environment": "Dev",
 "aws:RequestTag/User": "${aws:username}"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": "ec2:CreateTags",
 "Resource": "arn:aws:ec2:us-east-1::snapshot/*"
 }
 ]
}`

```

The following policy allows deletion of a snapshot only if the snapshot is tagged with
User:_username_ for the customer.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect":"Allow",
 "Action":"ec2:DeleteSnapshot",
 "Resource":"arn:aws:ec2:us-east-1::snapshot/*",
 "Condition":{
 "StringEquals":{
 "aws:ResourceTag/User":"${aws:username}"
 }
 }
 }
 ]
}`

```

The following policy allows a customer to create a snapshot but denies the action if the
snapshot being created has a tag key `value=stack`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect":"Allow",
 "Action":[
 "ec2:CreateSnapshot",
 "ec2:CreateTags"
 ],
 "Resource":"*"
 },
 {
 "Effect":"Deny",
 "Action":"ec2:CreateSnapshot",
 "Resource":"arn:aws:ec2:us-east-1::snapshot/*",
 "Condition":{
 "ForAnyValue:StringEquals":{
 "aws:TagKeys":"stack"
 }
 }
 }
 ]
}`

```

The following policy allows a customer to create snapshots but denies the action if the
snapshots being created have a tag key `value=stack`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect":"Allow",
 "Action":[
 "ec2:CreateSnapshots",
 "ec2:CreateTags"
 ],
 "Resource":"*"
 },
 {
 "Effect":"Deny",
 "Action":"ec2:CreateSnapshots",
 "Resource":"arn:aws:ec2:us-east-1::snapshot/*",
 "Condition":{
 "ForAnyValue:StringEquals":{
 "aws:TagKeys":"stack"
 }
 }
 }
 ]
}`

```

The following policy allows you to combine multiple actions into a single policy. You
can only create a snapshot (in the context of
`CreateSnapshots`)
when the snapshot is created in Region `us-east-1`. You can only create snapshots
(in the context of `CreateSnapshots`) when the snapshots are being created in the
Region `us-east-1` and when the instance type is
`t2*`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect":"Allow",
 "Action":[
 "ec2:CreateSnapshots",
 "ec2:CreateSnapshot",
 "ec2:CreateTags"
 ],
 "Resource": [
 "arn:aws:ec2:*:*:instance/*",
 "arn:aws:ec2:*:*:snapshot/*",
 "arn:aws:ec2:*:*:volume/*"
 ],
 "Condition":{
 "StringEqualsIgnoreCase": {
 "ec2:Region": "us-east-1"
 },
 "StringLikeIfExists": {
 "ec2:InstanceType": ["t2.*"]
 }
 }
 }
 ]
}`

```

### Example: Copying snapshots

Resource-level permissions specified for the **CopySnapshot** action apply to both the new snapshot and the source snapshot.

The following example policy allows principals to copy snapshots only if the new snapshot is created with tag key of `purpose` and a tag value of `production`(`purpose=production`).

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowCopySnapshotWithTags",
 "Effect": "Allow",
 "Action": "ec2:CopySnapshot",
 "Resource": "arn:aws:ec2:*:`111122223333`:snapshot/*",
 "Condition": {
 "StringEquals": {
 "aws:RequestTag/purpose": "production"
 }
 }
 }
 ]
}`

```

The following example policy allows principals to copy snapshots only if the source snapshot is owned by AWS account `123456789012`.

The following example policy allows principals to copy snapshots only if the source snapshot
is created with tag key of `CSISnapshotName`.

```
{
    "Effect": "Allow",
    "Action": "ec2:CopySnapshot",
    "Resource": "arn:aws:ec2:*::snapshot/${*}",
    "Condition": {
        "StringLike": {
            "aws:RequestTag/CSISnapshotName": "*"
         }
     }
},

{
    "Effect": "Allow",
    "Action": "ec2:CopySnapshot",
    "Resource": "arn:aws:ec2:*::snapshot/snap-*"
}

```

### Example: Modify permission settings for

snapshots

The following policy allows modification of a snapshot only if the snapshot is tagged
with `User:`username``, where
 `username` is the customer's AWS account user name. The request
fails if this condition is not met.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect":"Allow",
 "Action":"ec2:ModifySnapshotAttribute",
 "Resource":"arn:aws:ec2:us-east-1::snapshot/*",
 "Condition":{
 "StringEquals":{
 "aws:ResourceTag/user-name":"${aws:`username`}"
 }
 }
 }
 ]
}`

```
