

# AmazonEC2ContainerRegistryReadOnly
<a name="AmazonEC2ContainerRegistryReadOnly"></a>

**Description**: Provides read-only access to Amazon EC2 Container Registry repositories.

`AmazonEC2ContainerRegistryReadOnly` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AmazonEC2ContainerRegistryReadOnly-how-to-use"></a>

You can attach `AmazonEC2ContainerRegistryReadOnly` to your users, groups, and roles.

## Policy details
<a name="AmazonEC2ContainerRegistryReadOnly-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: December 21, 2015, 17:04 UTC 
+ **Edited time:** December 10, 2019, 20:56 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryReadOnly`

## Policy version
<a name="AmazonEC2ContainerRegistryReadOnly-version"></a>

**Policy version:** v3 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AmazonEC2ContainerRegistryReadOnly-json"></a>

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
        "ecr:GetRepositoryPolicy",
        "ecr:DescribeRepositories",
        "ecr:ListImages",
        "ecr:DescribeImages",
        "ecr:BatchGetImage",
        "ecr:GetLifecyclePolicy",
        "ecr:GetLifecyclePolicyPreview",
        "ecr:ListTagsForResource",
        "ecr:DescribeImageScanFindings"
      ],
      "Resource" : "*"
    }
  ]
}
```

## Learn more
<a name="AmazonEC2ContainerRegistryReadOnly-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)