

# AmazonMQApiReadOnlyAccess
<a name="AmazonMQApiReadOnlyAccess"></a>

**Description**: Provides read only access to AmazonMQ via our API/SDK.

`AmazonMQApiReadOnlyAccess` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AmazonMQApiReadOnlyAccess-how-to-use"></a>

You can attach `AmazonMQApiReadOnlyAccess` to your users, groups, and roles.

## Policy details
<a name="AmazonMQApiReadOnlyAccess-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: December 18, 2018, 20:31 UTC 
+ **Edited time:** December 18, 2018, 20:31 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AmazonMQApiReadOnlyAccess`

## Policy version
<a name="AmazonMQApiReadOnlyAccess-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AmazonMQApiReadOnlyAccess-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Action" : [
        "mq:Describe*",
        "mq:List*",
        "ec2:DescribeNetworkInterfaces",
        "ec2:DescribeSecurityGroups",
        "ec2:DescribeSubnets",
        "ec2:DescribeVpcs"
      ],
      "Effect" : "Allow",
      "Resource" : "*"
    }
  ]
}
```

## Learn more
<a name="AmazonMQApiReadOnlyAccess-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)