# AWS Global Networks for Transit Gateways service-linked roles

AWS Global Networks for Transit Gateways uses service-linked roles for the permissions that it requires to call other
AWS services on your behalf. These service-linked roles are not propagated to your
AWS Organizations management account.

## Permissions granted by the service-linked

role

AWS Global Networks for Transit Gateways uses a Network Manager service-linked role named AWSServiceRoleForNetworkManager to call
the actions on your behalf when you work with global networks.

The AWSServiceRoleForNetworkManager service-linked role trusts the following service to assume the role:

- `networkmanager.amazonaws.com`

This service-linked role uses the managed policy AWSNetworkManagerServiceRolePolicy.
To view the permissions for this policy, see [AWSNetworkManagerServiceRolePolicy](../../../aws-managed-policy/latest/reference/AWSNetworkManagerServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/AWSNetworkManagerServiceRolePolicy.md")
in the _AWS Managed Policy Reference_.

## Create the service-linked role

You don't need to manually create the **AWSServiceRoleForNetworkManager** role. global networks
creates this role for you when you create your first global network.

For global networks to create a service-linked role on your behalf, you must have the required
permissions. For more information, see [Service-linked role permissions](../../../IAM/latest/UserGuide/id_roles_create-service-linked-role.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/id_roles_create-service-linked-role.md#service-linked-role-permissions") in the _IAM User Guide_.

## Edit the service-linked role

You can edit the description of **AWSServiceRoleForNetworkManager** using IAM. For more
information, see [Edit a service-linked role description](../../../IAM/latest/UserGuide/id_roles_update-service-linked-role.md#edit-service-linked-role-iam-console "../../../IAM/latest/UserGuide/id_roles_update-service-linked-role.md#edit-service-linked-role-iam-console") in the _IAM User Guide_.

## Delete the service-linked role

If you no longer need to use global networks, we recommend that you delete the
**AWSServiceRoleForNetworkManager** role.

You can delete this service-linked role only after you delete your global network. For
information about how to delete your global network, see [Delete a global network](global-networks-deleting.md "global-networks-deleting.md").

You can use the IAM console, the IAM CLI, or the IAM API to delete service-linked roles.
For more information, see [Delete a service-linked role](../../../IAM/latest/UserGuide/id_roles_manage_delete.md#id_roles_manage_delete_slr "../../../IAM/latest/UserGuide/id_roles_manage_delete.md#id_roles_manage_delete_slr") in the _IAM User Guide_.

After you delete **AWSServiceRoleForNetworkManager**, Network Manager will create the role again when
you create a new global network.

## Supported Regions for AWS Global Networks for Transit Gateways service-linked roles

AWS Global Networks for Transit Gateways supports the custom-linked roles in all of AWS Regions where the service is
available. For more information, see [Region availability](what-are-global-networks.md#nm-available-regions "what-are-global-networks.md#nm-available-regions").
