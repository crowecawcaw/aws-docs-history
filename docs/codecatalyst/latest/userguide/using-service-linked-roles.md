Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Using service-linked roles for

CodeCatalyst

Amazon CodeCatalyst uses AWS Identity and Access Management (IAM) [service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role"). A service-linked role is a unique type of IAM role that is
linked directly to CodeCatalyst. Service-linked roles are predefined by CodeCatalyst and
include all the permissions that the service requires to call other AWS services on your
behalf.

A service-linked role makes setting up CodeCatalyst easier because you don’t have to
manually add the necessary permissions. CodeCatalyst defines the permissions of its
service-linked roles, and unless defined otherwise, only CodeCatalyst can assume its roles. The
defined permissions include the trust policy and the permissions policy, and that permissions
policy cannot be attached to any other IAM entity.

You can delete a service-linked role only after first deleting their related resources. This
protects your CodeCatalyst resources because you can't inadvertently remove permission to
access the resources.

For information about other services that support service-linked roles, see [AWS services that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") and look for the services that have **Yes** in the **Service-linked roles** column.
Choose a **Yes** with a link to view the service-linked role
documentation for that service.

## Service-linked role permissions for CodeCatalyst

CodeCatalyst uses the service-linked role named **AmazonCodeCatalystServiceRoleForIdentityCenterApplicationSynchronization** –
Allows Amazon CodeCatalyst read-only access to application instance profiles and associated directory users and groups on your behalf.

The AmazonCodeCatalystServiceRoleForIdentityCenterApplicationSynchronization service-linked role trusts the following services to assume the
role:

- `codecatalyst.amazonaws.com`

The role permissions policy named AmazonCodeCatalystServiceRoleForIdentityCenterApplicationSynchronizationPolicy allows CodeCatalyst to complete the
following actions on the specified resources:

- Action: `View application instance profiles and associated directory users and groups` for
  `CodeCatalyst spaces that support identity federation and SSO users and groups`

You must configure permissions to allow your users, groups, or roles to create, edit, or
delete a service-linked role. For more information, see [Service-linked role permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the
_IAM User Guide_.

## Creating a service-linked role for CodeCatalyst

You don't need to manually create a service-linked role. When you
create a space in the AWS Management Console, the AWS CLI, or the AWS API, CodeCatalyst creates
the service-linked role for you.

###### Important

This service-linked role can appear in your account if you completed an action in
another service that uses the features supported by this role. Also, if you were using the
CodeCatalyst service before November 17, 2023, when it began supporting service-linked roles,
then CodeCatalyst created the AmazonCodeCatalystServiceRoleForIdentityCenterApplicationSynchronization role in your account. To learn more, see [A
new role appeared in my AWS account](../../../IAM/latest/UserGuide/troubleshoot_roles.md#troubleshoot_roles_new-role-appeared "../../../IAM/latest/UserGuide/troubleshoot_roles.md#troubleshoot_roles_new-role-appeared").

If you delete this service-linked role, and then need to create it again, you can use the
same process to recreate the role in your account. When you create a space,
CodeCatalyst creates the service-linked role for you again.

You can also use the IAM console to create a service-linked role with the
**View application instance profiles and associated directory users and groups** use case. In the AWS CLI or the AWS API, create a
service-linked role with the `codecatalyst.amazonaws.com` service name. For more
information, see [Creating a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#create-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#create-service-linked-role") in the _IAM User Guide_. If you
delete this service-linked role, you can use this same process to create the role
again.

## Editing a service-linked role for CodeCatalyst

CodeCatalyst does not allow you to edit the AmazonCodeCatalystServiceRoleForIdentityCenterApplicationSynchronization service-linked role. After you
create a service-linked role, you cannot change the name of the role because various entities
might reference the role. However, you can edit the description of the role using IAM. For
more information, see [Editing
a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role") in the _IAM User Guide_.

## Deleting a service-linked role for CodeCatalyst

You don't need to manually delete the AmazonCodeCatalystServiceRoleForIdentityCenterApplicationSynchronization role. When you delete a space
in the AWS Management Console, the AWS CLI, or the AWS API, CodeCatalyst cleans up the resources and
deletes the service-linked role for you.

You can also use the IAM console, the AWS CLI or the AWS API to manually delete the
service-linked role. To do this, you must first manually clean up the resources for your
service-linked role and then you can manually delete it.

###### Note

If the CodeCatalyst service is using the role when you try to delete the resources,
then the deletion might fail. If that happens, wait for a few minutes and try the operation
again.

###### To delete CodeCatalyst resources used by the AmazonCodeCatalystServiceRoleForIdentityCenterApplicationSynchronization

- [Delete the space](spaces-delete.md "spaces-delete.md").

**To manually delete the service-linked role using
IAM**

Use the IAM console, the AWS CLI, or the AWS API to delete the AmazonCodeCatalystServiceRoleForIdentityCenterApplicationSynchronization service-linked
role. For more information, see [Deleting a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the _IAM User Guide_.

## Supported Regions for CodeCatalyst service-linked roles

CodeCatalyst supports using service-linked roles in all of the Regions where the service
is available. For more information, see [AWS Regions and endpoints](../../../general/latest/gr/rande.md "../../../general/latest/gr/rande.md").

CodeCatalyst does not support using service-linked roles in every Region where the
service is available. You can use the AmazonCodeCatalystServiceRoleForIdentityCenterApplicationSynchronization role in the following Regions.

| Region name               | Region identity | Support in CodeCatalyst |
| ------------------------- | --------------- | ----------------------- |
| US East (N. Virginia)     | us-east-1       | No                      |
| US East (Ohio)            | us-east-2       | No                      |
| US West (N. California)   | us-west-1       | No                      |
| US West (Oregon)          | us-west-2       | Yes                     |
| Africa (Cape Town)        | af-south-1      | No                      |
| Asia Pacific (Hong Kong)  | ap-east-1       | No                      |
| Asia Pacific (Jakarta)    | ap-southeast-3  | No                      |
| Asia Pacific (Mumbai)     | ap-south-1      | No                      |
| Asia Pacific (Osaka)      | ap-northeast-3  | No                      |
| Asia Pacific (Seoul)      | ap-northeast-2  | No                      |
| Asia Pacific (Singapore)  | ap-southeast-1  | No                      |
| Asia Pacific (Sydney)     | ap-southeast-2  | No                      |
| Asia Pacific (Tokyo)      | ap-northeast-1  | No                      |
| Canada (Central)          | ca-central-1    | No                      |
| Europe (Frankfurt)        | eu-central-1    | No                      |
| Europe (Ireland)          | eu-west-1       | Yes                     |
| Europe (London)           | eu-west-2       | No                      |
| Europe (Milan)            | eu-south-1      | No                      |
| Europe (Paris)            | eu-west-3       | No                      |
| Europe (Stockholm)        | eu-north-1      | No                      |
| Middle East (Bahrain)     | me-south-1      | No                      |
| Middle East (UAE)         | me-central-1    | No                      |
| South America (São Paulo) | sa-east-1       | No                      |
| AWS GovCloud (US-East)    | us-gov-east-1   | No                      |
| AWS GovCloud (US-West)    | us-gov-west-1   | No                      |
