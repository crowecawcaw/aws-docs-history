

# AmazonSageMakerGeospatialFullAccess
<a name="AmazonSageMakerGeospatialFullAccess"></a>

**Description**: This policy grants permissions that allow full access to Amazon SageMaker Geospatial through the AWS Management Console and SDK.

`AmazonSageMakerGeospatialFullAccess` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AmazonSageMakerGeospatialFullAccess-how-to-use"></a>

You can attach `AmazonSageMakerGeospatialFullAccess` to your users, groups, and roles.

## Policy details
<a name="AmazonSageMakerGeospatialFullAccess-details"></a>
+ **Type**: Service role policy 
+ **Creation time**: November 30, 2022, 10:06 UTC 
+ **Edited time:** November 30, 2022, 10:06 UTC
+ **ARN**: `arn:aws:iam::aws:policy/service-role/AmazonSageMakerGeospatialFullAccess`

## Policy version
<a name="AmazonSageMakerGeospatialFullAccess-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AmazonSageMakerGeospatialFullAccess-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "Action" : "sagemaker-geospatial:*",
      "Resource" : "*"
    },
    {
      "Effect" : "Allow",
      "Action" : [
        "iam:PassRole"
      ],
      "Resource" : "arn:aws:iam::*:role/*",
      "Condition" : {
        "StringEquals" : {
          "iam:PassedToService" : [
            "sagemaker-geospatial.amazonaws.com"
          ]
        }
      }
    }
  ]
}
```

## Learn more
<a name="AmazonSageMakerGeospatialFullAccess-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)