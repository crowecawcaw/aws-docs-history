

# FSxDeleteServiceLinkedRoleAccess
<a name="FSxDeleteServiceLinkedRoleAccess"></a>

**Description**: Allows Amazon FSx to delete its Service Linked Roles for Amazon S3 access

`FSxDeleteServiceLinkedRoleAccess` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="FSxDeleteServiceLinkedRoleAccess-how-to-use"></a>

This policy is attached to a service-linked role that allows the service to perform actions on your behalf. You cannot attach this policy to your users, groups, or roles.

## Policy details
<a name="FSxDeleteServiceLinkedRoleAccess-details"></a>
+ **Type**: Service-linked role policy 
+ **Creation time**: November 28, 2018, 10:40 UTC 
+ **Edited time:** November 28, 2018, 10:40 UTC
+ **ARN**: `arn:aws:iam::aws:policy/aws-service-role/FSxDeleteServiceLinkedRoleAccess`

## Policy version
<a name="FSxDeleteServiceLinkedRoleAccess-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="FSxDeleteServiceLinkedRoleAccess-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "Action" : [
        "iam:DeleteServiceLinkedRole",
        "iam:GetServiceLinkedRoleDeletionStatus",
        "iam:GetRole"
      ],
      "Resource" : "arn:*:iam::*:role/aws-service-role/s3.data-source.lustre.fsx.amazonaws.com/AWSServiceRoleForFSxS3Access_*"
    }
  ]
}
```

## Learn more
<a name="FSxDeleteServiceLinkedRoleAccess-learn-more"></a>
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)