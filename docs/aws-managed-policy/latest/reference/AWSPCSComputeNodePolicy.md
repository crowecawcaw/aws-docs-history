

# AWSPCSComputeNodePolicy
<a name="AWSPCSComputeNodePolicy"></a>

**Description**: Grants permission to AWS PCS compute nodes to connect to AWS PCS clusters.

`AWSPCSComputeNodePolicy` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AWSPCSComputeNodePolicy-how-to-use"></a>

You can attach `AWSPCSComputeNodePolicy` to your users, groups, and roles.

## Policy details
<a name="AWSPCSComputeNodePolicy-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: June 23, 2025, 18:07 UTC 
+ **Edited time:** February 12, 2026, 18:01 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AWSPCSComputeNodePolicy`

## Policy version
<a name="AWSPCSComputeNodePolicy-version"></a>

**Policy version:** v3 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AWSPCSComputeNodePolicy-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "Action" : [
        "pcs:RegisterComputeNodeGroupInstance"
      ],
      "Resource" : "*"
    }
  ]
}
```

## Learn more
<a name="AWSPCSComputeNodePolicy-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)