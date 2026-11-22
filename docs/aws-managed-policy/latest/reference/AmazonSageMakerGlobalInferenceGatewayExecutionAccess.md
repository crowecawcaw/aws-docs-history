

# AmazonSageMakerGlobalInferenceGatewayExecutionAccess

**Description**: This policy provides the permissions that a SageMaker global inference gateway execution role needs to reach the SageMaker HyperPod clusters in the gateway. It enables the role to describe the SageMaker HyperPod cluster, to access the cluster's Amazon EKS Kubernetes API, and to read the gateway's TLS server certificate from Amazon S3 (with AWS KMS through Amazon S3 for encrypted buckets).

`AmazonSageMakerGlobalInferenceGatewayExecutionAccess` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AmazonSageMakerGlobalInferenceGatewayExecutionAccess-how-to-use"></a>

You can attach `AmazonSageMakerGlobalInferenceGatewayExecutionAccess` to your users, groups, and roles.

## Policy details
<a name="AmazonSageMakerGlobalInferenceGatewayExecutionAccess-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: November 17, 2026, 23:37 UTC 
+ **Edited time:** November 17, 2026, 23:37 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AmazonSageMakerGlobalInferenceGatewayExecutionAccess`

## Policy version
<a name="AmazonSageMakerGlobalInferenceGatewayExecutionAccess-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AmazonSageMakerGlobalInferenceGatewayExecutionAccess-json"></a>

```json
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Sid" : "DescribeHyperPodCluster",
      "Effect" : "Allow",
      "Action" : "sagemaker:DescribeCluster",
      "Resource" : "arn:aws:sagemaker:*:*:cluster/*",
      "Condition" : {
        "StringEquals" : {
          "aws:ResourceAccount" : "${aws:PrincipalAccount}"
        }
      }
    },
    {
      "Sid" : "ReachMemberClusterApi",
      "Effect" : "Allow",
      "Action" : [
        "eks:AccessKubernetesApi",
        "eks:MutateViaKubernetesApi"
      ],
      "Resource" : "arn:aws:eks:*:*:cluster/*",
      "Condition" : {
        "StringEquals" : {
          "aws:ResourceAccount" : "${aws:PrincipalAccount}"
        }
      }
    },
    {
      "Sid" : "ReadGIGCertificate",
      "Effect" : "Allow",
      "Action" : "s3:GetObject",
      "Resource" : "arn:aws:s3:::hyperpod-tls*/*gig/*/*-certificate-*.pem",
      "Condition" : {
        "StringEquals" : {
          "s3:ExistingObjectTag/CreatedBy" : "HyperPodInference",
          "aws:ResourceAccount" : "${aws:PrincipalAccount}"
        }
      }
    },
    {
      "Sid" : "DecryptGIGCertificate",
      "Effect" : "Allow",
      "Action" : "kms:Decrypt",
      "Resource" : "arn:aws:kms:*:*:key/*",
      "Condition" : {
        "StringLike" : {
          "kms:ViaService" : "s3.*.amazonaws.com",
          "kms:EncryptionContext:aws:s3:arn" : "arn:aws:s3:::hyperpod-tls*"
        },
        "StringEquals" : {
          "aws:ResourceAccount" : "${aws:PrincipalAccount}"
        }
      }
    }
  ]
}
```

## Learn more
<a name="AmazonSageMakerGlobalInferenceGatewayExecutionAccess-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)