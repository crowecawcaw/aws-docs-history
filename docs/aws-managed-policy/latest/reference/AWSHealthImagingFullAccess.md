

# AWSHealthImagingFullAccess
<a name="AWSHealthImagingFullAccess"></a>

**Description**: Provides full access to AWS Health Imaging service.

`AWSHealthImagingFullAccess` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AWSHealthImagingFullAccess-how-to-use"></a>

You can attach `AWSHealthImagingFullAccess` to your users, groups, and roles.

## Policy details
<a name="AWSHealthImagingFullAccess-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: July 25, 2023, 23:39 UTC 
+ **Edited time:** July 25, 2023, 23:39 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AWSHealthImagingFullAccess`

## Policy version
<a name="AWSHealthImagingFullAccess-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AWSHealthImagingFullAccess-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "Action" : [
        "medical-imaging:*"
      ],
      "Resource" : "*"
    },
    {
      "Effect" : "Allow",
      "Action" : "iam:PassRole",
      "Resource" : "*",
      "Condition" : {
        "StringEquals" : {
          "iam:PassedToService" : "medical-imaging.amazonaws.com"
        }
      }
    }
  ]
}
```

## Learn more
<a name="AWSHealthImagingFullAccess-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)