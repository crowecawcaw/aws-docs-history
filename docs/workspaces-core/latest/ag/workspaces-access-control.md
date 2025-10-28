# Identity and access management for WorkSpaces Instances

By default, IAM users don't have permissions for WorkSpaces Instances resources and operations. To allow
IAM users to manage WorkSpaces resources Instances, you must create an IAM policy that explicitly grants
them permissions, and attach the policy to the IAM users or groups that require those
permissions.

To provide access, add permissions to your users, groups, or roles:

- Users and groups in AWS IAM Identity Center:

Create a permission set. Follow the instructions in [Create a permission set](../../../singlesignon/latest/userguide/howtocreatepermissionset.md "../../../singlesignon/latest/userguide/howtocreatepermissionset.md") in the _AWS IAM Identity Center User Guide_.

- Users managed in IAM through an identity provider:

Create a role for identity federation. Follow the instructions in [Create a role for a third-party identity provider (federation)](../../../IAM/latest/UserGuide/id_roles_create_for-idp.md "../../../IAM/latest/UserGuide/id_roles_create_for-idp.md")
in the _IAM User Guide_.

- IAM users:

      + Create a role that your user can assume. Follow the instructions in [Create a role for an IAM user](../../../IAM/latest/UserGuide/id_roles_create_for-user.md "../../../IAM/latest/UserGuide/id_roles_create_for-user.md") in the *IAM User Guide*.
      + (Not recommended) Attach a policy directly to a user or add a user to a user group. Follow the instructions in [Adding permissions to a user (console)](../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console "../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console") in the *IAM User Guide*.

  Following are additional resources for IAM:

- For more information about IAM policies, see [Policies and Permissions](../../../IAM/latest/UserGuide/access_policies.md "../../../IAM/latest/UserGuide/access_policies.md") in the
  _IAM User Guide_ guide.
- For more information about IAM, see [Identity and
  Access Management (IAM)](https://aws.amazon.com/iam "https://aws.amazon.com/iam") and the [_IAM User Guide_](../../../IAM/latest/UserGuide.md "../../../IAM/latest/UserGuide.md").
- For more information about WorkSpaces Instances specific resources, actions, and condition context keys
  for use in IAM permission policies, see [Actions, Resources, and Condition Keys for
  Amazon WorkSpaces Managed Instances](../../../IAM/latest/UserGuide/list_awsworkspacesmanagedinstances.md "../../../IAM/latest/UserGuide/list_awsworkspacesmanagedinstances.md") in the _IAM User Guide_.
- For a tool that helps you create IAM policies, see the [AWS Policy Generator](https://aws.amazon.com/blogs/aws/aws-policy-generator/ "https://aws.amazon.com/blogs/aws/aws-policy-generator/"). You can also use the
  [IAM Policy Simulator](../../../IAM/latest/UsingPolicySimulatorGuide.md "../../../IAM/latest/UsingPolicySimulatorGuide.md") to test whether a policy would allow or deny a
  specific request to AWS.

###### Contents

- [Amazon WorkSpaces Instances example policies](#workspaces-instances-example-iam-policies "#workspaces-instances-example-iam-policies")
- [Specify WorkSpaces resources in an IAM policy](#wsp_iam_resource "#wsp_iam_resource")

## Amazon WorkSpaces Instances example policies

The following example shows policy statements that you could use to grant access to perform WorkSpaces Instances tasks.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "workspaces-instances:*"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "ec2:CreateTags",
 "ec2:DescribeVolumes",
 "ec2:DescribeInstances",
 "ec2:DescribeInstanceStatus",
 "ec2:StopInstances",
 "ec2:StartInstances"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "ec2:RunInstances",
 "ec2:TerminateInstances",
 "ec2:DeleteVolume",
 "ec2:CreateVolume",
 "ec2:AttachVolume",
 "ec2:DetachVolume"
 ],
 "Resource": "*",
 "Condition": {
 "ForAnyValue:StringEquals": {
 "aws:CalledVia": "workspaces-instances.amazonaws.com"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "kms:Encrypt",
 "kms:Decrypt",
 "kms:GenerateDataKey*"
 ],
 "Resource": "*"
 }
 ]
}`

```

###### Note

In place of `*`, grant permissions to the specific KMS key that you are using.

If you are using the Amazon WorkSpaces Console, you will also need to add the following permissions:

```
iam:GetRole
iam:CreateServiceLinkedRole
```

###### Note

If you have already onboarded using Amazon WorkSpaces Console, `iam:CreateServiceLinkedRole` is optional.

Additional permissions may be required for specific partner requirements. For more information on partner permissions, refer to your partner specific guides.

## Specify WorkSpaces resources in an IAM policy

To specify an WorkSpaces Instances resource in the `Resource` element of the policy statement,
use the Amazon Resource Name (ARN) of the resource. You control access to your WorkSpaces Instances resources
by either allowing or denying permissions to use the API actions that are specified in the
`Action` element of your IAM policy statement. WorkSpaces Instances defines ARNs for WorkSpaces Instances,
bundles, IP groups, and directories.

### WorkSpaces Instances Instance ARN

A WorkSpaces Instances ARN has the syntax shown in the following example.

```
arn:aws:workspaces-instances:region:account_id:workspaceinstance/workspace_instance_identifier
```

_region_

The Region that the WorkSpaces Instance is in (for example,
`us-east-1`).

_account_id_

The ID of the AWS account, with no hyphens (for example,
`123456789012`).

_workspace_instance_identifier_

The ID of the WorkSpaces Instance (for example, `"Resource": "arn:aws:workspaces-instances:region:account_id:workspaceinstance/workspace_instance_identifier"`).

You can use the `*` wildcard to specify all WorkSpaces Instances that belong to a specific
account in a specific Region.
