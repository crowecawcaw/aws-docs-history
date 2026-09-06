

# AWS policy: SageMakerStudioDomainServiceRolePolicy
<a name="security-iam-awsmanpol-SageMakerStudioDomainServiceRolePolicy"></a>

This is the default policy for the SageMakerUnifiedStudioDomainServiceRole service role. This policy is used by Amazon SageMaker Unified Studio to access the SSM parameters in the user’s account. Those parameters are set by the administrator in the Amazon SageMaker Unified Studio project profiles. This policy also has permissions to AWS KMS for encrypted SSM parameters. The KMS key must be tagged with EnableKeyForAmazonDataZone to allow decrypting the SSM parameters.

To view the permissions for this policy, see [SageMakerStudioDomainServiceRolePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/SageMakerStudioDomainServiceRolePolicy.html) in the *AWS Managed Policy Reference*.