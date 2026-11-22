

# AmazonEC2ContainerRegistryPullOnly

**Description**: Provides access to pull images from Amazon EC2 Container Registry repositories.

`AmazonEC2ContainerRegistryPullOnly` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AmazonEC2ContainerRegistryPullOnly-how-to-use"></a>

You can attach `AmazonEC2ContainerRegistryPullOnly` to your users, groups, and roles.

## Policy details
<a name="AmazonEC2ContainerRegistryPullOnly-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: October 04, 2024, 16:58 UTC 
+ **Edited time:** November 17, 2026, 21:27 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryPullOnly`

## Policy version
<a name="AmazonEC2ContainerRegistryPullOnly-version"></a>

**Policy version:** v2 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AmazonEC2ContainerRegistryPullOnly-json"></a>

```json
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "Action" : [
        "ecr:GetAuthorizationToken",
        "ecr:BatchGetImage",
        "ecr:GetDownloadUrlForLayer",
        "ecr:BatchImportUpstreamImage"
      ],
      "Resource" : "*"
    },
    {
      "Effect" : "Allow",
      "Action" : [
        "signin:CreateBearerToken"
      ],
      "Resource" : "arn:aws:signin:*:*:service-principal/ecr.amazonaws.com"
    }
  ]
}
```

## Learn more
<a name="AmazonEC2ContainerRegistryPullOnly-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)