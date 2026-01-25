# AWS managed policies for Elastic Load Balancing

An AWS managed policy is a standalone policy that is created and administered by AWS. AWS managed policies are designed
to provide permissions for many common use cases so that you can start assigning permissions to users, groups, and roles.

Keep in mind that AWS managed policies might not grant least-privilege permissions for your specific use cases because
they're available for all AWS customers to use. We recommend that you reduce permissions further by defining
[customer managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#customer-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#customer-managed-policies") that are specific to your use cases.

You cannot change the permissions defined in AWS managed policies. If AWS updates the permissions defined in an AWS
managed policy, the update affects all principal identities (users, groups, and roles) that the policy is attached to. AWS is
most likely to update an AWS managed policy when a new AWS service is launched or new API operations become available for
existing services.

For more information, see [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") in the
_IAM User Guide_.

## AWS managed

policy: AWSElasticLoadBalancingClassicServiceRolePolicy

This policy includes all the permissions that Elastic Load Balancing (Classic Load Balancer)
requires to call other AWS services on your behalf. Service-linked roles are
predefined. With predefined roles you don't have to manually add the necessary
permissions for Elastic Load Balancing to complete actions on your behalf. You cannot attach, detach,
modify, or delete this policy.

To view the permissions for this policy, see [AWSElasticLoadBalancingClassicServiceRolePolicy](../../../aws-managed-policy/latest/reference/AWSElasticLoadBalancingClassicServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/AWSElasticLoadBalancingClassicServiceRolePolicy.md") in the _AWS Managed Policy Reference_.

## AWS managed policy:

AWSElasticLoadBalancingServiceRolePolicy

This policy includes all the permissions that Elastic Load Balancing requires to call other AWS
services on your behalf. Service-linked roles are predefined. With predefined roles
you don't have to manually add the necessary permissions for Elastic Load Balancing to complete
actions on your behalf. You cannot attach, detach, modify, or delete this policy.

To view the permissions for this policy, see [AWSElasticLoadBalancingServiceRolePolicy](../../../aws-managed-policy/latest/reference/AWSElasticLoadBalancingServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/AWSElasticLoadBalancingServiceRolePolicy.md") in the _AWS Managed Policy Reference_.

## AWS managed policy:

ElasticLoadBalancingFullAccess

This policy gives full access to the Elastic Load Balancing service and limited access to other
services via the AWS Management Console.

To view the permissions for this policy, see [ElasticLoadBalancingFullAccess](../../../aws-managed-policy/latest/reference/ElasticLoadBalancingFullAccess.md "../../../aws-managed-policy/latest/reference/ElasticLoadBalancingFullAccess.md") in the _AWS Managed Policy Reference_.

## AWS managed policy:

ElasticLoadBalancingReadOnly

This policy provides read-only access to Elastic Load Balancing and dependent services.

To view the permissions for this policy, see [ElasticLoadBalancingReadOnly](../../../aws-managed-policy/latest/reference/ElasticLoadBalancingReadOnly.md "../../../aws-managed-policy/latest/reference/ElasticLoadBalancingReadOnly.md") in the _AWS Managed Policy Reference_.

## Elastic Load Balancing updates to AWS managed policies

View details about updates to AWS managed policies for Elastic Load Balancing since this service
began tracking these changes.

| Change                                                                                                                                                              | Description                                                                                                                                                                                             | Date               |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| [AWSElasticLoadBalancingServiceRolePolicy](#AWSElasticLoadBalancingServiceRolePolicy "#AWSElasticLoadBalancingServiceRolePolicy") -<br>Update to an existing policy | Added the `ec2:AllocateIpamPoolCidr` action to grant<br>permissions to allocate CIDR blocks from IPAM pools.                                                                                            | February 17, 2025  |
| [ElasticLoadBalancingFullAccess](#ElasticLoadBalancingFullAccess "#ElasticLoadBalancingFullAccess") -<br>Update to an existing policy                               | Added the `arc-zonal-shift:*` actions to grant<br>permissions required for zonal shift.                                                                                                                 | November 28, 2023  |
| [ElasticLoadBalancingReadOnly](#ElasticLoadBalancingReadOnly "#ElasticLoadBalancingReadOnly") -<br>Update to an existing policy                                     | Added the following actions to grant permissions required for<br>zonal shift: `arc-zonal-shift:GetManagedResource`,<br>`arc-zonal-shift:ListManagedResources` and<br>`arc-zonal-shift:ListZonalShifts`. | November 28, 2023  |
| [AWSElasticLoadBalancingServiceRolePolicy](#AWSElasticLoadBalancingServiceRolePolicy "#AWSElasticLoadBalancingServiceRolePolicy") -<br>Update to an existing policy | Added the `ec2:DescribeVpcPeeringConnections` action<br>to grant permissions required for peering connections.                                                                                          | October 11, 2021   |
| [ElasticLoadBalancingFullAccess](#ElasticLoadBalancingFullAccess "#ElasticLoadBalancingFullAccess") -<br>Update to an existing policy                               | Added the `ec2:DescribeVpcPeeringConnections` action<br>to grant permissions required for peering connections.                                                                                          | October 11, 2021   |
| [ElasticLoadBalancingFullAccess](#ElasticLoadBalancingFullAccess "#ElasticLoadBalancingFullAccess") -<br>New policy                                                 | Provides full access to Elastic Load Balancing and dependent services.                                                                                                                                  | September 20, 2018 |
| [ElasticLoadBalancingReadOnly](#ElasticLoadBalancingReadOnly "#ElasticLoadBalancingReadOnly") -<br>New policy                                                       | Provides read-only access to Elastic Load Balancing and dependent services.                                                                                                                             | September 20, 2018 |
| Elastic Load Balancing started tracking changes                                                                                                                     | Elastic Load Balancing started tracking changes for its AWS managed policies.                                                                                                                           | September 20, 2018 |
