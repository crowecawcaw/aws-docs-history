# Amazon VPC Lattice API permissions

You must grant IAM identities (such as users or roles) permission to call the
VPC Lattice API actions they need, as described in [Policy actions
for VPC Lattice](security_iam_service-with-iam.md#security_iam_service-with-iam-id-based-policies-actions "security_iam_service-with-iam.md#security_iam_service-with-iam-id-based-policies-actions"). In addition,
for some VPC Lattice actions, you must grant IAM identities permission to call specific
actions from other AWS APIs.

## Required permissions for the API

When calling the following actions from the API, you must grant IAM users
permission to call the specified actions.

`CreateResourceConfiguration`

- `vpc-lattice:CreateResourceConfiguration`
- `ec2:DescribeSubnets`
- `rds:DescribeDBInstances`
- `rds:DescribeDBClusters`

`CreateResourceGateway`

- `vpc-lattice:CreateResourceGateway`
- `ec2:AssignPrivateIpAddresses`
- `ec2:AssignIpv6Addresses`
- `ec2:CreateNetworkInterface`
- `ec2:CreateNetworkInterfacePermission`
- `ec2:DeleteNetworkInterface`
- `ec2:DescribeNetworkInterfaces`
- `ec2:DescribeSecurityGroups`
- `ec2:DescribeSubnets`

`DeleteResourceGateway`

- `vpc-lattice:DeleteResourceGateway`
- `ec2:DeleteNetworkInterface`

`UpdateResourceGateway`

- `vpc-lattice:UpdateResourceGateway`
- `ec2:AssignPrivateIpAddresses`
- `ec2:AssignIpv6Addresses`
- `ec2:UnassignPrivateIpAddresses`
- `ec2:CreateNetworkInterface`
- `ec2:CreateNetworkInterfacePermission`
- `ec2:DeleteNetworkInterface`
- `ec2:DescribeNetworkInterfaces`
- `ec2:DescribeSecurityGroups`
- `ec2:DescribeSubnets`
- `ec2:ModifyNetworkInterfaceAttribute`

`CreateServiceNetworkResourceAssociation`

- `vpc-lattice:CreateServiceNetworkResourceAssociation`
- `ec2:AssignIpv6Addresses`
- `ec2:CreateNetworkInterface`
- `ec2:CreateNetworkInterfacePermission`
- `ec2:DescribeNetworkInterfaces`

`CreateServiceNetworkVpcAssociation`

- `vpc-lattice:CreateServiceNetworkVpcAssociation`
- `ec2:DescribeVpcs`
- `ec2:DescribeSecurityGroups` (Only needed when security groups are provided)

`UpdateServiceNetworkVpcAssociation`

- `vpc-lattice:UpdateServiceNetworkVpcAssociation`
- `ec2:DescribeSecurityGroups` (Only needed when security groups are provided)

`CreateTargetGroup`

- `vpc-lattice:CreateTargetGroup`
- `ec2:DescribeVpcs`

`RegisterTargets`

- `vpc-lattice:RegisterTargets`
- `ec2:DescribeInstances` (Only needed when `INSTANCE` is the target group type)
- `ec2:DescribeVpcs` (Only needed when `INSTANCE` or `IP` is the target group type)
- `ec2:DescribeSubnets` (Only needed when `INSTANCE` or `IP` is the target group type)
- `lambda:GetFunction` (Only needed when `LAMBDA` is the target group type)
- `lambda:AddPermission` (Only needed if the target group doesn't already have permission to invoke the specified Lambda
  function)

`DeregisterTargets`

- `vpc-lattice:DeregisterTargets`

`CreateAccessLogSubscription`

- `vpc-lattice:CreateAccessLogSubscription`
- `logs:GetLogDelivery`
- `logs:CreateLogDelivery`

`DeleteAccessLogSubscription`

- `vpc-lattice:DeleteAccessLogSubscription`
- `logs:DeleteLogDelivery`

`UpdateAccessLogSubscription`

- `vpc-lattice:UpdateAccessLogSubscription`
- `logs:UpdateLogDelivery`
