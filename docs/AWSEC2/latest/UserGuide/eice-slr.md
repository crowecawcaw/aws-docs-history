# Service-linked role for EC2 Instance Connect Endpoint

Amazon EC2 uses AWS Identity and Access Management (IAM) [service-linked
roles](../../../IAM/latest/UserGuide/id_roles.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles.md#iam-term-service-linked-role"). A service-linked role is a unique type of IAM role that is linked
directly to Amazon EC2. Service-linked roles are predefined by Amazon EC2 and include all the
permissions that Amazon EC2 requires to call other AWS services on your behalf. For more
information, see [Service-linked
roles](../../../IAM/latest/UserGuide/id_roles_create-service-linked-role.md "../../../IAM/latest/UserGuide/id_roles_create-service-linked-role.md") in the _IAM User Guide_.

## Service-linked role permissions for

EC2 Instance Connect Endpoint

Amazon EC2 uses **AWSServiceRoleForEC2InstanceConnect** to
create and manage network interfaces in your account that are required by
EC2 Instance Connect Endpoint.

The **AWSServiceRoleForEC2InstanceConnect**
service-linked role trusts the following service to assume the role:

- `ec2-instance-connect.amazonaws.com`

The **AWSServiceRoleForEC2InstanceConnect**
service-linked role uses the following managed policy:

- **Ec2InstanceConnectEndpoint**

To view the permissions for the managed policy, see [Ec2InstanceConnectEndpoint](../../../aws-managed-policy/latest/reference/Ec2InstanceConnectEndpoint.md "../../../aws-managed-policy/latest/reference/Ec2InstanceConnectEndpoint.md") in the _AWS Managed Policy
Reference_.

## Create a service-linked role for EC2 Instance Connect Endpoint

You don't need to manually create this service-linked role. When you create an
EC2 Instance Connect Endpoint, Amazon EC2 creates the service-linked role for you.

## Edit a service-linked role for EC2 Instance Connect Endpoint

EC2 Instance Connect Endpoint doesn't allow you to edit the **AWSServiceRoleForEC2InstanceConnect** service-linked role.

## Delete a service-linked role for EC2 Instance Connect Endpoint

If you no longer need to use EC2 Instance Connect Endpoint, we recommend that you delete the
**AWSServiceRoleForEC2InstanceConnect**
service-linked role.

You must delete all EC2 Instance Connect Endpoint resources before you can delete the
service-linked role.

To delete the service-linked role, see [Delete a service-linked role](../../../IAM/latest/UserGuide/id_roles_manage_delete.md#id_roles_manage_delete-slr "../../../IAM/latest/UserGuide/id_roles_manage_delete.md#id_roles_manage_delete-slr") in the
_IAM User Guide_.

You must configure permissions to allow an IAM entity (a user, group, or role) to create,
edit, or delete a service-linked role. For more information, see [Service-linked role permissions](../../../IAM/latest/UserGuide/id_roles_create-service-linked-role.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/id_roles_create-service-linked-role.md#service-linked-role-permissions") in the
_IAM User Guide_.
