# AWS managed policies for SageMaker AI job runtime

This AWS managed policy grants permissions needed for agent runtimes to invoke SageMaker AI job
runtime APIs during model customization. The policy can be attached to IAM roles used by
agent runtimes that interact with SageMaker AI jobs for sample generation, trajectory completion,
and reward submission.

###### Topics

- [AWS managed policy: AmazonSageMakerJobRuntimeAccess](#security-iam-awsmanpol-AmazonSageMakerJobRuntimeAccess "#security-iam-awsmanpol-AmazonSageMakerJobRuntimeAccess")
- [Amazon SageMaker AI updates to SageMaker AI job runtime managed policies](#security-iam-awsmanpol-job-runtime-updates "#security-iam-awsmanpol-job-runtime-updates")

## AWS managed policy: AmazonSageMakerJobRuntimeAccess

This policy provides the necessary permissions for agent runtimes to invoke SageMaker AI job
runtime APIs used during model customization for sample generation, trajectory
completion, and reward submission. All permissions are restricted to resources within the
same AWS account.

**Permissions details**

This policy includes the following permissions.

- `sagemaker` – Allows invoking job runtime APIs including
  generating samples, generating samples with response streaming, completing
  rollouts, and updating rewards on SageMaker AI job resources. Also allows calling APIs
  with bearer token authentication.

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
        }
    ]
}
```

For more information, see [AmazonSageMakerJobRuntimeAccess](../../../aws-managed-policy/latest/reference/AmazonSageMakerJobRuntimeAccess.md "../../../aws-managed-policy/latest/reference/AmazonSageMakerJobRuntimeAccess.md") in the AWS Managed Policy Reference
Guide.

## Amazon SageMaker AI updates to SageMaker AI job runtime managed policies

View details about updates to AWS managed policies for Amazon SageMaker AI since this service
began tracking these changes.

| Policy                                                                                                                                                            | Version | Change         | Date         |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | -------------- | ------------ |
| [AmazonSageMakerJobRuntimeAccess](#security-iam-awsmanpol-AmazonSageMakerJobRuntimeAccess "#security-iam-awsmanpol-AmazonSageMakerJobRuntimeAccess") – New policy | 1       | Initial policy | June 4, 2026 |
