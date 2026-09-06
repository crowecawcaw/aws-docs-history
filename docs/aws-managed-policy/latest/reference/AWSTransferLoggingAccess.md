

# AWSTransferLoggingAccess
<a name="AWSTransferLoggingAccess"></a>

**Description**: Allows AWS Transfer full access to create log streams and groups and put log events to your account

`AWSTransferLoggingAccess` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AWSTransferLoggingAccess-how-to-use"></a>

You can attach `AWSTransferLoggingAccess` to your users, groups, and roles.

## Policy details
<a name="AWSTransferLoggingAccess-details"></a>
+ **Type**: Service role policy 
+ **Creation time**: January 14, 2019, 15:32 UTC 
+ **Edited time:** January 14, 2019, 15:32 UTC
+ **ARN**: `arn:aws:iam::aws:policy/service-role/AWSTransferLoggingAccess`

## Policy version
<a name="AWSTransferLoggingAccess-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AWSTransferLoggingAccess-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "Action" : [
        "logs:CreateLogStream",
        "logs:DescribeLogStreams",
        "logs:CreateLogGroup",
        "logs:PutLogEvents"
      ],
      "Resource" : "*"
    }
  ]
}
```

## Learn more
<a name="AWSTransferLoggingAccess-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)