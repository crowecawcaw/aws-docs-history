

# AmazonEKSFargatePodExecutionRolePolicy
<a name="AmazonEKSFargatePodExecutionRolePolicy"></a>

**Description**: Provides access to other AWS service resources that are required to run Amazon EKS pods on AWS Fargate

`AmazonEKSFargatePodExecutionRolePolicy` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AmazonEKSFargatePodExecutionRolePolicy-how-to-use"></a>

You can attach `AmazonEKSFargatePodExecutionRolePolicy` to your users, groups, and roles.

## Policy details
<a name="AmazonEKSFargatePodExecutionRolePolicy-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: November 22, 2019, 04:34 UTC 
+ **Edited time:** November 22, 2019, 04:34 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AmazonEKSFargatePodExecutionRolePolicy`

## Policy version
<a name="AmazonEKSFargatePodExecutionRolePolicy-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AmazonEKSFargatePodExecutionRolePolicy-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "Action" : [
        "ecr:GetAuthorizationToken",
        "ecr:BatchCheckLayerAvailability",
        "ecr:GetDownloadUrlForLayer",
        "ecr:BatchGetImage"
      ],
      "Resource" : "*"
    }
  ]
}
```

## Learn more
<a name="AmazonEKSFargatePodExecutionRolePolicy-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)