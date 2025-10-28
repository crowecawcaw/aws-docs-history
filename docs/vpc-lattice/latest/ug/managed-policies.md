# AWS managed policies for Amazon VPC Lattice

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

## AWS managed policy:

VPCLatticeFullAccess

This policy provides full access to Amazon VPC Lattice and limited access to other dependent
services. It includes permissions to do the following:

- ACM – Retrieve the SSL/TLS certificate ARN for custom domain
  names.
- CloudWatch – View access logs and monitoring data.
- CloudWatch Logs – Set up and send access logs to CloudWatch Logs.
- Amazon EC2 – Configure network interfaces and retrieve information about EC2
  instances and VPCs. This is used to create resource configurations, resource
  gateways, and target groups, configure VPC Lattice entity associations,
  and register targets.
- Elastic Load Balancing – Retrieve information about an Application Load Balancer to register it as a
  target.
- Firehose – Retrieve information about delivery streams used to store access
  logs.
- Lambda – Retrieve information about a Lambda function to register it as a
  target.
- Amazon RDS – Retrieve information about RDS clusters and instances.
- Amazon S3 – Retrieve information about S3 buckets used to store access
  logs.

To view the permissions for this policy, see [VPCLatticeFullAccess](../../../aws-managed-policy/latest/reference/VPCLatticeFullAccess.md "../../../aws-managed-policy/latest/reference/VPCLatticeFullAccess.md") in the _AWS Managed Policy
Reference_.

To use other AWS services that VPC Lattice is integrated with and the entire suite of
VPC Lattice features, you must have specific additional permissions. These permissions are
not included in the `VPCLatticeFullAccess` managed policy because of the
[confused deputy](../../../IAM/latest/UserGuide/confused-deputy.md "../../../IAM/latest/UserGuide/confused-deputy.md") privilege escalation risk. For more information, see [Additional
required permissions for full access](security_iam_id-based-policies.md#security_iam_id-based-policy-additional-permissions "security_iam_id-based-policies.md#security_iam_id-based-policy-additional-permissions").

## AWS managed policy:

VPCLatticeReadOnlyAccess

This policy provides read-only access to Amazon VPC Lattice and limited access to other
dependent services. It includes permissions to do the following:

- ACM – Retrieve the SSL/TLS certificate ARN for custom domain
  names.
- CloudWatch – View access logs and monitoring data.
- CloudWatch Logs – View log delivery information for access log
  subscriptions.
- Amazon EC2 – Retrieve information about EC2 instances and VPCs to create
  target groups and register targets.
- Elastic Load Balancing – Retrieve information about an Application Load Balancer.
- Firehose – Retrieve information about delivery streams for access log
  delivery.
- Lambda – View information about a Lambda function.
- Amazon RDS – Retrieve information about RDS clusters and instances.
- Amazon S3 – Retrieve information about S3 buckets for access log
  delivery.

To view the permissions for this policy, see [VPCLatticeReadOnlyAccess](../../../aws-managed-policy/latest/reference/VPCLatticeReadOnlyAccess.md "../../../aws-managed-policy/latest/reference/VPCLatticeReadOnlyAccess.md") in the _AWS Managed Policy
Reference_.

## AWS managed policy:

VPCLatticeServicesInvokeAccess

This policy provides access to invoke Amazon VPC Lattice services.

To view the permissions for this policy, see [VPCLatticeServicesInvokeAccess](../../../aws-managed-policy/latest/reference/VPCLatticeServicesInvokeAccess.md "../../../aws-managed-policy/latest/reference/VPCLatticeServicesInvokeAccess.md") in the _AWS Managed Policy
Reference_.

## AWS managed policy:

AWSVpcLatticeServiceRolePolicy

This policy is attached to a service-linked role named **AWSServiceRoleForVpcLattice** to allow VPC Lattice to perform actions on your
behalf. You can't attach this policy to your IAM entities. For more information, see
[Using service-linked roles for Amazon VPC Lattice](using-service-linked-roles.md "using-service-linked-roles.md").

To view the permissions for this policy, see [AWSVpcLatticeServiceRolePolicy](../../../aws-managed-policy/latest/reference/AWSVpcLatticeServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/AWSVpcLatticeServiceRolePolicy.md") in the _AWS Managed Policy
Reference_.

## VPC Lattice updates to AWS managed policies

View details about updates to AWS managed policies for VPC Lattice since this service
began tracking these changes. For automatic alerts about changes to this page, subscribe
to the RSS feed for the VPC Lattice User Guide.

| Change                                                                                                                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Date             |
| ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| [VPCLatticeFullAccess](#vpc-lattice-fullaccess-policy "#vpc-lattice-fullaccess-policy")                                   | VPC Lattice adds read-only permissions to describe Amazon RDS clusters and instances.                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | December 1, 2024 |
| [VPCLatticeReadOnlyAccess](#vpc-lattice-read-onlyaccess-policy "#vpc-lattice-read-onlyaccess-policy")                     | VPC Lattice adds read-only permissions to describe Amazon RDS clusters and instances.                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | December 1, 2024 |
| [AWSVpcLatticeServiceRolePolicy](#service-linked-role-policy "#service-linked-role-policy")                               | VPC Lattice adds permissions to allow VPC Lattice to create a requester-managed network interface.                                                                                                                                                                                                                                                                                                                                                                                                                                                      | December 1, 2024 |
| [VPCLatticeFullAccess](#vpc-lattice-fullaccess-policy "#vpc-lattice-fullaccess-policy")                                   | VPC Lattice adds a new policy to grant permissions for full access to Amazon VPC Lattice and limited access to other dependent services.                                                                                                                                                                                                                                                                                                                                                                                                                | March 31, 2023   |
| [VPCLatticeReadOnlyAccess](#vpc-lattice-read-onlyaccess-policy "#vpc-lattice-read-onlyaccess-policy")                     | VPC Lattice adds a new policy to grant permissions for read-only access to Amazon VPC Lattice and limited access to other dependent services.                                                                                                                                                                                                                                                                                                                                                                                                           | March 31, 2023   |
| [VPCLatticeServicesInvokeAccess](#vpc-lattice-services-invoke-access-policy "#vpc-lattice-services-invoke-access-policy") | VPC Lattice adds a new policy to grant access to invoke Amazon VPC Lattice services.                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | March 31, 2023   |
| [AWSVpcLatticeServiceRolePolicy](#service-linked-role-policy "#service-linked-role-policy")                               | VPC Lattice adds permissions to its service-linked role to allow VPC Lattice to publish CloudWatch metrics in the `AWS/VpcLattice` namespace. The `AWSVpcLatticeServiceRolePolicy` policy includes permission to call the CloudWatch [PutMetricData](../../../AmazonCloudWatch/latest/APIReference/API_PutMetricData.md "../../../AmazonCloudWatch/latest/APIReference/API_PutMetricData.md") API action. For more information, see [Using service-linked roles for Amazon VPC Lattice](using-service-linked-roles.md "using-service-linked-roles.md"). | December 5, 2022 |
| VPC Lattice started tracking changes                                                                                      | VPC Lattice started tracking changes for its AWS managed policies.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | December 5, 2022 |
