

# Troubleshoot AWS Transit Gateway VPC attachment creation
<a name="transit-gateway-vpc-attach-troubleshooting"></a>

The following topic can help you troubleshoot problems that you might have when you create a VPC attachment.

**Problem**  
The VPC attachment failed. 

**Cause**  
The cause might be one of the following:

1. The user that is creating the VPC attachment does not have correct permissions to create service-linked role.

1. There is a throttling issue because of too many IAM requests, for example you are using CloudFormation to create permissions and roles.

1. The account has the service-linked role, and the service-linked role has been modified.

1. The transit gateway is not in the `available` state.

**Solution**  
Depending on the cause, try the following:

1. Verify that the user has the correct permissions to create service-linked roles. For more information, see [Service-linked role permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create-service-linked-role.html#service-linked-role-permissions) in the *IAM User Guide*. After the user has the permissions, create the VPC attachment.

1. Create the VPC attachment manually. For more information, see [Create a VPC attachment in AWS Transit Gateway](create-vpc-attachment.md).

1. Verify that the service-linked role has the correct permissions. For more information, see [Transit gateway service-linked role](service-linked-roles.md#tgw-service-linked-roles).

1. Verify that the transit gateway is in the `available` state. For more information, see [View transit gateway information in AWS Transit Gateway](view-tgws.md).