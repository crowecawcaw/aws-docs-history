

# Document history

The following table describes the important changes to the documentation since the last release of AWS Secrets Manager. For notification about updates to this documentation, you can subscribe to an RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [ASCP can assume an IAM role](document-history.md) | The AWS Secrets and Configuration Provider (ASCP) for Amazon EKS can now assume an IAM role before it retrieves secrets, for example a role in the account that owns the secrets. You set the role with `assumeRoleArn` in the `SecretProviderClass`. For more information, see [Assume an IAM role to retrieve secrets with the ASCP](https://docs.aws.amazon.com/secretsmanager/latest/userguide/integrating_ascp_assume_role.html). | November 13, 2026 | 
| [Cross-account replication](document-history.md) | Secrets Manager now lets you replicate a secret to a replica secret in a different AWS account in the same Region. For more information, see [Replicate AWS Secrets Manager secrets across accounts](https://docs.aws.amazon.com/secretsmanager/latest/userguide/cross-account-replicate-secrets.html). | November 10, 2026 | 
| [Update to AWS managed policy](document-history.md) | The `AWSSecretsManagerClientReadOnlyAccess` managed policy now includes `BatchGetSecretValue` and `ListSecrets` permissions. For information, see [Secrets Manager updates to AWS managed policies](https://docs.aws.amazon.com/secretsmanager/latest/userguide/reference_available-policies.html#security-iam-awsmanpol-updates). | June 2, 2026 | 
| [New AWS managed policy](document-history.md) | Secrets Manager has released a new managed policy `AWSSecretsManagerClientReadOnlyAccess` that provides read-only access to secrets for client applications. For information, see [Secrets Manager updates to AWS managed policies](https://docs.aws.amazon.com/secretsmanager/latest/userguide/reference_available-policies.html#security-iam-awsmanpol-updates). | November 5, 2025 | 
| [Added support for cost allocation tags](document-history.md) | Secrets Manager now supports cost allocation tags, allowing customers to categorize and track costs by department, team, or application. For more information, see [Using cost allocation tags with AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/cost-allocation-tags.html). | May 27, 2025 | 
| [Added IPv6 and dual-stack support](document-history.md) | Secrets Manager now supports dual-stack endpoints. See [IPv4 and IPv6 access](https://docs.aws.amazon.com/secretsmanager/latest/userguide/ip-access.html) for more information. | December 20, 2024 | 
| [Secrets Manager change to AWS managed policy](document-history.md) | The `SecretsManagerReadWrite` managed policy now includes `redshift-serverless` permission. For more information, see [AWS managed policy for AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/reference_available-policies.html)  | March 12, 2024 | 

## Earlier updates
<a name="w2aac57b7"></a>

The following table describes important changes in each release of the AWS Secrets Manager User Guide before February 2024.


| Change | Description | Date | 
| --- | --- | --- | 
| General availability | This is the initial public release of Secrets Manager. | Apr 4, 2018 | 