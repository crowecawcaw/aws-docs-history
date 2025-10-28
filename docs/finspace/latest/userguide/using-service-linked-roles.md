After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see
[Amazon FinSpace end of support](amazon-finspace-end-of-support.md "amazon-finspace-end-of-support.md").

# Using service-linked roles for

FinSpace

Amazon FinSpace uses AWS Identity and Access Management (IAM)[service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role"). A service-linked role is a unique type of IAM role that is
linked directly to FinSpace. Service-linked roles are predefined by FinSpace and
include all the permissions that the service requires to call other AWS services on your
behalf.

A service-linked role makes setting up FinSpace easier because you don’t have to
manually add the necessary permissions. FinSpace defines the permissions of its
service-linked roles, and unless defined otherwise, only FinSpace can assume its roles. The
defined permissions include the trust policy and the permissions policy, and that permissions
policy cannot be attached to any other IAM entity.

You can delete a service-linked role only after first deleting their related resources. This
protects your FinSpace resources because you can't inadvertently remove permission to
access the resources.

For information about other services that support service-linked roles, see [AWS Services That Work with
IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") and look for the services that have **Yes** in the
**Service-linked roles** column. Choose a **Yes** with a link to view the service-linked role documentation for that
service.

## Service-linked role permissions for

FinSpace

FinSpace uses the service-linked role named **AWSServiceRoleForFinSpace** –
Policy to enable access to AWS service and resources used or managed by Amazon FinSpace.

The AWSServiceRoleForFinSpace service-linked role trusts the following service to assume the
role:

- `finspace.amazonaws.com`

The role permissions policy named AWSFinSpaceServiceRolePolicy allows FinSpace to complete the following action on the
specified resources:

- Action: `cloudwatch:PutMetricData` on
  `*` in `AWS/FinSpace` and `AWS/Usage` CloudWatch namespace.

For more information about this policy, including the JSON policy document, see [AWSFinSpaceServiceRolePolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-AWSFinSpaceServiceRolePolicy "security-iam-awsmanpol.md#security-iam-awsmanpol-AWSFinSpaceServiceRolePolicy").

You must configure permissions to allow an IAM entity (such as a user, group, or role)
to create, edit, or delete a service-linked role. For more information, see [Service-linked role permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the _IAM User Guide_.

## Creating a service-linked role for

FinSpace

You don't need to manually create a service-linked role. When you
create a FinSpace environment in the AWS Management Console, the AWS CLI, or the AWS API, FinSpace
creates the service-linked role for you.

###### Important

This service-linked role can appear in your account if you completed an action in
another service that uses the features supported by this role. Also, if you were using the
FinSpace service before May 25, 2023, when it began supporting service-linked roles,
then FinSpace created the AWSServiceRoleForFinSpace role in your account. To learn more, see [A new
role appeared in my IAM account](../../../IAM/latest/UserGuide/troubleshoot_roles.md#troubleshoot_roles_new-role-appeared "../../../IAM/latest/UserGuide/troubleshoot_roles.md#troubleshoot_roles_new-role-appeared").

If you delete this service-linked role, and then need to create it again, you can use the
same process to recreate the role in your account. When you create a FinSpace environment,
FinSpace creates the service-linked role for you again.

## Editing a service-linked role for

FinSpace

FinSpace does not allow you to edit the AWSServiceRoleForFinSpace service-linked role. After you
create a service-linked role, you cannot change the name of the role because various entities
might reference the role. However, you can edit the description of the role using IAM. For
more information, see [Editing a
service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role") in the _IAM User Guide_.

## Deleting a service-linked role for FinSpace

If you no longer need to use a feature or service that requires a service-linked role, we
recommend that you delete that role. That way you don’t have an unused entity that is not
actively monitored or maintained. However, you must clean up the resources for your
service-linked role before you can manually delete it.

###### Note

If the FinSpace service is using the role when you try to delete the resources,
then the deletion might fail. If that happens, wait for a few minutes and try the operation
again.

###### Note

If you want to delete the AWSServiceRoleForFinSpace, you must first delete all of your FinSpace environments.

**To manually delete the service-linked role using
IAM**

Use the IAM console, the AWS CLI, or the AWS API to delete the AWSServiceRoleForFinSpace service-linked
role. For more information, see [Deleting a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the _IAM User Guide_.

## Supported regions for

FinSpace service-linked roles

FinSpace supports using service-linked roles in all of the regions where the service is available. For more information, see [Regions and IP ranges](regions-ip-ranges.md "regions-ip-ranges.md").
