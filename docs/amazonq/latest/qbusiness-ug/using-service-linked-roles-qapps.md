# Using service-linked roles for

Amazon Q Apps

Amazon Q Apps uses AWS Identity and Access Management (IAM)[service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role"). A service-linked role is a unique type of IAM role that
is linked directly to Amazon Q Apps. Service-linked roles are predefined by Amazon Q Apps and
include all the permissions that the service requires to performs Q Apps related
administrative actions to other AWS services on your behalf.

A service-linked role makes setting up Amazon Q Apps easier because you don’t have to
manually add the necessary permissions. Amazon Q Apps defines the permissions of its
service-linked roles, and unless defined otherwise, only Amazon Q Apps can assume its roles.
The defined permissions include the trust policy and the permissions policy, and that
permissions policy cannot be attached to any other IAM entity.

You can delete a service-linked role only after first deleting their related resources.
This protects your Amazon Q Apps resources because you can't inadvertently remove permission
to access the resources.

For information about other services that support service-linked roles, see [AWS services that
work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") and look for the services that have **Yes** in the **Service-linked roles** column.
Choose a **Yes** with a link to view the service-linked role
documentation for that service.

## Service-linked role permissions for

Amazon Q Apps

Amazon Q Apps uses one service-linked role named
`AWSServiceRoleForAmazonQApps` that performs Q Apps related
administrative actions in your account. Examples of these actions include allowing CloudWatch
to publish metrics to your AWS account.

The `AWSServiceRoleForAmazonQApps` service-linked role trusts the
following services to assume the role:

- qapps.amazonaws.com

The `AWSServiceRoleForAmazonQApps` service-linked role uses the managed
policy `QAppsServiceRolePolicy`.

The content of this policy and any updates to it are described in [AWS managed policies for Amazon Q Apps](security-iam-awsmanpol-qapps.md "security-iam-awsmanpol-qapps.md").

You must configure permissions to allow an IAM entity (such as a user, group, or
role) to create, edit, or delete a service-linked role. For more information, see [Service-Linked Role Permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the IAM User Guide.

## Creating a service-linked role for Amazon Q Apps

You don't need to manually create a service-linked role. When you [create an
Amazon Q Business application](../business-use-dg/create-app.md "../business-use-dg/create-app.md") in the AWS Management Console, the AWS CLI, or the
AWS API, Amazon Q Apps creates the service-linked role for you.

If you delete this service-linked role, and then need to create it again, you can use
the same process to recreate the role in your account. When you create a new
application, Amazon Q Apps creates the service-linked role for you again.

## Editing a service-linked role for Amazon Q Apps

Amazon Q Apps does not allow you to edit service-linked roles. After you create a
service-linked role, you cannot change the name of the role because various entities
might reference the role. However, you can edit the description of the role using IAM.
For more information, see [Editing
a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role") in the _IAM User Guide_.

## Deleting a service-linked role for Amazon Q Apps

You can manually delete your `AWSServiceRoleForQApps` role. If you no
longer need to use a feature or service that requires a service-linked role, we
recommend that you delete that role. That way you don’t have an unused entity that is
not actively monitored or maintained. However, you must delete your Q application or
turn on QApps on all existing Q applications before you can manually delete the
service-linked role associated with it.

###### Note

If the Amazon Q Apps service is using the role when you try to delete the resources,
then the deletion might fail. If that happens, wait for a few minutes and try the
operation again.

**To manually delete the service-linked role using
IAM**

Use the IAM console, the IAM CLI, or the IAM API to delete the
`AWSServiceRoleForQApps` service-linked role. For more information, see
[Deleting a Service-Linked Role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the
_IAM User Guide_.

## Supported regions for Amazon Q Apps service-linked

roles

Amazon Q Apps supports using service-linked roles in all of the regions where the
service is available. For more information, see [Amazon Q Business
endpoints and quotas](../../../general/latest/gr/amazonq.md "../../../general/latest/gr/amazonq.md").
