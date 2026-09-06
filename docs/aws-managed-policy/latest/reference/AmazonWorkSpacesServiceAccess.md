

# AmazonWorkSpacesServiceAccess
<a name="AmazonWorkSpacesServiceAccess"></a>

**Description**: Provides customer account access to AWS WorkSpaces service for launching a Workspace.

`AmazonWorkSpacesServiceAccess` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AmazonWorkSpacesServiceAccess-how-to-use"></a>

You can attach `AmazonWorkSpacesServiceAccess` to your users, groups, and roles.

## Policy details
<a name="AmazonWorkSpacesServiceAccess-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: June 27, 2019, 19:19 UTC 
+ **Edited time:** March 18, 2020, 23:32 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AmazonWorkSpacesServiceAccess`

## Policy version
<a name="AmazonWorkSpacesServiceAccess-version"></a>

**Policy version:** v2 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AmazonWorkSpacesServiceAccess-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Action" : [
        "ec2:CreateNetworkInterface",
        "ec2:DeleteNetworkInterface",
        "ec2:DescribeNetworkInterfaces"
      ],
      "Effect" : "Allow",
      "Resource" : "*"
    }
  ]
}
```

## Learn more
<a name="AmazonWorkSpacesServiceAccess-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)