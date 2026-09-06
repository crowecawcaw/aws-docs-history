

# Generating data keys
<a name="generating-data-keys"></a>

Authorized users can use the GenerateDataKey API (and related APIs) to request a specific type of data key or a random key of arbitrary length. This topic provides a simplified view of this API operation. For details, see the GenerateDataKey APIs in the *AWS Key Management Service API Reference*.
+ [GenerateDataKey](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateDataKey.html)
+ [GenerateDataKeyWithoutPlaintext](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateDataKeyWithoutPlaintext.html)
+ [GenerateDataKeyPair](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateDataKeyPair.html)
+ [GenerateDataKeyPairWithoutPlaintext](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateDataKeyPairWithoutPlaintext.html)

The following is the `GenerateDataKey` request syntax.

```
{
	“EncryptionContext”: {“string” : “string”},
	“GrantTokens”: [“string”],
	“KeyId”: “string”,
	“NumberOfBytes”: “number”
}
```

The request accepts the following data in JSON format.

**KeyId**  
Key identifier of the key used to encrypt the data key. This value must identify a symmetric encryption KMS key.  
This parameter is required.

**NumberOfBytes**  
An integer that contains the number of bytes to generate. This parameter is required.  
Caller must provide either `KeySpec` or `NumberOfBytes`, but not both.

**EncryptionContext**  
(Optional) Name-value pair that contains additional data to authenticate during the encryption and decryption processes that use the key.

**GrantTokens**  
(Optional) A list of grant tokens that represent grants that provide permissions to generate or use a key. For more information on grants and grant tokens, see [Authentication and access control for AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/control-access.html) in the *AWS Key Management Service Developer Guide*. 

After authenticating the command, AWS KMS, acquires the current active EKT associated with the KMS key. It passes the EKT along with your provided request and any encryption context to an HSM over a protected session between the AWS KMS host and an HSM in the domain.

The HSM does the following:

1. Generates the requested secret material and hold it in volatile memory.

1. Decrypts the *EKT* matching the key ID of the KMS key that is defined in the request to obtain the active *HBK = Decrypt(DKi, EKT)*.

1. Generates a random nonce *N*.

1. Generates a 256-bit AES-GCM derived encryption key *K* from *HBK* and *N*.

1. Encrypts the secret material *ciphertext = Encrypt(K, context, secret)*.

`GenerateDataKey` returns the plaintext secret material and the ciphertext to you over the secure channel between the AWS KMS host and the HSM. AWS KMS then sends it to you over the TLS session. AWS KMS does not retain the plaintext or ciphertext. Without possession of the *ciphertext*, the encryption context, and the authorization to use the *KMS key*, the underlying secret cannot be returned.

The following is the response syntax. 

```
{
	"CiphertextBlob": "blob",
	"KeyId": "string",
	"Plaintext": "blob"
}
```

The management of data keys is left to you as the application developer. For best practice client-side encryption with AWS KMS data keys (but not data key pairs), you can use the [AWS Encryption SDK](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/).

Data keys can be rotated at any frequency. Further, the data key can be reencrypted under a different KMS key or a rotated KMS key using the `ReEncrypt` API operation. For details, see [ReEncrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API_ReEncrypt.html) in the *AWS Key Management Service API Reference*.