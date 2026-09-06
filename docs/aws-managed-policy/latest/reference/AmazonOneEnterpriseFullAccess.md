

# AmazonOneEnterpriseFullAccess
<a name="AmazonOneEnterpriseFullAccess"></a>

**Description**: This policy grants administrative permissions that allow access to all Amazon One Enterprise resources and operations.

`AmazonOneEnterpriseFullAccess` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AmazonOneEnterpriseFullAccess-how-to-use"></a>

You can attach `AmazonOneEnterpriseFullAccess` to your users, groups, and roles.

## Policy details
<a name="AmazonOneEnterpriseFullAccess-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: November 28, 2023, 04:58 UTC 
+ **Edited time:** November 28, 2023, 04:58 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AmazonOneEnterpriseFullAccess`

## Policy version
<a name="AmazonOneEnterpriseFullAccess-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AmazonOneEnterpriseFullAccess-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Sid" : "FullAccessStatementID",
      "Effect" : "Allow",
      "Action" : [
        "one:*"
      ],
      "Resource" : "*"
    }
  ]
}
```

## Learn more
<a name="AmazonOneEnterpriseFullAccess-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)