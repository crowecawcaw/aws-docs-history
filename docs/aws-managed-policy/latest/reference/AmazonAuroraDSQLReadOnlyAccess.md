

# AmazonAuroraDSQLReadOnlyAccess
<a name="AmazonAuroraDSQLReadOnlyAccess"></a>

**Description**: Provides read only access to Aurora DSQL

`AmazonAuroraDSQLReadOnlyAccess` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AmazonAuroraDSQLReadOnlyAccess-how-to-use"></a>

You can attach `AmazonAuroraDSQLReadOnlyAccess` to your users, groups, and roles.

## Policy details
<a name="AmazonAuroraDSQLReadOnlyAccess-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: December 03, 2024, 15:21 UTC 
+ **Edited time:** May 13, 2026, 18:57 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AmazonAuroraDSQLReadOnlyAccess`

## Policy version
<a name="AmazonAuroraDSQLReadOnlyAccess-version"></a>

**Policy version:** v10 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AmazonAuroraDSQLReadOnlyAccess-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Sid" : "DsqlReadOnlyPermissions",
      "Effect" : "Allow",
      "Action" : [
        "dsql:GetClusterPolicy",
        "dsql:GetCluster",
        "dsql:GetVpcEndpointServiceName",
        "dsql:ListClusters",
        "dsql:ListTagsForResource",
        "dsql:GetStream",
        "dsql:ListStreams"
      ],
      "Resource" : "*"
    },
    {
      "Sid" : "RelatedServicesPermissions",
      "Effect" : "Allow",
      "Action" : [
        "cloudwatch:GetMetricData"
      ],
      "Resource" : "*"
    }
  ]
}
```

## Learn more
<a name="AmazonAuroraDSQLReadOnlyAccess-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)