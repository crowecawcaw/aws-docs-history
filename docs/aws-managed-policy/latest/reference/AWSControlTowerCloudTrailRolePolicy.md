

# AWSControlTowerCloudTrailRolePolicy
<a name="AWSControlTowerCloudTrailRolePolicy"></a>

**Description**: AWS Control Tower enables AWS CloudTrail as a best practice and provides this role to AWS CloudTrail. AWS CloudTrail assumes this role to create and publish CloudTrail logs

`AWSControlTowerCloudTrailRolePolicy` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AWSControlTowerCloudTrailRolePolicy-how-to-use"></a>

You can attach `AWSControlTowerCloudTrailRolePolicy` to your users, groups, and roles.

## Policy details
<a name="AWSControlTowerCloudTrailRolePolicy-details"></a>
+ **Type**: Service role policy 
+ **Creation time**: November 05, 2025, 21:19 UTC 
+ **Edited time:** February 12, 2026, 18:02 UTC
+ **ARN**: `arn:aws:iam::aws:policy/service-role/AWSControlTowerCloudTrailRolePolicy`

## Policy version
<a name="AWSControlTowerCloudTrailRolePolicy-version"></a>

**Policy version:** v3 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AWSControlTowerCloudTrailRolePolicy-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "Action" : "logs:CreateLogStream",
      "Resource" : "arn:aws:logs:*:*:log-group:aws-controltower/CloudTrailLogs*:*"
    },
    {
      "Effect" : "Allow",
      "Action" : "logs:PutLogEvents",
      "Resource" : "arn:aws:logs:*:*:log-group:aws-controltower/CloudTrailLogs*:*"
    }
  ]
}
```

## Learn more
<a name="AWSControlTowerCloudTrailRolePolicy-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)