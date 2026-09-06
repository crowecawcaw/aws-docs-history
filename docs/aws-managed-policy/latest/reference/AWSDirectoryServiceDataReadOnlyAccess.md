

# AWSDirectoryServiceDataReadOnlyAccess
<a name="AWSDirectoryServiceDataReadOnlyAccess"></a>

**Description**: Provides read-only access to AWS Directory Service Data

`AWSDirectoryServiceDataReadOnlyAccess` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AWSDirectoryServiceDataReadOnlyAccess-how-to-use"></a>

You can attach `AWSDirectoryServiceDataReadOnlyAccess` to your users, groups, and roles.

## Policy details
<a name="AWSDirectoryServiceDataReadOnlyAccess-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: September 18, 2024, 22:00 UTC 
+ **Edited time:** September 18, 2024, 22:00 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AWSDirectoryServiceDataReadOnlyAccess`

## Policy version
<a name="AWSDirectoryServiceDataReadOnlyAccess-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AWSDirectoryServiceDataReadOnlyAccess-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Sid" : "DSDataReadOnlyAccess",
      "Effect" : "Allow",
      "Action" : [
        "ds:AccessDSData",
        "ds-data:DescribeGroup",
        "ds-data:DescribeUser",
        "ds-data:ListGroupMembers",
        "ds-data:ListGroups",
        "ds-data:ListGroupsForMember",
        "ds-data:ListUsers",
        "ds-data:SearchGroups",
        "ds-data:SearchUsers"
      ],
      "Resource" : [
        "arn:aws:ds:*:*:directory/*"
      ]
    }
  ]
}
```

## Learn more
<a name="AWSDirectoryServiceDataReadOnlyAccess-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)