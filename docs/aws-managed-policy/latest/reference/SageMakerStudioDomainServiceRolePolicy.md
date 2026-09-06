

# SageMakerStudioDomainServiceRolePolicy
<a name="SageMakerStudioDomainServiceRolePolicy"></a>

**Description**: Service role for domain level actions in the portal that are performed by Amazon SageMaker Studio.

`SageMakerStudioDomainServiceRolePolicy` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="SageMakerStudioDomainServiceRolePolicy-how-to-use"></a>

You can attach `SageMakerStudioDomainServiceRolePolicy` to your users, groups, and roles.

## Policy details
<a name="SageMakerStudioDomainServiceRolePolicy-details"></a>
+ **Type**: Service role policy 
+ **Creation time**: November 20, 2024, 21:56 UTC 
+ **Edited time:** November 20, 2024, 21:56 UTC
+ **ARN**: `arn:aws:iam::aws:policy/service-role/SageMakerStudioDomainServiceRolePolicy`

## Policy version
<a name="SageMakerStudioDomainServiceRolePolicy-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="SageMakerStudioDomainServiceRolePolicy-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Sid" : "SSMGetParameterStatement",
      "Effect" : "Allow",
      "Action" : [
        "ssm:GetParameter"
      ],
      "Resource" : [
        "arn:aws:ssm:*:*:parameter/amazon/datazone/profiles/*"
      ]
    },
    {
      "Sid" : "UseKMSKeyPermissionsStatement",
      "Effect" : "Allow",
      "Action" : [
        "kms:Decrypt"
      ],
      "Resource" : "*",
      "Condition" : {
        "StringEquals" : {
          "aws:ResourceTag/EnableKeyForAmazonDataZone" : "true"
        },
        "Null" : {
          "aws:ResourceTag/EnableKeyForAmazonDataZone" : "false"
        },
        "StringLike" : {
          "kms:ViaService" : "ssm.*.amazonaws.com",
          "kms:EncryptionContext:PARAMETER_ARN" : "arn:aws:ssm:*:*:parameter/amazon/datazone/profiles*"
        }
      }
    }
  ]
}
```

## Learn more
<a name="SageMakerStudioDomainServiceRolePolicy-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)