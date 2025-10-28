# Use service-linked roles for Verified Access

AWS Verified Access uses an IAM service-linked role, which is a type of IAM role that is
linked directly to an AWS service. The service-linked roles for Verified Access are defined by Verified Access
and include all the permissions that the service requires to call other AWS services on
your behalf.

A service-linked role makes setting up Verified Access easier because you don’t have to manually add
the necessary permissions. Verified Access defines the permissions of its service-linked roles, and unless
defined otherwise, only Verified Access can assume its roles. The defined permissions include the trust
policy and the permissions policy, and this permissions policy cannot be attached to any other
IAM entity.

## Service-linked role permissions for Verified Access

Verified Access uses the service-linked role named **AWSServiceRoleForVPCVerifiedAccess**
to provision resources in your account that are required to use the service.

The **AWSServiceRoleForVPCVerifiedAccess** service-linked role trusts the following services to
assume the role:

- `verified-access.amazonaws.com`

The role permissions policy, named **AWSVPCVerifiedAccessServiceRolePolicy**, allows Verified Access to
complete the following actions on the specified resources:

- Action `ec2:CreateNetworkInterface` on all subnets and security groups, as well as
  all network interfaces with the tag `VerifiedAccessManaged=true`
- Action `ec2:CreateTags` on all network interfaces at creation time
- Action `ec2:DeleteNetworkInterface` on all network interfaces with
  the tag `VerifiedAccessManaged=true`
- Action `ec2:ModifyNetworkInterfaceAttribute` on all security groups and
  all network interfaces with the tag `VerifiedAccessManaged=true`

You can also view the permissions for this policy in the _AWS Managed
Policy Reference Guide_; see [AWSVPCVerifiedAccessServiceRolePolicy](../../../aws-managed-policy/latest/reference/AWSVPCVerifiedAccessServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/AWSVPCVerifiedAccessServiceRolePolicy.md").

You must configure permissions to allow an IAM entity (such as a user, group, or role)
to create, edit, or delete a service-linked role. For more information, see [Service-linked role permissions](../../../IAM/latest/UserGuide/id_roles_create-service-linked-role.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/id_roles_create-service-linked-role.md#service-linked-role-permissions") in the _IAM User Guide_.

## Create a service-linked role for Verified Access

You don't need to manually create a service-linked role. When you call
**CreateVerifiedAccessEndpoint** in the AWS Management Console, the AWS CLI, or the AWS
API, Verified Access creates the service-linked role for you.

If you delete this service-linked role, and then need to create it again, you can use the
same process to recreate the role in your account. When you call
**CreateVerifiedAccessEndpoint** once again, Verified Access creates the service-linked
role for you again.

## Edit a service-linked role for Verified Access

Verified Access does not allow you to edit the **AWSServiceRoleForVPCVerifiedAccess** service-linked role.
After you create a service-linked role, you cannot change the name of the role because various
entities might reference the role. However, you can edit the description of the role using
IAM. For more information, see [Edit a service-linked role description](../../../IAM/latest/UserGuide/id_roles_update-service-linked-role.md#edit-service-linked-role-iam-console "../../../IAM/latest/UserGuide/id_roles_update-service-linked-role.md#edit-service-linked-role-iam-console") in the _IAM User Guide_.

## Delete a service-linked role for Verified Access

You don't need to manually delete the **AWSServiceRoleForVPCVerifiedAccess** role. When you call
**DeleteVerifiedAccessEndpoint** in the AWS Management Console, the AWS CLI, or the AWS
API, Verified Access cleans up the resources and deletes the service-linked role for you.

**To manually delete the service-linked role using
IAM**

Use the IAM console, the AWS CLI, or the AWS API to delete the **AWSServiceRoleForVPCVerifiedAccess**
service-linked role. For more information, see [Delete a service-linked role](../../../IAM/latest/UserGuide/id_roles_manage_delete.md#id_roles_manage_delete_slr "../../../IAM/latest/UserGuide/id_roles_manage_delete.md#id_roles_manage_delete_slr") in the _IAM User Guide_.

## Supported Regions for Verified Access service-linked roles

Verified Access supports using service-linked roles in all of the AWS Regions where the service is
available. For more information, see [AWS Regions and endpoints](../../../general/latest/gr/rande.md "../../../general/latest/gr/rande.md").
