# Controls with parameters

In AWS Control Tower, RCP-based and certain SCP-based controls support configuration. These
controls contain elements that are included by AWS Control Tower conditionally, based on the
configuration you select.

For example, some control policies include inline templating variables, such as the one
shown in the example that follows. The example shows the
**ExemptedPrincipalArns** parameter.

```
 {
            "Sid": "CTEC2PV1",
            "Effect": "Deny",
            "Action": [
                "ec2:CreateSnapshot",
                "ec2:CreateSnapshots"
            ],
            "Resource": "arn:*:ec2:*:*:volume/*",
            "Condition": {
                "Bool": {
                    "ec2:Encrypted": "false"
                }{% if ExemptedPrincipalArns %},
                "ArnNotLike": {
                    "aws:PrincipalArn": {{ExemptedPrincipalArns}}
                }{% endif %}
            }
        }
```

###### A control may support any of the following four configuration parameters:

- **ExemptedPrincipalArns**: A list of AWS IAM principal ARNs
  that are exempted from this control.
  - This parameter allows you to exempt IAM Principals from this control by way of
    an **ArnNotLikeIfExists** condition key operator and
    **aws:PrincipalArn** condition key that is applied to the
    control policy by AWS Control Tower when you enable the control. The
    **ExemptedPrincipalArns** parameter allows you to use the
    wildcard character (\*) in the IAM principal ARNs that you specify. You can use
    the wildcard character to exempt all IAM principals in an AWS account, or
    exempt a common principal across multiple AWS accounts.
  - When you use the wildcard character to exempt principals, be sure that you follow
    the principal of least privilege: include only those IAM principal ARNs that you
    require to be exempt from a control. Otherwise, if your exemptions are too broad,
    the control may not come into effect when you intend it to.

- **AllowedRegions**: List of AWS
  Regions exempted from the control.
- **ExemptedActions**: List of AWS IAM
  actions exempted from the control.
- **ExemptedResourceArns**: List of resource ARNs
  exempted from the control.
  For more details about configuring controls with parameters, see [`ControlParameter`](../../../controlcatalog/latest/APIReference/API_ControlParameter.md "../../../controlcatalog/latest/APIReference/API_ControlParameter.md") in the _AWS Control Tower API Reference_.

**List of parameterized controls**

| **Control identifier**                        | **Display name**                                                                                                                                                 |
| --------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AWS-GR_AUDIT_BUCKET_ENCRYPTION_ENABLED        | Disallow modification of an Amazon S3 bucket default encryption                                                                                                  |
| AWS-GR_AUDIT_BUCKET_LOGGING_ENABLED           | Disallow modification of server access logging for an Amazon S3 bucket                                                                                           |
| AWS-GR_AUDIT_BUCKET_POLICY_CHANGES_PROHIBITED | Disallow policy changes to an Amazon S3 bucket                                                                                                                   |
| AWS-GR_AUDIT_BUCKET_RETENTION_POLICY          | Set a retention policy for log archive                                                                                                                           |
| AWS-GR_DISALLOW_CROSS_REGION_NETWORKING       | Disallow cross-region networking for Amazon EC2, Amazon CloudFront, and AWS Global Accelerator                                                                   |
| AWS-GR_DISALLOW_VPC_INTERNET_ACCESS           | Disallow internet access for an Amazon VPC instance managed by a customer                                                                                        |
| AWS-GR_DISALLOW_VPN_CONNECTIONS               | Disallow AWS Virtual Private Network (VPN) connections                                                                                                           |
| AWS-GR_RESTRICT_ROOT_USER                     | Disallow actions as a root user                                                                                                                                  |
| AWS-GR_RESTRICT_ROOT_USER_ACCESS_KEYS         | Disallow creation of access keys for the root user                                                                                                               |
| AWS-GR_RESTRICT_S3_CROSS_REGION_REPLICATION   | Disallow cross region replication for S3 buckets                                                                                                                 |
| AWS-GR_RESTRICT_S3_DELETE_WITHOUT_MFA         | Disallow delete actions on S3 buckets without MFA                                                                                                                |
| CT.APPSYNC.PV.1                               | Require an AWS AppSync GraphQL API to be configured with private visibility                                                                                      |
| CT.EC2.PV.1                                   | Require an Amazon EBS snapshot to be created from an encrypted EC2 volume                                                                                        |
| CT.EC2.PV.2                                   | Require that an attached Amazon EBS volume is configured to encrypt data at rest                                                                                 |
| CT.EC2.PV.3                                   | Require that an Amazon EBS snapshot cannot be publicly restorable                                                                                                |
| CT.EC2.PV.4                                   | Require that Amazon EBS direct APIs are not called                                                                                                               |
| CT.EC2.PV.5                                   | Disallow the use of Amazon EC2 VM import and export                                                                                                              |
| CT.EC2.PV.6                                   | Disallow the use of deprecated Amazon EC2 RequestSpotFleet and RequestSpotInstances API actions                                                                  |
| CT.KMS.PV.1                                   | Require an AWS KMS key policy to have a statement that limits creation of AWS KMS grants to AWS services                                                         |
| CT.KMS.PV.2                                   | Require that an AWS KMS asymmetric key with RSA key material used for encryption does not have a key length of 2048 bits                                         |
| CT.KMS.PV.3                                   | Require that an AWS KMS key is configured with the bypass policy lockout safety check enabled                                                                    |
| CT.KMS.PV.4                                   | Require that an AWS KMS customer-managed key (CMK) is configured with key material originating from AWS CloudHSM                                                 |
| CT.KMS.PV.5                                   | Require that an AWS KMS customer-managed key (CMK) is configured with imported key material                                                                      |
| CT.KMS.PV.6                                   | Require that an AWS KMS customer-managed key (CMK) is configured with key material originating from an external key store (XKS)                                  |
| CT.LAMBDA.PV.1                                | Require an AWS Lambda function URL to use AWS IAM-based authentication                                                                                           |
| CT.LAMBDA.PV.2                                | Require an AWS Lambda function or AWS Lambda function URL to be configured for access only to principals within your AWS account                                 |
| CT.KMS.PV.7                                   | Require that the organization's AWS Key Management Service resources are accessible only by IAM principals that belong to the organization, or by an AWS service |
| CT.S3.PV.2                                    | Require all requests to Amazon S3 resources use authentication based on an Authorization header                                                                  |
| CT.S3.PV.3                                    | Require requests to Amazon S3 resources to use a minimum TLS version of 1.3                                                                                      |
| CT.S3.PV.4                                    | Require that the organization's Amazon S3 resources are accessible only by IAM principals that belong to the organization or by an AWS service                   |
| CT.S3.PV.5                                    | Require encryption of data in transit for calls to Amazon S3 resources                                                                                           |
| CT.S3.PV.6                                    | Require all object uploads to Amazon S3 buckets to use server-side encryption with an AWS KMS key (SSE-KMS                                                       |
| CT.SECRETSMANAGER.PV.1                        | Require that the organization's AWS Secrets Manager resources are accessible only by IAM principals that belong to the organization or by an AWS service         |
| CT.SQS.PV.1                                   | Require that the organization's Amazon SQS resources are accessible only by IAM principals that belong to the organization, or by an AWS service                 |
| CT.STS.PV.1                                   | Require that the organization's AWS Security Token Service resources are accessible only by IAM principals that belong to the organization, or by an AWS service |
