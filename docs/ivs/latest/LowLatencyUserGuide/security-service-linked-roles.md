# Using Service-Linked Roles for

Amazon IVS

Amazon IVS uses IAM[service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role"). A service-linked role is a unique type of IAM role that is
linked directly to an AWS service. Service-linked roles are predefined by Amazon IVS and
include all the permissions that the service requires to call other AWS services on your
behalf.

A service-linked role makes setting up Amazon IVS easier because you don’t have to
manually add the necessary permissions. Amazon IVS defines the permissions of its
service-linked roles, and only Amazon IVS can assume its roles. The defined permissions
include the trust policy and the permissions policy, and that permissions policy cannot be
attached to any other IAM entity.

You can delete an IVS service-linked role only after first deleting the related IVS
resources. This prevents you from inadvertently removing permission for IVS to access the AWS
resources associated with the service-linked role.

For information about other services that support service-linked roles, see [AWS Services That Work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") and look for the services that have **Yes** in the **Service-Linked Role** column.
Choose a **Yes** with a link to view the service-linked role
documentation for that service.

## Service-Linked Role Permissions for Amazon IVS

Amazon IVS uses the service-linked role named **AWSServiceRoleForIVSRecordToS3**
to access Amazon S3 buckets on behalf of your Amazon IVS Channels.

The AWSServiceRoleForIVSRecordToS3 service-linked role trusts the following services to assume the
role:

- `ivs.amazonaws.com`

The role permissions policy allows Amazon IVS to complete the following actions on the
specified resources:

- Action: `s3:PutObject` on
  `your Amazon S3 buckets`

You must configure permissions to allow an IAM entity (such as a user, group, or role)
to create, edit, or delete a service-linked role. For more information, see [Service-Linked Role Permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the
_IAM User Guide_.

## Creating a Service-Linked Role for Amazon IVS

You don't need to manually create the service-linked role for IVS. Amazon IVS creates
it for you, when you create a recording-configuration resource in the Amazon IVS Console, the
AWS CLI, or the AWS API. The service-linked role is named
AWSServiceRoleForIVSRecordToS3.

###### Important

This service-linked role can appear in your account if you completed an action in
another service that uses the features supported by this role.
To learn more,
see [A
New Role Appeared in My IAM Account](../../../IAM/latest/UserGuide/troubleshoot_roles.md#troubleshoot_roles_new-role-appeared "../../../IAM/latest/UserGuide/troubleshoot_roles.md#troubleshoot_roles_new-role-appeared").

If you delete this service-linked role and then need to create it again, you can use the
same process to recreate the role in your account. When you create a recording-configuration resource,
Amazon IVS creates the service-linked role for you again.

## Editing a Service-Linked Role for Amazon IVS

Amazon IVS does not allow you to edit the AWSServiceRoleForIVSRecordToS3 service-linked role. After you
create a service-linked role, you cannot change the name of the role because various entities
might reference the role. However, you can edit the description of the role using IAM. For
more information, see [Editing
a Service-Linked Role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role") in the _IAM User Guide_.

## Deleting a Service-Linked Role for Amazon IVS

If you no longer need to use a feature or service that requires a service-linked role, we
recommend that you delete that role. That way you don’t have an unused entity that is not
actively monitored or maintained. However, you must clean up the resources for your
service-linked role before you can manually delete it.

###### Note

If the Amazon IVS service is using the role when you try to delete the resources,
then the deletion might fail. If that happens, wait for a few minutes and try the operation
again.

**To delete Amazon IVS resources used by the AWSServiceRoleForIVSRecordToS3
service-linked role:**

Use the Amazon IVS Console, the AWS CLI, or the AWS API to remove the recording-configuration
association from all channels and delete all recording-configuration resources in the region.

**To manually delete the service-linked role using
IAM:**

Use the IAM console, the AWS CLI, or the AWS API to delete the AWSServiceRoleForIVSRecordToS3 service-linked
role. For more information, see [Deleting a Service-Linked Role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the _IAM User Guide_.

## Supported Regions for Amazon IVS Service-Linked Roles

Amazon IVS supports using service-linked roles in all of the regions where the service
is available. For more information, see [Amazon IVS Service Endpoints](../../../general/latest/gr/ivs.md "../../../general/latest/gr/ivs.md").
