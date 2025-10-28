# AWS Cloud WAN service-linked roles

AWS Cloud WAN uses the following service-linked roles for the permissions that it requires to
call other AWS services on your behalf:

- [AWSServiceRoleForNetworkManagerCloudWAN](#security-iam-awsmanpol-AWSServiceRoleForNetworkManagerCloudWAN "#security-iam-awsmanpol-AWSServiceRoleForNetworkManagerCloudWAN")
- [AWSServiceRoleForVPCTransitGateway](#security-iam-awsmanpol-AWSServiceRoleForVPCTransitGateway "#security-iam-awsmanpol-AWSServiceRoleForVPCTransitGateway")
- [AWSServiceRoleForNetworkManager](#security-iam-awsmanpol-AWSServiceRoleForNetworkManager "#security-iam-awsmanpol-AWSServiceRoleForNetworkManager")

## AWSServiceRoleForNetworkManagerCloudWAN

AWS Cloud WAN uses the service-linked role named
AWSServiceRoleForNetworkManagerCloudWAN to create and announce
transit gateway route tables, and then propagates transit gateway routes to those tables.

The AWSServiceRoleForNetworkManagerCloudWAN service-linked role
trusts the following service to assume the role:

- `networkmanager.amazonaws.com`

This service-linked role uses the managed policy AWSNetworkManagerCloudWANServiceRolePolicy.
To view the permissions for this policy, see [AWSNetworkManagerCloudWANServiceRolePolicy](../../../aws-managed-policy/latest/reference/AWSNetworkManagerCloudWANServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/AWSNetworkManagerCloudWANServiceRolePolicy.md")
in the _AWS Managed Policy Reference_.

## AWSServiceRoleForVPCTransitGateway

Amazon VPC uses the service-linked role named AWSServiceRoleForVPCTransitGateway
to create and manage resources for your transit gateway on your behalf.

The AWSServiceRoleForVPCTransitGateway service-linked role trusts the
following service to assume the role:

- `transitgateway.amazonaws.com`

This service-linked role uses the managed policy AWSVPCTransitGatewayServiceRolePolicy.
To view the permissions for this policy, see [AWSVPCTransitGatewayServiceRolePolicy](../../../aws-managed-policy/latest/reference/AWSVPCTransitGatewayServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/AWSVPCTransitGatewayServiceRolePolicy.md")
in the _AWS Managed Policy Reference_.

## AWSServiceRoleForNetworkManager

AWS Cloud WAN uses the service-linked role named AWSServiceRoleForNetworkManager to call actions on
your behalf when you work with global networks.

The AWSServiceRoleForNetworkManager service-linked role trusts
the following service to assume the role:

- `networkmanager.amazonaws.com`

This service-linked role uses the managed policy AWSNetworkManagerServiceRolePolicy.
To view the permissions for this policy, see [AWSNetworkManagerServiceRolePolicy](../../../aws-managed-policy/latest/reference/AWSNetworkManagerServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/AWSNetworkManagerServiceRolePolicy.md")
in the _AWS Managed Policy Reference_.

## Create the service-linked role

You don't need to manually create these service-linked roles.

- Network Manager creates the AWSServiceRoleForNetworkManager role when you create your first
  global network.
- Amazon VPC creates the AWSServiceRoleForVPCTransitGateway role when
  you attach a VPC to a transit gateway in your account.

For Network Manager to create a service-linked role on your behalf, you must have the
required permissions. For more information, see [Service-linked role permissions](../../../IAM/latest/UserGuide/id_roles_create-service-linked-role.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/id_roles_create-service-linked-role.md#service-linked-role-permissions") in the
_IAM User Guide_.

## Edit the service-linked role

You can edit the descriptions of the AWSServiceRoleForNetworkManager and
AWSServiceRoleForVPCTransitGateway roles using IAM. For more
information, see [Edit a service-linked role description](../../../IAM/latest/UserGuide/id_roles_update-service-linked-role.md#edit-service-linked-role-iam-console "../../../IAM/latest/UserGuide/id_roles_update-service-linked-role.md#edit-service-linked-role-iam-console") in the _IAM User Guide_.

## Delete the service-linked role

If you no longer need to use Network Manager, we recommend that you delete the
AWSServiceRoleForNetworkManager and AWSServiceRoleForVPCTransitGateway
roles.

You can delete these service-linked roles only after you delete your global network.
For information about deleting your global network, see [Delete a
global network](../tgwnm/global-networks-deleting.md "../tgwnm/global-networks-deleting.md").

You can use the IAM console, the IAM CLI, or the IAM API to delete service-linked roles.
For more information, see [Delete a service-linked role](../../../IAM/latest/UserGuide/id_roles_manage_delete.md#id_roles_manage_delete_slr "../../../IAM/latest/UserGuide/id_roles_manage_delete.md#id_roles_manage_delete_slr") in the _IAM User Guide_.

After you delete AWSServiceRoleForNetworkManager, Network Manager will create the role
again when you create a new global network. After you delete
AWSServiceRoleForVPCTransitGateway, Amazon VPC will create the role again
when you attach a VPC to a transit gateway in your account.

## Supported Regions

Service-linked roles are supported in all the AWS Regions where the service
is available. For more information, see [Region availability](what-is-cloudwan.md#cloudwan-available-regions "what-is-cloudwan.md#cloudwan-available-regions").
