# Generating data keys

Authorized users can use the GenerateDataKey API (and related APIs) to request a specific
type of data key or a random key of arbitrary length. This topic provides a simplified view of
this API operation. For details, see the GenerateDataKey APIs in the _AWS Key Management Service API Reference_.

- [GenerateDataKey](../APIReference/API_GenerateDataKey.md "../APIReference/API_GenerateDataKey.md")
- [GenerateDataKeyWithoutPlaintext](../APIReference/API_GenerateDataKeyWithoutPlaintext.md "../APIReference/API_GenerateDataKeyWithoutPlaintext.md")
- [GenerateDataKeyPair](../APIReference/API_GenerateDataKeyPair.md "../APIReference/API_GenerateDataKeyPair.md")
- [GenerateDataKeyPairWithoutPlaintext](../APIReference/API_GenerateDataKeyPairWithoutPlaintext.md "../APIReference/API_GenerateDataKeyPairWithoutPlaintext.md")
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

Key identifier of the key used to encrypt the data key. This value must identify a
symmetric encryption KMS key.

This parameter is required.

**NumberOfBytes**

An integer that contains the number of bytes to generate. This parameter is
required.

Caller must provide either `KeySpec` or `NumberOfBytes`, but
not both.

**EncryptionContext**

(Optional) Name-value pair that contains additional data to authenticate during the
encryption and decryption processes that use the key.

**GrantTokens**

(Optional) A list of grant tokens that represent grants that provide permissions to
generate or use a key. For more information on grants and grant tokens, see [Authentication and access control for AWS KMS](../developerguide/control-access.md "../developerguide/control-access.md") in the _AWS Key Management Service Developer Guide_.

After authenticating the command, AWS KMS, acquires the current active EKT associated with
the KMS key. It passes the EKT along with your provided request and any encryption context
to an HSM over a protected session between the AWS KMS host and an HSM in the domain.

The HSM does the following:

1. Generates the requested secret material and hold it in volatile memory.
2. Decrypts the _EKT_ matching the key ID of the KMS key that is defined
   in the request to obtain the active _HBK = Decrypt(DKi,
   EKT)_.
3. Generates a random nonce _N_.
4. Generates a 256-bit AES-GCM derived encryption key _K_ from
   _HBK_ and _N_.
5. Encrypts the secret material _ciphertext = Encrypt(K, context,
   secret)_.
   `GenerateDataKey` returns the plaintext secret material and the ciphertext to
   you over the secure channel between the AWS KMS host and the HSM. AWS KMS then sends it to you
   over the TLS session. AWS KMS does not retain the plaintext or ciphertext. Without possession of
   the _ciphertext_, the encryption context, and the authorization to use the
   _KMS key_, the underlying secret cannot be returned.

The following is the response syntax.

```
{
	"CiphertextBlob": "blob",
	"KeyId": "string",
	"Plaintext": "blob"
}
```

The management of data keys is left to you as the application developer. For best practice
client-side encryption with AWS KMS data keys (but not data key pairs), you can use the [AWS Encryption SDK](../../../encryption-sdk/latest/developer-guide.md "../../../encryption-sdk/latest/developer-guide.md").

Data keys can be rotated at any frequency. Further, the data key can be reencrypted under
a different KMS key or a rotated KMS key using the `ReEncrypt` API operation.
For details, see [ReEncrypt](../APIReference/API_ReEncrypt.md "../APIReference/API_ReEncrypt.md") in the
_AWS Key Management Service API Reference_.
