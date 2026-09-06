

# AmazonEKSWorkerNodePolicy
<a name="AmazonEKSWorkerNodePolicy"></a>

**Description**: This policy allows Amazon EKS worker nodes to connect to Amazon EKS Clusters.

`AmazonEKSWorkerNodePolicy` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AmazonEKSWorkerNodePolicy-how-to-use"></a>

You can attach `AmazonEKSWorkerNodePolicy` to your users, groups, and roles.

## Policy details
<a name="AmazonEKSWorkerNodePolicy-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: May 27, 2018, 21:09 UTC 
+ **Edited time:** November 27, 2023, 00:06 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AmazonEKSWorkerNodePolicy`

## Policy version
<a name="AmazonEKSWorkerNodePolicy-version"></a>

**Policy version:** v3 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AmazonEKSWorkerNodePolicy-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Sid" : "WorkerNodePermissions",
      "Effect" : "Allow",
      "Action" : [
        "ec2:DescribeInstances",
        "ec2:DescribeInstanceTypes",
        "ec2:DescribeRouteTables",
        "ec2:DescribeSecurityGroups",
        "ec2:DescribeSubnets",
        "ec2:DescribeVolumes",
        "ec2:DescribeVolumesModifications",
        "ec2:DescribeVpcs",
        "eks:DescribeCluster",
        "eks-auth:AssumeRoleForPodIdentity"
      ],
      "Resource" : "*"
    }
  ]
}
```

## Learn more
<a name="AmazonEKSWorkerNodePolicy-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)