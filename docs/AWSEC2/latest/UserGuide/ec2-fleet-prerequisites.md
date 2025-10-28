# EC2 Fleet prerequisites

###### To create an EC2 Fleet, the following prerequisites must be in

place:

- [Launch
  template](#ec2-fleet-prerequisites-launch-template "#ec2-fleet-prerequisites-launch-template")
- [Service-linked role for
  EC2 Fleet](#ec2-fleet-service-linked-role "#ec2-fleet-service-linked-role")
- [Grant access to
  customer managed keys for use with encrypted AMIs and EBS snapshots](#ec2-fleet-service-linked-roles-access-to-cmks "#ec2-fleet-service-linked-roles-access-to-cmks")
- [Permissions for EC2 Fleet users](#ec2-fleet-iam-users "#ec2-fleet-iam-users")

## Launch

template

A launch template specifies the configuration information about the instances
to launch, such as the instance type and Availability Zone. For more information
about launch templates, see [Store instance launch parameters in Amazon EC2 launch templates](ec2-launch-templates.md "ec2-launch-templates.md").

## Service-linked role for

EC2 Fleet

The `AWSServiceRoleForEC2Fleet` role grants the EC2 Fleet permission to
request, launch, terminate, and tag instances on your behalf. Amazon EC2 uses this
service-linked role to complete the following actions:

- `ec2:RunInstances` – Launch instances.
- `ec2:RequestSpotInstances` – Request Spot Instances.
- `ec2:TerminateInstances` – Terminate
  instances.
- `ec2:DescribeImages` – Describe Amazon Machine Images (AMIs) for the
  instances.
- `ec2:DescribeInstanceStatus` – Describe the status of the
  instances.
- `ec2:DescribeSubnets` – Describe the subnets for instances.
- `ec2:CreateTags` – Add tags to the EC2 Fleet, instances,
  and volumes.

Ensure that this role exists before you use the AWS CLI or an API to create an
EC2 Fleet.

###### Note

An `instant` EC2 Fleet does not require this role.

To create the role, use the IAM console as follows.

###### To create the AWSServiceRoleForEC2Fleet role for EC2 Fleet

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Roles**.
3. Choose **Create role**.
4. On the **Select trusted entity** page, do the following:
   1. For **Trusted entity type**, choose
      **AWS service**.
   2. Under **Use case**, for **Service or
      use case**, choose **EC2 -
      Fleet**.

   ###### Tip

   Be sure to choose **EC2 - Fleet**. If you
   choose **EC2**, the **EC2 -
   Fleet** use case does not appear in the
   **Use case** list. The **EC2 -
   Fleet** use case will automatically create a
   policy with the required IAM permissions and will suggest
   **AWSServiceRoleForEC2Fleet** as the
   role name. 3. Choose **Next**.

5. On the **Add permissions page**, choose
   **Next**.
6. On the **Name, review, and create** page, choose
   **Create role**.

If you no longer need to use EC2 Fleet, we recommend that you delete the
**AWSServiceRoleForEC2Fleet** role. After this role is
deleted from your account, you can create the role again if you create another
fleet.

For more information, see [Service-linked
roles](../../../IAM/latest/UserGuide/id_roles_create-service-linked-role.md "../../../IAM/latest/UserGuide/id_roles_create-service-linked-role.md") in the _IAM User Guide_.

## Grant access to

customer managed keys for use with encrypted AMIs and EBS snapshots

If you specify an [encrypted AMI](AMIEncryption.md "AMIEncryption.md") or an
encrypted Amazon EBS snapshot in your EC2 Fleet and you use an AWS KMS key for encryption,
you must grant the **AWSServiceRoleForEC2Fleet** role
permission to use the customer managed key so that Amazon EC2 can launch instances on your
behalf. To do this, you must add a grant to the customer managed key, as shown in the
following procedure.

When providing permissions, grants are an alternative to key policies. For
more information, see [Using grants](../../../kms/latest/developerguide/grants.md "../../../kms/latest/developerguide/grants.md")
and [Using key policies in
AWS KMS](../../../kms/latest/developerguide/key-policies.md "../../../kms/latest/developerguide/key-policies.md") in the _AWS Key Management Service Developer Guide_.

###### To grant the AWSServiceRoleForEC2Fleet role permissions to use the

customer managed key

- Use the [create-grant](../../../cli/latest/reference/kms/create-grant.md "../../../cli/latest/reference/kms/create-grant.md") command to add a grant to the customer managed key and
  to specify the principal (the
  **AWSServiceRoleForEC2Fleet** service-linked role)
  that is given permission to perform the operations that the grant
  permits. The customer managed key is specified by the `key-id`
  parameter and the ARN of the customer managed key. The principal is specified by
  the `grantee-principal` parameter and the ARN of the
  **AWSServiceRoleForEC2Fleet** service-linked
  role.

```
aws kms create-grant \
    --region `us-east-1` \
    --key-id arn:aws:kms:`us-east-1`:`444455556666`:key/`1234abcd-12ab-34cd-56ef-1234567890ab` \
    --grantee-principal arn:aws:iam::`111122223333`:role/AWSServiceRoleForEC2Fleet \
    --operations "Decrypt" "Encrypt" "GenerateDataKey" "GenerateDataKeyWithoutPlaintext" "CreateGrant" "DescribeKey" "ReEncryptFrom" "ReEncryptTo"
```

## Permissions for EC2 Fleet users

If your users will create or manage an EC2 Fleet, be sure to grant them the
required permissions.

###### To create a policy for EC2 Fleet

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Policies**.
3. Choose **Create policy**.
4. On the **Create policy** page, choose the
   **JSON** tab, replace the text with the following,
   and choose **Review policy**.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ec2:*"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "iam:ListRoles",
 "iam:PassRole",
 "iam:ListInstanceProfiles"
 ],
 "Resource":"arn:aws:iam::123456789012:role/DevTeam*"
 }
 ]
}`

```

