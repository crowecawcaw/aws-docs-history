# Service-linked roles for Budgets

Budgets uses AWS Identity and Access Management (IAM) [service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role"). A service-linked role is a unique type of IAM
role that is linked directly to Budgets. Service-linked roles are predefined by
Budgets and include all the permissions that the service requires to call other
AWS services on your behalf.

Budgets defines the permissions of its service-linked roles, and unless defined
otherwise, only Budgets can assume its roles. The defined permissions include the
trust policy and the permissions policy, and that permissions policy cannot be
attached to any other IAM entity.

For information about other services that support service-linked roles, see [AWS services that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") and look for the services that have
**Yes** in the **Service-Linked
Role** column. Choose a **Yes** with a
link to view the service-linked role documentation for that service.

## Service-linked role permissions for

Budgets

Budgets uses the service-linked role named
`AWSServiceRoleForBudgets`, which enables Budgets to verify
access to billing views that are shared across account boundaries.

The purpose of this service-linked role is to verify that customers have
access to the underlying billing view data associated with a Budget when
updating the spend of a Budget.

The `AWSServiceRoleForBudgets` service-linked role trusts the
`budgets.amazonaws.com` service to assume the role.

The role permissions policy, `BudgetsServiceRolePolicy`, allows
Budgets to complete the following action on all Billing View resources that the
customer has access to:

- billing:GetBillingViewData

For more information, see [Allows Budgets to call services required to verify
billing view access](billing-permissions-ref.md#budget-managedIAM-billing-view "billing-permissions-ref.md#budget-managedIAM-billing-view").

To view the full permissions details of the service-linked role
`BudgetsServiceRolePolicy`, see [BudgetsServiceRolePolicy](../../../aws-managed-policy/latest/reference/BudgetsBillingViewAccessPolicy.md "../../../aws-managed-policy/latest/reference/BudgetsBillingViewAccessPolicy.md") in the _AWS Managed Policy Reference Guide_.

You must configure permissions to allow an IAM entity (such as a user, group,
or role) to create, edit, or delete a service-linked role. For more information,
see [Service-linked role permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the _IAM
User Guide_.

## Creating the Budgets service-linked

role

You don't need to manually create a service-linked role. When you make a
request to CreateBudget or UpdateBudget with a BillingView from another account
that you have access to, the service automatically creates the service-linked
role for you.

If you delete this service-linked role, and then need to create it again, you
can use the same process to recreate the role in your account.

## Editing the Budgets service-linked

role

You can't edit the name or permissions of the
`AWSServiceRoleForBudgets` service-linked role because various
entities might reference the role. However, you can edit the description of the
role using IAM. For more information, see [Editing a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role") in the IAM User Guide.

**To allow an IAM entity to edit the description of the
`AWSServiceRoleForBudgets` service-linked
role**

Add the following statement to the permissions policy for the IAM entity that
needs to edit the description of a service-linked role.

```
{
    "Effect": "Allow",
    "Action": [
        "iam:UpdateRoleDescription"
    ],
    "Resource": "arn:aws:iam::*:role/aws-service-role/budgets.amazonaws.com/AWSServiceRoleForBudgets",
    "Condition": {"StringLike": {"iam:AWSServiceName": "budgets.amazonaws.com"}}
}
```

## Deleting the Budgets service-linked

role

If you no longer need to use Budgets, we recommend that you delete the
`AWSServiceRoleForBudgets` service-linked role. That way, you
don't have an unused entity that isn't actively monitored or maintained.
However, before you can manually delete the service-linked role, you must delete
any Budgets in your account that are associated with a Billing View from another
account. If you try deleting the service-linked role before this is done, the
request will fail.

**To manually delete the service-linked role using
IAM**

Use the IAM console, the AWS Command Line Interface (AWS CLI), or the
AWS API to delete the `AWSServiceRoleForBudgets` service-linked
role. For more information, see [Deleting a Service-Linked Role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the _IAM
User Guide_.

## Supported Regions for Budgets

service-linked roles

Budgets supports using service-linked roles in all of the AWS Regions where
the service is available. For more information, see AWS service
endpoints.
