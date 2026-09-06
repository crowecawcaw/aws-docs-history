

# AmazonSSMDirectoryServiceAccess
<a name="AmazonSSMDirectoryServiceAccess"></a>

**Description**: This policy allows SSM Agent to access Directory Service on behalf of the customer for domain-join the managed instance.

`AmazonSSMDirectoryServiceAccess` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AmazonSSMDirectoryServiceAccess-how-to-use"></a>

You can attach `AmazonSSMDirectoryServiceAccess` to your users, groups, and roles.

## Policy details
<a name="AmazonSSMDirectoryServiceAccess-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: March 15, 2019, 17:44 UTC 
+ **Edited time:** March 15, 2019, 17:44 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AmazonSSMDirectoryServiceAccess`

## Policy version
<a name="AmazonSSMDirectoryServiceAccess-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AmazonSSMDirectoryServiceAccess-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "Action" : [
        "ds:CreateComputer",
        "ds:DescribeDirectories"
      ],
      "Resource" : "*"
    }
  ]
}
```

## Learn more
<a name="AmazonSSMDirectoryServiceAccess-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)