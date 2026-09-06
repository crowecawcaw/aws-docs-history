

# Data retrieval APIs for AWS Payment Cryptography
<a name="awspaymentcryptography"></a>

AWS Payment Cryptography provides the following APIs for data retrieval.



| Actions | Description | Access level | 
| --- | --- | --- | 
| <a name="payment-cryptography-GetAlias"></a>[GetAlias](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_GetAlias.html) | Return the keyArn associated with an aliasName | Read | 
| <a name="payment-cryptography-GetCertificateSigningRequest"></a>[GetCertificateSigningRequest](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_GetCertificateSigningRequest.html) | Return the Certificate Signing Request for a public key from a key of class PUBLIC\_KEY | Read | 
| <a name="payment-cryptography-GetDefaultKeyReplicationRegions"></a>[GetDefaultKeyReplicationRegions](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_GetDefaultKeyReplicationRegions.html) | Retrieve the default key replication regions configured at the account level | Read | 
| <a name="payment-cryptography-GetKey"></a>[GetKey](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_GetKey.html) | Return the detailed information about the specified key | Read | 
| <a name="payment-cryptography-GetMpaTeamAssociation"></a>[GetMpaTeamAssociation](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_GetMpaTeamAssociation.html) | Retrieve information about an MPA approval team association for a payment cryptography action | Read | 
| <a name="payment-cryptography-GetParametersForExport"></a>[GetParametersForExport](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_GetParametersForExport.html) | Get the export token and the signing key certificate to initiate a TR-34 key export | Read | 
| <a name="payment-cryptography-GetParametersForImport"></a>[GetParametersForImport](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_GetParametersForImport.html) | Get the import token and the wrapping key certificate to initiate a TR-34 key import | Read | 
| <a name="payment-cryptography-GetPublicKeyCertificate"></a>[GetPublicKeyCertificate](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_GetPublicKeyCertificate.html) | Return the public key from a key of class PUBLIC\_KEY | Read | 
| <a name="payment-cryptography-GetResourcePolicy"></a>[GetResourcePolicy](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_GetResourcePolicy.html) | Retrieve the resource-based policy attached to a key | Read | 
| <a name="payment-cryptography-ListAliases"></a>[ListAliases](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ListAliases.html) | Return a list of aliases created for all keys in the caller's AWS account and Region | List | 
| <a name="payment-cryptography-ListKeys"></a>[ListKeys](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ListKeys.html) | Return a list of keys created in the caller's AWS account and Region | List | 
| <a name="payment-cryptography-ListTagsForResource"></a>[ListTagsForResource](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ListTagsForResource.html) | Return a list of tags created in the caller's AWS account and Region | Read | 