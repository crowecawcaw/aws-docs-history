# Use service-linked roles for transit gateways in AWS Transit Gateway

Amazon VPC uses service-linked roles for the permissions that it requires to call other AWS
services on your behalf. For more information, see [Service-linked
roles](../../../IAM/latest/UserGuide/id_roles_create-service-linked-role.md "../../../IAM/latest/UserGuide/id_roles_create-service-linked-role.md") in the _IAM User Guide_.

## Transit gateway service-linked role

Amazon VPC uses service-linked roles for the permissions that it requires to call other AWS
services on your behalf when you work with a transit gateway.

### Permissions granted by the service-linked

role

Amazon VPC uses the service-linked role named **AWSServiceRoleForVPCTransitGateway**
to call the following actions on your behalf when you work with a transit gateway:

- `ec2:CreateNetworkInterface`
- `ec2:DescribeNetworkInterfaces`
- `ec2:ModifyNetworkInterfaceAttribute`
- `ec2:DeleteNetworkInterface`
- `ec2:CreateNetworkInterfacePermission`
- `ec2:AssignIpv6Addresses`
- `ec2:UnAssignIpv6Addresses`

The **AWSServiceRoleForVPCTransitGateway** role trusts the
following services to assume the role:

- `transitgateway.amazonaws.com`

**AWSServiceRoleForVPCTransitGateway** uses the managed policy
[AWSVPCTransitGatewayServiceRolePolicy](security-iam-awsmanpol.md#AWSVPCTransitGatewayServiceRolePolicy "security-iam-awsmanpol.md#AWSVPCTransitGatewayServiceRolePolicy").

You must configure permissions to allow an IAM entity (such as a user, group, or role)
to create, edit, or delete a service-linked role. For more information, see [Service-linked role permissions](../../../IAM/latest/UserGuide/id_roles_create-service-linked-role.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/id_roles_create-service-linked-role.md#service-linked-role-permissions") in the _IAM User Guide_.

### Create the service-linked role

You don't need to manually create the **AWSServiceRoleForVPCTransitGateway** role.
Amazon VPC creates this role for you when you attach a VPC in your account to a transit gateway.

### Edit the service-linked role

You can edit the description of
**AWSServiceRoleForVPCTransitGateway** using IAM. For more
information, see [Edit a service-linked role description](../../../IAM/latest/UserGuide/id_roles_update-service-linked-role.md#edit-service-linked-role-iam-console "../../../IAM/latest/UserGuide/id_roles_update-service-linked-role.md#edit-service-linked-role-iam-console") in the
_IAM User Guide_.

### Delete the service-linked role

If you no longer need to use transit gateways, we recommend that you delete
**AWSServiceRoleForVPCTransitGateway**.

You can delete this service-linked role only after you delete all transit gateway VPC attachments in
your AWS account. This ensures that you can't inadvertently remove permission to access your
VPC attachments.

You can use the IAM console, the IAM CLI, or the IAM API to delete
service-linked roles. For more information, see [Delete a service-linked role](../../../IAM/latest/UserGuide/id_roles_manage_delete.md#id_roles_manage_delete_slr "../../../IAM/latest/UserGuide/id_roles_manage_delete.md#id_roles_manage_delete_slr") in the
_IAM User Guide_.

After you delete **AWSServiceRoleForVPCTransitGateway**, Amazon VPC creates
the role again if you attach a VPC in your account to a transit gateway.
