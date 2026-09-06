

# AmazonElasticContainerRegistryPublicFullAccess
<a name="AmazonElasticContainerRegistryPublicFullAccess"></a>

**Description**: Provides administrative access to Amazon ECR Public resources

`AmazonElasticContainerRegistryPublicFullAccess` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AmazonElasticContainerRegistryPublicFullAccess-how-to-use"></a>

You can attach `AmazonElasticContainerRegistryPublicFullAccess` to your users, groups, and roles.

## Policy details
<a name="AmazonElasticContainerRegistryPublicFullAccess-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: December 01, 2020, 17:25 UTC 
+ **Edited time:** December 01, 2020, 17:25 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AmazonElasticContainerRegistryPublicFullAccess`

## Policy version
<a name="AmazonElasticContainerRegistryPublicFullAccess-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AmazonElasticContainerRegistryPublicFullAccess-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "Action" : [
        "ecr-public:*",
        "sts:GetServiceBearerToken"
      ],
      "Resource" : "*"
    }
  ]
}
```

## Learn more
<a name="AmazonElasticContainerRegistryPublicFullAccess-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)