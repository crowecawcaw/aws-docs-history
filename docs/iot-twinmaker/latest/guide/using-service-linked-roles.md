# Using service-linked roles for

AWS IoT TwinMaker

AWS IoT TwinMaker uses AWS Identity and Access Management (IAM) [service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role"). A service-linked role is a unique type of IAM role that is
linked directly to AWS IoT TwinMaker. Service-linked roles are predefined by AWS IoT TwinMaker and
include all the permissions that the service requires to call other AWS services on your
behalf.

A service-linked role makes setting up AWS IoT TwinMaker easier because you don’t have to
manually add the necessary permissions. AWS IoT TwinMaker defines the permissions of its
service-linked roles, and unless defined otherwise, only AWS IoT TwinMaker can assume its roles. The
defined permissions include the trust policy and the permissions policy, and that permissions
policy cannot be attached to any other IAM entity.

You can delete a service-linked role only after first deleting their related resources. This
protects your AWS IoT TwinMaker resources because you can't inadvertently remove permission to
access the resources.

For information about other services that support service-linked roles, see [AWS services that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") and look for the services that have **Yes** in the **Service-linked roles** column.
Choose a **Yes** with a link to view the service-linked role
documentation for that service.

## Service-linked role permissions for AWS IoT TwinMaker

AWS IoT TwinMaker uses the service-linked role named **AWSServiceRoleForIoTTwinMaker** –
Allows AWS IoT TwinMaker to call other AWS services and to sync their resources on your behalf.

The AWSServiceRoleForIoTTwinMaker service-linked role trusts the following services to assume the
role:

- `iottwinmaker.amazonaws.com`

The role permissions policy named AWSIoTTwinMakerServiceRolePolicy allows AWS IoT TwinMaker to complete the
following actions on the specified resources:

- Action: `iotsitewise:DescribeAsset, iotsitewise:ListAssets, iotsitewise:DescribeAssetModel, and iotsitewise:ListAssetModels, iottwinmaker:GetEntity, iottwinmaker:CreateEntity, iottwinmaker:UpdateEntity, iottwinmaker:DeleteEntity, iottwinmaker:ListEntities, iottwinmaker:GetComponentType, iottwinmaker:CreateComponentType, iottwinmaker:UpdateComponentType, iottwinmaker:DeleteComponentType, iottwinmaker:ListComponentTypes` on
  `all your iotsitewise asset and asset-model resources`

You must configure permissions to allow your users, groups, or roles to create, edit, or
delete a service-linked role. For more information, see [Service-linked role permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the
_IAM User Guide_.

## Creating a service-linked role for AWS IoT TwinMaker

You don't need to manually create a service-linked role. When you
synchronize your AWS IoT SiteWise assets and asset models (asset sync) in the AWS Management Console, the AWS CLI, or the AWS API, AWS IoT TwinMaker creates
the service-linked role for you.

If you delete this service-linked role, and then need to create it again, you can use the
same process to recreate the role in your account. When you synchronize your AWS IoT SiteWise assets and asset models (asset sync),
AWS IoT TwinMaker creates the service-linked role for you again.

You can also use the IAM console to create a service-linked role with the
**"IoT TwinMaker - Managed Role"** use case. In the AWS CLI or the AWS API, create a
service-linked role with the `iottwinmaker.amazonaws.com` service name. For more
information, see [Creating a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#create-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#create-service-linked-role") in the _IAM User Guide_. If you
delete this service-linked role, you can use this same process to create the role
again.

## Editing a service-linked role for AWS IoT TwinMaker

AWS IoT TwinMaker does not allow you to edit the AWSServiceRoleForIoTTwinMaker service-linked role. After you
create a service-linked role, you cannot change the name of the role because various entities
might reference the role. However, you can edit the description of the role using IAM. For
more information, see [Editing
a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role") in the _IAM User Guide_.

## Deleting a service-linked role for AWS IoT TwinMaker

If you no longer need to use a feature or service that requires a service-linked role, we
recommend that you delete that role. That way you don’t have an unused entity that is not
actively monitored or maintained. However, you must clean up any serviceLinked-workspaces that
are still using your service-linked role before you can manually delete the role.

###### Note

If the AWS IoT TwinMaker service is using the role when you try to delete the resources,
then the deletion might fail. If that happens, wait for a few minutes and try the operation
again.

**To manually delete the service-linked role using
IAM**

Use the IAM console, the AWS CLI, or the AWS API to delete the AWSServiceRoleForIoTTwinMaker service-linked
role. For more information, see [Deleting a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the _IAM User Guide_.

## Supported Regions for AWS IoT TwinMaker service-linked roles

AWS IoT TwinMaker supports using service-linked roles in all of the Regions where the service
is available. For more information, see [AWS Regions and endpoints](../../../general/latest/gr/iot-twinmaker.md "../../../general/latest/gr/iot-twinmaker.md").
