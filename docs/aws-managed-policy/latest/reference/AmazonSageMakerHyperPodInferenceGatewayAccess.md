

# AmazonSageMakerHyperPodInferenceGatewayAccess
<a name="AmazonSageMakerHyperPodInferenceGatewayAccess"></a>

**Description**: This policy provides the permissions required to set up and operate the SageMaker HyperPod inference gateway. It enables the gateway to manage AWS Certificate Manager (ACM) certificates for TLS termination when deploying and serving inference workloads on HyperPod clusters.

`AmazonSageMakerHyperPodInferenceGatewayAccess` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AmazonSageMakerHyperPodInferenceGatewayAccess-how-to-use"></a>

You can attach `AmazonSageMakerHyperPodInferenceGatewayAccess` to your users, groups, and roles.

## Policy details
<a name="AmazonSageMakerHyperPodInferenceGatewayAccess-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: September 09, 2026, 23:27 UTC 
+ **Edited time:** September 09, 2026, 23:27 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AmazonSageMakerHyperPodInferenceGatewayAccess`

## Policy version
<a name="AmazonSageMakerHyperPodInferenceGatewayAccess-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AmazonSageMakerHyperPodInferenceGatewayAccess-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Sid" : "ImportOwnedCert",
      "Effect" : "Allow",
      "Action" : [
        "acm:ImportCertificate",
        "acm:AddTagsToCertificate"
      ],
      "Resource" : "arn:aws:acm:*:*:certificate/*",
      "Condition" : {
        "StringEquals" : {
          "aws:RequestTag/CreatedBy" : "HyperPodInference",
          "aws:ResourceAccount" : "${aws:PrincipalAccount}"
        },
        "ForAllValues:StringEquals" : {
          "aws:TagKeys" : [
            "CreatedBy"
          ]
        }
      }
    },
    {
      "Sid" : "ReadOwnedCerts",
      "Effect" : "Allow",
      "Action" : [
        "acm:DescribeCertificate",
        "acm:ListTagsForCertificate"
      ],
      "Resource" : "arn:aws:acm:*:*:certificate/*",
      "Condition" : {
        "StringEquals" : {
          "aws:ResourceTag/CreatedBy" : "HyperPodInference",
          "aws:ResourceAccount" : "${aws:PrincipalAccount}"
        }
      }
    },
    {
      "Sid" : "DeleteOwnedImportedCerts",
      "Effect" : "Allow",
      "Action" : [
        "acm:DeleteCertificate"
      ],
      "Resource" : "arn:aws:acm:*:*:certificate/*",
      "Condition" : {
        "StringEquals" : {
          "aws:ResourceTag/CreatedBy" : "HyperPodInference",
          "aws:ResourceAccount" : "${aws:PrincipalAccount}",
          "acm:CertificateKeyPairOrigin" : "CUSTOMER_PROVIDED"
        }
      }
    }
  ]
}
```

## Learn more
<a name="AmazonSageMakerHyperPodInferenceGatewayAccess-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)