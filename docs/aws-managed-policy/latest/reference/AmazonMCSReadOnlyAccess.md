

# AmazonMCSReadOnlyAccess
<a name="AmazonMCSReadOnlyAccess"></a>

**Description**: Provide read only access to Amazon Managed Apache Cassandra Service

`AmazonMCSReadOnlyAccess` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AmazonMCSReadOnlyAccess-how-to-use"></a>

You can attach `AmazonMCSReadOnlyAccess` to your users, groups, and roles.

## Policy details
<a name="AmazonMCSReadOnlyAccess-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: December 03, 2019, 13:46 UTC 
+ **Edited time:** April 17, 2020, 19:21 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AmazonMCSReadOnlyAccess`

## Policy version
<a name="AmazonMCSReadOnlyAccess-version"></a>

**Policy version:** v2 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AmazonMCSReadOnlyAccess-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "Action" : [
        "cassandra:Select"
      ],
      "Resource" : "*"
    },
    {
      "Effect" : "Allow",
      "Action" : [
        "application-autoscaling:DescribeScalableTargets",
        "application-autoscaling:DescribeScalingActivities",
        "application-autoscaling:DescribeScalingPolicies",
        "application-autoscaling:DescribeScheduledActions",
        "cloudwatch:DescribeAlarms"
      ],
      "Resource" : "*"
    }
  ]
}
```

## Learn more
<a name="AmazonMCSReadOnlyAccess-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)