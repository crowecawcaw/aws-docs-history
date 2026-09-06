

# AmazonDocDBElasticReadOnlyAccess
<a name="AmazonDocDBElasticReadOnlyAccess"></a>

**Description**: Provides read-only access to Amazon DocDB-Elastic and CloudWatch metrics.

`AmazonDocDBElasticReadOnlyAccess` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AmazonDocDBElasticReadOnlyAccess-how-to-use"></a>

You can attach `AmazonDocDBElasticReadOnlyAccess` to your users, groups, and roles.

## Policy details
<a name="AmazonDocDBElasticReadOnlyAccess-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: June 08, 2023, 14:37 UTC 
+ **Edited time:** June 21, 2023, 16:57 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AmazonDocDBElasticReadOnlyAccess`

## Policy version
<a name="AmazonDocDBElasticReadOnlyAccess-version"></a>

**Policy version:** v2 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AmazonDocDBElasticReadOnlyAccess-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "Action" : [
        "docdb-elastic:ListClusters",
        "docdb-elastic:GetCluster",
        "docdb-elastic:ListClusterSnapshots",
        "docdb-elastic:GetClusterSnapshot",
        "docdb-elastic:ListTagsForResource"
      ],
      "Resource" : "*"
    },
    {
      "Effect" : "Allow",
      "Action" : [
        "cloudwatch:GetMetricData",
        "cloudwatch:GetMetricStatistics",
        "cloudwatch:ListMetrics"
      ],
      "Resource" : "*"
    }
  ]
}
```

## Learn more
<a name="AmazonDocDBElasticReadOnlyAccess-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)