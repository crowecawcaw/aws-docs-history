AWS Resource Explorer now provides immediate access to resource search and
discovery capabilities in a Region. With this launch, you no longer need to activate
Resource Explorer to discover your resources. [Learn more](manage-immediate-resource-discovery-experience.md "manage-immediate-resource-discovery-experience.md")

# Using service-linked roles for

Resource Explorer

AWS Resource Explorer uses AWS Identity and Access Management (IAM) [service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role"). A service-linked role is a unique type of IAM role
that is linked directly to Resource Explorer. Service-linked roles are predefined by Resource Explorer and include
all the permissions that the service requires to call other AWS services on your
behalf.

A service-linked role makes configuring Resource Explorer easier because you don’t have to manually
add the necessary permissions. Resource Explorer defines the permissions of its service-linked roles,
and unless defined otherwise, only Resource Explorer can assume its roles. The defined permissions
include both the trust policy and the permissions policy, and that permissions policy can't
be assigned to any other IAM entity.

For information about other services that support service-linked roles, see [AWS services
that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") in the _IAM User Guide_.
There, look for the services that have **Yes** in the **Service-linked roles** column. Choose a **Yes** with a link to view the service-linked role documentation for that
service.

## Service-linked role permissions for Resource Explorer

Resource Explorer uses the service-linked role named `AWSServiceRoleForResourceExplorer`. This role grants
permissions to the Resource Explorer service to view resources and AWS CloudTrail events in your
AWS account on your behalf and to index those resources to support searching.

The `AWSServiceRoleForResourceExplorer` service-linked role trusts only the service with the
following service principal to assume the role:

- `resource-explorer-2.amazonaws.com`

The role permissions policy named [AWSResourceExplorerServiceRolePolicy](security_iam_awsmanpol.md#security_iam_awsmanpol_AWSResourceExplorerServiceRolePolicy "security_iam_awsmanpol.md#security_iam_awsmanpol_AWSResourceExplorerServiceRolePolicy") allows
Resource Explorer read-only
access to retrieve resource names and properties for supported AWS resources. To view
the services and resources that Resource Explorer supports, see [Resource
types you can search for with Resource Explorer](supported-resource-types.md "supported-resource-types.md"). To see the latest version of this
AWS managed policy, [`AWSResourceExplorerServiceRolePolicy`](../../../aws-managed-policy/latest/reference/AWSResourceExplorerServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/AWSResourceExplorerServiceRolePolicy.md") in the _AWS Managed Policy
Reference Guide_. To see permission changes to this policy, see [Resource Explorer updates to AWS managed
policies](security_iam_awsmanpol.md#security_iam_awsmanpol_updates "security_iam_awsmanpol.md#security_iam_awsmanpol_updates").

A principal is an IAM entity such as a user, group, or role. If you let Resource Explorer
create the service-linked role for you when it creates the index in the first Region of
the account, then the principal performing the task needs only the permissions required
to create the Resource Explorer index. To create the service-linked role manually using IAM, then
the principal performing the task must have permission to create a service-linked role.
For more information, see [Service-linked role permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the
_IAM User Guide_.

## Creating a service-linked role for Resource Explorer

You don't need to manually create a service-linked role. When you turn on Resource Explorer in
the AWS Management Console, or run [CreateIndex](../apireference/API_CreateIndex.md "../apireference/API_CreateIndex.md") in the first
AWS Region in your account using the AWS CLI or an AWS API, Resource Explorer creates the
service-linked role for you.

If you delete this service-linked role, and then need to create it again, you can use
the same process to re-create the role in your account. When you [RegisterResourceExplorer](../apireference/API_RegisterResourceExplorer.md "../apireference/API_RegisterResourceExplorer.md") in the first Region in your account, Resource Explorer
creates the service-linked role for you again.

## Editing a service-linked role for Resource Explorer

Resource Explorer doesn't allow you to edit the `AWSServiceRoleForResourceExplorer` service-linked role.
After you create a service-linked role, you can't change the name of the role because
various entities might reference the role. However, you can edit the description of the
role using IAM. For more information, see [Editing a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role") in the
_IAM User Guide_.

## Deleting a service-linked role for Resource Explorer

You can use the IAM console, the AWS CLI, or the AWS API to manually delete the
service-linked role. To do this, you must first remove the Resource Explorer indexes from every
AWS Region in your account and then you can manually delete the service-linked
role.

###### Note

If the Resource Explorer service is using the role when you try to delete the resources, the
deletion fails. If that happens, ensure that all indexes from all Regions are
deleted, then wait for a few minutes and try the operation again.

**To manually delete the service-linked role using
IAM**

Use the IAM console, the AWS CLI, or the AWS API to delete the
`AWSServiceRoleForResourceExplorer` service-linked role. For more information, see [Deleting a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the
_IAM User Guide_.

## Supported Regions for Resource Explorer service-linked roles

Resource Explorer supports using service-linked roles in all of the Regions where the service is
available. For more information, see [AWS service endpoints](../../../general/latest/gr/rande.md "../../../general/latest/gr/rande.md") in the
_Amazon Web Services General Reference_.
