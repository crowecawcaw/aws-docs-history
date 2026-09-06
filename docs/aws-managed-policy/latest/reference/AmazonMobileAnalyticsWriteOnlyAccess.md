

# AmazonMobileAnalyticsWriteOnlyAccess
<a name="AmazonMobileAnalyticsWriteOnlyAccess"></a>

**Description**: Provides write only access to put event data for all application resources. (Recommended for SDK integration)

`AmazonMobileAnalyticsWriteOnlyAccess` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AmazonMobileAnalyticsWriteOnlyAccess-how-to-use"></a>

You can attach `AmazonMobileAnalyticsWriteOnlyAccess` to your users, groups, and roles.

## Policy details
<a name="AmazonMobileAnalyticsWriteOnlyAccess-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: February 06, 2015, 18:40 UTC 
+ **Edited time:** February 06, 2015, 18:40 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AmazonMobileAnalyticsWriteOnlyAccess`

## Policy version
<a name="AmazonMobileAnalyticsWriteOnlyAccess-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AmazonMobileAnalyticsWriteOnlyAccess-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "Action" : "mobileanalytics:PutEvents",
      "Resource" : "*"
    }
  ]
}
```

## Learn more
<a name="AmazonMobileAnalyticsWriteOnlyAccess-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)