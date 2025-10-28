# Using service-linked roles for {evws}

{evws-long} uses {aws} Identity and Access Management (IAM) [service-linked roles](../../../IAM/latest/UserGuide/id_roles.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles.md#iam-term-service-linked-role").
A service-linked role is a unique type of IAM role that is linked directly to {evws}.
Service-linked roles are predefined by {evws} and include all the permissions that the service requires to call other {aws} services on your behalf.

A service-linked role makes setting up {evws} easier because you don’t have to manually add the necessary permissions.
{evws} defines the permissions of its service-linked roles, and unless defined otherwise, only {evws} can assume its roles.
The defined permissions include the trust policy and the permissions policy, and that permissions policy cannot be attached to any other IAM entity.

You can delete a service-linked role only after first deleting their related resources.
This protects your {evws} resources because you can’t inadvertently remove permission to access the resources.

For information about other services that support service-linked roles, see [{aws} services that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") and look for the services that have **Yes** in the **Service-linked role** column.
Choose a **Yes** with a link to view the service-linked role documentation for that service.

## Service-linked role permissions for {evws}

{evws} uses the service-linked role named `AWSServiceRoleForAmazonEVS`.
The role allows {evws} to manage environments in your account.
The attached policy allows the role to manage the following resources: EVS elastic network interfaces, EVS VLAN subnets, EVS hosts, VPCs, and CloudWatch metrics.

The `AWSServiceRoleForAmazonEVS` service-linked role trusts the following services to assume the role:

- `evs.amazonaws.com`

The role permissions policy allows {evws} to complete the following actions on the specified resources:

- [AmazonEVSServiceRolePolicy](../../../aws-managed-policy/latest/reference/AmazonEVSServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/AmazonEVSServiceRolePolicy.md")

You must configure permissions to allow an IAM entity (such as a user, group, or role) to create, edit, or delete a service-linked role.
For more information, see [Service-linked role permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the _IAM User Guide_.

## Creating a service-linked role for {evws}

You don’t need to manually create a service-linked role. When you create an environment in the {aws-management-console}, the {aws} CLI, or the {aws} API, {evws} creates the service-linked role for you.

If you delete this service-linked role, and then need to create it again, you can use the same process to recreate the role in your account.
When you create an environment, {evws} creates the service-linked role for you again.

## Editing a service-linked role for {evws}

{evws} does not allow you to edit the `AWSServiceRoleForAmazonEVS` service-linked role.
After you create a service-linked role, you cannot change the name of the role because various entities might reference the role.
However, you can edit the description of the role using IAM.
For more information, see [Editing a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role") in the _IAM User Guide_.

## Deleting a service-linked role for {evws}

If you no longer need to use a feature or service that requires a service-linked role, we recommend that you delete that role.
That way you don’t have an unused entity that is not actively monitored or maintained.
However, you must clean up your service-linked role before you can manually delete it.

### Cleaning up a service-linked role

Before you can use IAM to delete a service-linked role, you must first delete any resources used by the role.
For steps to delete an {evws} environment with hosts, see [Delete the Amazon EVS hosts and environment](getting-started.md#getting-started-cleanup-env-hosts "getting-started.md#getting-started-cleanup-env-hosts").

###### Note

If the {evws} service is using the role when you try to delete the resources, then the deletion might fail.
If that happens, wait for a few minutes and try the operation again.

### Manually delete the service-linked role

Use the IAM console, the {aws} CLI, or the {aws} API to delete the `AWSServiceRoleForAmazonEVS` service-linked role.
For more information, see [Deleting a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the _IAM User Guide_.

## Supported regions for {evws} service-linked roles

{evws} supports using service-linked roles in all of the regions where the service is available.
For more information, see [{evws-long} endpoints and quotas](../../../general/latest/gr/evs.md "../../../general/latest/gr/evs.md") in the _{aws} General Reference Guide_.
