# Service-linked roles for

AWS PCS

AWS Parallel Computing Service uses AWS Identity and Access Management (IAM) [service-linked roles](../../../IAM/latest/UserGuide/id_roles.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles.md#iam-term-service-linked-role"). A service-linked role is a unique type of IAM role that is
linked directly to AWS PCS. Service-linked roles are predefined by AWS PCS and
include all the permissions that the service requires to call other AWS services on your
behalf.

A service-linked role makes setting up AWS PCS easier because you don’t have to
manually add the necessary permissions. AWS PCS defines the permissions of its
service-linked roles, and unless defined otherwise, only AWS PCS can assume its roles. The
defined permissions include the trust policy and the permissions policy, and that permissions
policy cannot be attached to any other IAM entity.

You can delete a service-linked role only after first deleting its related resources. This
protects your AWS PCS resources because you can't accidentally remove permission to
access the resources.

For information about other services that support service-linked roles, see [AWS services that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") and look for the services that have **Yes** in the **Service-linked roles** column.
Choose a **Yes** with a link to view the service-linked role
documentation for that service.

## Service-linked role permissions for AWS PCS

AWS PCS uses the service-linked role named **AWSServiceRoleForPCS** –
Grants permission to AWS PCS to manage Amazon EC2 resources.

The AWSServiceRoleForPCS service-linked role trusts the following services to assume the
role:

- `pcs.amazonaws.com`

The role permissions policy named [AWSPCSServiceRolePolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-service-role-policy "security-iam-awsmanpol.md#security-iam-awsmanpol-service-role-policy")
allows AWS PCS to complete actions on specific resources.

You must configure permissions to allow your users, groups, or roles to create, edit, or
delete a service-linked role. For more information, see [Service-linked role permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the
_IAM User Guide_.

## Creating a service-linked role for AWS PCS

You don't need to manually create a service-linked role. AWS PCS creates
a service-linked role for you when you create a cluster.

## Editing a service-linked role for AWS PCS

AWS PCS does not allow you to edit the AWSServiceRoleForPCS service-linked role. After you
create a service-linked role, you cannot change the name of the role because various entities
might reference the role. However, you can edit the description of the role using IAM. For
more information, see [Editing
a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role") in the _IAM User Guide_.

## Deleting a service-linked role for AWS PCS

If you no longer need to use a feature or service that requires a service-linked role, we
recommend that you delete that role. That way you don’t have an unused entity that is not
actively monitored or maintained. However, you must clean up the resources for your
service-linked role before you can manually delete it.

###### Note

If the AWS PCS service is using the role when you try to delete the resources,
then the deletion might fail. If that happens, wait for a few minutes and try the operation
again.

**To remove AWS PCS resources used by the AWSServiceRoleForPCS**

You must delete all your clusters to delete the AWSServiceRoleForPCS service-linked role.
For more information, see [Delete a cluster](what-is-service.md "what-is-service.md").

**To manually delete the service-linked role using
IAM**

Use the IAM console, the AWS CLI, or the AWS API to delete the AWSServiceRoleForPCS service-linked
role. For more information, see [Deleting a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the _IAM User Guide_.

## Supported Regions for AWS PCS service-linked roles

AWS PCS supports using service-linked roles in all of the Regions where the service
is available. For more information, see [AWS Regions and endpoints](../../../general/latest/gr/rande.md "../../../general/latest/gr/rande.md").
