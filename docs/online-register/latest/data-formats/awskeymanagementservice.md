

# Data retrieval APIs for AWS Key Management Service
<a name="awskeymanagementservice"></a>

AWS Key Management Service provides the following APIs for data retrieval.



| Actions | Description | Access level | 
| --- | --- | --- | 
| <a name="kms-DescribeCustomKeyStores"></a>[DescribeCustomKeyStores](https://docs.aws.amazon.com/kms/latest/APIReference/API_DescribeCustomKeyStores.html) | Controls permission to view detailed information about custom key stores in the account and region | Read | 
| <a name="kms-DescribeKey"></a>[DescribeKey](https://docs.aws.amazon.com/kms/latest/APIReference/API_DescribeKey.html) | Controls permission to view detailed information about an AWS KMS key | Read | 
| <a name="kms-GetKeyLastUsage"></a>[GetKeyLastUsage](https://docs.aws.amazon.com/kms/latest/APIReference/API_GetKeyLastUsage.html) | Controls permission to view the last usage of an AWS KMS key | Read | 
| <a name="kms-GetKeyPolicy"></a>[GetKeyPolicy](https://docs.aws.amazon.com/kms/latest/APIReference/API_GetKeyPolicy.html) | Controls permission to view the key policy for the specified AWS KMS key | Read | 
| <a name="kms-GetKeyRotationStatus"></a>[GetKeyRotationStatus](https://docs.aws.amazon.com/kms/latest/APIReference/API_GetKeyRotationStatus.html) | Controls permission to view the key rotation status for an AWS KMS key | Read | 
| <a name="kms-GetParametersForImport"></a>[GetParametersForImport](https://docs.aws.amazon.com/kms/latest/APIReference/API_GetParametersForImport.html) | Controls permission to get data that is required to import cryptographic material into a customer managed key, including a public key and import token | Read | 
| <a name="kms-GetPublicKey"></a>[GetPublicKey](https://docs.aws.amazon.com/kms/latest/APIReference/API_GetPublicKey.html) | Controls permission to download the public key of an asymmetric AWS KMS key | Read | 
| <a name="kms-ListAliases"></a>[ListAliases](https://docs.aws.amazon.com/kms/latest/APIReference/API_ListAliases.html) | Controls permission to view the aliases that are defined in the account. Aliases are optional friendly names that you can associate with AWS KMS keys | List | 
| <a name="kms-ListGrants"></a>[ListGrants](https://docs.aws.amazon.com/kms/latest/APIReference/API_ListGrants.html) | Controls permission to view all grants for an AWS KMS key | List | 
| <a name="kms-ListKeyPolicies"></a>[ListKeyPolicies](https://docs.aws.amazon.com/kms/latest/APIReference/API_ListKeyPolicies.html) | Controls permission to view the names of key policies for an AWS KMS key | List | 
| <a name="kms-ListKeyRotations"></a>[ListKeyRotations](https://docs.aws.amazon.com/kms/latest/APIReference/API_ListKeyRotations.html) | Controls permission to view the list of key materials for an AWS KMS key | List | 
| <a name="kms-ListKeys"></a>[ListKeys](https://docs.aws.amazon.com/kms/latest/APIReference/API_ListKeys.html) | Controls permission to view the key ID and Amazon Resource Name (ARN) of all AWS KMS keys in the account | List | 
| <a name="kms-ListResourceTags"></a>[ListResourceTags](https://docs.aws.amazon.com/kms/latest/APIReference/API_ListResourceTags.html) | Controls permission to view all tags that are attached to an AWS KMS key | List | 
| <a name="kms-ListRetirableGrants"></a>[ListRetirableGrants](https://docs.aws.amazon.com/kms/latest/APIReference/API_ListRetirableGrants.html) | Controls permission to view grants in which the specified principal is the retiring principal. Other principals might be able to retire the grant and this principal might be able to retire other grants | List | 