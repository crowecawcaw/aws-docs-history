

# AmazonECSInfrastructureRolePolicyForVpcLattice
<a name="AmazonECSInfrastructureRolePolicyForVpcLattice"></a>

**Description**: Provides access to other AWS service resources required to manage VPC Lattice feature in ECS workloads on your behalf.

`AmazonECSInfrastructureRolePolicyForVpcLattice` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AmazonECSInfrastructureRolePolicyForVpcLattice-how-to-use"></a>

You can attach `AmazonECSInfrastructureRolePolicyForVpcLattice` to your users, groups, and roles.

## Policy details
<a name="AmazonECSInfrastructureRolePolicyForVpcLattice-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: November 15, 2024, 20:02 UTC 
+ **Edited time:** November 15, 2024, 20:02 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AmazonECSInfrastructureRolePolicyForVpcLattice`

## Policy version
<a name="AmazonECSInfrastructureRolePolicyForVpcLattice-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AmazonECSInfrastructureRolePolicyForVpcLattice-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Sid" : "ManagedVpcLatticeTargetRegistration",
      "Effect" : "Allow",
      "Action" : [
        "vpc-lattice:RegisterTargets",
        "vpc-lattice:DeregisterTargets"
      ],
      "Resource" : [
        "arn:aws:vpc-lattice:*:*:targetgroup/*"
      ]
    },
    {
      "Sid" : "DescribeVpcLatticeTargetGroup",
      "Effect" : "Allow",
      "Action" : "vpc-lattice:GetTargetGroup",
      "Resource" : [
        "arn:aws:vpc-lattice:*:*:targetgroup/*"
      ]
    },
    {
      "Sid" : "ListVpcLatticeTargets",
      "Effect" : "Allow",
      "Action" : "vpc-lattice:ListTargets",
      "Resource" : [
        "arn:aws:vpc-lattice:*:*:targetgroup/*"
      ]
    },
    {
      "Sid" : "DescribeEc2Resources",
      "Effect" : "Allow",
      "Action" : [
        "ec2:DescribeSubnets",
        "ec2:DescribeVpcs",
        "ec2:DescribeInstances"
      ],
      "Resource" : [
        "*"
      ]
    }
  ]
}
```

## Learn more
<a name="AmazonECSInfrastructureRolePolicyForVpcLattice-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)