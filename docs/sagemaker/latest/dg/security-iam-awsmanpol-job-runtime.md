

# AWS managed policies for SageMaker AI job runtime
<a name="security-iam-awsmanpol-job-runtime"></a>

Attach this policy to the IAM role that your agent runtime uses. It grants your agent runtime the permissions needed to invoke Amazon SageMaker AI job runtime APIs during model customization for sample generation, trajectory completion, and reward submission.

**Topics**
+ [AWS managed policy: AmazonSageMakerJobRuntimeAccess](#security-iam-awsmanpol-AmazonSageMakerJobRuntimeAccess)
+ [Amazon SageMaker AI updates to SageMaker AI job runtime managed policies](#security-iam-awsmanpol-job-runtime-updates)

## AWS managed policy: AmazonSageMakerJobRuntimeAccess
<a name="security-iam-awsmanpol-AmazonSageMakerJobRuntimeAccess"></a>

Use this policy to give your agent runtime the permissions to invoke SageMaker AI job runtime APIs during model customization for sample generation, trajectory completion, and reward submission. This policy restricts all permissions to resources within your AWS account.

Permissions details

This policy includes the following permissions.
+ `sagemaker` – Grants permissions to invoke job runtime APIs including generating samples, generating samples with response streaming, completing rollouts, and updating rewards on SageMaker AI job resources. Also grants permissions to call APIs with bearer token authentication.
+ `kms` – Grants permissions to decrypt and generate data keys to support AWS KMS encryption for Multi-Turn Reinforcement Learning (MTRL) runtime when you configure a customer managed key. This policy restricts these permissions to KMS keys in your own account (`aws:ResourceAccount` equals `aws:PrincipalAccount`) and requires that SageMaker AI service integrations route the requests (`kms:ViaService` set to `sagemaker.*.amazonaws.com`).

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "SageMakerJobRuntimePermissions",
            "Effect": "Allow",
            "Action": [
                "sagemaker:Sample",
                "sagemaker:SampleWithResponseStream",
                "sagemaker:CompleteRollout",
                "sagemaker:UpdateReward"
            ],
            "Resource": "arn:aws:sagemaker:*:*:job/*",
            "Condition": {
                "StringEquals": {
                    "aws:ResourceAccount": "${aws:PrincipalAccount}"
                }
            }
        },
        {
            "Sid": "BearerTokenPermissions",
            "Effect": "Allow",
            "Action": [
                "sagemaker:CallWithBearerToken"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "aws:ResourceAccount": "${aws:PrincipalAccount}"
                }
            }
        },
        {
            "Sid": "KMSPermissionsForMTRLRuntime",
            "Effect": "Allow",
            "Action": [
                "kms:Decrypt",
                "kms:GenerateDataKey"
            ],
            "Resource": "arn:aws:kms:*:*:key/*",
            "Condition": {
                "StringEquals": {
                    "aws:ResourceAccount": "${aws:PrincipalAccount}"
                },
                "StringLike": {
                    "kms:ViaService": "sagemaker.*.amazonaws.com"
                }
            }
        }
    ]
}
```

For more information about this policy, see [AmazonSageMakerJobRuntimeAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonSageMakerJobRuntimeAccess.html) in the AWS Managed Policy Reference Guide.

## Amazon SageMaker AI updates to SageMaker AI job runtime managed policies
<a name="security-iam-awsmanpol-job-runtime-updates"></a>

View details about updates to AWS managed policies for Amazon SageMaker AI since Amazon SageMaker AI began tracking these changes.


**Policy version history**  

| Policy | Version | Change | Date | 
| --- | --- | --- | --- | 
| [AmazonSageMakerJobRuntimeAccess](#security-iam-awsmanpol-AmazonSageMakerJobRuntimeAccess) – Updated | 2 | Added `kms:Decrypt` and `kms:GenerateDataKey` permissions to support AWS KMS encryption for Multi-Turn Reinforcement Learning (MTRL) runtime. Permissions are scoped to KMS keys in your own account and restricted to requests routed through SageMaker AI service integrations. | August 07, 2026 | 
| [AmazonSageMakerJobRuntimeAccess](#security-iam-awsmanpol-AmazonSageMakerJobRuntimeAccess) – New policy | 1 | Initial policy | June 4, 2026 | 