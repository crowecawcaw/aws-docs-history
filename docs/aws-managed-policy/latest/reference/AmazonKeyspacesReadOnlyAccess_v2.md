

# AmazonKeyspacesReadOnlyAccess\_v2
<a name="AmazonKeyspacesReadOnlyAccess_v2"></a>

**Description**: Provide read only access to Amazon Keyspaces and related AWS services.

`AmazonKeyspacesReadOnlyAccess_v2` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AmazonKeyspacesReadOnlyAccess_v2-how-to-use"></a>

You can attach `AmazonKeyspacesReadOnlyAccess_v2` to your users, groups, and roles.

## Policy details
<a name="AmazonKeyspacesReadOnlyAccess_v2-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: September 12, 2023, 17:01 UTC 
+ **Edited time:** February 12, 2026, 18:02 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AmazonKeyspacesReadOnlyAccess_v2`

## Policy version
<a name="AmazonKeyspacesReadOnlyAccess_v2-version"></a>

**Policy version:** v4 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AmazonKeyspacesReadOnlyAccess_v2-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "Action" : [
        "cassandra:Select",
        "cassandra:ListStreams",
        "cassandra:GetStream",
        "cassandra:GetShardIterator",
        "cassandra:GetRecords"
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
        "cloudwatch:DescribeAlarms",
        "cloudwatch:GetMetricData",
        "kms:DescribeKey",
        "kms:ListAliases"
      ],
      "Resource" : "*"
    },
    {
      "Effect" : "Allow",
      "Action" : [
        "ec2:DescribeNetworkInterfaces",
        "ec2:DescribeVpcEndpoints"
      ],
      "Resource" : "*"
    }
  ]
}
```

## Learn more
<a name="AmazonKeyspacesReadOnlyAccess_v2-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)