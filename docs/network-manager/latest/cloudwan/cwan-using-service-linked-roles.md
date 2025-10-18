# AWS Cloud WAN service-linked roles

AWS Cloud WAN uses the following service-linked roles for the permissions that it requires to
 call other AWS services on your behalf:


* [AWSServiceRoleForNetworkManagerCloudWAN](#security-iam-awsmanpol-AWSServiceRoleForNetworkManagerCloudWAN "#security-iam-awsmanpol-AWSServiceRoleForNetworkManagerCloudWAN")
* [AWSServiceRoleForVPCTransitGateway](#security-iam-awsmanpol-AWSServiceRoleForVPCTransitGateway "#security-iam-awsmanpol-AWSServiceRoleForVPCTransitGateway")
* [AWSServiceRoleForNetworkManager](#security-iam-awsmanpol-AWSServiceRoleForNetworkManager "#security-iam-awsmanpol-AWSServiceRoleForNetworkManager")

## AWSServiceRoleForNetworkManagerCloudWAN


AWS Cloud WAN uses the service-linked role named
 AWSServiceRoleForNetworkManagerCloudWAN to create and announce
 transit gateway route tables, and then propagates transit gateway routes to those tables. 


The AWSServiceRoleForNetworkManagerCloudWAN service-linked role 
 trusts the following service to assume the role: 



* `networkmanager.amazonaws.com`

This service-linked role uses the managed policy AWSNetworkManagerCloudWANServiceRolePolicy.
 To view the permissions for this policy, see [AWSNetworkManagerCloudWANServiceRolePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSNetworkManagerCloudWANServiceRolePolicy.html "https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSNetworkManagerCloudWANServiceRolePolicy.html") 
 in the *AWS Managed Policy Reference*.


## AWSServiceRoleForVPCTransitGateway


Amazon VPC uses the service-linked role named AWSServiceRoleForVPCTransitGateway 
 to create and manage resources for your transit gateway on your behalf.


The AWSServiceRoleForVPCTransitGateway service-linked role trusts the 
 following service to assume the role:



* `transitgateway.amazonaws.com`

This service-linked role uses the managed policy AWSVPCTransitGatewayServiceRolePolicy.
 To view the permissions for this policy, see [AWSVPCTransitGatewayServiceRolePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSVPCTransitGatewayServiceRolePolicy.html "https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSVPCTransitGatewayServiceRolePolicy.html") 
 in the *AWS Managed Policy Reference*.


## AWSServiceRoleForNetworkManager


AWS Cloud WAN uses the service-linked role named AWSServiceRoleForNetworkManager to call actions on
 your behalf when you work with global networks. 


The AWSServiceRoleForNetworkManager service-linked role trusts 
 the following service to assume the role:



* `networkmanager.amazonaws.com`

This service-linked role uses the managed policy AWSNetworkManagerServiceRolePolicy.
 To view the permissions for this policy, see [AWSNetworkManagerServiceRolePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSNetworkManagerServiceRolePolicy.html "https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSNetworkManagerServiceRolePolicy.html") 
 in the *AWS Managed Policy Reference*.


## Create the service-linked role


You don't need to manually create these service-linked roles.



* Network Manager creates the AWSServiceRoleForNetworkManager role when you create your first
 global network.
* Amazon VPC creates the AWSServiceRoleForVPCTransitGateway role when
 you attach a VPC to a transit gateway in your account.

For Network Manager to create a service-linked role on your behalf, you must have the
 required permissions. For more information, see [Service-linked role permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create-service-linked-role.html#service-linked-role-permissions "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create-service-linked-role.html#service-linked-role-permissions") in the
 *IAM User Guide*.


## Edit the service-linked role


You can edit the descriptions of the AWSServiceRoleForNetworkManager and
 AWSServiceRoleForVPCTransitGateway roles using IAM. For more
 information, see [Edit a service-linked role description](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_update-service-linked-role.html#edit-service-linked-role-iam-console "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_update-service-linked-role.html#edit-service-linked-role-iam-console") in the *IAM User Guide*.


## Delete the service-linked role


If you no longer need to use Network Manager, we recommend that you delete the
 AWSServiceRoleForNetworkManager and AWSServiceRoleForVPCTransitGateway 
 roles.


You can delete these service-linked roles only after you delete your global network.
 For information about deleting your global network, see [Delete a
 global network](https://docs.aws.amazon.com/network-manager/latest/tgwnm/global-networks-deleting.html "https://docs.aws.amazon.com/network-manager/latest/tgwnm/global-networks-deleting.html").


You can use the IAM console, the IAM CLI, or the IAM API to delete service-linked roles.
 For more information, see [Delete a service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_manage_delete.html#id_roles_manage_delete_slr "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_manage_delete.html#id_roles_manage_delete_slr") in the *IAM User Guide*.


After you delete AWSServiceRoleForNetworkManager, Network Manager will create the role 
 again when you create a new global network. After you delete
 AWSServiceRoleForVPCTransitGateway, Amazon VPC will create the role again
 when you attach a VPC to a transit gateway in your account.


## Supported Regions


Service-linked roles are supported in all the AWS Regions where the service
 is available. For more information, see [Region availability](what-is-cloudwan.md#cloudwan-available-regions "what-is-cloudwan.md#cloudwan-available-regions").
