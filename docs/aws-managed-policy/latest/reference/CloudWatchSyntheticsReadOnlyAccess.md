

# CloudWatchSyntheticsReadOnlyAccess
<a name="CloudWatchSyntheticsReadOnlyAccess"></a>

**Description**: Provides read only access to CloudWatch Synthetics.

`CloudWatchSyntheticsReadOnlyAccess` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="CloudWatchSyntheticsReadOnlyAccess-how-to-use"></a>

You can attach `CloudWatchSyntheticsReadOnlyAccess` to your users, groups, and roles.

## Policy details
<a name="CloudWatchSyntheticsReadOnlyAccess-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: November 25, 2019, 17:45 UTC 
+ **Edited time:** March 06, 2020, 19:26 UTC
+ **ARN**: `arn:aws:iam::aws:policy/CloudWatchSyntheticsReadOnlyAccess`

## Policy version
<a name="CloudWatchSyntheticsReadOnlyAccess-version"></a>

**Policy version:** v2 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="CloudWatchSyntheticsReadOnlyAccess-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "Action" : [
        "synthetics:Describe*",
        "synthetics:Get*",
        "synthetics:List*"
      ],
      "Resource" : "*"
    }
  ]
}
```

## Learn more
<a name="CloudWatchSyntheticsReadOnlyAccess-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)