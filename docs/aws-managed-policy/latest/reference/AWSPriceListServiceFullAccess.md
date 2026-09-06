

# AWSPriceListServiceFullAccess
<a name="AWSPriceListServiceFullAccess"></a>

**Description**: Provides full access to AWS Price List Service.

`AWSPriceListServiceFullAccess` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AWSPriceListServiceFullAccess-how-to-use"></a>

You can attach `AWSPriceListServiceFullAccess` to your users, groups, and roles.

## Policy details
<a name="AWSPriceListServiceFullAccess-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: November 22, 2017, 00:36 UTC 
+ **Edited time:** July 02, 2024, 13:34 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AWSPriceListServiceFullAccess`

## Policy version
<a name="AWSPriceListServiceFullAccess-version"></a>

**Policy version:** v2 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AWSPriceListServiceFullAccess-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Sid" : "AWSPriceListServiceFullAccess",
      "Effect" : "Allow",
      "Action" : [
        "pricing:*"
      ],
      "Resource" : "*"
    }
  ]
}
```

## Learn more
<a name="AWSPriceListServiceFullAccess-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)