# Service-linked roles for Cost

Optimization Hub

Cost Optimization Hub uses AWS Identity and Access Management (IAM) [service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role"). A service-linked role is a unique type of IAM
role that is linked directly to Cost Optimization Hub. Service-linked roles are
predefined by Cost Optimization Hub and include all the permissions that the service
requires to call other AWS services on your behalf.

A service-linked role makes setting up Cost Optimization Hub easier because you
don’t have to manually add the necessary permissions. Cost Optimization Hub defines
the permissions of its service-linked roles, and unless defined otherwise, only Cost
Optimization Hub can assume its roles. The defined permissions include the trust
policy and the permissions policy, and that permissions policy cannot be attached to
any other IAM entity.

For information about other services that support service-linked roles, see [AWS services that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") and look for the services that have
**Yes** in the **Service-Linked
Role** column. Choose a **Yes** with a
link to view the service-linked role documentation for that service.

## Service-linked role

permissions for Cost Optimization Hub

Cost Optimization Hub uses the service-linked role named
`AWSServiceRoleForCostOptimizationHub`, which enables access to
AWS services and resources used or managed by Cost Optimization Hub.

The `AWSServiceRoleForCostOptimizationHub` service-linked role
trusts the `cost-optimization-hub.bcm.amazonaws.com` service to
assume the role.

The role permissions policy,
`CostOptimizationHubServiceRolePolicy`, allows Cost Optimization Hub
to complete the following actions on the specified resources:

- organizations:DescribeOrganization
- organizations:ListAccounts
- organizations:ListAWSServiceAccessForOrganization
- organizations:ListParents
- organizations:DescribeOrganizationalUnit
- organizations:ListDelegatedAdministrators
- ce:ListCostAllocationTags
- ce:GetCostAndUsage
- ce:GetDimensionValues

For more information, see [Allows Cost Optimization Hub to call services required
to make the service work](billing-permissions-ref.md#cost-optimization-hub-managedIAM "billing-permissions-ref.md#cost-optimization-hub-managedIAM").

To view the full permissions details of the service-linked role
`CostOptimizationHubServiceRolePolicy`, see [CostOptimizationHubServiceRolePolicy](../../../aws-managed-policy/latest/reference/CostOptimizationHubServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/CostOptimizationHubServiceRolePolicy.md") in the
_AWS Managed Policy Reference
Guide_.

You must configure permissions to allow an IAM entity (such as a user, group,
or role) to create, edit, or delete a service-linked role. For more information,
see [Service-linked role permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the _IAM
User Guide_.

## Creating the Cost

Optimization Hub service-linked role

You don't need to manually create a service-linked role. When you enable Cost
Optimization Hub, the service automatically creates the service-linked role for
you. You can enable Cost Optimization Hub through the AWS Cost Management console, or via the
API or AWS CLI. For more information, see Enable Cost Optimization Hub in this
user guide.

If you delete this service-linked role, and then need to create it again, you
can use the same process to recreate the role in your account.

## Editing the Cost Optimization

Hub service-linked role

You can't edit the name or permissions of the
`AWSServiceRoleForCostOptimizationHub` service-linked role
because various entities might reference the role. However, you can edit the
description of the role using IAM. For more information, see [Editing a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role") in the IAM User Guide.

**To allow an IAM entity to edit the description of the
`AWSServiceRoleForCostOptimizationHub` service-linked
role**

Add the following statement to the permissions policy for the IAM entity that
needs to edit the description of a service-linked role.

```
{
    "Effect": "Allow",
    "Action": [
        "iam:UpdateRoleDescription"
    ],
    "Resource": "arn:aws:iam::*:role/aws-service-role/cost-optimization-hub.bcm.amazonaws.com/AWSServiceRoleForCostOptimizationHub",
    "Condition": {"StringLike": {"iam:AWSServiceName": "cost-optimization-hub.bcm.amazonaws.com"}}
}
```

## Deleting the Cost

Optimization Hub service-linked role

If you no longer need to use Cost Optimization Hub, we recommend that you
delete the `AWSServiceRoleForCostOptimizationHub` service-linked
role. That way, you don't have an unused entity that isn't actively monitored or
maintained. However, before you can manually delete the service-linked role, you
must opt out of Cost Optimization Hub.

**To opt out of Cost Optimization Hub**

For information about opting out of Cost Optimization Hub, see [Opting out of Cost Optimization Hub](coh-getting-started.md#coh-opt-out "coh-getting-started.md#coh-opt-out").

**To manually delete the service-linked role using
IAM**

Use the IAM console, the AWS Command Line Interface (AWS CLI), or the
AWS API to delete the `AWSServiceRoleForCostOptimizationHub`
service-linked role. For more information, see [Deleting a Service-Linked Role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the _IAM
User Guide_.

## Supported Regions for Cost

Optimization Hub service-linked roles

Cost Optimization Hub supports using service-linked roles in all of the AWS
Regions where the service is available. For more information, see AWS service
endpoints.
