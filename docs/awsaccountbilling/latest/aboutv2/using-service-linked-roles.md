# Using service-linked roles for

AWS Billing

AWS Billing uses AWS Identity and Access Management (IAM) [service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role"). A service-linked role is a unique type of IAM role that is
linked directly to AWS Billing. Service-linked roles are predefined by AWS Billing and
include all the permissions that the service requires to call other AWS services on your
behalf.

A service-linked role makes setting up AWS Billing easier because you don’t have to
manually add the necessary permissions. AWS Billing defines the permissions of its
service-linked roles, and unless defined otherwise, only AWS Billing can assume its roles. The
defined permissions include the trust policy and the permissions policy, and that permissions
policy cannot be attached to any other IAM entity.

You can delete a service-linked role only after first deleting their related resources. This
protects your AWS Billing resources because you can't inadvertently remove permission to
access the resources.

For information about other services that support service-linked roles, see [AWS services that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") and look for the services that have **Yes** in the **Service-linked roles**
column. Choose a **Yes** with a link to view the service-linked
role documentation for that service.

## Service-linked role permissions for

AWS Billing

AWS Billing uses the service-linked role named **Billing** –
Allows billing service to validate access to billing view data for derived billing views.

The Billing service-linked role trusts the following services to assume the
role:

- `billing.amazonaws.com`

The role permissions policy named AWSBillingServiceRolePolicy allows AWS Billing to complete the
following actions on the specified resources:

- Action: `billing:GetBillingViewData` on
  `arn:${Partition}:billing:::billingview/*`

You must configure permissions to allow your users, groups, or roles to create, edit, or
delete a service-linked role. For more information, see [Service-linked role permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the
_IAM User Guide_.

## Creating a service-linked role for

AWS Billing

You don't need to manually create a service-linked role. When you create or associate a
billing view using a billing view from a different account in the AWS Management Console, the AWS CLI, or the
AWS API, AWS Billing creates the service-linked role for you.

###### Important

This service-linked role can appear in your account if you completed an action in
another service that uses the features supported by this role. Also, if you were using the
AWS Billing service before January 1, 2017, when it began supporting service-linked roles,
then AWS Billing created the Billing role in your account. To learn more, see [A
new role appeared in my AWS account](../../../IAM/latest/UserGuide/troubleshoot_roles.md#troubleshoot_roles_new-role-appeared "../../../IAM/latest/UserGuide/troubleshoot_roles.md#troubleshoot_roles_new-role-appeared").

## Editing a service-linked role for

AWS Billing

AWS Billing does not allow you to edit the Billing service-linked role. After you
create a service-linked role, you cannot change the name of the role because various entities
might reference the role. However, you can edit the description of the role using IAM. For
more information, see [Editing
a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role") in the _IAM User Guide_.

## Deleting a service-linked role for

AWS Billing

If you no longer need to use a feature or service that requires a service-linked role, we
recommend that you delete that role. That way you don’t have an unused entity that is not
actively monitored or maintained. However, you must clean up your service-linked role before
you can manually delete it.

### Manually delete the service-linked role

Use the IAM console, the AWS CLI, or the AWS API to delete the Billing
service-linked role. For more information, see [Deleting a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the
_IAM User Guide_.

## Supported Regions for AWS Billing service-linked roles

AWS Billing supports using service-linked roles in all of the Regions where the service
is available. For more information, see [AWS Regions and endpoints](../../../general/latest/gr/rande.md "../../../general/latest/gr/rande.md").
