# Using service-linked roles for Amazon VPC Lattice

Amazon VPC Lattice uses a service-linked role for the permissions that it requires to call
other AWS services on your behalf. For more information, see [Service-linked
roles](../../../IAM/latest/UserGuide/id_roles_create-service-linked-role.md "../../../IAM/latest/UserGuide/id_roles_create-service-linked-role.md") in the _IAM User Guide_.

VPC Lattice uses the service-linked role named AWSServiceRoleForVpcLattice.

## Service-linked role permissions for VPC Lattice

The **AWSServiceRoleForVpcLattice** service-linked role trusts the following service
to assume the role:

- `vpc-lattice.amazonaws.com`

The role permissions policy named AWSVpcLatticeServiceRolePolicy allows
VPC Lattice to publish CloudWatch metrics in the `AWS/VpcLattice` namespace.
For more information, see [AWSVpcLatticeServiceRolePolicy](../../../aws-managed-policy/latest/reference/AWSVpcLatticeServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/AWSVpcLatticeServiceRolePolicy.md") in the _AWS Managed Policy Reference_.

You must configure permissions to allow an IAM entity (such as a user, group, or
role) to create, edit, or delete a service-linked role. For more information, see
[Example policy: Create a service-linked role](security_iam_id-based-policies.md#security_iam_id-based-policy-examples-service-linked-role "security_iam_id-based-policies.md#security_iam_id-based-policy-examples-service-linked-role").

## Create a service-linked role for VPC Lattice

You don't need to manually create a service-linked role. When you
create VPC Lattice resources in the AWS Management Console, the AWS CLI, or the AWS API, VPC Lattice
creates the service-linked role for you.

If you delete this service-linked role, and then need to create it again, you can use
the same process to recreate the role in your account. When you
create VPC Lattice resources, VPC Lattice creates the service-linked role for you again.

## Edit a service-linked role for VPC Lattice

You can edit the description of **AWSServiceRoleForVpcLattice** using IAM. For more
information, see [Edit a service-linked role description](../../../IAM/latest/UserGuide/id_roles_update-service-linked-role.md#edit-service-linked-role-iam-console "../../../IAM/latest/UserGuide/id_roles_update-service-linked-role.md#edit-service-linked-role-iam-console") in the
_IAM User Guide_.

## Delete a service-linked role for VPC Lattice

If you no longer need to use Amazon VPC Lattice, we recommend that you delete
**AWSServiceRoleForVpcLattice**.

You can delete this service-linked role only after you delete all VPC Lattice
resources in your AWS account.

Use the IAM console, the AWS CLI, or the AWS API to delete the
**AWSServiceRoleForVpcLattice** service-linked role. For more information, see
[Delete a service-linked role](../../../IAM/latest/UserGuide/id_roles_manage_delete.md#id_roles_manage_delete_slr "../../../IAM/latest/UserGuide/id_roles_manage_delete.md#id_roles_manage_delete_slr") in the _IAM User Guide_.

After you delete a service-linked role, VPC Lattice creates the role again when you
create VPC Lattice resources in your AWS account.

## Supported Regions for VPC Lattice service-linked roles

VPC Lattice supports using service-linked roles in all of the Regions where the
service is available.
