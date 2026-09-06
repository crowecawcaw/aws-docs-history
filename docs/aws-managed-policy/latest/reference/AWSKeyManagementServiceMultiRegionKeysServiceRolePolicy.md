

# AWSKeyManagementServiceMultiRegionKeysServiceRolePolicy
<a name="AWSKeyManagementServiceMultiRegionKeysServiceRolePolicy"></a>

**Description**: Enables AWS KMS to synchronize the shared properties of multi-Region keys.

`AWSKeyManagementServiceMultiRegionKeysServiceRolePolicy` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AWSKeyManagementServiceMultiRegionKeysServiceRolePolicy-how-to-use"></a>

This policy is attached to a service-linked role that allows the service to perform actions on your behalf. You cannot attach this policy to your users, groups, or roles.

## Policy details
<a name="AWSKeyManagementServiceMultiRegionKeysServiceRolePolicy-details"></a>
+ **Type**: Service-linked role policy 
+ **Creation time**: June 16, 2021, 15:37 UTC 
+ **Edited time:** November 13, 2024, 22:53 UTC
+ **ARN**: `arn:aws:iam::aws:policy/aws-service-role/AWSKeyManagementServiceMultiRegionKeysServiceRolePolicy`

## Policy version
<a name="AWSKeyManagementServiceMultiRegionKeysServiceRolePolicy-version"></a>

**Policy version:** v2 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AWSKeyManagementServiceMultiRegionKeysServiceRolePolicy-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Sid" : "KMSSynchronizeMultiRegionKey",
      "Effect" : "Allow",
      "Action" : [
        "kms:SynchronizeMultiRegionKey"
      ],
      "Resource" : "*"
    }
  ]
}
```

## Learn more
<a name="AWSKeyManagementServiceMultiRegionKeysServiceRolePolicy-learn-more"></a>
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)