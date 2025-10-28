# Using service-linked roles for Resale Authorization

with AWS Marketplace

AWS Marketplace uses AWS Identity and Access Management (IAM) [service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role"). A service-linked role is a unique type of IAM role that is
linked directly to AWS Marketplace. Service-linked roles are predefined by AWS Marketplace and
include all the permissions that the service requires to call other AWS services on your
behalf.

A service-linked role makes setting up AWS Marketplace easier because you don’t have to
manually add the necessary permissions. AWS Marketplace defines the permissions of its
service-linked roles, and unless defined otherwise, only AWS Marketplace can assume its roles.
The defined permissions include the trust policy and the permissions policy, and that
permissions policy cannot be attached to any other IAM entity.

You can delete a service-linked role only after first deleting their related resources.
This protects your AWS Marketplace resources because you can't inadvertently remove permission
to access the resources.

For information about other services that support service-linked roles, see [AWS services
that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") and look for the services that have **Yes** in the **Service-linked roles** column. Choose
a **Yes** with a link to view the service-linked role
documentation for that service.

###### Topics

- [Service-linked role permissions for AWS Marketplace](#slr-permissions "#slr-permissions")
- [Creating a service-linked role for AWS Marketplace](#create-slr "#create-slr")
- [Editing a service-linked role for AWS Marketplace](#edit-slr "#edit-slr")
- [Deleting a service-linked role for AWS Marketplace](#delete-slr "#delete-slr")
- [Supported Regions for AWS Marketplace service-linked
  roles](#slr-regions "#slr-regions")

## Service-linked role permissions for AWS Marketplace

AWS Marketplace uses the service-linked role named **AWSServiceRoleForMarketplaceResaleAuthorization**, which
enables access to AWS services and resources used or managed by AWS Marketplace for Resale
Authorizations.

The AWSServiceRoleForMarketplaceResaleAuthorization service-linked role trusts the following services to assume the
role:

- `resale-authorization.marketplace.amazonaws.com`

The role permissions policy named
**AWSMarketplaceResaleAuthorizationServiceRolePolicy** allows
AWS Marketplace to share ResaleAuthorization resources between manufacturers (ISVs) and channel partners using AWS Resource Access Manager (AWS RAM).

For details about the permissions in this policy, see [AWSMarketplaceResaleAuthorizationServiceRolePolicy](../../../aws-managed-policy/latest/reference/AWSMarketplaceResaleAuthorizationServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/AWSMarketplaceResaleAuthorizationServiceRolePolicy.md") in the _AWS Managed Policy Reference_.

For information about policy updates, see [AWS managed policy updates](security-iam-awsmanpol.md#security-iam-awsmanpol-updates "security-iam-awsmanpol.md#security-iam-awsmanpol-updates") in this guide.

You must configure permissions to allow your users, groups, or roles to create, edit, or
delete a service-linked role. For more information, see [Service-linked role permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the
_IAM User Guide_.

## Creating a service-linked role for AWS Marketplace

You don't need to manually create a service-linked role. When you choose a
service-linked role in the AWS Marketplace Management Portal, AWS Marketplace creates the service-linked role for you.

###### To create a service-linked role

1. In the [AWS Marketplace Management Portal](http://aws.amazon.com/marketplace/management/ "http://aws.amazon.com/marketplace/management/"),
   sign in to the management account and choose **Settings**.
2. In the **Settings** section, select the **Service-linked
   roles** tab.
3. On the **Service-linked roles** page, select
   **Service-linked role for Resale Authorizations** or **Resale
   Authorizations integration**, and then choose **Create service-linked
   role** or **Configure integration**.
4. On the **Service-linked role for Resale Authorizations** or
   **Create Resale Authorizations integrations** page, review the
   information and confirm by choosing **Create service-linked role** or
   **Create integration**.

A message appears on the **Service-linked roles** page, indicating
that the Resale Authorization service-linked role was successfully created.

If you delete a service-linked role, you can follow these steps to recreate it.

## Editing a service-linked role for AWS Marketplace

AWS Marketplace does not allow you to edit the AWSServiceRoleForMarketplaceResaleAuthorization service-linked role. After you
create a service-linked role, you cannot change the name of the role because various
entities might reference the role. However, you can edit the description of the role using
IAM. For more information, see [Editing a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role") in the
_IAM User Guide_.

## Deleting a service-linked role for AWS Marketplace

If you no longer need a feature or service that requires a service-linked role, we
recommend that you delete that role. That way you don’t have an unused entity that is not
actively monitored or maintained.

###### Note

If independent software vendors (ISVs) don't have the role, AWS Resource Access Manager won't
automatically share new Resale Authorizations with the targeted channel partner. If
channel partners don't have the role, AWS Resource Access Manager won't automatically accept the Resale
Authorization targeted to them.

**To manually delete the service-linked role using
IAM**

Use the IAM console, the AWS CLI, or the AWS API to delete the AWSServiceRoleForMarketplaceResaleAuthorization
service-linked role. For more information, see [Deleting a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the
_IAM User Guide_.

## Supported Regions for AWS Marketplace service-linked

roles

AWS Marketplace supports using service-linked roles in all of the Regions where the
service is available. For more information, see [AWS Regions and endpoints](../../../general/latest/gr/aws-marketplace.md#aws-marketplace_region "../../../general/latest/gr/aws-marketplace.md#aws-marketplace_region").
