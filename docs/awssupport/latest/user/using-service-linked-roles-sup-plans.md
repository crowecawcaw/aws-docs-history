# Using service-linked roles for AWS Support Plans

AWS Support Plans uses an AWS Identity and Access Management (IAM) [service-linked role](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role") to read and update AWS resources used to manage your
account's support plan on your behalf.

The `AWSServiceRoleForSupportPlans` service-linked role is a unique IAM role that is
linked directly to Support Plans. This service-linked role is predefined, and it includes the
permissions that Support Plans requires to call other AWS services on your behalf.

The `AWSServiceRoleForSupportPlans` service-linked role trusts the
`supportplans.amazonaws.com` service to assume the role.

## Service-linked role permissions for AWS Support Plans

This role uses the `AWSSupportPlansServiceRolePolicy` AWS managed policy. This managed
policy is attached to the role and allows the role permission to complete actions on
your behalf.

The role's permissions policy allows Support Plans to perform the following actions on
your behalf:

- `organizations:ListAccounts`
- `supportplans:AcceptSupportAgreement`
- `supportplans:CancelSupportAgreement`
- `supportplans:CreateSupportAgreement`
- `supportplans:GetSupportAgreement`
- `supportplans:ListSupportAgreementRevisions`
- `supportplans:ListSupportAgreements`
- `supportplans:RejectSupportAgreement`
- `supportplans:StartSupportPlanUpdate`
- `supportplans:UpdateSupportAgreement`

For more information about the allowed actions, see the [AWSSupportPlansServiceRolePolicy](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/aws-service-role/AWSSupportPlansServiceRolePolicy$jsonEditor "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/aws-service-role/AWSSupportPlansServiceRolePolicy$jsonEditor") policy in the IAM console.

## Creating a service-linked role for AWS Support Plans

You don't need to manually create the `AWSServiceRoleForSupportPlans` role. When you
create a support plan through the Support Plan Management page in the AWS Management Console,
Support Plans automatically creates this role for you.

###### Note

If you need to create this role manually, you can use the IAM console, AWS CLI,
or the IAM API. For more information, see [Creating a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#create-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#create-service-linked-role") in the
_IAM User Guide_.

## Editing a service-linked role for AWS Support Plans

You can use IAM to edit the description for the
`AWSServiceRoleForSupportPlans` service-linked role. You can't edit the trust policy
or permissions policy, and you can't attach additional policies to this role. For more
information, see [Editing a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role") in the
_IAM User Guide_.

## Deleting a service-linked role for AWS Support Plans

Support Plans doesn't delete the `AWSServiceRoleForSupportPlans` service-linked role on
your behalf. If you want to delete this role, you must first cancel your active support
plan. To do this, contact Support. After Support confirms the cancellation, you can use the IAM
console, AWS CLI, or the IAM API to delete the role. For more information, see [Deleting a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the
_IAM User Guide_.
