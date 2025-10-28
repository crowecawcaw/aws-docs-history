# Service-linked roles for split cost

allocation data

Split cost allocation data uses AWS Identity and Access Management (IAM) [service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role"). A service-linked role is a unique type of IAM
role that is linked directly to split cost allocation data. Service-linked roles are
predefined by split cost allocation data and include all the permissions that the
service requires to call other AWS services on your behalf.

A service-linked role makes setting up split cost allocation data easier because
you don’t have to manually add the necessary permissions. Split cost allocation data
defines the permissions of its service-linked roles, and unless defined otherwise,
only split cost allocation data can assume its roles. The defined permissions
include the trust policy and the permissions policy, and that permissions policy
cannot be attached to any other IAM entity.

For information about other services that support service-linked roles, see [AWS services that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") and look for the services that have
**Yes** in the **Service-Linked
Role** column. Choose a **Yes** with a
link to view the service-linked role documentation for that service.

## Service-linked role permissions for split

cost allocation data

Split cost allocation data uses the service-linked role named
`AWSServiceRoleForSplitCostAllocationData`,
which enables access to AWS services and resources used or managed by split
cost allocation data.

The `AWSServiceRoleForSplitCostAllocationData`
service-linked role trusts the
`split-cost-allocation-data.bcm.amazonaws.com` service to assume
the role.

The role permissions policy,
`SplitCostAllocationDataServiceRolePolicy`,
allows split cost allocation data to complete the following actions on the
specified resources:

- organizations:DescribeOrganization
- organizations:ListAccounts
- organizations:ListAWSServiceAccessForOrganization
- organizations:ListParents
- aps:ListWorkspaces
- aps:QueryMetrics

For more information, see [Allows split cost allocation data to call services
required to make the service work](billing-permissions-ref.md#split-cost-allocation-data-managedIAM "billing-permissions-ref.md#split-cost-allocation-data-managedIAM").

To view the full permissions details of the service-linked role
`SplitCostAllocationDataServiceRolePolicy`,
see [`SplitCostAllocationDataServiceRolePolicy`](../../../aws-managed-policy/latest/reference/CostOptimizationHubServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/CostOptimizationHubServiceRolePolicy.md")
in the _AWS Managed Policy Reference
Guide_.

You must configure permissions to allow an IAM entity (such as a user, group,
or role) to create, edit, or delete a service-linked role. For more information,
see [Service-linked role permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the IAM User Guide.

## Creating the split cost allocation data

service-linked role

You don't need to manually create a service-linked role. When you opt in to
split cost allocation data, the service automatically creates the service-linked
role for you. You can enable split cost allocation data through the AWS Cost Management
console. For more information, see [Enabling split cost allocation data](../../../cur/latest/userguide/enabling-split-cost-allocation-data.md "../../../cur/latest/userguide/enabling-split-cost-allocation-data.md").

If you delete this service-linked role, and then need to create it again, you
can use the same process to recreate the role in your account.

## Editing the split cost allocation data

service-linked role

You can't edit the name or permissions of the
`AWSServiceRoleForSplitCostAllocationData`
service-linked role because various entities might reference the role. However,
you can edit the description of the role using IAM. For more information, see
[Editing a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role") in the IAM User Guide.

**To allow an IAM entity to edit the description of the
`AWSServiceRoleForSplitCostAllocationData`
service-linked role**

Add the following statement to the permissions policy for the IAM entity that
needs to edit the description of a service-linked role.

```
{
    "Effect": "Allow",
    "Action": [
        "iam:UpdateRoleDescription"
    ],
    "Resource": "arn:aws:iam::*:role/aws-service-role/split-cost-allocation-data.bcm.amazonaws.com/AWSServiceRoleForSplitCostAllocationData",
    "Condition": {"StringLike": {"iam:AWSServiceName": "split-cost-allocation-data.bcm.amazonaws.com"}}
}
```

## Deleting the split cost allocation data

service-linked role

If you no longer need to use split cost allocation data, we recommend that you
delete the `AWSServiceRoleForSplitCostAllocationData`
service-linked role. That way, you don't have an unused entity that isn't
actively monitored or maintained. However, before you can manually delete the
service-linked role, you must opt out of split cost allocation data.

**To opt out of split cost allocation data**

For information about opting out of split cost allocation data, see [Enabling split cost allocation data](../../../cur/latest/userguide/enabling-split-cost-allocation-data.md "../../../cur/latest/userguide/enabling-split-cost-allocation-data.md").

**To manually delete the service-linked role using
IAM**

Use the IAM console, the AWS Command Line Interface (AWS CLI), or the
AWS API to delete the
`AWSServiceRoleForSplitCostAllocationData`
service-linked role. For more information, see [Deleting a Service-Linked Role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the _IAM
User Guide_.

## Supported Regions for split cost allocation

data service-linked roles

Split cost allocation data supports using service-linked roles in all of the
AWS Regions where split cost allocation data is available. For more
information, see AWS service endpoints.
