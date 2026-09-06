

# AWSSystemsManagerForSAPReadOnlyAccess
<a name="AWSSystemsManagerForSAPReadOnlyAccess"></a>

**Description**: Provides read only access to AWS Systems Manager for SAP service

`AWSSystemsManagerForSAPReadOnlyAccess` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AWSSystemsManagerForSAPReadOnlyAccess-how-to-use"></a>

You can attach `AWSSystemsManagerForSAPReadOnlyAccess` to your users, groups, and roles.

## Policy details
<a name="AWSSystemsManagerForSAPReadOnlyAccess-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: November 17, 2022, 02:11 UTC 
+ **Edited time:** November 17, 2022, 02:11 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AWSSystemsManagerForSAPReadOnlyAccess`

## Policy version
<a name="AWSSystemsManagerForSAPReadOnlyAccess-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AWSSystemsManagerForSAPReadOnlyAccess-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "Action" : [
        "ssm-sap:get*",
        "ssm-sap:list*"
      ],
      "Resource" : "arn:*:ssm-sap:*:*:*"
    }
  ]
}
```

## Learn more
<a name="AWSSystemsManagerForSAPReadOnlyAccess-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)