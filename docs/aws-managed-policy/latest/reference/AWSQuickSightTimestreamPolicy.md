

# AWSQuickSightTimestreamPolicy
<a name="AWSQuickSightTimestreamPolicy"></a>

**Description**: AWS QuickSight access to AWS Timestream APIs. Customers can attach this policy to AWS QuickSight role to allow retrieval of data and metadata.

`AWSQuickSightTimestreamPolicy` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AWSQuickSightTimestreamPolicy-how-to-use"></a>

You can attach `AWSQuickSightTimestreamPolicy` to your users, groups, and roles.

## Policy details
<a name="AWSQuickSightTimestreamPolicy-details"></a>
+ **Type**: Service role policy 
+ **Creation time**: September 30, 2020, 21:47 UTC 
+ **Edited time:** September 30, 2020, 21:47 UTC
+ **ARN**: `arn:aws:iam::aws:policy/service-role/AWSQuickSightTimestreamPolicy`

## Policy version
<a name="AWSQuickSightTimestreamPolicy-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AWSQuickSightTimestreamPolicy-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "Action" : [
        "timestream:Select",
        "timestream:CancelQuery",
        "timestream:ListTables",
        "timestream:ListDatabases",
        "timestream:ListMeasures",
        "timestream:DescribeTable",
        "timestream:DescribeDatabase",
        "timestream:SelectValues",
        "timestream:DescribeEndpoints"
      ],
      "Resource" : "*"
    }
  ]
}
```

## Learn more
<a name="AWSQuickSightTimestreamPolicy-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)