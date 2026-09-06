

# AmazonSageMakerHyperPodGatedModelAccess
<a name="AmazonSageMakerHyperPodGatedModelAccess"></a>

**Description**: This Amazon Managed Policy provides the necessary permissions for SageMaker HyperPod to access gated models in SageMaker Jumpstart. It allows creating presigned URLs for hub content in the SageMaker Public Hub.

`AmazonSageMakerHyperPodGatedModelAccess` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AmazonSageMakerHyperPodGatedModelAccess-how-to-use"></a>

You can attach `AmazonSageMakerHyperPodGatedModelAccess` to your users, groups, and roles.

## Policy details
<a name="AmazonSageMakerHyperPodGatedModelAccess-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: January 17, 2026, 01:04 UTC 
+ **Edited time:** February 12, 2026, 18:00 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AmazonSageMakerHyperPodGatedModelAccess`

## Policy version
<a name="AmazonSageMakerHyperPodGatedModelAccess-version"></a>

**Policy version:** v3 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AmazonSageMakerHyperPodGatedModelAccess-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Sid" : "CreatePresignedUrlAccess",
      "Effect" : "Allow",
      "Action" : [
        "sagemaker:CreateHubContentPresignedUrls"
      ],
      "Resource" : [
        "arn:aws:sagemaker:*:*:hub/SageMakerPublicHub",
        "arn:aws:sagemaker:*:*:hub-content/SageMakerPublicHub/*/*"
      ],
      "Condition" : {
        "StringEquals" : {
          "aws:ResourceAccount" : "${aws:PrincipalAccount}"
        }
      }
    }
  ]
}
```

## Learn more
<a name="AmazonSageMakerHyperPodGatedModelAccess-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)