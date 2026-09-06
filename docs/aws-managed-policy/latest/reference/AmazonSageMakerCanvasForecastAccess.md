

# AmazonSageMakerCanvasForecastAccess
<a name="AmazonSageMakerCanvasForecastAccess"></a>

**Description**: This policy grants permissions commonly needed to use SageMaker Canvas with Amazon Forecast.

`AmazonSageMakerCanvasForecastAccess` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AmazonSageMakerCanvasForecastAccess-how-to-use"></a>

You can attach `AmazonSageMakerCanvasForecastAccess` to your users, groups, and roles.

## Policy details
<a name="AmazonSageMakerCanvasForecastAccess-details"></a>
+ **Type**: Service role policy 
+ **Creation time**: August 24, 2022, 20:04 UTC 
+ **Edited time:** August 24, 2022, 20:04 UTC
+ **ARN**: `arn:aws:iam::aws:policy/service-role/AmazonSageMakerCanvasForecastAccess`

## Policy version
<a name="AmazonSageMakerCanvasForecastAccess-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AmazonSageMakerCanvasForecastAccess-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "Action" : [
        "s3:GetObject",
        "s3:PutObject"
      ],
      "Resource" : [
        "arn:aws:s3:::sagemaker-*/Canvas*",
        "arn:aws:s3:::sagemaker-*/canvas*"
      ]
    },
    {
      "Effect" : "Allow",
      "Action" : [
        "s3:ListBucket"
      ],
      "Resource" : [
        "arn:aws:s3:::sagemaker-*"
      ]
    }
  ]
}
```

## Learn more
<a name="AmazonSageMakerCanvasForecastAccess-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)