

# ApplicationAutoScalingForAmazonAppStreamAccess
<a name="ApplicationAutoScalingForAmazonAppStreamAccess"></a>

**Description**: Policy to enable Application Autoscaling for Amazon AppStream

`ApplicationAutoScalingForAmazonAppStreamAccess` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="ApplicationAutoScalingForAmazonAppStreamAccess-how-to-use"></a>

You can attach `ApplicationAutoScalingForAmazonAppStreamAccess` to your users, groups, and roles.

## Policy details
<a name="ApplicationAutoScalingForAmazonAppStreamAccess-details"></a>
+ **Type**: Service role policy 
+ **Creation time**: February 06, 2017, 21:39 UTC 
+ **Edited time:** February 06, 2017, 21:39 UTC
+ **ARN**: `arn:aws:iam::aws:policy/service-role/ApplicationAutoScalingForAmazonAppStreamAccess`

## Policy version
<a name="ApplicationAutoScalingForAmazonAppStreamAccess-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="ApplicationAutoScalingForAmazonAppStreamAccess-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "Action" : [
        "appstream:UpdateFleet",
        "appstream:DescribeFleets"
      ],
      "Resource" : [
        "*"
      ]
    },
    {
      "Effect" : "Allow",
      "Action" : [
        "cloudwatch:DescribeAlarms"
      ],
      "Resource" : [
        "*"
      ]
    }
  ]
}
```

## Learn more
<a name="ApplicationAutoScalingForAmazonAppStreamAccess-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)