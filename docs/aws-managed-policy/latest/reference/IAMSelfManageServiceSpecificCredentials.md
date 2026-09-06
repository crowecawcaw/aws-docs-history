

# IAMSelfManageServiceSpecificCredentials
<a name="IAMSelfManageServiceSpecificCredentials"></a>

**Description**: Allows an IAM user to manage their own Service Specific Credentials.

`IAMSelfManageServiceSpecificCredentials` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="IAMSelfManageServiceSpecificCredentials-how-to-use"></a>

You can attach `IAMSelfManageServiceSpecificCredentials` to your users, groups, and roles.

## Policy details
<a name="IAMSelfManageServiceSpecificCredentials-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: December 22, 2016, 17:25 UTC 
+ **Edited time:** December 22, 2016, 17:25 UTC
+ **ARN**: `arn:aws:iam::aws:policy/IAMSelfManageServiceSpecificCredentials`

## Policy version
<a name="IAMSelfManageServiceSpecificCredentials-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="IAMSelfManageServiceSpecificCredentials-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "Action" : [
        "iam:CreateServiceSpecificCredential",
        "iam:ListServiceSpecificCredentials",
        "iam:UpdateServiceSpecificCredential",
        "iam:DeleteServiceSpecificCredential",
        "iam:ResetServiceSpecificCredential"
      ],
      "Resource" : "arn:aws:iam::*:user/${aws:username}"
    }
  ]
}
```

## Learn more
<a name="IAMSelfManageServiceSpecificCredentials-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)