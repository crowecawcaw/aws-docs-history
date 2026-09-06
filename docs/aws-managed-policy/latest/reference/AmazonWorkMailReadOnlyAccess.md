

# AmazonWorkMailReadOnlyAccess
<a name="AmazonWorkMailReadOnlyAccess"></a>

**Description**: Provides read only access to WorkMail and SES.

`AmazonWorkMailReadOnlyAccess` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AmazonWorkMailReadOnlyAccess-how-to-use"></a>

You can attach `AmazonWorkMailReadOnlyAccess` to your users, groups, and roles.

## Policy details
<a name="AmazonWorkMailReadOnlyAccess-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: February 06, 2015, 18:40 UTC 
+ **Edited time:** July 25, 2019, 08:24 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AmazonWorkMailReadOnlyAccess`

## Policy version
<a name="AmazonWorkMailReadOnlyAccess-version"></a>

**Policy version:** v4 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AmazonWorkMailReadOnlyAccess-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "Action" : [
        "ses:Describe*",
        "ses:Get*",
        "workmail:Describe*",
        "workmail:Get*",
        "workmail:List*",
        "workmail:Search*",
        "lambda:ListFunctions",
        "iam:ListRoles",
        "logs:DescribeLogGroups",
        "cloudwatch:GetMetricData"
      ],
      "Resource" : "*"
    }
  ]
}
```

## Learn more
<a name="AmazonWorkMailReadOnlyAccess-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)