

# AmazonInspectorReadOnlyAccess
<a name="AmazonInspectorReadOnlyAccess"></a>

**Description**: Provides read only access to Amazon Inspector.

`AmazonInspectorReadOnlyAccess` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AmazonInspectorReadOnlyAccess-how-to-use"></a>

You can attach `AmazonInspectorReadOnlyAccess` to your users, groups, and roles.

## Policy details
<a name="AmazonInspectorReadOnlyAccess-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: October 07, 2015, 17:08 UTC 
+ **Edited time:** October 01, 2019, 15:17 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AmazonInspectorReadOnlyAccess`

## Policy version
<a name="AmazonInspectorReadOnlyAccess-version"></a>

**Policy version:** v4 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AmazonInspectorReadOnlyAccess-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "Action" : [
        "inspector:Describe*",
        "inspector:Get*",
        "inspector:List*",
        "inspector:Preview*",
        "ec2:DescribeInstances",
        "ec2:DescribeTags",
        "sns:ListTopics",
        "events:DescribeRule",
        "events:ListRuleNamesByTarget"
      ],
      "Resource" : "*"
    }
  ]
}
```

## Learn more
<a name="AmazonInspectorReadOnlyAccess-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)