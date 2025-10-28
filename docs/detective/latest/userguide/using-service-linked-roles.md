# Using service-linked roles for

Detective

Amazon Detective uses AWS Identity and Access Management (IAM)[service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role"). A service-linked role is a unique type of IAM role that is
linked directly to Detective. Service-linked roles are predefined by Detective and
include all the permissions that the service requires to call other AWS services on your
behalf.

A service-linked role makes setting up Detective easier because you do not have to
manually add the necessary permissions. Detective defines the permissions of its
service-linked roles, and unless defined otherwise, only Detective can assume its roles. The
defined permissions include the trust policy and the permissions policy, and that permissions
policy cannot be attached to any other IAM entity.

You can delete a service-linked role only after first deleting their related resources. This
protects your Detective resources because you cannot inadvertently remove permission to
access the resources.

For information about other services that support service-linked roles, see [AWS services that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") and look for the services that have **Yes** in the **Service-Linked Role** column.
Choose a **Yes** with a link to view the service-linked role
documentation for that service.

## Service-linked role permissions for Detective

Detective uses the service-linked role named **AWSServiceRoleForDetective** –
Allows Detective to access AWS Organizations information on your behalf.

The AWSServiceRoleForDetective service-linked role trusts the following services to assume the
role:

- `detective.amazonaws.com`

The AWSServiceRoleForDetective service-linked role uses the managed policy [AmazonDetectiveServiceLinkedRolePolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-amazondetectiveservicelinkedrolepolicy "security-iam-awsmanpol.md#security-iam-awsmanpol-amazondetectiveservicelinkedrolepolicy").

For details about updates to the `AmazonDetectiveServiceLinkedRolePolicy`
policy see [Amazon Detective updates to AWS managed policies](security-iam-awsmanpol.md#security-iam-awsmanpol-updates "security-iam-awsmanpol.md#security-iam-awsmanpol-updates"). For automatic alerts about changes to
this policy, subscribe to the RSS feed on the [Detective document history](doc-history.md "doc-history.md")
page.

You must configure permissions to allow an IAM entity (such as a user, group, or role)
to create, edit, or delete a service-linked role. For more information, see [Service-linked role permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the
_IAM User Guide_.

## Creating a service-linked role for Detective

You do not need to manually create a service-linked role. When you
designate the Detective administrator account for an organization in the AWS Management Console, the AWS CLI, or the AWS API, Detective creates
the service-linked role for you.

If you delete this service-linked role, and then need to create it again, you can use the
same process to recreate the role in your account. When you designate the Detective administrator account for an organization,
Detective creates the service-linked role for you again.

## Editing a service-linked role for Detective

Detective does not allow you to edit the AWSServiceRoleForDetective service-linked role. After you
create a service-linked role, you cannot change the name of the role because various entities
might reference the role. However, you can edit the description of the role using IAM. For
more information, see [Editing
a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role") in the _IAM User Guide_.

## Deleting a service-linked role for Detective

If you no longer need to use a feature or service that requires a service-linked role, we
recommend that you delete that role. That way you don’t have an unused entity that is not
actively monitored or maintained. However, you must clean up the resources for your
service-linked role before you can manually delete it.

###### Note

If the Detective service is using the role when you try to delete the resources,
then the deletion might fail. If that happens, wait for a few minutes and then try the
operation again.

###### To delete Detective resources used by the AWSServiceRoleForDetective

1. Remove the Detective administrator account. See [Designating the Detective administrator for an
   organization](accounts-designate-admin.md "accounts-designate-admin.md").
2. Repeat the process in each Region where you designated the Detective administrator
   account.

**To manually delete the service-linked role using
IAM**

Use the IAM console, the AWS CLI, or the AWS API to delete the AWSServiceRoleForDetective
service-linked role. For more information, see [Deleting a
Service-Linked Role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the _IAM User Guide_.

## Supported Regions for Detective service-linked roles

Detective supports using service-linked roles in all of the Regions where the service
is available. For more information, see [AWS Regions and Endpoints](../../../general/latest/gr/rande.md "../../../general/latest/gr/rande.md").
