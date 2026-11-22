

# AmazonSageMakerHyperPodInferenceGatewayMetricsPublisherAccess

**Description**: This policy provides the permissions that the SageMaker HyperPod inference gateway metrics publisher needs to send gateway metrics to a SageMaker global inference gateway. It enables the publisher to write records to the global inference gateway's Amazon Kinesis Data Streams stream, and to use AWS KMS keys through Amazon Kinesis Data Streams to encrypt those records.

`AmazonSageMakerHyperPodInferenceGatewayMetricsPublisherAccess` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AmazonSageMakerHyperPodInferenceGatewayMetricsPublisherAccess-how-to-use"></a>

You can attach `AmazonSageMakerHyperPodInferenceGatewayMetricsPublisherAccess` to your users, groups, and roles.

## Policy details
<a name="AmazonSageMakerHyperPodInferenceGatewayMetricsPublisherAccess-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: November 17, 2026, 21:57 UTC 
+ **Edited time:** November 17, 2026, 21:57 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AmazonSageMakerHyperPodInferenceGatewayMetricsPublisherAccess`

## Policy version
<a name="AmazonSageMakerHyperPodInferenceGatewayMetricsPublisherAccess-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AmazonSageMakerHyperPodInferenceGatewayMetricsPublisherAccess-json"></a>

```json
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Sid" : "PublishGatewayMetrics",
      "Effect" : "Allow",
      "Action" : "kinesis:PutRecords",
      "Resource" : "arn:aws:kinesis:*:*:stream/gig-metrics-*"
    },
    {
      "Sid" : "EncryptGatewayMetrics",
      "Effect" : "Allow",
      "Action" : "kms:GenerateDataKey",
      "Resource" : "arn:aws:kms:*:*:key/*",
      "Condition" : {
        "StringLike" : {
          "kms:ViaService" : "kinesis.*.amazonaws.com",
          "kms:EncryptionContext:aws:kinesis:arn" : "arn:aws:kinesis:*:*:stream/gig-metrics-*"
        }
      }
    }
  ]
}
```

## Learn more
<a name="AmazonSageMakerHyperPodInferenceGatewayMetricsPublisherAccess-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)