# Troubleshoot AWS Transit Gateway VPC attachment creation

The following topic can help you troubleshoot problems that you might have when you create
a VPC attachment.

###### Problem

The VPC attachment failed.

###### Cause

The cause might be one of the following:

1. The user that is creating the VPC attachment does not have correct permissions to
   create service-linked role.
2. There is a throttling issue because of too many IAM requests, for example you are using
   AWS CloudFormation to create permissions and roles.
3. The account has the service-linked role, and the service-linked role has been
   modified.
4. The transit gateway is not in the `available` state.

###### Solution

Depending on the cause, try the following:

1. Verify that the user has the correct permissions to create service-linked roles.
   For more information, see [Service-linked role permissions](../../../IAM/latest/UserGuide/id_roles_create-service-linked-role.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/id_roles_create-service-linked-role.md#service-linked-role-permissions") in the _IAM User Guide_.
   After the user has the permissions, create the VPC attachment.
2. Create the VPC attachment manually. For more information, see
   [Create a VPC attachment in AWS Transit Gateway](create-vpc-attachment.md "create-vpc-attachment.md").
3. Verify that the service-linked role has the correct permissions. For more information, see
   [Transit gateway service-linked role](service-linked-roles.md#tgw-service-linked-roles "service-linked-roles.md#tgw-service-linked-roles").
4. Verify that the transit gateway is in the `available` state. For more
   information, see [View transit gateway information in AWS Transit Gateway](view-tgws.md "view-tgws.md").
