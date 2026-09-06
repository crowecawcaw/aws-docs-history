

# AWS Global Networks for Transit Gateways service-linked roles
<a name="nm-service-linked-roles"></a>

AWS Global Networks for Transit Gateways uses service-linked roles for the permissions that it requires to call other AWS services on your behalf. These service-linked roles are not propagated to your AWS Organizations management account.

## Permissions granted by the service-linked role
<a name="service-linked-role-permissions"></a>

AWS Global Networks for Transit Gateways uses a Network Manager service-linked role named AWSServiceRoleForNetworkManager to call the actions on your behalf when you work with global networks.

The AWSServiceRoleForNetworkManager service-linked role trusts the following service to assume the role: 
+ `networkmanager.amazonaws.com`

This service-linked role uses the managed policy AWSNetworkManagerServiceRolePolicy. To view the permissions for this policy, see [AWSNetworkManagerServiceRolePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSNetworkManagerServiceRolePolicy.html) in the *AWS Managed Policy Reference*.

## Create the service-linked role
<a name="create-service-linked-role"></a>

You don't need to manually create the **AWSServiceRoleForNetworkManager** role. global networks creates this role for you when you create your first global network.

For global networks to create a service-linked role on your behalf, you must have the required permissions. For more information, see [Service-linked role permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create-service-linked-role.html#service-linked-role-permissions) in the *IAM User Guide*.

## Edit the service-linked role
<a name="edit-service-linked-role"></a>

You can edit the description of **AWSServiceRoleForNetworkManager** using IAM. For more information, see [Edit a service-linked role description](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_update-service-linked-role.html#edit-service-linked-role-iam-console) in the *IAM User Guide*.

## Delete the service-linked role
<a name="delete-service-linked-role"></a>

If you no longer need to use global networks, we recommend that you delete the **AWSServiceRoleForNetworkManager** role.

You can delete this service-linked role only after you delete your global network. For information about how to delete your global network, see [Delete a global network](global-networks-deleting.md).

You can use the IAM console, the IAM CLI, or the IAM API to delete service-linked roles. For more information, see [Delete a service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_manage_delete.html#id_roles_manage_delete_slr) in the *IAM User Guide*.

After you delete **AWSServiceRoleForNetworkManager**, Network Manager will create the role again when you create a new global network.

## Supported Regions for AWS Global Networks for Transit Gateways service-linked roles
<a name="slr-regions"></a>

AWS Global Networks for Transit Gateways supports the custom-linked roles in all of AWS Regions where the service is available. For more information, see [Region availability](what-are-global-networks.md#nm-available-regions).