The `ec2:*` grants a user permission to call all Amazon EC2 API
actions. To limit the user to specific Amazon EC2 API actions, specify those
actions instead.

The user must have permission to call the `iam:ListRoles`
action to enumerate existing IAM roles, the `iam:PassRole`
action to specify the EC2 Fleet role, and the
`iam:ListInstanceProfiles` action to enumerate existing
instance profiles.

(Optional) To enable a user to create roles or instance profiles using
the IAM console, you must also add the following actions to the
policy:

    * `iam:AddRoleToInstanceProfile`
    * `iam:AttachRolePolicy`
    * `iam:CreateInstanceProfile`
    * `iam:CreateRole`
    * `iam:GetRole`
    * `iam:ListPolicies`

5. On the **Review policy** page, enter a policy name
   and description, and choose **Create policy**.
6. To provide access, add permissions to your users, groups, or roles:
   - Users and groups in AWS IAM Identity Center:

   Create a permission set. Follow the instructions in [Create a permission set](../../../singlesignon/latest/userguide/howtocreatepermissionset.md "../../../singlesignon/latest/userguide/howtocreatepermissionset.md") in the _AWS IAM Identity Center User Guide_.
   - Users managed in IAM through an identity provider:

   Create a role for identity federation. Follow the instructions in [Create a role for a third-party identity provider (federation)](../../../IAM/latest/UserGuide/id_roles_create_for-idp.md "../../../IAM/latest/UserGuide/id_roles_create_for-idp.md")
   in the _IAM User Guide_.
   - IAM users:
     - Create a role that your user can assume. Follow the instructions in [Create a role for an IAM user](../../../IAM/latest/UserGuide/id_roles_create_for-user.md "../../../IAM/latest/UserGuide/id_roles_create_for-user.md") in the _IAM User Guide_.
     - (Not recommended) Attach a policy directly to a user or add a user to a user group. Follow the instructions in [Adding permissions to a user (console)](../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console "../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console") in the _IAM User Guide_.
