# Using service-linked roles for AWS HealthOmics

AWS HealthOmics uses AWS Identity and Access Management (IAM) [service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role"). A service-linked role is a unique type of IAM role that is
linked directly to AWS HealthOmics. Service-linked roles are predefined by AWS HealthOmics and
include all the permissions that the service requires to call other AWS services on your
behalf.

A service-linked role makes setting up AWS HealthOmics easier because you don’t have to
manually add the necessary permissions. AWS HealthOmics defines the permissions of its
service-linked roles, and unless defined otherwise, only AWS HealthOmics can assume its roles. The
defined permissions include the trust policy and the permissions policy, and that permissions
policy cannot be attached to any other IAM entity.

You can delete a service-linked role only after first deleting their related resources. This
protects your AWS HealthOmics resources because you can't inadvertently remove permission to
access the resources.

For information about other services that support service-linked roles, see [AWS services that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") and look for the services that have **Yes** in the **Service-linked roles** column.
Choose a **Yes** with a link to view the service-linked role
documentation for that service.

## Service-linked role permissions for AWS HealthOmics

AWS HealthOmics uses a service-linked role named
**AwsServiceRoleForHealthOmics** – a managed IAM policy with scoped permissions that provides permissions for AWS HealthOmics to manage VPC network resources, including creating, configuring, and deleting Elastic Network Interfaces (ENIs) on your behalf.

The AwsServiceRoleForHealthOmics service-linked role trusts the
`omics.amazonaws.com` service principal to assume the role.

The role permissions policy is the AWSHealthOmicsServiceLinkedRolePolicy AWS managed policy. For the
full list of permissions that this policy grants including the JSON policy document, see [AWSHealthOmicsServiceLinkedRolePolicy](../../../aws-managed-policy/latest/reference/AWSHealthOmicsServiceLinkedRolePolicy.md "../../../aws-managed-policy/latest/reference/AWSHealthOmicsServiceLinkedRolePolicy.md") in the
_AWS Managed Policy Reference Guide_.

You must configure permissions to allow your users, groups, or roles to create, edit, or
delete a service-linked role. For more information, see [Service-linked role permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the
_IAM User Guide_.

## Creating a service-linked role for AWS HealthOmics

You don't need to manually create a service-linked role. AWS HealthOmics create the service-linked role for you the first time when you create a run-specific configuration with VPC configuration.

If you delete this service-linked role, and then need to create it again, you can use the
same process to recreate the role in your account. For more
information, see [Creating a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#create-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#create-service-linked-role") in the _IAM User Guide_.

## Editing a service-linked role for AWS HealthOmics

AWS HealthOmics does not allow you to edit the AwsServiceRoleForHealthOmics service-linked role. After you
create a service-linked role, you cannot change the name of the role because various entities
might reference the role. However, you can edit the description of the role using IAM. For
more information, see [Editing
a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role") in the _IAM User Guide_.

## Deleting a service-linked role for AWS HealthOmics

If you no longer need to use the feature that requires a service-linked role, we
recommend that you delete that role. That way you don’t have an unused entity that is not
actively monitored or maintained.

###### Note

If the AWS HealthOmics service is using the role when you try to delete the resources,
then the deletion might fail. If that happens, wait for a few minutes and try the operation
again.

You can delete this service-linked role only when there is no active run using any of the run-specific configurations that have VPC configuration. This ensures that you can't inadvertently remove permissions for AWS HealthOmics to manage VPC network resources on your behalf.

**To manually delete the service-linked role using
IAM**

Use the IAM console, the AWS CLI, or the AWS API to delete the AwsServiceRoleForHealthOmics service-linked
role. For more information, see [Deleting a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the _IAM User Guide_.

## Supported Regions for AWS HealthOmics service-linked roles

AWS HealthOmics supports using service-linked roles in all of the Regions where the service
is available. For more information, see [AWS Regions and endpoints](../../../general/latest/gr/rande.md "../../../general/latest/gr/rande.md").
