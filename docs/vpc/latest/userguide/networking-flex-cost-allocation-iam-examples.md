

# Networking Flexible Cost Allocation policy examples

The following example IAM policies grant permissions for Networking Flexible Cost Allocation (FCA). To grant a user permission to work with FCA, attach a policy to an IAM role or user. For more information, see [Identity and access management for Amazon VPC](security-iam.md).

## Read-only access
<a name="networking-flex-cost-allocation-iam-examples-readonly"></a>

The following example policy grants read-only access to FCA policies, policy versions, and associations.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ec2:DescribeNetworkingFlexCostAllocationPolicies",
        "ec2:GetNetworkingFlexCostAllocationPolicyVersions",
        "ec2:DescribeNetworkingFlexCostAllocationPolicyAssociations"
      ],
      "Resource": "*"
    }
  ]
}
```

## Full access
<a name="networking-flex-cost-allocation-iam-examples-full"></a>

The following example policy grants full access to FCA policies and associations.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ec2:CreateNetworkingFlexCostAllocationPolicy",
        "ec2:ModifyNetworkingFlexCostAllocationPolicy",
        "ec2:DeleteNetworkingFlexCostAllocationPolicies",
        "ec2:AssociateNetworkingFlexCostAllocationPolicy",
        "ec2:DisassociateNetworkingFlexCostAllocationPolicy",
        "ec2:DescribeNetworkingFlexCostAllocationPolicies",
        "ec2:GetNetworkingFlexCostAllocationPolicyVersions",
        "ec2:DescribeNetworkingFlexCostAllocationPolicyAssociations"
      ],
      "Resource": "*"
    },
    {
      "Effect": "Allow",
      "Action": "ec2:CreateTags",
      "Resource": "arn:aws:ec2:*:*:fca-policy/*",
      "Condition": {
        "StringEquals": {
          "ec2:CreateAction": "CreateNetworkingFlexCostAllocationPolicy"
        }
      }
    }
  ]
}
```

The `ec2:CreateTags` statement allows tagging a policy on creation with `--tag-specifications`. Without it, a create request that includes tags fails with an `UnauthorizedOperation` error.

These actions support resource-level permissions. The preceding example uses `"*"` for the `Resource` element. To restrict access to specific policies, replace `"*"` with the policy ARN, in the format `arn:aws:ec2:{{region}}:{{account-id}}:fca-policy/{{policy-id}}`.

## Permissions to associate resources
<a name="networking-flex-cost-allocation-iam-examples-associate"></a>

To associate a policy with a resource, the IAM principal also needs permission to describe that resource. The following example policy grants the describe permissions for all supported resource types. Combine these permissions with the FCA management permissions from the preceding example.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ec2:DescribeNatGateways",
        "ec2:DescribeInstances",
        "ec2:DescribeVpcPeeringConnections",
        "ec2:DescribeVpcs",
        "ec2:DescribeSubnets"
      ],
      "Resource": "*"
    }
  ]
}
```