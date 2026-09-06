

# AWSElementalMediaConnectCreateBridge
<a name="AWSElementalMediaConnectCreateBridge"></a>

**Description**: Provides full access to create MediaConnect Gateway Bridges and all its associated sub-resources.

`AWSElementalMediaConnectCreateBridge` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AWSElementalMediaConnectCreateBridge-how-to-use"></a>

You can attach `AWSElementalMediaConnectCreateBridge` to your users, groups, and roles.

## Policy details
<a name="AWSElementalMediaConnectCreateBridge-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: March 19, 2026, 16:57 UTC 
+ **Edited time:** March 19, 2026, 16:57 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AWSElementalMediaConnectCreateBridge`

## Policy version
<a name="AWSElementalMediaConnectCreateBridge-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AWSElementalMediaConnectCreateBridge-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "Action" : [
        "mediaconnect:CreateBridge",
        "mediaconnect:AddBridgeSources",
        "mediaconnect:AddBridgeOutputs"
      ],
      "Resource" : [
        "arn:aws:mediaconnect:*:*:bridge:*:*",
        "arn:aws:mediaconnect:*:*:bridge:*:*/bridgeSource/*",
        "arn:aws:mediaconnect:*:*:bridge:*:*/bridgeOutput/*"
      ]
    }
  ]
}
```

## Learn more
<a name="AWSElementalMediaConnectCreateBridge-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)