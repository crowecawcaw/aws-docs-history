

# Decrypt
<a name="decrypt-operation"></a>

A call to AWS KMS to decrypt a ciphertext value accepts an encrypted value ciphertext and an encryption context. AWS KMS authenticates the call using [AWS signature version 4 signed requests](https://docs.aws.amazon.com/general/latest/gr/signing_aws_api_requests.html) and extracts the HBKID for the wrapping key from the ciphertext. The HBKID is used to obtain the *EKT* required to decrypt the ciphertext, the key ID, and the policy for the key ID. The request is authorized based on the key policy, grants that may be present, and any associated IAM policies that reference the key ID. The `Decrypt` function is analogous to the encryption function.

The following is the `Decrypt` request syntax.

```
{
	"CiphertextBlob": "blob",
	"EncryptionContext": { "string" : "string" }
	"GrantTokens": ["string"]
}
```

The following are the request parameters.

**CiphertextBlob**  
Ciphertext including metadata.

** EncryptionContext**  
(Optional) The encryption context. If this was specified in the `Encrypt` function, it must be specified here or the decryption operation fails. For more information, see [Encryption context](https://docs.aws.amazon.com/kms/latest/developerguide/encrypt-context.html) in the *AWS Key Management Service Developer Guide*.

**GrantTokens**  
(Optional) A list of grant tokens that represent grants that provide permissions to perform decryption.

The *ciphertext* and the *EKT* are sent, along with the encryption context, over an authenticated session to an HSM for decryption.

The HSM runs the following:

1. Decrypts the *EKT* to obtain the *HBK = Decrypt(DKi, EKT) *.

1. Extracts the nonce *N* from the *ciphertext* structure.

1. Regenerates a 256-bit AES-GCM derived encryption key *K* from *HBK* and *N*.

1. Decrypts the *ciphertext* to obtain *plaintext = Decrypt(K, context, ciphertext) *.

The resulting key ID and plaintext are returned to the AWS KMS host over the secure session and then back to the calling customer application over a TLS connection.

The following is the response syntax.

```
{
    "KeyId": "string",
    "Plaintext": blob
}
```

If the calling application wants to ensure that the authenticity of the plaintext, it must verify that the key ID returned is the one expected.