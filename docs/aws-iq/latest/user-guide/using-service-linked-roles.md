End of support notice: On May 28, 2026, AWS
will end support for AWS IQ. After May 28, 2026, you will
no longer be able to access the AWS IQ console or AWS IQ resources.
For more information, see [AWS IQ end of support](../experts-user-guide/aws-iq-end-of-support.md "../experts-user-guide/aws-iq-end-of-support.md") in the _AWS IQ User Guide for Experts_.

# Using service-linked roles in AWS IQ

AWS IQ uses AWS Identity and Access Management (IAM) [service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role"). A service-linked role is a unique type of IAM role that is
linked directly to AWS IQ. Service-linked roles are predefined by AWS IQ and include all the
permissions that the service requires to call other AWS services on your behalf.

For information about other services that support service-linked roles, see [AWS services that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") and look for the services that have
**Yes** in the **Service-linked roles** column. Choose
**Yes** with a link to view the service-linked role documentation for that
service.

###### Topics

- [AWSServiceRoleForAWSIQPermission](#first-concept-chapter "#first-concept-chapter")
- [AWSServiceRoleForAWSIQContract](#second-concept-chapter "#second-concept-chapter")
- [Creating a service-linked role for AWS
  IQ](#creating-a-service-linked-role-iq "#creating-a-service-linked-role-iq")
- [Editing a service-linked role for AWS
  IQ](#editing-a-service-linked-role-iq "#editing-a-service-linked-role-iq")
- [Deleting a service-linked role for AWS
  IQ](#deleting-a-service-linked-role-iq "#deleting-a-service-linked-role-iq")
- [Supported Regions for AWS IQ
  service-linked roles](#supported-regions-for-service-linked-roles-iq "#supported-regions-for-service-linked-roles-iq")

## `AWSServiceRoleForAWSIQPermission`

AWS IQ uses the service-linked role named `AWSServiceRoleForAWSIQPermission`.
This role provides AWS IQ permissions to control the life cycle of permissions requests that
you grant to AWS IQ experts.

The `AWSServiceRoleForAWSIQPermission` service-linked role trusts the following
services to assume the role: `permission.iq.amazonaws.com`

The role permissions policy, `AWSIQPermissionServiceRolePolicy`, allows AWS IQ
to complete the following actions on the specified resources:

- Action: `iam:DeleteRole`, `iam:ListAttachedRolePolicies`,`iam:AttachRolePolicy`, `iam:DetachRolePolicy` on
  `AWSIQPermission-*`

###### Note

The policy includes the condition key `{ "ArnEquals": { "iam:PolicyARN":
 "arn:aws:iam::aws:policy/AWSDenyAll" }`, which means that the service can only attach the
`AWSDenyAll` policy.

## `AWSServiceRoleForAWSIQContract`

AWS IQ uses the service-linked role named `AWSServiceRoleForAWSIQContract`.
This role provides AWS IQ permissions to execute approved AWS IQ payment requests on your
behalf. The `AWSServiceRoleForAWSIQContract` service-linked role trusts the following
services to assume the role: `contract.iq.amazonaws.com`.

The role permissions policy named `AWSIQContractServiceRolePolicy` allows AWS
IQ to complete the following actions on the specified resources:

- Action: `aws-marketplace:Subscribe` on `*`

You must configure permissions to allow an IAM entity such as a user, group, or role to
create, edit, or delete a service-linked role. For more information, see [Service-linked role permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions").

## Creating a service-linked role for AWS

IQ

In AWS IQ, AWS Marketplace creates the service-linked role for you when you set up integration with
AWS License Manager. For more information, see [Creating a service-linked role for AWS Marketplace](../../../marketplace/latest/buyerguide/buyer-using-service-linked-roles-license-manager.md#buyer-creating-service-linked-role "../../../marketplace/latest/buyerguide/buyer-using-service-linked-roles-license-manager.md#buyer-creating-service-linked-role").

## Editing a service-linked role for AWS

IQ

In AWS IQ, AWS Marketplace doesn't allow you to edit the service-linked role. For more information,
see [Editing a service-linked role for AWS Marketplace](../../../marketplace/latest/buyerguide/buyer-using-service-linked-roles-license-manager.md#buyer-editing-service-linked-role "../../../marketplace/latest/buyerguide/buyer-using-service-linked-roles-license-manager.md#buyer-editing-service-linked-role").

## Deleting a service-linked role for AWS

IQ

If you don't need to use a feature or service that requires a service-linked role, we
recommend deleting that role. For more information, see [Deleting a service-linked role for AWS Marketplace](../../../marketplace/latest/buyerguide/buyer-using-service-linked-roles-license-manager.md#buyer-delete-service-linked-role "../../../marketplace/latest/buyerguide/buyer-using-service-linked-roles-license-manager.md#buyer-delete-service-linked-role").

## Supported Regions for AWS IQ

service-linked roles

AWS IQ, through AWS Marketplace, supports using service-linked roles in all of the AWS Regions
where service is available. For more information, see [AWS Marketplace Regions and Endpoints](../../../general/latest/gr/aws-marketplace.md#aws-marketplace_region "../../../general/latest/gr/aws-marketplace.md#aws-marketplace_region").
