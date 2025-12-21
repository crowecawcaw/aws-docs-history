# Service-linked roles for user attributes for cost allocation

User attributes for cost allocation uses AWS Identity and Access Management (IAM) [service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role"). A service-linked role is a unique type of IAM
role that is linked directly to user attributes for cost allocation. Service-linked roles are
predefined by user attributes for cost allocation and include all the permissions that the
service requires to call other AWS services on your behalf.

A service-linked role makes setting up user attributes for cost allocation easier because
you don't have to manually add the necessary permissions. User attributes for cost allocation
defines the permissions of its service-linked role, and unless defined otherwise,
only user attributes for cost allocation can assume that role. The defined permissions
include the trust policy and the permissions policy, and that permissions policy
cannot be attached to any other IAM entity.

For information about other services that support service-linked roles, see [AWS services that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") and look for the services that have
**Yes** in the **Service-Linked
Role** column. Choose a **Yes** with a
link to view the service-linked role documentation for that service.

## Service-linked role permissions for

user attributes for cost allocation

User attributes for cost allocation uses the service-linked role named
`AWSServiceRoleForUserAttributeCostAllocation`, which grants
user attributes for cost allocation permissions to read user attributes from AWS IAM
Identity Center on your behalf.

The `AWSServiceRoleForUserAttributeCostAllocation` service-linked
role trusts the `user-attribute-cost-allocation-data.amazonaws.com`
service to assume the role.

The service-linked role uses two types of policies:

- **Inline role permissions policy:** Contains the permissions that allow user attributes for cost allocation to access user information from your AWS IAM Identity Center instance through Identity Store APIs. This policy includes the necessary KMS permissions when customers encrypt their Identity Center data, and is scoped to your specific account and Identity Center instance.
- **AWS managed policy (AWSUserAttributeCostAllocationPolicy):** Provides additional permissions to the service to fetch the service-linked role for internal usage.

For more information on updates to the AWSUserAttributeCostAllocationPolicy managed policy, see [AWS managed policies for AWS Billing and Cost Management](security-iam-awsmanpol.md "security-iam-awsmanpol.md").

You must configure permissions to allow an IAM entity (such as a user, group,
or role) to create, edit, or delete a service-linked role. For more information,
see [Service-linked role permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the IAM User Guide.

## Creating the user attributes for cost allocation

service-linked role

You don't need to manually create a service-linked role. When you enable
user attributes for cost allocation in the AWS Cost Management console, the service
automatically creates the service-linked role for you.

If you delete this service-linked role, and then need to create it again, you
can use the same process to recreate the role in your account. When you enable
user attributes for cost allocation, the service creates the service-linked role for you
again.

## Editing the user attributes for cost allocation

service-linked role

You can't edit the name or permissions of the
`AWSServiceRoleForUserAttributeCostAllocation` service-linked
role because various entities might reference the role. However, you can edit
the description of the role using IAM. For more information, see [Editing a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role") in the IAM User Guide.

## Deleting the user attributes for cost allocation

service-linked role

If you no longer need to use user attributes for cost allocation, we recommend that you
delete the `AWSServiceRoleForUserAttributeCostAllocation`
service-linked role. That way, you don't have an unused entity that isn't
actively monitored or maintained. However, before you can manually delete the
service-linked role, you must first opt out of user attributes for cost allocation.

### Cleaning up the service-linked

role

Before you can use IAM to delete the service-linked role, you must first
opt out of user attributes for cost allocation by disabling all user attributes in
the user attributes for cost allocation preferences.

### Manually delete the service-linked

role

Use the IAM console, the AWS CLI, or the AWS API to delete the
`AWSServiceRoleForUserAttributeCostAllocation` service-linked
role. For more information, see [Deleting a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the _IAM User Guide_.

## Supported Regions for user attributes for cost

allocation service-linked roles

User attributes for cost allocation supports using service-linked roles in all of the
AWS Regions where the service is available. For more information, see AWS
service endpoints.
