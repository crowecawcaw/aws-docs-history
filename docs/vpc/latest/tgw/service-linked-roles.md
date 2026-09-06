

# Use service-linked roles for transit gateways in AWS Transit Gateway
<a name="service-linked-roles"></a>

Amazon VPC uses service-linked roles for the permissions that it requires to call other AWS services on your behalf. For more information, see [Service-linked roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create-service-linked-role.html) in the *IAM User Guide*.

## Transit gateway service-linked role
<a name="tgw-service-linked-roles"></a>

Amazon VPC uses service-linked roles for the permissions that it requires to call other AWS services on your behalf when you work with a transit gateway.

### Permissions granted by the service-linked role
<a name="service-linked-role-permissions"></a>

Amazon VPC uses the service-linked role named **AWSServiceRoleForVPCTransitGateway** to call the following actions on your behalf when you work with a transit gateway:
+ `ec2:CreateNetworkInterface`
+ `ec2:DescribeNetworkInterfaces`
+ `ec2:ModifyNetworkInterfaceAttribute`
+ `ec2:DeleteNetworkInterface`
+ `ec2:CreateNetworkInterfacePermission`
+ `ec2:AssignIpv6Addresses`
+ `ec2:UnAssignIpv6Addresses`

The **AWSServiceRoleForVPCTransitGateway** role trusts the following services to assume the role:
+ `transitgateway.amazonaws.com`

**AWSServiceRoleForVPCTransitGateway** uses the managed policy [AWSVPCTransitGatewayServiceRolePolicy](security-iam-awsmanpol.md#AWSVPCTransitGatewayServiceRolePolicy).

You must configure permissions to allow an IAM entity (such as a user, group, or role) to create, edit, or delete a service-linked role. For more information, see [Service-linked role permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create-service-linked-role.html#service-linked-role-permissions) in the *IAM User Guide*.

### Create the service-linked role
<a name="create-service-linked-role"></a>

You don't need to manually create the **AWSServiceRoleForVPCTransitGateway** role. Amazon VPC creates this role for you when you attach a VPC in your account to a transit gateway.

### Edit the service-linked role
<a name="edit-service-linked-role"></a>

You can edit the description of **AWSServiceRoleForVPCTransitGateway** using IAM. For more information, see [Edit a service-linked role description](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_update-service-linked-role.html#edit-service-linked-role-iam-console) in the *IAM User Guide*.

### Delete the service-linked role
<a name="delete-service-linked-role"></a>

If you no longer need to use transit gateways, we recommend that you delete **AWSServiceRoleForVPCTransitGateway**.

You can delete this service-linked role only after you delete all transit gateway VPC attachments in your AWS account. This ensures that you can't inadvertently remove permission to access your VPC attachments.

You can use the IAM console, the IAM CLI, or the IAM API to delete service-linked roles. For more information, see [Delete a service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_manage_delete.html#id_roles_manage_delete_slr) in the *IAM User Guide*.

After you delete **AWSServiceRoleForVPCTransitGateway**, Amazon VPC creates the role again if you attach a VPC in your account to a transit gateway.